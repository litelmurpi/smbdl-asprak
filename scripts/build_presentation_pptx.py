#!/usr/bin/env python3
"""
Generator Presentasi PowerPoint Native (.pptx)
Materi Pengayaan SMBD Lanjut: Stored Procedure, UDF, Cursor & Error Handling
Desain: Pixel-Accurate Web Dark Modern Glassmorphism (Grainient Backdrop + Floating Tablet Chassis).
"""

import os
import re
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.dml.color import RGBColor

# Palet Warna Web-Based Liquid Glass & Cyber Glow
COLOR_CYAN = RGBColor(0, 229, 255)           # #00E5FF
COLOR_SKY = RGBColor(56, 189, 248)           # #38BDF8
COLOR_BLUE = RGBColor(37, 99, 235)           # #2563EB
COLOR_PURPLE = RGBColor(192, 132, 252)       # #C084FC
COLOR_GREEN = RGBColor(52, 211, 153)         # #34D399
COLOR_RED = RGBColor(239, 68, 68)            # #EF4444
COLOR_AMBER = RGBColor(245, 158, 11)         # #F59E0B
COLOR_CORAL = RGBColor(248, 113, 113)        # #F87171

COLOR_CHASSIS_BG = RGBColor(11, 17, 34)      # #0B1122
COLOR_CHASSIS_BORDER = RGBColor(40, 60, 95)  # #283C5F
COLOR_CARD_BG = RGBColor(16, 26, 52)         # #101A34
COLOR_CARD_BORDER = RGBColor(46, 63, 102)    # #2E3F66
COLOR_CODE_BG = RGBColor(3, 7, 18)           # #030712
COLOR_CODE_BORDER = RGBColor(30, 41, 59)     # #1E293B

COLOR_TEXT_WHITE = RGBColor(255, 255, 255)   # #FFFFFF
COLOR_TEXT_PRIMARY = RGBColor(241, 245, 249) # #F1F5F9
COLOR_TEXT_BODY = RGBColor(203, 213, 225)    # #CBD5E1
COLOR_TEXT_MUTED = RGBColor(148, 163, 184)   # #94A3B8

FONT_HEADING = "Plus Jakarta Sans"
FONT_BODY = "Inter"
FONT_MONO = "JetBrains Mono"

# Kata kunci SQL untuk pewarnaan sintaks di terminal code box
SQL_KEYWORDS = {
    'CREATE', 'PROCEDURE', 'FUNCTION', 'DELIMITER', 'BEGIN', 'END', 'IF', 'THEN',
    'ELSEIF', 'ELSE', 'RETURNS', 'DETERMINISTIC', 'DECLARE', 'CURSOR', 'FOR', 'OPEN',
    'FETCH', 'CLOSE', 'LOOP', 'LEAVE', 'HANDLER', 'NOT', 'FOUND', 'CONTINUE', 'EXIT',
    'SIGNAL', 'SQLSTATE', 'SET', 'SELECT', 'FROM', 'WHERE', 'INTO', 'UPDATE',
    'INSERT', 'VALUES', 'START', 'TRANSACTION', 'COMMIT', 'ROLLBACK', 'LOCK',
    'ENGINE', 'PRIMARY', 'KEY', 'FOREIGN', 'REFERENCES', 'ON', 'DELETE', 'CASCADE',
    'RESTRICT', 'DEFAULT', 'READS', 'SQL', 'DATA', 'NO', 'COUNT', 'SUM', 'COALESCE',
    'CONCAT', 'CHAR_LENGTH', 'FOR', 'UPDATE', 'CHECK', 'OR', 'AND', 'IS', 'NULL', 'LIKE'
}

SQL_TYPES = {'INT', 'CHAR', 'VARCHAR', 'DECIMAL', 'DATE', 'DATETIME', 'BOOLEAN'}

def tokenize_sql_line(line):
    tokens = []
    idx = line.find('--')
    code_part = line if idx == -1 else line[:idx]
    comment_part = "" if idx == -1 else line[idx:]

    if code_part:
        pattern = r"('[^']*'|\b[A-Za-z_][A-Za-z0-9_]*\b|\b\d+\b|[^\s\w]+|\s+)"
        for match in re.finditer(pattern, code_part):
            val = match.group(0)
            u_val = val.upper()
            if val.startswith("'") and val.endswith("'"):
                tokens.append(('string', val))
            elif u_val in SQL_KEYWORDS:
                tokens.append(('keyword', val))
            elif u_val in SQL_TYPES:
                tokens.append(('type', val))
            elif val.isdigit():
                tokens.append(('number', val))
            elif val.startswith('@') or val.startswith('v_') or val.startswith('p_'):
                tokens.append(('variable', val))
            else:
                tokens.append(('normal', val))

    if comment_part:
        tokens.append(('comment', comment_part))

    return tokens

def create_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]
    bg_path = "presentations/assets/slide_bg_16_9.png"

    def apply_slide_chassis(slide):
        # 1. Background Grainient Wallpaper
        if os.path.exists(bg_path):
            slide.shapes.add_picture(bg_path, 0, 0, prs.slide_width, prs.slide_height)

        # 2. Floating Glass Tablet Chassis
        chassis = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            Inches(0.65), Inches(0.4), Inches(12.033), Inches(6.7)
        )
        chassis.fill.solid()
        chassis.fill.fore_color.rgb = COLOR_CHASSIS_BG
        chassis.line.color.rgb = COLOR_CHASSIS_BORDER
        chassis.line.width = Pt(1.25)
        return chassis

    def add_header(slide, category, title, title_accent=None, submeta=None):
        # Category Pill Badge (Left)
        badge = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            Inches(1.0), Inches(0.65), Inches(2.7), Inches(0.36)
        )
        badge.fill.solid()
        badge.fill.fore_color.rgb = RGBColor(12, 28, 56)
        badge.line.color.rgb = COLOR_CYAN
        badge.line.width = Pt(1)
        tf_b = badge.text_frame
        tf_b.vertical_anchor = MSO_ANCHOR.MIDDLE
        p_b = tf_b.paragraphs[0]
        p_b.text = f"● {category.upper()}"
        p_b.font.name = FONT_MONO
        p_b.font.size = Pt(9.5)
        p_b.font.bold = True
        p_b.font.color.rgb = COLOR_CYAN
        p_b.alignment = PP_ALIGN.CENTER

        # Submeta (Right)
        if submeta:
            tb_sm = slide.shapes.add_textbox(Inches(7.0), Inches(0.65), Inches(5.3), Inches(0.36))
            tf_sm = tb_sm.text_frame
            p_sm = tf_sm.paragraphs[0]
            p_sm.text = submeta
            p_sm.font.name = FONT_BODY
            p_sm.font.size = Pt(10)
            p_sm.font.color.rgb = COLOR_TEXT_MUTED
            p_sm.alignment = PP_ALIGN.RIGHT

        # Slide Main Title with Accent
        tb_t = slide.shapes.add_textbox(Inches(1.0), Inches(1.05), Inches(11.3), Inches(0.65))
        tf_t = tb_t.text_frame
        tf_t.word_wrap = True
        p_t = tf_t.paragraphs[0]

        run_main = p_t.add_run()
        run_main.text = title + " "
        run_main.font.name = FONT_HEADING
        run_main.font.size = Pt(21)
        run_main.font.bold = True
        run_main.font.color.rgb = COLOR_TEXT_WHITE

        if title_accent:
            run_acc = p_t.add_run()
            run_acc.text = title_accent
            run_acc.font.name = FONT_HEADING
            run_acc.font.size = Pt(21)
            run_acc.font.bold = True
            run_acc.font.color.rgb = COLOR_CYAN

        # Footer Branding Line inside Chassis
        tb_f = slide.shapes.add_textbox(Inches(1.0), Inches(6.65), Inches(8.0), Inches(0.35))
        p_fl = tb_f.text_frame.paragraphs[0]
        p_fl.text = "Laboratorium Sistem Informasi · Pengayaan SMBD Lanjut · Universitas Amikom Yogyakarta"
        p_fl.font.name = FONT_BODY
        p_fl.font.size = Pt(9.0)
        p_fl.font.color.rgb = COLOR_TEXT_MUTED

    def add_card(slide, left, top, width, height, card_title, body_text, num_tag=None, border_color=None, highlight=False):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = RGBColor(19, 32, 64) if highlight else COLOR_CARD_BG
        card.line.color.rgb = border_color or (COLOR_CYAN if highlight else COLOR_CARD_BORDER)
        card.line.width = Pt(1.25 if highlight else 1.0)

        tb = slide.shapes.add_textbox(left + Inches(0.18), top + Inches(0.14), width - Inches(0.36), height - Inches(0.28))
        tf = tb.text_frame
        tf.word_wrap = True

        p1 = tf.paragraphs[0]
        if num_tag:
            run_num = p1.add_run()
            run_num.text = f"[{num_tag}] "
            run_num.font.name = FONT_MONO
            run_num.font.size = Pt(10.5)
            run_num.font.bold = True
            run_num.font.color.rgb = COLOR_CYAN

        run_title = p1.add_run()
        run_title.text = card_title
        run_title.font.name = FONT_HEADING
        run_title.font.size = Pt(12)
        run_title.font.bold = True
        run_title.font.color.rgb = COLOR_TEXT_WHITE

        p2 = tf.add_paragraph()
        p2.space_before = Pt(6)
        run_b = p2.add_run()
        run_b.text = body_text
        run_b.font.name = FONT_BODY
        run_b.font.size = Pt(9.5)
        run_b.font.color.rgb = COLOR_TEXT_BODY

        return card

    def add_code_box(slide, left, top, width, height, filename, code_str):
        # Outer Terminal Box
        box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        box.fill.solid()
        box.fill.fore_color.rgb = COLOR_CODE_BG
        box.line.color.rgb = COLOR_CODE_BORDER
        box.line.width = Pt(1)

        # Mac Traffic Light Buttons (Red, Yellow, Green)
        dot_y = top + Inches(0.12)
        colors_dots = [COLOR_RED, COLOR_AMBER, COLOR_GREEN]
        for idx, dot_col in enumerate(colors_dots):
            dot = slide.shapes.add_shape(MSO_SHAPE.OVAL, left + Inches(0.15 + idx * 0.18), dot_y, Inches(0.11), Inches(0.11))
            dot.fill.solid()
            dot.fill.fore_color.rgb = dot_col
            dot.line.fill.background()

        # Terminal File Title
        tb_title = slide.shapes.add_textbox(left + Inches(0.8), top + Inches(0.04), width - Inches(2.2), Inches(0.28))
        p_t = tb_title.text_frame.paragraphs[0]
        p_t.text = f"terminal · {filename}"
        p_t.font.name = FONT_MONO
        p_t.font.size = Pt(9.0)
        p_t.font.color.rgb = COLOR_SKY

        # Code Container
        tb_code = slide.shapes.add_textbox(left + Inches(0.15), top + Inches(0.32), width - Inches(0.3), height - Inches(0.40))
        tf_code = tb_code.text_frame
        tf_code.word_wrap = True
        tf_code.margin_top = Inches(0.02)
        tf_code.margin_bottom = Inches(0.02)
        tf_code.margin_left = Inches(0.05)
        tf_code.margin_right = Inches(0.05)

        lines = code_str.strip().split("\n")
        if len(lines) > 24:
            font_size = Pt(7.2)
            space_after = Pt(0)
        elif len(lines) > 18:
            font_size = Pt(8.0)
            space_after = Pt(0.5)
        else:
            font_size = Pt(9.0)
            space_after = Pt(1.5)

        for line_idx, line in enumerate(lines):
            p = tf_code.paragraphs[0] if line_idx == 0 else tf_code.add_paragraph()
            p.space_after = space_after
            tokens = tokenize_sql_line(line)
            if not tokens:
                p.text = " "
                continue

            for t_type, t_val in tokens:
                run = p.add_run()
                run.text = t_val
                run.font.name = FONT_MONO
                run.font.size = font_size

                if t_type == 'keyword':
                    run.font.bold = True
                    run.font.color.rgb = COLOR_CYAN
                elif t_type == 'type':
                    run.font.bold = True
                    run.font.color.rgb = COLOR_PURPLE
                elif t_type == 'string':
                    run.font.color.rgb = COLOR_GREEN
                elif t_type == 'variable':
                    run.font.color.rgb = COLOR_AMBER
                elif t_type == 'number':
                    run.font.color.rgb = COLOR_CORAL
                elif t_type == 'comment':
                    run.font.italic = True
                    run.font.color.rgb = COLOR_TEXT_MUTED
                else:
                    run.font.color.rgb = COLOR_TEXT_PRIMARY

        return box

    def add_table(slide, left, top, width, height, headers, rows, col_widths=None):
        num_rows = len(rows) + 1
        num_cols = len(headers)
        table_shape = slide.shapes.add_table(num_rows, num_cols, left, top, width, height)
        tbl = table_shape.table

        if col_widths and len(col_widths) == num_cols:
            for idx, w in enumerate(col_widths):
                tbl.columns[idx].width = w

        # Header Row
        for col_idx, h_text in enumerate(headers):
            cell = tbl.cell(0, col_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = RGBColor(26, 45, 88)
            p = cell.text_frame.paragraphs[0]
            p.text = ""
            run = p.add_run()
            run.text = h_text
            run.font.name = FONT_HEADING
            run.font.size = Pt(10.5)
            run.font.bold = True
            run.font.color.rgb = COLOR_CYAN
            p.alignment = PP_ALIGN.LEFT

        # Data Rows
        for r_idx, row_data in enumerate(rows):
            bg_cell = COLOR_CARD_BG if r_idx % 2 == 0 else RGBColor(13, 21, 42)
            for c_idx, val in enumerate(row_data):
                cell = tbl.cell(r_idx + 1, c_idx)
                cell.fill.solid()
                cell.fill.fore_color.rgb = bg_cell
                p = cell.text_frame.paragraphs[0]
                p.text = ""
                run = p.add_run()
                run.text = str(val)
                run.font.name = FONT_BODY
                run.font.size = Pt(9.5)
                if c_idx == 0:
                    run.font.bold = True
                    run.font.color.rgb = COLOR_TEXT_WHITE
                else:
                    run.font.color.rgb = COLOR_TEXT_PRIMARY
                p.alignment = PP_ALIGN.LEFT

        return table_shape

    def add_notes(slide, notes_text):
        tf = slide.notes_slide.notes_text_frame
        tf.text = notes_text

    # =========================================================================
    # SLIDE 1: COVER
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    apply_slide_chassis(s1)

    # Category and Univ
    tb_c = s1.shapes.add_textbox(Inches(1.1), Inches(0.9), Inches(11.0), Inches(0.4))
    tf_c = tb_c.text_frame
    p_c = tf_c.paragraphs[0]
    r_cat = p_c.add_run()
    r_cat.text = "● SISTEM INFORMASI 2024/2025 · SMBD LANJUT   "
    r_cat.font.name = FONT_MONO
    r_cat.font.size = Pt(10.5)
    r_cat.font.bold = True
    r_cat.font.color.rgb = COLOR_CYAN

    r_u = p_c.add_run()
    r_u.text = "Universitas Amikom Yogyakarta"
    r_u.font.name = FONT_BODY
    r_u.font.size = Pt(10.5)
    r_u.font.color.rgb = COLOR_TEXT_MUTED

    # Hero Title (Two-Tone Gradient Feel)
    tb_hero = s1.shapes.add_textbox(Inches(1.1), Inches(1.5), Inches(11.0), Inches(1.8))
    tf_h = tb_hero.text_frame
    tf_h.word_wrap = True

    p_h1 = tf_h.paragraphs[0]
    p_h1.text = "Pemrograman Prosedural Database:"
    p_h1.font.name = FONT_HEADING
    p_h1.font.size = Pt(32)
    p_h1.font.bold = True
    p_h1.font.color.rgb = COLOR_TEXT_WHITE

    p_h2 = tf_h.add_paragraph()
    p_h2.text = "Stored Procedure, UDF & Cursor"
    p_h2.font.name = FONT_HEADING
    p_h2.font.size = Pt(32)
    p_h2.font.bold = True
    p_h2.font.color.rgb = COLOR_CYAN

    # Description
    tb_desc = s1.shapes.add_textbox(Inches(1.1), Inches(3.45), Inches(10.8), Inches(0.9))
    tf_d = tb_desc.text_frame
    tf_d.word_wrap = True
    p_d = tf_d.paragraphs[0]
    p_d.text = "Penyusunan logika bisnis terpusat di sisi server (RDBMS): User Defined Function (UDF), Stored Procedure dengan parameter IN/OUT/INOUT, iterasi baris per baris dengan CURSOR, dan penanganan galat terstruktur (SIGNAL SQLSTATE & HANDLER) pada kasus ritel minimarket 3NF."
    p_d.font.name = FONT_BODY
    p_d.font.size = Pt(12)
    p_d.font.color.rgb = COLOR_TEXT_BODY

    # 3 Badges
    badges = [
        ("Materi Praktikum", "Pengayaan Praktikum 4"),
        ("Studi Kasus Ritel", "Otomasi Nota & Stok 3NF"),
        ("Tantangan Tugas", "10 Soal Bertingkat + Solusi")
    ]
    for i, (b_label, b_val) in enumerate(badges):
        b_x = Inches(1.1 + i * 3.7)
        b_box = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, b_x, Inches(4.6), Inches(3.5), Inches(0.9))
        b_box.fill.solid()
        b_box.fill.fore_color.rgb = COLOR_CARD_BG
        b_box.line.color.rgb = COLOR_CARD_BORDER
        tf_b = b_box.text_frame
        p_l = tf_b.paragraphs[0]
        p_l.text = b_label.upper()
        p_l.font.name = FONT_MONO
        p_l.font.size = Pt(9.0)
        p_l.font.color.rgb = COLOR_SKY
        p_v = tf_b.add_paragraph()
        p_v.text = b_val
        p_v.font.name = FONT_HEADING
        p_v.font.size = Pt(12.5)
        p_v.font.bold = True
        p_v.font.color.rgb = COLOR_TEXT_WHITE

    # Bottom Hint
    tb_hint = s1.shapes.add_textbox(Inches(1.1), Inches(5.8), Inches(10.0), Inches(0.35))
    p_hint = tb_hint.text_frame.paragraphs[0]
    p_hint.text = "Tekan Space atau Panah Kanan untuk navigasi · Didukung DeckCraft & PowerPoint Native"
    p_hint.font.name = FONT_MONO
    p_hint.font.size = Pt(10)
    p_hint.font.color.rgb = COLOR_TEXT_MUTED

    # Footer
    tb_foot = s1.shapes.add_textbox(Inches(1.1), Inches(6.65), Inches(11.0), Inches(0.35))
    p_foot = tb_foot.text_frame.paragraphs[0]
    p_foot.text = "Laboratorium Sistem Informasi · Pengayaan SMBD Lanjut · Slide 01 / 12"
    p_foot.font.name = FONT_BODY
    p_foot.font.size = Pt(9.0)
    p_foot.font.color.rgb = COLOR_TEXT_MUTED

    add_notes(s1, "Selamat datang di modul pengayaan Sistem Manajemen Basis Data Lanjut (SMBD Lanjut). Pada sesi ini mahasiswa akan mempelajari cara membangun logika bisnis di sisi RDBMS MySQL menggunakan Stored Procedure, UDF, Cursor, dan Error Handling pada basis data minimarket 3NF.")

    # =========================================================================
    # SLIDE 2: ARSITEKTUR CLIENT-SERVER
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    apply_slide_chassis(s2)
    add_header(s2, "01 · Konsepsi & Arsitektur", "Kenapa Menaruh Logika Bisnis di Database?", "Hemat Jaringan & Keamanan Data", "Keuntungan Stored Routine")

    tb_sub2 = s2.shapes.add_textbox(Inches(1.0), Inches(1.6), Inches(11.3), Inches(0.4))
    p_s2 = tb_sub2.text_frame.paragraphs[0]
    p_s2.text = "Memindahkan logika transaksi langsung ke dalam database engine memberikan 4 keuntungan praktis:"
    p_s2.font.name = FONT_BODY
    p_s2.font.size = Pt(11)
    p_s2.font.color.rgb = COLOR_TEXT_BODY

    cards_s2 = [
        ("Hemat Jaringan", "Aplikasi kasir cukup kirim 1 perintah CALL, bukan bolak-balik kirim belasan kueri lewat jaringan WiFi/kabel.", "01"),
        ("Aturan Terpusat", "Rumus diskon, batas stok, dan poin ditulis sekali di database. Seluruh aplikasi kasir memakai aturan yang sama.", "02"),
        ("Eksekusi Cepat", "Rencana eksekusi (execution plan) disimpan di buffer memori database. Eksekusi berikutnya berjalan langsung tanpa parsing ulang.", "03"),
        ("Akses Lebih Aman", "Kasir cukup diberi izin EXECUTE pada prosedur penjualan tanpa diberi izin mengubah tabel master fisik secara langsung.", "04"),
    ]
    card_w = Inches(2.68)
    card_h = Inches(4.3)
    for i, (c_title, c_text, c_num) in enumerate(cards_s2):
        add_card(s2, Inches(1.0 + i * 2.88), Inches(2.1), card_w, card_h, c_title, c_text, num_tag=c_num, highlight=(i==0))

    add_notes(s2, "Tekankan kepada mahasiswa bahwa keuntungan terbesar Stored Routine terletak pada berkurangnya traffic bolak-balik antara server aplikasi dan database.")

    # =========================================================================
    # SLIDE 3: KOMPARASI FUNCTION VS PROCEDURE
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    apply_slide_chassis(s3)
    add_header(s3, "02 · Komparasi Logika", "Perbedaan Utama: Function vs Procedure", "Kriteria & Batasan", "Function vs Procedure")

    tb_sub3 = s3.shapes.add_textbox(Inches(1.0), Inches(1.6), Inches(11.3), Inches(0.4))
    p_s3 = tb_sub3.text_frame.paragraphs[0]
    p_s3.text = "Meskipun sama-sama blok kode di sisi server, keduanya dirancang untuk tugas yang berbeda:"
    p_s3.font.name = FONT_BODY
    p_s3.font.size = Pt(11)
    p_s3.font.color.rgb = COLOR_TEXT_BODY

    headers_s3 = ["Kriteria", "User Defined Function (UDF)", "Stored Procedure"]
    rows_s3 = [
        ["Nilai Kembalian", "Wajib 1 nilai skalar via klausa RETURNS & RETURN.", "Tidak ada return langsung; memakai parameter OUT / INOUT."],
        ["Cara Panggil", "Dipanggil di dalam kueri SQL biasa (SELECT fc(), WHERE fc() > 0).", "Dipanggil terpisah sebagai perintah mandiri: CALL sp_name(argumen);."],
        ["Ubah Data (DML)", "Dilarang mengubah isi tabel saat dipanggil kueri baca.", "Bebas mengubah data, mengontrol transaksi COMMIT/ROLLBACK, dan kueri dinamis."],
        ["Kapan Dipakai", "Perhitungan skalar, format teks, konversi nilai, atau nomor urut nota.", "Alur transaksi multi-tabel, batch processing berkala, dan otomasi kasir."]
    ]
    add_table(s3, Inches(1.0), Inches(2.1), Inches(11.3), Inches(4.3), headers_s3, rows_s3, [Inches(2.7), Inches(4.3), Inches(4.3)])
    add_notes(s3, "Ingatkan aturan MySQL: Function tidak boleh melakukan INSERT/UPDATE/DELETE jika dipanggil dari SELECT.")

    # =========================================================================
    # SLIDE 4: ANATOMI UDF
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    apply_slide_chassis(s4)
    add_header(s4, "03 · Function (UDF)", "User Defined Function & Karakteristik Sifat", "Nilai Kembalian Tunggal", "Fungsi Buatan Sendiri")

    udf_code = (
        "DELIMITER $$\n"
        "CREATE FUNCTION fcHitungDiskon(\n"
        "    p_total INT,\n"
        "    p_poin  INT\n"
        ")\n"
        "RETURNS DECIMAL(10,2)\n"
        "DETERMINISTIC\n"
        "NO SQL\n"
        "BEGIN\n"
        "    DECLARE v_diskon DECIMAL(10,2) DEFAULT 0.00;\n"
        "    IF p_poin >= 50 THEN\n"
        "        SET v_diskon = p_total * 0.10; -- Diskon 10%\n"
        "    ELSEIF p_poin >= 20 THEN\n"
        "        SET v_diskon = p_total * 0.05; -- Diskon 5%\n"
        "    END IF;\n"
        "    RETURN v_diskon;\n"
        "END$$\n"
        "DELIMITER ;\n\n"
        "-- Pemanggilan UDF dalam Kueri SQL Biasa:\n"
        "SELECT Nonota, fcHitungDiskon(150000, 35) AS diskon FROM nota;"
    )
    add_code_box(s4, Inches(1.0), Inches(1.9), Inches(6.8), Inches(4.5), "fcHitungDiskon.sql", udf_code)
    add_card(s4, Inches(8.0), Inches(1.9), Inches(4.3), Inches(2.15), "Klausa DETERMINISTIC", "Wajib dideklarasikan pada sistem dengan replikasi binlog aktif. DETERMINISTIC menyatakan bahwa input yang sama selalu menghasilkan output yang sama persis.")
    add_card(s4, Inches(8.0), Inches(4.25), Inches(4.3), Inches(2.15), "Kategori Akses SQL", "• NO SQL: fungsi murni tanpa akses data tabel.\n• READS SQL DATA: fungsi membaca data tabel via SELECT INTO.\n• MODIFIES SQL DATA: memodifikasi data (hanya diizinkan di procedure).")
    add_notes(s4, "Jelaskan pentingnya klausa DELIMITER $$ agar MySQL tidak mengartikan titik koma di dalam fungsi sebagai akhir kueri.")

    # =========================================================================
    # SLIDE 5: MODE PARAMETER SP
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    apply_slide_chassis(s5)
    add_header(s5, "04 · Parameter SP", "Mode Parameter Stored Procedure:", "IN, OUT & INOUT", "Mekanisme Pertukaran Nilai")

    params = [
        ("IN (Input Saja)", "Nilai dikirim oleh pemanggil ke dalam prosedur. Perubahan nilai di dalam prosedur tidak mengubah variabel di luar (read-only).", "IN"),
        ("OUT (Keluaran Saja)", "Nilai awalnya kosong (NULL). Prosedur mengisi nilai hasil perhitungan, lalu dikembalikan ke variabel pemanggil.", "OUT"),
        ("INOUT (Bolak-Balik)", "Membawa nilai awal dari luar, diproses atau dimodifikasi di dalam prosedur, lalu nilai barunya dikembalikan lagi.", "INOUT")
    ]
    for i, (p_title, p_desc, p_badge) in enumerate(params):
        add_card(s5, Inches(1.0 + i * 3.84), Inches(1.85), Inches(3.64), Inches(2.1), p_title, p_desc, num_tag=p_badge)

    sp_code = (
        "DELIMITER $$\n"
        "CREATE PROCEDURE sp_HitungBonusKasir(\n"
        "    IN  p_KodeKasir VARCHAR(3),      -- Input: kode kasir\n"
        "    OUT p_TotalNota INT,             -- Output: jumlah nota\n"
        "    INOUT p_SaldoBonus DECIMAL(12,2) -- Input & Output: saldo bonus\n"
        ")\n"
        "BEGIN\n"
        "    SELECT COUNT(*) INTO p_TotalNota FROM nota WHERE KodeKasir = p_KodeKasir;\n"
        "    SET p_SaldoBonus = p_SaldoBonus + (p_TotalNota * 2500);\n"
        "END$$\n"
        "DELIMITER ;\n"
        "-- Eksekusi: SET @b = 50000; CALL sp_HitungBonusKasir('001', @nota, @b); SELECT @nota, @b;"
    )
    add_code_box(s5, Inches(1.0), Inches(4.15), Inches(11.3), Inches(2.3), "sp_HitungBonusKasir.sql", sp_code)
    add_notes(s5, "Tekankan bahwa variabel session di MySQL menggunakan simbol '@' (contoh: @total, @bonus). Parameter OUT dan INOUT wajib dipanggil menggunakan variabel session ini.")

    # =========================================================================
    # SLIDE 6: CONTROL FLOW
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    apply_slide_chassis(s6)
    add_header(s6, "05 · Kontrol Alur", "Logika Alur: Percabangan & Perulangan", "IF, CASE, WHILE & LOOP", "Algoritma Prosedural")

    cf_code1 = (
        "-- 1. PERCABANGAN IF-ELSEIF-ELSE\n"
        "IF v_stok <= 0 THEN\n"
        "    SET v_status = 'HABIS';\n"
        "ELSEIF v_stok <= 5 THEN\n"
        "    SET v_status = 'KRITIS';\n"
        "ELSE\n"
        "    SET v_status = 'AMAN';\n"
        "END IF;\n\n"
        "-- 2. PERCABANGAN CASE\n"
        "CASE p_grade\n"
        "    WHEN 'A' THEN SET v_diskon = 0.20;\n"
        "    WHEN 'B' THEN SET v_diskon = 0.10;\n"
        "    ELSE SET v_diskon = 0.00;\n"
        "END CASE;"
    )
    add_code_box(s6, Inches(1.0), Inches(1.85), Inches(5.5), Inches(4.6), "Percabangan (IF & CASE)", cf_code1)

    cf_code2 = (
        "-- 3. PENGULANGAN WHILE LOOP\n"
        "WHILE v_counter < 10 DO\n"
        "    SET v_total = v_total + v_counter;\n"
        "    SET v_counter = v_counter + 1;\n"
        "END WHILE;\n\n"
        "-- 4. LOOP & LEAVE (BREAK)\n"
        "baca_loop: LOOP\n"
        "    FETCH cur_produk INTO v_kode, v_stok;\n"
        "    IF v_selesai = 1 THEN\n"
        "        LEAVE baca_loop; -- Keluar loop\n"
        "    END IF;\n"
        "    -- Proses data baris...\n"
        "END LOOP baca_loop;"
    )
    add_code_box(s6, Inches(6.8), Inches(1.85), Inches(5.5), Inches(4.6), "Pengulangan (WHILE & LOOP)", cf_code2)
    add_notes(s6, "Ingatkan perbedaan END IF; dan END CASE; yang wajib diakhiri titik koma di blok BEGIN...END.")

    # =========================================================================
    # SLIDE 7: CURSOR
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    apply_slide_chassis(s7)
    add_header(s7, "06 · Cursor & Iterasi", "Cursor: Memproses Data Baris demi Baris", "5 Langkah Siklus", "Pointer Baris demi Baris")

    cursor_steps = [
        ("1. DECLARE", "Mendeklarasikan nama kursor dan kueri SELECT yang akan dibaca.", "01"),
        ("2. OPEN", "Mengeksekusi kueri SELECT dan menyiapkan pointer data di memori.", "02"),
        ("3. FETCH", "Mengambil nilai satu baris ke variabel lokal dan menggeser pointer.", "03"),
        ("4. CLOSE", "Menutup kursor dan membebaskan alokasi memori buffer server.", "04"),
    ]
    for i, (cs_title, cs_desc, cs_num) in enumerate(cursor_steps):
        add_card(s7, Inches(1.0 + i * 2.88), Inches(1.85), Inches(2.68), Inches(1.8), cs_title, cs_desc, num_tag=cs_num)

    cur_sql = (
        "DECLARE v_selesai INT DEFAULT 0;\n"
        "DECLARE v_kode CHAR(4); DECLARE v_stok INT;\n"
        "DECLARE cur_cek_stok CURSOR FOR SELECT KodeProduk, stok FROM produk WHERE stok < 10;\n"
        "DECLARE CONTINUE HANDLER FOR NOT FOUND SET v_selesai = 1;\n\n"
        "OPEN cur_cek_stok;\n"
        "ulang_loop: LOOP\n"
        "    FETCH cur_cek_stok INTO v_kode, v_stok;\n"
        "    IF v_selesai = 1 THEN LEAVE ulang_loop; END IF;\n"
        "    -- Eksekusi logika otomasi restock produk...\n"
        "END LOOP ulang_loop;\n"
        "CLOSE cur_cek_stok;"
    )
    add_code_box(s7, Inches(1.0), Inches(3.85), Inches(11.3), Inches(2.6), "Alur Lengkap Implementasi CURSOR", cur_sql)
    add_notes(s7, "Jelaskan urutan deklarasi variabel di MySQL: variabel biasa dulu, lalu CURSOR, baru kemudian HANDLER.")

    # =========================================================================
    # SLIDE 8: ERROR HANDLING
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    apply_slide_chassis(s8)
    add_header(s8, "07 · Penanganan Error", "Error Handling: Menjaga Transaksi Tetap Aman", "SIGNAL & HANDLER", "Mencegah Data Selisih")

    err_code = (
        "DELIMITER $$\n"
        "CREATE PROCEDURE sp_ValidasiTambahKasir(\n"
        "    IN p_Kode CHAR(3), IN p_Nama VARCHAR(30), IN p_Pass CHAR(6)\n"
        ")\n"
        "BEGIN\n"
        "    -- 1. Validasi Panjang Password Kasir Wajib Tepat 6 Karakter\n"
        "    IF CHAR_LENGTH(p_Pass) <> 6 THEN\n"
        "        SIGNAL SQLSTATE '45000'\n"
        "            SET MESSAGE_TEXT = 'Gagal: Kata sandi kasir wajib tepat 6 karakter.';\n"
        "    END IF;\n\n"
        "    -- 2. Handler jika terjadi pelanggaran Duplicate Key Primary Key\n"
        "    BEGIN\n"
        "        DECLARE EXIT HANDLER FOR 1062\n"
        "        BEGIN\n"
        "            SIGNAL SQLSTATE '45000'\n"
        "                SET MESSAGE_TEXT = 'Gagal: Kode kasir tersebut sudah terdaftar.';\n"
        "        END;\n"
        "        INSERT INTO kasir (KodeKasir, NamaKasir, Pass) VALUES (p_Kode, p_Nama, p_Pass);\n"
        "    END;\n"
        "END$$\n"
        "DELIMITER ;"
    )
    add_code_box(s8, Inches(1.0), Inches(1.85), Inches(7.2), Inches(4.6), "sp_ValidasiTambahKasir.sql", err_code)
    add_card(s8, Inches(8.4), Inches(1.85), Inches(3.9), Inches(2.2), "SIGNAL SQLSTATE '45000'", "SQLSTATE '45000' adalah kode standar ANSI SQL untuk mendefinisikan *unhandled user-defined exception*. Pesan galat kustom dikirim langsung ke aplikasi kasir.")
    add_card(s8, Inches(8.4), Inches(4.25), Inches(3.9), Inches(2.2), "CONTINUE vs EXIT HANDLER", "• EXIT: Menyetop eksekusi blok kode dan langsung keluar dari compound statement.\n• CONTINUE: Menjalankan aksi handler dan tetap melanjutkan baris instruksi berikutnya.")
    add_notes(s8, "Tekankan bahwa penanganan galat terstruktur mencegah aplikasi crash tanpa pesan yang jelas.")

    # =========================================================================
    # SLIDE 9: SKEMA 3NF
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    apply_slide_chassis(s9)
    add_header(s9, "08 · Basis Data 3NF", "Skema Fisik 5 Tabel Basis Data Minimarket", "Studi Kasus Kelompok 7", "Normalisasi 3NF")

    tabel_cards = [
        ("KASIR (Parent)", "• KodeKasir: CHAR(3) [PK]\n• NamaKasir: VARCHAR(30)\n• Pass: CHAR(6) [CHK 6 char]", "01"),
        ("CUSTOMER (Parent)", "• KodeCus: CHAR(5) [PK]\n• NamaCus: VARCHAR(50)\n• PointTerkumpul: INT", "02"),
        ("PRODUK (Parent)", "• KodeProduk: CHAR(4) [PK]\n• NamaProduk: VARCHAR(50)\n• Harga: INT, stok: INT", "03"),
        ("NOTA (Header)", "• Nonota: CHAR(10) [PK]\n• KodeKasir: FK kasir\n• KodeCus: FK customer", "04"),
        ("ITEMNOTA (Bridge N:M)", "• Nonota: CHAR(10) [PK, FK]\n• KodeProduk: CHAR(4) [PK, FK]\n• banyak: INT, hargajual: INT", "05"),
    ]
    card_w9 = Inches(2.14)
    for i, (t_name, t_cols, t_num) in enumerate(tabel_cards):
        add_card(s9, Inches(1.0 + i * 2.3), Inches(1.85), card_w9, Inches(2.4), t_name, t_cols, num_tag=t_num)

    sql_ddl_snip = (
        "-- Relasi Many-to-Many antara NOTA dan PRODUK dipecah pada ITEMNOTA:\n"
        "CREATE TABLE itemnota (\n"
        "    Nonota CHAR(10) NOT NULL,\n"
        "    KodeProduk CHAR(4) NOT NULL,\n"
        "    banyak INT NOT NULL DEFAULT 1,\n"
        "    hargajual INT NOT NULL,\n"
        "    PRIMARY KEY (Nonota, KodeProduk),\n"
        "    CONSTRAINT fk_itemnota_nota FOREIGN KEY (Nonota) REFERENCES nota(Nonota) ON DELETE CASCADE,\n"
        "    CONSTRAINT fk_itemnota_produk FOREIGN KEY (KodeProduk) REFERENCES produk(KodeProduk)\n"
        ") ENGINE=InnoDB;"
    )
    add_code_box(s9, Inches(1.0), Inches(4.45), Inches(11.3), Inches(2.0), "ITEMNOTA Bridge Table DDL", sql_ddl_snip)
    add_notes(s9, "Jelaskan mengapa Nonota dan KodeProduk dijadikan Composite Primary Key pada itemnota.")

    # =========================================================================
    # SLIDE 10: TRANSAKSI CHECKOUT
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    apply_slide_chassis(s10)
    add_header(s10, "09 · Transaksi Ritel", "Studi Kasus: Checkout Kasir & Auto-Deduct Stok", "ACID & Locking", "Pessimistic Locking & Transaksi")

    co_code = (
        "DELIMITER $$\n"
        "CREATE PROCEDURE sp_CheckoutItem(\n"
        "    IN p_Nonota CHAR(10), IN p_KodeProduk CHAR(4), IN p_Qty INT\n"
        ")\n"
        "BEGIN\n"
        "    DECLARE v_stok_saat_ini INT;\n"
        "    DECLARE v_harga_produk INT;\n"
        "    DECLARE EXIT HANDLER FOR SQLEXCEPTION\n"
        "    BEGIN\n"
        "        ROLLBACK; -- Batalkan seluruh perubahan jika terjadi galat\n"
        "        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Transaksi kasir gagal. Rollback executed.';\n"
        "    END;\n\n"
        "    START TRANSACTION;\n"
        "    -- 1. Validasi persediaan stok barang\n"
        "    SELECT stok, Harga INTO v_stok_saat_ini, v_harga_produk FROM produk WHERE KodeProduk = p_KodeProduk FOR UPDATE;\n"
        "    IF v_stok_saat_ini < p_Qty THEN\n"
        "        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Stok barang tidak mencukupi untuk checkout.';\n"
        "    END IF;\n\n"
        "    -- 2. Masukkan item transaksi & kurangi stok fisik\n"
        "    INSERT INTO itemnota (Nonota, KodeProduk, banyak, hargajual) VALUES (p_Nonota, p_KodeProduk, p_Qty, v_harga_produk);\n"
        "    UPDATE produk SET stok = stok - p_Qty WHERE KodeProduk = p_KodeProduk;\n"
        "    COMMIT; -- Simpan permanen perubahan transaksi\n"
        "END$$\n"
        "DELIMITER ;"
    )
    add_code_box(s10, Inches(1.0), Inches(1.85), Inches(7.2), Inches(4.6), "sp_CheckoutItem.sql (Transaction + Lock)", co_code)
    add_card(s10, Inches(8.4), Inches(1.85), Inches(3.9), Inches(2.2), "Pessimistic Locking (FOR UPDATE)", "Klausa 'FOR UPDATE' mengunci baris produk yang sedang dibeli agar tidak dibaca/diubah transaksi lain secara bersamaan, mencegah masalah *race condition* stok negatif.")
    add_card(s10, Inches(8.4), Inches(4.25), Inches(3.9), Inches(2.2), "ACID: START & ROLLBACK", "Jika operasi insert ke itemnota berhasil namun update stok gagal, perintah ROLLBACK memastikan basis data kembali ke status awal yang bersih.")
    add_notes(s10, "Tekankan prinsip ACID. Stored procedure adalah tempat ideal untuk membungkus transaksi bisnis agar tidak bocor ke sisi klien.")

    # =========================================================================
    # SLIDE 11: TUGAS MAHASISWA
    # =========================================================================
    s11 = prs.slides.add_slide(blank_layout)
    apply_slide_chassis(s11)
    add_header(s11, "10 · Lembar Tugas", "10 Soal Praktikum Mandiri Bertingkat", "Latihan Mandiri Mahasiswa", "4 Tingkat Kesulitan Berjenjang")

    tasks = [
        ("Tingkat 1: UDF Skalar", "• Soal 1: UDF fcCekStatusStok (KOSONG, KRITIS, TERSEDIA)\n• Soal 2: UDF fcLevelLoyalitas (PLATINUM, GOLD, SILVER, BRONZE)\n• Soal 3: UDF fcFormatRupiah ('Rp. 15.000')", "Level 1", COLOR_CYAN),
        ("Tingkat 2: Stored Procedure", "• Soal 4: SP sp_RegistrasiCustomer (Insert + auto umur)\n• Soal 5: SP sp_GantiPasswordKasir (Validasi 6 digit)\n• Soal 6: SP sp_TotalBelanjaNota (Parameter OUT grand total)", "Level 2", COLOR_BLUE),
        ("Tingkat 3: CURSOR Loop", "• Soal 7: SP sp_AkumulasiPoinNota (Loop baris per customer)\n• Soal 8: SP sp_LaporanRestokOtomatis (Loop stok < 10)", "Level 3", COLOR_AMBER),
        ("Tingkat 4: Error Handling", "• Soal 9: SP sp_BatalNotaTransaksi (Rollback stok + SIGNAL)\n• Soal 10: SP sp_AuditKasirProteksi (Catat log ke tabel audit)", "Level 4", COLOR_CORAL),
    ]
    card_w11 = Inches(2.68)
    for i, (tk_title, tk_desc, tk_lvl, tk_col) in enumerate(tasks):
        add_card(s11, Inches(1.0 + i * 2.88), Inches(1.85), card_w11, Inches(4.6), tk_title, tk_desc, num_tag=tk_lvl, border_color=tk_col, highlight=(i==0))

    add_notes(s11, "Mahasiswa wajib mengerjakan minimal Soal 1 s.d. Soal 8. Soal 9 dan 10 adalah nilai pengayaan khusus.")

    # =========================================================================
    # SLIDE 12: PANDUAN ASPRAK
    # =========================================================================
    s12 = prs.slides.add_slide(blank_layout)
    apply_slide_chassis(s12)
    add_header(s12, "11 · Panduan Asprak", "Kunci Jawaban & Panduan Verifikasi Teknis", "🔒 Akses Terproteksi", "Pedoman Khusus Dosen & Asisten")

    sol_code = (
        "-- KUNCI SOAL 1: fcCekStatusStok\n"
        "CREATE FUNCTION fcCekStatusStok(p_kodeproduk CHAR(4)) RETURNS VARCHAR(30) DETERMINISTIC READS SQL DATA\n"
        "BEGIN\n"
        "    DECLARE v_stok INT; DECLARE v_status VARCHAR(30);\n"
        "    SELECT stok INTO v_stok FROM produk WHERE kodeproduk = p_kodeproduk;\n"
        "    IF v_stok IS NULL THEN SET v_status = 'PRODUK TIDAK ADA';\n"
        "    ELSEIF v_stok = 0 THEN SET v_status = 'KOSONG';\n"
        "    ELSEIF v_stok <= 5 THEN SET v_status = 'KRITIS';\n"
        "    ELSE SET v_status = CONCAT('TERSEDIA (', v_stok, ' Unit)');\n"
        "    END IF;\n"
        "    RETURN v_status;\n"
        "END;\n\n"
        "-- KUNCI SOAL 7: sp_AkumulasiPoinNota (CURSOR)\n"
        "CREATE PROCEDURE sp_HitungTotalBelanjaKasir(IN p_KodeKasir CHAR(3), OUT p_GrandTotal INT)\n"
        "BEGIN\n"
        "    SELECT COALESCE(SUM(i.banyak * i.hargajual), 0) INTO p_GrandTotal\n"
        "    FROM nota n JOIN itemnota i ON n.Nonota = i.Nonota WHERE n.KodeKasir = p_KodeKasir;\n"
        "END;"
    )
    add_code_box(s12, Inches(1.0), Inches(1.85), Inches(7.2), Inches(4.6), "Solusi Resmi Soal 1 & 7", sol_code)
    add_card(s12, Inches(8.4), Inches(1.85), Inches(3.9), Inches(2.2), "Kriteria Penilaian", "1. Fungsionalitas kueri (40%)\n2. Penanganan kondisi batas NULL/0 (20%)\n3. Struktur kontrol & efisiensi kursor (20%)\n4. Keamanan transaksi & integritas DML (20%)")
    add_card(s12, Inches(8.4), Inches(4.25), Inches(3.9), Inches(2.2), "Rubrik Pengujian Lab", "Gunakan dataset 'minimarket_db.sql'. Lakukan pengujian dengan menginputkan produk dengan stok 0, stok 3, dan produk yang tidak terdaftar di tabel.")
    add_notes(s12, "Perhatikan apakah mahasiswa menggunakan SELECT INTO atau cursor.")

    # Simpan berkas
    os.makedirs("presentations", exist_ok=True)
    out_path = "presentations/Materi_Pengayaan_Stored_Procedure_UDF_Cursor.pptx"
    prs.save(out_path)
    print(f"Presentation saved successfully to: {out_path}")

    # Salin ke public agar bisa diunduh
    os.makedirs("public", exist_ok=True)
    pub_path = "public/Materi_Pengayaan_Stored_Procedure_UDF_Cursor.pptx"
    prs.save(pub_path)
    print(f"Presentation copied to public: {pub_path}")

    return os.path.abspath(out_path)

if __name__ == "__main__":
    create_presentation()
