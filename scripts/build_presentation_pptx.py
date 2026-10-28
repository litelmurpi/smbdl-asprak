#!/usr/bin/env python3
"""
Generator Presentasi PowerPoint Native (.pptx)
Materi Pengayaan SMBD Lanjut: Stored Procedure, UDF, Cursor & Error Handling
Menggunakan python-pptx dengan estetika Dark Modern Glassmorphism.
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.dml.color import RGBColor

# Palet Warna Dark Cyber / Liquid Glass
COLOR_BG_DARK = RGBColor(8, 11, 18)         # #080B12
COLOR_SURFACE_CARD = RGBColor(15, 23, 42)    # #0F172A
COLOR_SURFACE_HOVER = RGBColor(30, 41, 59)   # #1E293B
COLOR_SURFACE_CODE = RGBColor(3, 7, 18)      # #030712
COLOR_BORDER_SUBTLE = RGBColor(51, 65, 85)   # #334155
COLOR_BORDER_CYAN = RGBColor(0, 229, 255)    # #00E5FF
COLOR_CYAN = RGBColor(0, 229, 255)           # #00E5FF
COLOR_BLUE = RGBColor(37, 99, 235)           # #2563EB
COLOR_GREEN = RGBColor(16, 185, 129)         # #10B981
COLOR_RED = RGBColor(244, 63, 94)            # #F43F5E
COLOR_AMBER = RGBColor(245, 158, 11)         # #F59E0B
COLOR_TEXT_PRIMARY = RGBColor(255, 255, 255) # #FFFFFF
COLOR_TEXT_BODY = RGBColor(209, 221, 240)    # #D1DDF0
COLOR_TEXT_MUTED = RGBColor(148, 163, 184)   # #94A3B8

FONT_HEADING = "Plus Jakarta Sans"
FONT_BODY = "Inter"
FONT_MONO = "JetBrains Mono"

def create_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    def set_slide_background(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = COLOR_BG_DARK
        bg.line.fill.background()
        return bg

    def add_header(slide, category, title, subtitle=None):
        # Category Tag
        tag = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.4), Inches(2.8), Inches(0.36))
        tag.fill.solid()
        tag.fill.fore_color.rgb = RGBColor(12, 30, 60)
        tag.line.color.rgb = COLOR_CYAN
        tag.line.width = Pt(1)
        tf_tag = tag.text_frame
        tf_tag.vertical_anchor = MSO_ANCHOR.MIDDLE
        p_tag = tf_tag.paragraphs[0]
        p_tag.text = f"● {category.upper()}"
        p_tag.font.name = FONT_MONO
        p_tag.font.size = Pt(10)
        p_tag.font.bold = True
        p_tag.font.color.rgb = COLOR_CYAN
        p_tag.alignment = PP_ALIGN.CENTER

        # Title
        tb_title = slide.shapes.add_textbox(Inches(0.8), Inches(0.78), Inches(11.7), Inches(0.7))
        tf_title = tb_title.text_frame
        tf_title.word_wrap = True
        p_title = tf_title.paragraphs[0]
        p_title.text = title
        p_title.font.name = FONT_HEADING
        p_title.font.size = Pt(22)
        p_title.font.bold = True
        p_title.font.color.rgb = COLOR_TEXT_PRIMARY

        # Subtitle
        if subtitle:
            tb_sub = slide.shapes.add_textbox(Inches(0.8), Inches(1.42), Inches(11.7), Inches(0.38))
            tf_sub = tb_sub.text_frame
            tf_sub.word_wrap = True
            p_sub = tf_sub.paragraphs[0]
            p_sub.text = subtitle
            p_sub.font.name = FONT_BODY
            p_sub.font.size = Pt(11.5)
            p_sub.font.color.rgb = COLOR_TEXT_MUTED

        # Footer branding line
        tb_foot = slide.shapes.add_textbox(Inches(0.8), Inches(7.0), Inches(11.7), Inches(0.32))
        tf_foot = tb_foot.text_frame
        p_foot = tf_foot.paragraphs[0]
        p_foot.text = "SMBD Lanjut · Laboratorium Sistem Informasi Universitas Amikom Yogyakarta"
        p_foot.font.name = FONT_BODY
        p_foot.font.size = Pt(9.5)
        p_foot.font.color.rgb = COLOR_TEXT_MUTED

    def add_card(slide, left, top, width, height, card_title, body_text, num_tag=None, border_color=None):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_SURFACE_CARD
        card.line.color.rgb = border_color or COLOR_BORDER_SUBTLE
        card.line.width = Pt(1)

        # Title text box
        tb = slide.shapes.add_textbox(left + Inches(0.18), top + Inches(0.15), width - Inches(0.36), height - Inches(0.3))
        tf = tb.text_frame
        tf.word_wrap = True

        p1 = tf.paragraphs[0]
        if num_tag:
            run_num = p1.add_run()
            run_num.text = f"[{num_tag}] "
            run_num.font.name = FONT_MONO
            run_num.font.size = Pt(11)
            run_num.font.bold = True
            run_num.font.color.rgb = COLOR_CYAN

        run_title = p1.add_run()
        run_title.text = card_title
        run_title.font.name = FONT_HEADING
        run_title.font.size = Pt(12.5)
        run_title.font.bold = True
        run_title.font.color.rgb = COLOR_TEXT_PRIMARY

        p2 = tf.add_paragraph()
        p2.space_before = Pt(8)
        run_body = p2.add_run()
        run_body.text = body_text
        run_body.font.name = FONT_BODY
        run_body.font.size = Pt(10)
        run_body.font.color.rgb = COLOR_TEXT_BODY

        return card

    def add_code_box(slide, left, top, width, height, header_title, code_str):
        box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        box.fill.solid()
        box.fill.fore_color.rgb = COLOR_SURFACE_CODE
        box.line.color.rgb = COLOR_BORDER_SUBTLE
        box.line.width = Pt(1)

        # Header tag
        tb_hdr = slide.shapes.add_textbox(left + Inches(0.15), top + Inches(0.06), width - Inches(0.3), Inches(0.28))
        tf_hdr = tb_hdr.text_frame
        p_hdr = tf_hdr.paragraphs[0]
        p_hdr.text = f"Terminal / SQL: {header_title}"
        p_hdr.font.name = FONT_MONO
        p_hdr.font.size = Pt(9.5)
        p_hdr.font.bold = True
        p_hdr.font.color.rgb = COLOR_CYAN

        # Code content
        tb_code = slide.shapes.add_textbox(left + Inches(0.15), top + Inches(0.35), width - Inches(0.3), height - Inches(0.4))
        tf_code = tb_code.text_frame
        tf_code.word_wrap = True
        
        # Calculate optimal font size based on lines
        lines_count = len(code_str.strip().split("\n"))
        f_size = Pt(8.5) if lines_count > 18 else Pt(9.5)

        p_code = tf_code.paragraphs[0]
        run_code = p_code.add_run()
        run_code.text = code_str
        run_code.font.name = FONT_MONO
        run_code.font.size = f_size
        run_code.font.color.rgb = RGBColor(226, 232, 240)

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
            cell.fill.fore_color.rgb = RGBColor(24, 38, 70)
            p = cell.text_frame.paragraphs[0]
            p.text = ""
            run = p.add_run()
            run.text = h_text
            run.font.name = FONT_HEADING
            run.font.size = Pt(11)
            run.font.bold = True
            run.font.color.rgb = COLOR_CYAN
            p.alignment = PP_ALIGN.LEFT

        # Data Rows
        for r_idx, row_data in enumerate(rows):
            bg_cell = COLOR_SURFACE_CARD if r_idx % 2 == 0 else RGBColor(19, 29, 52)
            for c_idx, val in enumerate(row_data):
                cell = tbl.cell(r_idx + 1, c_idx)
                cell.fill.solid()
                cell.fill.fore_color.rgb = bg_cell
                p = cell.text_frame.paragraphs[0]
                p.text = ""
                run = p.add_run()
                run.text = str(val)
                run.font.name = FONT_BODY
                run.font.size = Pt(10)
                # First column bold
                if c_idx == 0:
                    run.font.bold = True
                    run.font.color.rgb = COLOR_TEXT_PRIMARY
                else:
                    run.font.color.rgb = RGBColor(241, 245, 249) # Bright White
                p.alignment = PP_ALIGN.LEFT

        return table_shape

    def add_notes(slide, notes_text):
        notes_slide = slide.notes_slide
        tf = notes_slide.notes_text_frame
        tf.text = notes_text

    # =========================================================================
    # SLIDE 1: COVER
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_background(s1)

    # Big Glow Box
    glow = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.0), Inches(11.733), Inches(5.4))
    glow.fill.solid()
    glow.fill.fore_color.rgb = RGBColor(12, 19, 36)
    glow.line.color.rgb = COLOR_BORDER_CYAN
    glow.line.width = Pt(1.5)

    # Tag Top
    tb_tag = s1.shapes.add_textbox(Inches(1.2), Inches(1.3), Inches(9.0), Inches(0.4))
    p = tb_tag.text_frame.paragraphs[0]
    p.text = "SISTEM INFORMASI 2024/2025 · SMBD LANJUT · UNIVERSITAS AMIKOM YOGYAKARTA"
    p.font.name = FONT_MONO
    p.font.size = Pt(10.5)
    p.font.bold = True
    p.font.color.rgb = COLOR_CYAN

    # Main Hero Title
    tb_hero = s1.shapes.add_textbox(Inches(1.2), Inches(1.8), Inches(10.8), Inches(1.6))
    tf = tb_hero.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Pemrograman Prosedural Database:\nStored Procedure, UDF & Cursor"
    p.font.name = FONT_HEADING
    p.font.size = Pt(32)
    p.font.bold = True
    p.font.color.rgb = COLOR_TEXT_PRIMARY

    # Description
    tb_desc = s1.shapes.add_textbox(Inches(1.2), Inches(3.6), Inches(10.5), Inches(0.9))
    tf = tb_desc.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Penyusunan logika bisnis terpusat di sisi server (RDBMS): User Defined Function (UDF), Stored Procedure dengan parameter IN/OUT/INOUT, iterasi baris per baris dengan CURSOR, dan penanganan galat terstruktur (SIGNAL SQLSTATE & HANDLER) pada kasus ritel minimarket 3NF."
    p.font.name = FONT_BODY
    p.font.size = Pt(13)
    p.font.color.rgb = COLOR_TEXT_BODY

    # 3 Badges
    badges = [
        ("Materi Praktikum", "Pengayaan Praktikum 4"),
        ("Studi Kasus Ritel", "Otomasi Nota & Stok 3NF"),
        ("Tantangan Tugas", "10 Soal Bertingkat + Kunci Solusi")
    ]
    for i, (b_label, b_val) in enumerate(badges):
        b_x = Inches(1.2 + i * 3.6)
        b_box = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, b_x, Inches(4.7), Inches(3.4), Inches(0.9))
        b_box.fill.solid()
        b_box.fill.fore_color.rgb = RGBColor(18, 28, 54)
        b_box.line.color.rgb = COLOR_BORDER_SUBTLE
        tf_b = b_box.text_frame
        p_l = tf_b.paragraphs[0]
        p_l.text = b_label.upper()
        p_l.font.name = FONT_MONO
        p_l.font.size = Pt(9.5)
        p_l.font.color.rgb = COLOR_TEXT_MUTED
        p_v = tf_b.add_paragraph()
        p_v.text = b_val
        p_v.font.name = FONT_HEADING
        p_v.font.size = Pt(12.5)
        p_v.font.bold = True
        p_v.font.color.rgb = COLOR_TEXT_PRIMARY

    add_notes(s1, "Selamat datang di modul pengayaan Sistem Manajemen Basis Data Lanjut (SMBD Lanjut). Pada sesi ini mahasiswa akan mempelajari cara membangun logika bisnis di sisi RDBMS MySQL menggunakan Stored Procedure, UDF, Cursor, dan Error Handling pada basis data minimarket 3NF.")

    # =========================================================================
    # SLIDE 2: ARSITEKTUR CLIENT-SERVER
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_background(s2)
    add_header(s2, "01 · Arsitektur Rutin", "Mengapa Memindahkan Logika ke Sisi Server?", "Stored Routine memindahkan beban eksekusi dari aplikasi klien langsung ke memori database engine.")

    cards_s2 = [
        ("Reduksi Latensi Jaringan", "Menggantikan belasan kueri SELECT dan UPDATE bolak-balik jaringan menjadi satu perintah CALL, memangkas network latency secara drastis.", "01"),
        ("Logika Terpusat & Konsisten", "Formula bisnis (diskon, aturan poin member, batas stok) didefinisikan satu kali di database; seluruh aplikasi kasir (desktop/web/mobile) menggunakan aturan seragam.", "02"),
        ("Execution Plan Caching", "Rencana eksekusi (*execution plan*) dikompilasi satu kali dan disimpan di memori buffer RDBMS. Eksekusi berikutnya berjalan instan tanpa parsing kueri ulang.", "03"),
        ("Isolasi Izin Akses & Keamanan", "Kasir cukup diberi izin EXECUTE pada procedure penjualan tanpa diberi izin langsung mengubah tabel master produk dan kasir fisik.", "04"),
    ]
    card_w = Inches(2.78)
    card_h = Inches(4.5)
    for i, (c_title, c_text, c_num) in enumerate(cards_s2):
        add_card(s2, Inches(0.8 + i * 2.98), Inches(2.0), card_w, card_h, c_title, c_text, num_tag=c_num)

    add_notes(s2, "Tekankan kepada mahasiswa bahwa keuntungan terbesar Stored Routine terletak pada berkurangnya traffic bolak-balik antara server aplikasi dan database. Kasir cukup mengirim 'CALL sp_Checkout(...)' daripada 5 kueri terpisah.")

    # =========================================================================
    # SLIDE 3: KOMPARASI FUNCTION VS PROCEDURE
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_background(s3)
    add_header(s3, "02 · Komparasi Hakiki", "Perbedaan Hakiki: Function vs Procedure", "Meskipun sama-sama blok kode terkompilasi, keduanya memiliki batasan arsitektural yang berbeda:")

    headers_s3 = ["Parameter Karakteristik", "User Defined Function (UDF)", "Stored Procedure"]
    rows_s3 = [
        ["Nilai Kembalian (Return)", "Wajib 1 nilai skalar via klausa RETURNS & RETURN.", "Tidak memiliki return langsung; lewat parameter OUT / INOUT / result set."],
        ["Metode Pemanggilan", "Dipanggil di dalam ekspresi kueri SQL biasa (SELECT fc(), WHERE fc() > 0).", "Dipanggil secara mandiri sebagai perintah terpisah: CALL sp_name(argumen);."],
        ["Manipulasi Fisik (DML)", "Sangat dibatasi; dilarang mengubah state tabel (INSERT/UPDATE/DELETE) pada kueri baca.", "Bebas DML penuh; dapat memutasi data, transaksi COMMIT/ROLLBACK, dan dynamic SQL."],
        ["Fokus Penggunaan", "Kalkulasi skalar, format teks, konversi mata uang, atau generator kode unik.", "Alur kerja transaksi multi-tabel, batch processing berkala, dan otomasi checkout kasir."]
    ]
    add_table(s3, Inches(0.8), Inches(2.0), Inches(11.733), Inches(4.4), headers_s3, rows_s3, [Inches(2.8), Inches(4.46), Inches(4.46)])
    add_notes(s3, "Ingatkan aturan MySQL: Function tidak boleh melakukan INSERT/UPDATE/DELETE jika dipanggil dari SELECT. Jika butuh mengubah data tabel, wajib gunakan Stored Procedure.")

    # =========================================================================
    # SLIDE 4: ANATOMI USER DEFINED FUNCTION (UDF)
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_background(s4)
    add_header(s4, "03 · Function (UDF)", "Anatomi & Karakteristik User Defined Function", "Fungsi skalar mengolah nilai input dan menghasilkan tepat satu nilai keluaran.")

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
    add_code_box(s4, Inches(0.8), Inches(2.0), Inches(6.8), Inches(4.5), "fcHitungDiskon.sql", udf_code)

    add_card(s4, Inches(7.8), Inches(2.0), Inches(4.7), Inches(2.1), "Klausa DETERMINISTIC", "Wajib dideklarasikan pada sistem dengan replikasi binlog aktif. DETERMINISTIC menyatakan bahwa input yang sama selalu menghasilkan output yang sama persis.")
    add_card(s4, Inches(7.8), Inches(4.3), Inches(4.7), Inches(2.2), "Kategori Akses SQL", "• NO SQL: fungsi murni tanpa akses data tabel.\n• READS SQL DATA: fungsi membaca data tabel via SELECT INTO.\n• MODIFIES SQL DATA: memodifikasi data (hanya diizinkan di procedure).")
    add_notes(s4, "Jelaskan pentingnya klausa DELIMITER $$ agar MySQL tidak mengartikan titik koma di dalam fungsi sebagai akhir kueri.")

    # =========================================================================
    # SLIDE 5: MODE PARAMETER SP (IN, OUT, INOUT)
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    set_slide_background(s5)
    add_header(s5, "04 · Parameter SP", "Mode Parameter Stored Procedure: IN, OUT & INOUT", "Mekanisme pertukaran data antara pemanggil (caller) dan server prosedur database.")

    params = [
        ("IN (Input Param)", "Bersifat Pass-by-Value (read-only). Nilai dikirim oleh caller ke dalam prosedur. Prosedur dapat mengubah variabel lokalnya, tetapi nilai variabel pemanggil di luar tidak berubah.", "IN"),
        ("OUT (Output Param)", "Bersifat Pass-by-Reference (write-only). Nilai awal saat masuk diabaikan (NULL). Prosedur mengisi nilai ke parameter ini, dan nilainya dapat dibaca oleh caller setelah selesai.", "OUT"),
        ("INOUT (Dual Param)", "Bersifat Dua Arah (read-write). Caller mengirimkan nilai awal ke prosedur, kemudian prosedur memproses dan mengubah nilai tersebut kembali ke caller.", "INOUT")
    ]
    for i, (p_title, p_desc, p_badge) in enumerate(params):
        add_card(s5, Inches(0.8 + i * 3.98), Inches(2.0), Inches(3.78), Inches(2.2), p_title, p_desc, num_tag=p_badge)

    sp_code = (
        "DELIMITER $$\n"
        "CREATE PROCEDURE sp_HitungBonusKasir(\n"
        "    IN  p_KodeKasir VARCHAR(3),      -- Input: kode kasir\n"
        "    OUT p_TotalNota INT,             -- Output: jumlah nota ditangani\n"
        "    INOUT p_SaldoBonus DECIMAL(12,2) -- Input & Output: saldo bonus\n"
        ")\n"
        "BEGIN\n"
        "    SELECT COUNT(*) INTO p_TotalNota FROM nota WHERE KodeKasir = p_KodeKasir;\n"
        "    SET p_SaldoBonus = p_SaldoBonus + (p_TotalNota * 2500);\n"
        "END$$\n"
        "DELIMITER ;\n"
        "-- Eksekusi: SET @b = 50000; CALL sp_HitungBonusKasir('001', @nota, @b); SELECT @nota, @b;"
    )
    add_code_box(s5, Inches(0.8), Inches(4.4), Inches(11.733), Inches(2.2), "Sintaks Parameter IN, OUT, INOUT", sp_code)
    add_notes(s5, "Tekankan bahwa variabel session di MySQL menggunakan simbol '@' (contoh: @total, @bonus). Parameter OUT dan INOUT wajib dipanggil menggunakan variabel session ini.")

    # =========================================================================
    # SLIDE 6: CONTROL FLOW
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    set_slide_background(s6)
    add_header(s6, "05 · Control Flow", "Struktur Kontrol Alur Logika di MySQL", "Membangun percabangan keputusan dan iterasi algoritmik di sisi database engine.")

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
    add_code_box(s6, Inches(0.8), Inches(2.0), Inches(5.7), Inches(4.5), "Percabangan (IF & CASE)", cf_code1)

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
    add_code_box(s6, Inches(6.8), Inches(2.0), Inches(5.7), Inches(4.5), "Pengulangan (WHILE & LOOP)", cf_code2)
    add_notes(s6, "Ingatkan perbedaan END IF; dan END CASE; yang wajib diakhiri titik koma di blok BEGIN...END.")

    # =========================================================================
    # SLIDE 7: CURSOR
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    set_slide_background(s7)
    add_header(s7, "06 · Cursor & Iterasi", "Pengolahan Baris Tunggal Menggunakan CURSOR", "Mekanisme membaca result set baris per baris secara berurutan (*read-only, non-scrollable*).")

    cursor_steps = [
        ("1. DECLARE", "Mendeklarasikan nama kursor dan kueri SELECT yang akan ditampung.", "01"),
        ("2. OPEN", "Mengeksekusi kueri SELECT dan menginisialisasi pointer data ke baris awal.", "02"),
        ("3. FETCH", "Mengambil nilai kolom baris aktif ke variabel lokal dan menggeser pointer.", "03"),
        ("4. CLOSE", "Menutup kursor dan membebaskan alokasi memori buffer RDBMS.", "04"),
    ]
    for i, (cs_title, cs_desc, cs_num) in enumerate(cursor_steps):
        add_card(s7, Inches(0.8 + i * 2.98), Inches(2.0), Inches(2.78), Inches(1.8), cs_title, cs_desc, num_tag=cs_num)

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
    add_code_box(s7, Inches(0.8), Inches(4.0), Inches(11.733), Inches(2.6), "Alur Lengkap Implementasi CURSOR", cur_sql)
    add_notes(s7, "Jelaskan urutan deklarasi variabel di MySQL: variabel biasa dulu, lalu CURSOR, baru kemudian HANDLER. Urutan ini tidak boleh terbalik.")

    # =========================================================================
    # SLIDE 8: ERROR HANDLING & TRANSACTION
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    set_slide_background(s8)
    add_header(s8, "07 · Error Handling", "Penanganan Galat Terstruktur & Integritas Transaksi", "Menjamin konsistensi database menggunakan DECLARE HANDLER dan SIGNAL kustom.")

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
    add_code_box(s8, Inches(0.8), Inches(2.0), Inches(7.5), Inches(4.5), "sp_ValidasiTambahKasir.sql", err_code)

    add_card(s8, Inches(8.5), Inches(2.0), Inches(4.0), Inches(2.1), "SIGNAL SQLSTATE '45000'", "SQLSTATE '45000' adalah kode standar ANSI SQL untuk mendefinisikan *unhandled user-defined exception*. Pesan galat kustom dikirim langsung ke aplikasi.")
    add_card(s8, Inches(8.5), Inches(4.3), Inches(4.0), Inches(2.2), "CONTINUE vs EXIT HANDLER", "• EXIT: Menyetop eksekusi blok kode dan langsung keluar dari compound statement.\n• CONTINUE: Menjalankan aksi handler dan tetap melanjutkan baris instruksi berikutnya.")
    add_notes(s8, "Tekankan bahwa penanganan galat terstruktur mencegah aplikasi crash tanpa pesan yang jelas saat terjadi kesalahan integritas data.")

    # =========================================================================
    # SLIDE 9: SKEMA FISIK 5 TABEL MINIMARKET (3NF)
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    set_slide_background(s9)
    add_header(s9, "08 · Studi Kasus 3NF", "Skema Fisik 5 Tabel Basis Data Minimarket", "Hasil normalisasi Third Normal Form (3NF) kasus ritel kelompok 7 Amikom:")

    tabel_cards = [
        ("KASIR (Parent)", "• KodeKasir: CHAR(3) [PK]\n• NamaKasir: VARCHAR(30)\n• Pass: CHAR(6) [CHK 6 char]", "Tabel Petugas"),
        ("CUSTOMER (Parent)", "• KodeCus: CHAR(5) [PK]\n• NamaCus: VARCHAR(50)\n• PointTerkumpul: INT", "Tabel Anggota"),
        ("PRODUK (Parent)", "• KodeProduk: CHAR(4) [PK]\n• NamaProduk: VARCHAR(50)\n• Harga: INT, stok: INT", "Barang Toko"),
        ("NOTA (Child / Header)", "• Nonota: CHAR(10) [PK]\n• KodeKasir: FK kasir\n• KodeCus: FK customer", "Header Transaksi"),
        ("ITEMNOTA (Bridge N:M)", "• Nonota: CHAR(10) [PK, FK]\n• KodeProduk: CHAR(4) [PK, FK]\n• banyak: INT, hargajual: INT", "Detail Belanja"),
    ]
    card_w9 = Inches(2.2)
    for i, (t_name, t_cols, t_sub) in enumerate(tabel_cards):
        add_card(s9, Inches(0.8 + i * 2.38), Inches(2.0), card_w9, Inches(2.4), t_name, t_cols, num_tag=str(i+1))

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
    add_code_box(s9, Inches(0.8), Inches(4.6), Inches(11.733), Inches(2.0), "DDL Tabel Jembatan (Bridge Table ITEMNOTA)", sql_ddl_snip)
    add_notes(s9, "Jelaskan mengapa Nonota dan KodeProduk dijadikan Composite Primary Key pada itemnota untuk mencegah duplikasi item belanja di nota yang sama.")

    # =========================================================================
    # SLIDE 10: TRANSAKSI CHECKOUT LENGKAP
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    set_slide_background(s10)
    add_header(s10, "09 · Prosedur Transaksi", "Studi Kasus: Checkout Kasir & Auto-Deduct Stok", "Otomasi transaksi kasir dengan proteksi atomisitas (ACID Transactions):")

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
    add_code_box(s10, Inches(0.8), Inches(2.0), Inches(7.5), Inches(4.5), "sp_CheckoutItem.sql (Transaction + Lock)", co_code)

    add_card(s10, Inches(8.5), Inches(2.0), Inches(4.0), Inches(2.1), "Pessimistic Locking (FOR UPDATE)", "Klausa 'FOR UPDATE' mengunci baris produk yang sedang dibeli agar tidak dibaca/diubah transaksi lain secara bersamaan, mencegah masalah *race condition* stok negatif.")
    add_card(s10, Inches(8.5), Inches(4.3), Inches(4.0), Inches(2.2), "ACID: START TRANSACTION & ROLLBACK", "Jika operasi insert ke itemnota berhasil namun update stok gagal, perintah ROLLBACK memastikan basis data kembali ke status awal yang bersih.")
    add_notes(s10, "Tekankan prinsip ACID. Stored procedure adalah tempat ideal untuk membungkus transaksi bisnis agar tidak bocor ke sisi klien.")

    # =========================================================================
    # SLIDE 11: TUGAS MAHASISWA
    # =========================================================================
    s11 = prs.slides.add_slide(blank_layout)
    set_slide_background(s11)
    add_header(s11, "10 · Lembar Tugas", "10 Soal Praktikum Mandiri Bertingkat", "Latihan berjenjang 4 tingkat kesulitan untuk menguji penguasaan materi:")

    tasks = [
        ("Tingkat 1: UDF Skalar", "• Soal 1: UDF fcCekStatusStok (KOSONG, KRITIS, TERSEDIA)\n• Soal 2: UDF fcLevelLoyalitas (PLATINUM, GOLD, SILVER, BRONZE)\n• Soal 3: UDF fcFormatRupiah ('Rp. 15.000')", "Level 1"),
        ("Tingkat 2: Stored Procedure", "• Soal 4: SP sp_RegistrasiCustomer (Insert + auto cek umur)\n• Soal 5: SP sp_GantiPasswordKasir (Validasi password lama & 6 digit)\n• Soal 6: SP sp_TotalBelanjaNota (Parameter OUT grand total belanja)", "Level 2"),
        ("Tingkat 3: CURSOR Loop", "• Soal 7: SP sp_AkumulasiPoinNota (Loop baris nota per customer)\n• Soal 8: SP sp_LaporanRestokOtomatis (Loop produk stok < 10)", "Level 3"),
        ("Tingkat 4: Error Handling", "• Soal 9: SP sp_BatalNotaTransaksi (Rollback stok + SIGNAL)\n• Soal 10: SP sp_AuditKasirProteksi (Catat log ke tabel audit)", "Level 4"),
    ]
    card_w11 = Inches(2.78)
    for i, (tk_title, tk_desc, tk_lvl) in enumerate(tasks):
        add_card(s11, Inches(0.8 + i * 2.98), Inches(2.0), card_w11, Inches(4.5), tk_title, tk_desc, num_tag=tk_lvl)

    add_notes(s11, "Mahasiswa wajib mengerjakan minimal Soal 1 s.d. Soal 8. Soal 9 dan 10 adalah nilai pengayaan khusus bagi praktikan yang ingin mendapatkan nilai sempurna A.")

    # =========================================================================
    # SLIDE 12: PANDUAN ASPRAK (KUNCI JAWABAN)
    # =========================================================================
    s12 = prs.slides.add_slide(blank_layout)
    set_slide_background(s12)
    add_header(s12, "11 · Panduan Asprak", "Kunci Jawaban & Panduan Pengujian Teknis", "Referensi kueri resmi asisten praktikum dalam menguji hasil pekerjaan praktikan:")

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
    add_code_box(s12, Inches(0.8), Inches(2.0), Inches(7.5), Inches(4.5), "Solusi Resmi Soal 1 & 7", sol_code)

    add_card(s12, Inches(8.5), Inches(2.0), Inches(4.0), Inches(2.1), "Kriteria Penilaian", "1. Fungsionalitas kueri (40%)\n2. Penanganan kondisi batas NULL/0 (20%)\n3. Struktur kontrol & efisiensi kursor (20%)\n4. Keamanan transaksi & integritas DML (20%)")
    add_card(s12, Inches(8.5), Inches(4.3), Inches(4.0), Inches(2.2), "Rubrik Pengujian Lab", "Gunakan dataset 'minimarket_db.sql'. Lakukan pengujian dengan menginputkan produk dengan stok 0, stok 3, dan produk yang tidak terdaftar di tabel.")
    add_notes(s12, "Perhatikan apakah mahasiswa menggunakan SELECT INTO atau cursor. Jika hanya butuh kalkulasi agregat SUM, ingatkan bahwa kueri agregat murni jauh lebih cepat daripada membuat cursor loop.")

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
