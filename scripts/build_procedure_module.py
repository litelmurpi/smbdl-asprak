import os
import sys
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

def create_procedure_document(filename="Modul_Pengayaan_SMBD_Lanjut_Procedure_Function.docx"):
    doc = docx.Document()
    
    # ---------------- PAGE SETUP (Letter Size, 0.75 inch margins) ----------------
    for section in doc.sections:
        section.page_width = Inches(8.5)
        section.page_height = Inches(11.0)
        section.top_margin = Inches(0.75)
        section.bottom_margin = Inches(0.75)
        section.left_margin = Inches(0.75)
        section.right_margin = Inches(0.75)
        
        # Header setup: Right aligned "SISTEM INFORMASI 2024/2025     [PAGE]"
        header = section.header
        hp = header.paragraphs[0]
        hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        hrun = hp.add_run("SISTEM INFORMASI 2024/2025     ")
        hrun.font.name = "Calibri"
        hrun.font.size = Pt(9.5)
        hrun.font.color.rgb = RGBColor(120, 120, 120)
        
        fld = OxmlElement('w:fldSimple')
        fld.set(qn('w:instr'), 'PAGE')
        hp._p.append(fld)
        
    # Styles definition
    styles = doc.styles
    normal_style = styles['Normal']
    normal_style.font.name = 'Calibri'
    normal_style.font.size = Pt(10)
    normal_style.font.color.rgb = RGBColor(30, 30, 30)
    normal_style.paragraph_format.line_spacing = 1.15
    normal_style.paragraph_format.space_after = Pt(4)

    # ---------------- XML HELPER FUNCTIONS ----------------
    def set_cell_shading(cell, color_hex):
        shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
        cell._tc.get_or_add_tcPr().append(shd)

    def set_cell_margins(cell, top=100, bottom=100, left=140, right=140):
        tcPr = cell._tc.get_or_add_tcPr()
        tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
        tcPr.append(tcMar)

    def set_table_borders(table, color="D0D7DE", sz="4", val="single"):
        tblPr = table._tbl.tblPr
        borders = parse_xml(
            f'<w:tblBorders {nsdecls("w")}>'
            f'<w:top w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
            f'<w:bottom w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
            f'<w:left w:val="none"/>'
            f'<w:right w:val="none"/>'
            f'<w:insideH w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
            f'<w:insideV w:val="none"/>'
            f'</w:tblBorders>'
        )
        tblPr.append(borders)

    def add_title(text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_before = Pt(6)
        p.paragraph_format.space_after = Pt(10)
        run = p.add_run(text)
        run.font.name = "Calibri"
        run.font.size = Pt(12.5)
        run.font.bold = True
        run.font.color.rgb = RGBColor(15, 45, 80)
        return p

    def add_h1(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(13)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.font.name = "Calibri"
        run.font.size = Pt(11)
        run.font.bold = True
        run.font.color.rgb = RGBColor(20, 50, 95)
        return p

    def add_h2(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.font.name = "Calibri"
        run.font.size = Pt(10.5)
        run.font.bold = True
        run.font.color.rgb = RGBColor(35, 70, 115)
        return p

    def add_p(text, bold_prefix=None, space_after=4):
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(space_after)
        p.paragraph_format.line_spacing = 1.15
        if bold_prefix:
            r_pre = p.add_run(bold_prefix)
            r_pre.font.bold = True
            r_pre.font.name = "Calibri"
            r_pre.font.size = Pt(10)
            r_pre.font.color.rgb = RGBColor(25, 25, 25)
        run = p.add_run(text)
        run.font.name = "Calibri"
        run.font.size = Pt(10)
        return p

    def add_bullet(text, bold_prefix=None, level=0):
        p = doc.add_paragraph()
        p.paragraph_format.left_indent = Inches(0.25 * (level + 1))
        p.paragraph_format.first_line_indent = Inches(-0.18)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.line_spacing = 1.12
        
        r_bullet = p.add_run("• ")
        r_bullet.font.name = "Calibri"
        r_bullet.font.bold = True
        r_bullet.font.size = Pt(10)
        r_bullet.font.color.rgb = RGBColor(40, 70, 110)
        
        if bold_prefix:
            r_pre = p.add_run(bold_prefix)
            r_pre.font.bold = True
            r_pre.font.name = "Calibri"
            r_pre.font.size = Pt(10)
            r_pre.font.color.rgb = RGBColor(30, 30, 30)
            
        run = p.add_run(text)
        run.font.name = "Calibri"
        run.font.size = Pt(10)
        return p

    def add_code(code_text):
        table = doc.add_table(rows=1, cols=1)
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        cell = table.cell(0, 0)
        cell.width = Inches(7.0)
        set_cell_shading(cell, "F5F7FA")
        set_cell_margins(cell, top=90, bottom=90, left=130, right=130)
        
        tcPr = cell._tc.get_or_add_tcPr()
        borders = parse_xml(
            f'<w:tcBorders {nsdecls("w")}>'
            f'<w:top w:val="single" w:sz="4" w:space="0" w:color="D8DFE8"/>'
            f'<w:left w:val="single" w:sz="18" w:space="0" w:color="1A4A7A"/>'
            f'<w:bottom w:val="single" w:sz="4" w:space="0" w:color="D8DFE8"/>'
            f'<w:right w:val="single" w:sz="4" w:space="0" w:color="D8DFE8"/>'
            f'</w:tcBorders>'
        )
        tcPr.append(borders)
        
        cp = cell.paragraphs[0]
        cp.paragraph_format.space_before = Pt(0)
        cp.paragraph_format.space_after = Pt(0)
        cp.paragraph_format.line_spacing = 1.1
        c_run = cp.add_run(code_text.strip())
        c_run.font.name = 'Consolas'
        c_run.font.size = Pt(8.5)
        c_run.font.color.rgb = RGBColor(30, 45, 65)
        
        sp = doc.add_paragraph()
        sp.paragraph_format.space_before = Pt(2)
        sp.paragraph_format.space_after = Pt(3)

    def add_custom_table(headers, data, col_widths=None):
        table = doc.add_table(rows=len(data) + 1, cols=len(headers))
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        set_table_borders(table)
        
        hdr_cells = table.rows[0].cells
        for i, header_text in enumerate(headers):
            hdr_cells[i].text = header_text
            set_cell_shading(hdr_cells[i], "1F3A60")
            set_cell_margins(hdr_cells[i], top=100, bottom=100, left=120, right=120)
            p = hdr_cells[i].paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.runs[0].font.name = "Calibri"
            p.runs[0].font.bold = True
            p.runs[0].font.size = Pt(9)
            p.runs[0].font.color.rgb = RGBColor(255, 255, 255)
            
        for r_idx, row_data in enumerate(data):
            row_cells = table.rows[r_idx + 1].cells
            bg_color = "F8FAFC" if r_idx % 2 == 1 else "FFFFFF"
            for c_idx, cell_value in enumerate(row_data):
                row_cells[c_idx].text = str(cell_value)
                set_cell_shading(row_cells[c_idx], bg_color)
                set_cell_margins(row_cells[c_idx], top=80, bottom=80, left=110, right=110)
                p = row_cells[c_idx].paragraphs[0]
                p.paragraph_format.space_after = Pt(1)
                p.paragraph_format.space_before = Pt(1)
                p.paragraph_format.line_spacing = 1.1
                p.runs[0].font.name = "Calibri"
                p.runs[0].font.size = Pt(8.5)
                p.runs[0].font.color.rgb = RGBColor(40, 40, 40)
                if c_idx == 0:
                    p.runs[0].font.bold = True
                    
        if col_widths:
            for row in table.rows:
                for c_idx, w in enumerate(col_widths):
                    row.cells[c_idx].width = Inches(w)
                    
        sp = doc.add_paragraph()
        sp.paragraph_format.space_before = Pt(2)
        sp.paragraph_format.space_after = Pt(3)

    # ---------------- DOCUMENT CONTENT GENERATION ----------------
    print("Writing Stored Routine Document Content...")

    add_title("MATERI PRAKTIKUM PENGAYAAN: PEMBAHASAN MENDALAM STORED PROCEDURE, UDF, CURSOR & ERROR HANDLING")

    add_p(
        "Modul pengayaan ini disusun secara komprehensif untuk melengkapi Materi Praktikum 4 "
        "(USER DEFINE FUNCTION & STORE PROCEDURE) pada mata kuliah Sistem Manajemen Basis Data Lanjut (SMBD Lanjut). "
        "Fokus modul ini adalah memberikan pemahaman mendalam mengenai arsitektur logika bisnis terkompilasi di sisi server (RDBMS), "
        "perbedaan hakiki antara User Defined Function (UDF) dan Stored Procedure, klasifikasi parameter IN, OUT, dan INOUT, "
        "mekanisme iterasi baris per baris dengan CURSOR, penanganan eksepsi (Error Handling) menggunakan HANDLER dan SIGNAL SQLSTATE, "
        "serta penerapan skenario otomasi transaksi kasir minimarket 3NF lengkap dengan 10 latihan soal bertingkat dan lampiran kunci jawaban khusus asisten/dosen."
    )

    # =========================================================================
    # 1. KONSEP DASAR PEMROGRAMAN PROSEDURAL DI RDBMS
    # =========================================================================
    add_h1("1. KONSEP DASAR & ARSITEKTUR STORED ROUTINES")
    add_p(
        "Dalam rekayasa sistem basis data relasional enterprise, Stored Routine adalah blok kode prosedural SQL yang disimpan "
        "secara permanen di dalam katalog basis data (data dictionary) dan dieksekusi langsung oleh database engine di sisi server. "
        "Stored Routine terdiri dari dua jenis utama: User Defined Function (UDF) dan Stored Procedure."
    )

    add_h2("1.1 Mengapa Memindahkan Logika Bisnis ke Database?")
    add_bullet(
        "Pada arsitektur tradisional, aplikasi klien harus mengirimkan belasan kueri SELECT, INSERT, dan UPDATE secara bolak-balik "
        "melalui jaringan. Dengan Stored Routine, aplikasi klien cukup mengirimkan satu perintah CALL, dan seluruh rangkaian kueri dieksekusi "
        "langsung di memori server, memangkas latensi jaringan secara dramatis.",
        bold_prefix="Reduksi Lalu Lintas Jaringan (Network Traffic Optimization): "
    )
    add_bullet(
        "Logika transaksi kritis—seperti pemotongan stok barang, kalkulasi diskon member, dan akumulasi poin reward—disentralisasi "
        "di dalam basis data. Semua aplikasi klien (aplikasi POS kasir, aplikasi mobile e-commerce, web portal admin) memanggil subrutin "
        "yang sama, menghilangkan risiko inkonsistensi perhitungan.",
        bold_prefix="Sentralisasi Logika Bisnis (Centralized Business Logic): "
    )
    add_bullet(
        "Stored Routine dikompilasi satu kali dan rencana eksekusinya disimpan di dalam cache memori RDBMS. Eksekusi berulang "
        "tidak memerlukan proses parsing dan optimasi sintaks dari awal, menghasilkan performa eksekusi kueri yang jauh lebih cepat.",
        bold_prefix="Kompilasi dan Eksekusi Cepat (Execution Plan Caching): "
    )
    add_bullet(
        "Aplikasi kasir tidak perlu diberi izin akses langsung (INSERT/UPDATE) ke tabel fisik PRODUK dan CUSTOMER. Cukup berikan izin "
        "EXECUTE pada Stored Procedure checkout, sehingga basis data terlindungi dari manipulasi langsung.",
        bold_prefix="Lapisan Keamanan Berlapis (Security & Privilege Isolation): "
    )

    add_h2("1.2 Perbedaan Hakiki Function vs Stored Procedure")
    headers_fp = ["Parameter Komparasi", "User Defined Function (UDF)", "Stored Procedure"]
    data_fp = [
        ["Nilai Kembalian (Return)", "Wajib mengembalikan satu nilai skalar tunggal melalui klausa RETURNS dan pernyataan RETURN.", "Tidak mengembalikan nilai melalui klausa RETURN; dapat mengembalikan nilai via parameter OUT/INOUT atau result set."],
        ["Cara Pemanggilan", "Dipanggil di dalam ekspresi kueri SQL biasa (contoh: SELECT fc_name(), WHERE fc_name() > 0).", "Dipanggil secara mandiri menggunakan perintah eksplisit: CALL proc_name(param)."],
        ["Manipulasi Data Fisik (DML)", "Sangat dibatasi; secara standar tidak boleh melakukan modifikasi data (INSERT/UPDATE/DELETE) yang mengubah state tabel.", "Mendukung eksekusi DML penuh, transaksi (COMMIT/ROLLBACK), dynamic SQL, dan pemanggilan procedure lain."],
        ["Tujuan Utama", "Melakukan kalkulasi matematis, manipulasi teks, atau transformasi data yang menghasilkan nilai tunggal.", "Mengeksekusi alur kerja bisnis lengkap, batch processing, dan transaksi multi-tabel."]
    ]
    add_custom_table(headers_fp, data_fp, col_widths=[1.8, 2.6, 2.6])

    # =========================================================================
    # 2. USER DEFINED FUNCTION (UDF)
    # =========================================================================
    add_h1("2. USER DEFINED FUNCTION (UDF) DI MYSQL")
    add_p(
        "User Defined Function memungkinkan perancang basis data membuat fungsi matematis, pemformatan string, "
        "dan logika kustom yang belum disediakan oleh fungsi bawaan (built-in functions) MySQL."
    )

    add_h2("2.1 Sintaks Lengkap Deklarasi Function")
    add_code(
"""CREATE [DEFINER = user]
FUNCTION [IF NOT EXISTS] func_name ([param_name param_type, ...])
RETURNS return_type
[DETERMINISTIC | NOT DETERMINISTIC]
[CONTAINS SQL | NO SQL | READS SQL DATA | MODIFIES SQL DATA]
[SQL SECURITY { DEFINER | INVOKER }]
BEGIN
    DECLARE variabel_lokal tipe_data [DEFAULT nilai];
    -- Logika komputasi prosedural
    RETURN nilai_kembalian;
END;"""
    )

    add_h2("2.2 Karakteristik Penentu Function")
    add_bullet(
        "Fungsi selalu menghasilkan nilai keluaran yang sama jika diberikan argumen input yang sama. "
        "Contoh: fungsi penambah angka atau pemotong string. Wajib dideklarasikan pada sistem dengan binary logging aktif.",
        bold_prefix="DETERMINISTIC: "
    )
    add_bullet(
        "Fungsi dapat menghasilkan nilai berbeda meskipun argumennya sama (contoh: fungsi yang membaca waktu saat ini NOW() atau membaca data tabel fisik yang dinamis).",
        bold_prefix="NOT DETERMINISTIC: "
    )
    add_bullet(
        "Memberitahukan kepada query optimizer bahwa fungsi hanya membaca data dari tabel (SELECT) tanpa melakukan mutasi data.",
        bold_prefix="READS SQL DATA: "
    )

    add_h2("2.3 Contoh Implementasi UDF: Generator Kode & Poin Belanja")
    add_code(
"""-- 1. Mengubah Delimiter agar titik-koma di dalam blok BEGIN-END tidak memutus eksekusi
DELIMITER $$

-- 2. Function Generator Nomor Nota Transaksi Otomatis (Format: YYMMDDXXXX)
CREATE FUNCTION fcGenerateNoNota(tgl DATE)
RETURNS CHAR(10)
DETERMINISTIC
READS SQL DATA
BEGIN
    DECLARE tgl_prefix CHAR(6);
    DECLARE last_seq INT DEFAULT 0;
    DECLARE new_nota CHAR(10);
    
    -- Mengambil format YYMMDD (contoh: 2022-08-03 -> '220803')
    SET tgl_prefix = DATE_FORMAT(tgl, '%y%m%d');
    
    -- Mencari nomor urut transaksi terakhir pada tanggal tersebut
    SELECT IFNULL(MAX(CAST(RIGHT(nonota, 4) AS UNSIGNED)), 0) INTO last_seq
    FROM nota
    WHERE LEFT(nonota, 6) = tgl_prefix;
    
    -- Menggabungkan tanggal prefix dengan 4 digit nomor urut baru
    SET new_nota = CONCAT(tgl_prefix, LPAD(last_seq + 1, 4, '0'));
    RETURN new_nota;
END$$

-- 3. Function Kalkulasi Poin Belanja (1 Poin tiap kelipatan Rp 10.000)
CREATE FUNCTION fcHitungPoinBelanja(total_belanja INT)
RETURNS INT
DETERMINISTIC
NO SQL
BEGIN
    DECLARE jml_poin INT DEFAULT 0;
    IF total_belanja >= 10000 THEN
        SET jml_poin = FLOOR(total_belanja / 10000);
    END IF;
    RETURN jml_poin;
END$$

DELIMITER ;

-- Pengujian Eksekusi:
SELECT fcGenerateNoNota('2022-08-03') AS nota_baru;
SELECT fcHitungPoinBelanja(14800) AS poin_diperoleh;"""
    )

    # =========================================================================
    # 3. STORED PROCEDURE & PARAMETER IN, OUT, INOUT
    # =========================================================================
    add_h1("3. STORED PROCEDURE: MANAJEMEN PARAMETER & TRANSAKSI")
    add_p(
        "Stored Procedure dirancang untuk menangani tugas transaksi yang kompleks. Parameter pada Stored Procedure "
        "dapat dikonfigurasikan ke dalam tiga mode interaksi data:"
    )

    add_h2("3.1 Tiga Mode Parameter Stored Procedure")
    headers_pm = ["Mode Parameter", "Arah Aliran Data", "Karakteristik & Perilaku Teknis"]
    data_pm = [
        ["IN (Default)", "Pemanggil -> Procedure", "Nilai dilewatkan ke dalam procedure sebagai input. Procedure dapat membaca nilai tersebut, namun perubahan variabel di dalam procedure tidak akan mempengaruhi nilai pemanggil."],
        ["OUT", "Procedure -> Pemanggil", "Variabel diinisialisasi sebagai NULL di dalam procedure. Procedure mengisinya dengan hasil perhitungan, dan nilai tersebut dikembalikan ke pemanggil saat procedure selesai."],
        ["INOUT", "Pemanggil <-> Procedure", "Variabel membawa nilai awal dari pemanggil ke dalam procedure, nilainya dimodifikasi oleh procedure, dan nilai hasil akhirnya dikembalikan ke pemanggil."]
    ]
    add_custom_table(headers_pm, data_pm, col_widths=[1.5, 2.0, 3.5])

    add_h2("3.2 Contoh Implementasi Parameter IN, OUT, dan INOUT")
    add_code(
"""DELIMITER $$

-- Procedure dengan parameter IN dan OUT: Registrasi Member Baru & Mengembalikan Kode Barunya
CREATE PROCEDURE spRegistrasiMember(
    IN p_nama VARCHAR(50),
    IN p_tgllahir DATE,
    IN p_jenkel CHAR(1),
    IN p_alamat VARCHAR(100),
    IN p_hp VARCHAR(15),
    OUT p_kode_dihasilkan CHAR(5)
)
BEGIN
    DECLARE last_num INT DEFAULT 0;
    
    -- Generate Kode Member Baru (Format M0001, M0002, dst)
    SELECT IFNULL(MAX(CAST(RIGHT(kodecus, 4) AS UNSIGNED)), 0) INTO last_num FROM customer;
    SET p_kode_dihasilkan = CONCAT('M', LPAD(last_num + 1, 4, '0'));
    
    -- Simpan ke tabel fisik customer
    INSERT INTO customer (kodecus, namacus, tgllahir, jenkelcus, almtcus, hpcus, pointterkumpul)
    VALUES (p_kode_dihasilkan, p_nama, p_tgllahir, p_jenkel, p_alamat, p_hp, 0);
END$$

-- Procedure dengan parameter INOUT: Menghitung Tambahan Poin Bonus Transaksi
CREATE PROCEDURE spHitungBonusLoyalitas(
    IN p_status_member VARCHAR(20),
    INOUT p_poin INT
)
BEGIN
    IF p_status_member = 'VIP' THEN
        SET p_poin = p_poin + 20; -- Bonus tambahan 20 poin
    ELSEIF p_status_member = 'REGULER' THEN
        SET p_poin = p_poin + 5;  -- Bonus tambahan 5 poin
    END IF;
END$$

DELIMITER ;

-- Pengujian Eksekusi Parameter OUT:
CALL spRegistrasiMember('Rina Melati', '1998-07-21', 'P', 'Yogyakarta', '081299887766', @kode_baru);
SELECT @kode_baru AS 'ID Member Terdaftar';

-- Pengujian Eksekusi Parameter INOUT:
SET @poin_awal = 10;
CALL spHitungBonusLoyalitas('VIP', @poin_awal);
SELECT @poin_awal AS 'Total Poin Setelah Bonus'; -- Output: 30"""
    )

    # =========================================================================
    # 4. KONTROL ALUR LOGIKA
    # =========================================================================
    add_h1("4. KONTROL ALUR LOGIKA (CONTROL FLOW STATEMENTS)")
    add_p("MySQL menyediakan struktur kendali prosedural lengkap di dalam blok BEGIN-END:")

    add_bullet(
        "Struktur percabangan bersyarat: IF kondisi THEN ... ELSEIF kondisi THEN ... ELSE ... END IF;",
        bold_prefix="Pernyataan IF-THEN-ELSE: "
    )
    add_bullet(
        "Struktur percabangan bernilai jamak: CASE ekspresi WHEN nilai THEN ... ELSE ... END CASE;",
        bold_prefix="Pernyataan CASE: "
    )
    add_bullet(
        "Perulangan tak terbatas yang dihentikan secara eksplisit menggunakan perintah LEAVE label_loop: [label:] LOOP ... IF kondisi THEN LEAVE [label]; END IF; END LOOP [label];",
        bold_prefix="Perulangan LOOP-LEAVE: "
    )
    add_bullet(
        "Perulangan dengan evaluasi kondisi di awal: WHILE kondisi DO ... END WHILE;",
        bold_prefix="Perulangan WHILE-DO: "
    )
    add_bullet(
        "Perulangan dengan evaluasi kondisi di akhir: REPEAT ... UNTIL kondisi END REPEAT;",
        bold_prefix="Perulangan REPEAT-UNTIL: "
    )

    # =========================================================================
    # 5. CURSOR & ITERASI DATA
    # =========================================================================
    add_h1("5. CURSOR & ITERASI BARIS DATA DI MYSQL")
    add_p(
        "Secara default, kueri SQL bekerja berbasis himpunan (set-based). Namun, ketika sistem membutuhkan evaluasi logika individual "
        "yang berbeda untuk setiap baris data, digunakan CURSOR. Cursor adalah penunjuk memori (pointer) yang menampung baris hasil kueri "
        "dan memungkinkan pembacaan data secara sekuensial baris per baris (*row-by-row navigation*)."
    )

    add_h2("5.1 Empat Siklus Hidup Cursor")
    add_bullet("Mendefinisikan kueri SQL yang akan ditampung ke dalam kursor: DECLARE nama_cursor CURSOR FOR select_statement;", bold_prefix="1. DECLARE CURSOR: ")
    add_bullet("Mendaftarkan penangan kondisi ketika cursor telah mencapai baris terakhir: DECLARE CONTINUE HANDLER FOR NOT FOUND SET v_selesai = 1;", bold_prefix="2. DECLARE HANDLER: ")
    add_bullet("Menginisialisasi memori dan mengeksekusi kueri pembentuk cursor: OPEN nama_cursor;", bold_prefix="3. OPEN: ")
    add_bullet("Mengambil nilai kolom pada baris aktif ke dalam variabel lokal: FETCH nama_cursor INTO var1, var2; dilanjutkan dengan penutupan memori: CLOSE nama_cursor;", bold_prefix="4. FETCH & CLOSE: ")

    add_h2("5.2 Contoh Nyata: Pembagian Bonus Poin Massal Customer (Modul 4 Halaman 17)")
    add_code(
"""DELIMITER $$

CREATE PROCEDURE spProsesBonusPoinMassal()
BEGIN
    DECLARE v_kodecus CHAR(5);
    DECLARE v_poin_saat_ini INT;
    DECLARE v_selesai INT DEFAULT 0;
    
    -- 1. Deklarasi Cursor untuk memilih customer (Kecuali customer umum M0000)
    DECLARE curCustomer CURSOR FOR
        SELECT kodecus, pointterkumpul 
        FROM customer 
        WHERE kodecus <> 'M0000';
        
    -- 2. Deklarasi Handler NOT FOUND
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET v_selesai = 1;
    
    -- 3. Membuka Cursor
    OPEN curCustomer;
    
    loopCustomer: LOOP
        -- 4. Mengambil baris data
        FETCH curCustomer INTO v_kodecus, v_poin_saat_ini;
        
        IF v_selesai = 1 THEN
            LEAVE loopCustomer;
        END IF;
        
        -- Evaluasi Aturan Bisnis Bonus Poin
        IF v_poin_saat_ini >= 100 THEN
            UPDATE customer SET pointterkumpul = pointterkumpul + 20 WHERE kodecus = v_kodecus;
        ELSEIF v_poin_saat_ini > 50 THEN
            UPDATE customer SET pointterkumpul = pointterkumpul + 15 WHERE kodecus = v_kodecus;
        ELSEIF v_poin_saat_ini > 20 THEN
            UPDATE customer SET pointterkumpul = pointterkumpul + 10 WHERE kodecus = v_kodecus;
        ELSE
            UPDATE customer SET pointterkumpul = pointterkumpul + 7 WHERE kodecus = v_kodecus;
        END IF;
    END LOOP loopCustomer;
    
    -- 5. Menutup Cursor
    CLOSE curCustomer;
    
    SELECT 'Pemrosesan bonus poin seluruh member selesai dieksekusi.' AS status_eksekusi;
END$$

DELIMITER ;

-- Eksekusi:
CALL spProsesBonusPoinMassal();"""
    )

    # =========================================================================
    # 6. ERROR HANDLING & EXCEPTION
    # =========================================================================
    add_h1("6. PENANGANAN GALAT & INTEGRITAS TRANSAKSI (ERROR HANDLING)")
    add_p(
        "Dalam aplikasi kasir tingkat produksi, kegagalan database engine tidak boleh menyebabkan data tidak konsisten "
        "(misal: uang kasir tercatat tetapi stok barang tidak berkurang). MySQL menyediakan sistem penanganan galat terstruktur:"
    )

    add_h2("6.1 HANDLER & SIGNAL SQLSTATE")
    add_bullet(
        "Mendefinisikan aksi otomatis saat terjadi galat (SQLEXCEPTION) atau peringatan (SQLWARNING). "
        "Aksi dapat berupa CONTINUE (melanjutkan baris berikutnya) atau EXIT (segera menghentikan blok BEGIN-END saat itu).",
        bold_prefix="DECLARE ... HANDLER: "
    )
    add_bullet(
        "Melempar pesan kesalahan kustom ke aplikasi klien. Kode SQLSTATE '45000' adalah kode standar yang dipesan untuk exception pengguna (User-Defined Unhandled Exception).",
        bold_prefix="SIGNAL SQLSTATE '45000': "
    )

    add_h2("6.2 Contoh Implementasi: Validasi Stok & Pembatalan Transaksi Kasir")
    add_code(
"""DELIMITER $$

CREATE PROCEDURE spKurangiStokBarang(
    IN p_kodeproduk CHAR(4),
    IN p_qty INT
)
BEGIN
    DECLARE v_stok_tersedia INT;
    
    -- Mengambil stok barang saat ini
    SELECT stok INTO v_stok_tersedia 
    FROM produk 
    WHERE kodeproduk = p_kodeproduk;
    
    -- Validasi 1: Periksa apakah kode produk valid
    IF v_stok_tersedia IS NULL THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Kesalahan: Kode produk barang tidak ditemukan dalam database.';
    END IF;
    
    -- Validasi 2: Periksa kecukupan stok
    IF v_stok_tersedia < p_qty THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Transaksi Dibatalkan: Stok produk di gudang tidak mencukupi.';
    ELSE
        -- Update stok fisik produk
        UPDATE produk 
        SET stok = stok - p_qty 
        WHERE kodeproduk = p_kodeproduk;
    END IF;
END$$

DELIMITER ;

-- Pengujian 1: Stok Cukup (Berhasil)
CALL spKurangiStokBarang('P001', 2);

-- Pengujian 2: Stok Melebihi Batas (Sistem melempar Error 45000)
CALL spKurangiStokBarang('P001', 9999);
-- Respon: ERROR 1644 (45000): Transaksi Dibatalkan: Stok produk di gudang tidak mencukupi."""
    )

    # =========================================================================
    # 7. STUDI KASUS PROSEDUR TRANSAKSI KASIR LENGKAP
    # =========================================================================
    add_h1("7. STUDI KASUS: PROSEDUR TRANSAKSI CHECKOUT KASIR TERPADU")
    add_p(
        "Untuk mengintegrasikan seluruh materi (UDF, Stored Procedure, Parameter, dan Error Handling), "
        "berikut adalah prosedur transaksi checkout penjualan lengkap yang menghubungkan tabel KASIR, CUSTOMER, NOTA, ITEMNOTA, dan PRODUK:"
    )

    add_code(
"""DELIMITER $$

CREATE PROCEDURE spCheckoutTransaksi(
    IN p_kodekasir CHAR(3),
    IN p_kodecus CHAR(5),
    IN p_kodeproduk CHAR(4),
    IN p_banyak INT,
    OUT p_nonota_dihasilkan CHAR(10),
    OUT p_total_bayar INT,
    OUT p_poin_baru INT
)
BEGIN
    DECLARE v_harga_satuan INT;
    DECLARE v_stok_tersedia INT;
    DECLARE v_tgl_hari_ini DATE;
    
    -- Tangani potensi kegagalan integritas dengan ROLLBACK
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;
    
    SET v_tgl_hari_ini = CURRENT_DATE();
    
    -- 1. Validasi Keberadaan Data Produk & Stok
    SELECT harga, stok INTO v_harga_satuan, v_stok_tersedia 
    FROM produk WHERE kodeproduk = p_kodeproduk;
    
    IF v_harga_satuan IS NULL THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error: Produk tidak terdaftar.';
    END IF;
    
    IF v_stok_tersedia < p_banyak THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error: Kuantitas beli melebihi persediaan stok toko.';
    END IF;
    
    -- 2. Generate Nomor Nota Baru secara otomatis
    SET p_nonota_dihasilkan = fcGenerateNoNota(v_tgl_hari_ini);
    SET p_total_bayar = v_harga_satuan * p_banyak;
    SET p_poin_baru = fcHitungPoinBelanja(p_total_bayar);
    
    -- 3. Memulai Transaksi Atomik
    START TRANSACTION;
        -- Simpan Header Nota
        INSERT INTO nota (nonota, kodekasir, tgltran, kodecus)
        VALUES (p_nonota_dihasilkan, p_kodekasir, v_tgl_hari_ini, p_kodecus);
        
        -- Simpan Detil Item Nota
        INSERT INTO itemnota (nonota, kodeproduk, banyak, hargajual)
        VALUES (p_nonota_dihasilkan, p_kodeproduk, p_banyak, v_harga_satuan);
        
        -- Kurangi Stok Barang
        UPDATE produk SET stok = stok - p_banyak WHERE kodeproduk = p_kodeproduk;
        
        -- Tambahkan Poin Belanja ke Member (Jika bukan customer umum M0000)
        IF p_kodecus <> 'M0000' AND p_poin_baru > 0 THEN
            UPDATE customer SET pointterkumpul = pointterkumpul + p_poin_baru WHERE kodecus = p_kodecus;
        END IF;
    COMMIT;
END$$

DELIMITER ;"""
    )

    # =========================================================================
    # 8. LEMBAR TUGAS PRAKTIKUM (UNTUK MAHASISWA)
    # =========================================================================
    doc.add_page_break()
    add_h1("8. LEMBAR TUGAS & LATIHAN SOAL PRAKTIKUM (UNTUK MAHASISWA)")
    add_p(
        "Petunjuk Pengerjaan Mahasiswa / Praktikan:\n"
        "1. Pastikan basis data minimarket praktikum (PRODUK, KASIR, CUSTOMER, NOTA, ITEMNOTA) telah aktif.\n"
        "2. Tuliskan kueri pembuatan Function / Procedure lengkap dengan penyesuaian DELIMITER.\n"
        "3. Lakukan pengujian eksekusi (CALL / SELECT) dan tangkap layar (screenshot) kode kueri serta output terminal.\n"
        "4. Perhatikan penggunaan tipe parameter (IN, OUT, INOUT) dan penanganan kondisi error sesuai instruksi soal."
    )

    add_h2("Tingkat 1: User Defined Function (UDF) & Logika Kalkulasi")
    add_p(
        "Buatlah UDF bernama 'fcCekStatusStok' yang menerima input parameter 'p_kodeproduk' (CHAR(4)) dan mengembalikan nilai skalar string (VARCHAR(20)). "
        "Ketentuan: jika stok = 0 kembalikan 'KOSONG', jika stok 1 s.d. 5 kembalikan 'KRITIS', selain itu kembalikan 'TERSEDIA (X Unit)'. "
        "Uji function ini menggunakan kueri SELECT pada tabel produk.",
        bold_prefix="Soal 1 (UDF Evaluasi Persediaan Stok): "
    )
    add_p(
        "Toko ingin mengklasifikasikan jenjang keanggotaan pelanggan. Buatlah UDF bernama 'fcLevelLoyalitas' yang menerima input 'p_point' (INT) "
        "dan mengembalikan status (VARCHAR(15)) dengan kriteria: Point >= 100 'PLATINUM', Point 50-99 'GOLD', Point 20-49 'SILVER', dan Point < 20 'BRONZE'. "
        "Tampilkan daftar nama customer beserta level loyalitasnya menggunakan fungsi ini.",
        bold_prefix="Soal 2 (UDF Klasifikasi Member Loyal): "
    )
    add_p(
        "Buatlah UDF bernama 'fcFormatRupiah' yang menerima input nominal angka (INT) dan mengembalikan string berformat mata uang "
        "Indonesia dengan awalan 'Rp. ' dan pemisah ribuan titik (contoh: 15000 menjadi 'Rp. 15.000'). Uji dengan menampilkan daftar harga produk.",
        bold_prefix="Soal 3 (UDF Pemformatan Teks Rupiah): "
    )

    add_h2("Tingkat 2: Stored Procedure dengan Parameter IN, OUT, dan INOUT")
    add_p(
        "Buatlah Stored Procedure bernama 'spCariDataCustomer' dengan satu parameter IN (p_kodecus CHAR(5)) dan tiga parameter OUT "
        "(p_nama VARCHAR(50), p_alamat VARCHAR(100), p_poin INT). Procedure bertugas mencari data customer bersangkutan dan menyimpan nilainya "
        "ke ketiga parameter OUT. Tulis kueri pemanggilan dan periksa variabel outputnya.",
        bold_prefix="Soal 4 (Procedure Parameter OUT Informasi Customer): "
    )
    add_p(
        "Manajemen minimarket ingin melakukan diskon persentase harga barang. Buatlah Stored Procedure bernama 'spTerapkanDiskonProduk' "
        "yang memiliki parameter IN 'p_kodeproduk' (CHAR(4)) dan parameter INOUT 'p_harga' (INT). Nilai harga lama yang dilewatkan ke parameter "
        "akan dipotong sebesar 10%, kemudian nilai harga baru tersebut diperbarui ke tabel PRODUK dan nilainya dikembalikan ke pemanggil.",
        bold_prefix="Soal 5 (Procedure Parameter INOUT Diskon Harga): "
    )
    add_p(
        "Buatlah Stored Procedure bernama 'spTambahKasirBaru' yang menerima parameter IN nama kasir dan password kasir. "
        "Di dalam procedure, generate kode kasir 3 digit otomatis (contoh: '003', '004') dan simpan ke tabel KASIR. "
        "Tampilkan data kasir baru yang berhasil ditambahkan.",
        bold_prefix="Soal 6 (Procedure Registrasi Staf Kasir): "
    )

    add_h2("Tingkat 3: Cursor & Batch Processing Transaksi")
    add_p(
        "Buatlah Stored Procedure bernama 'spKompilasiBelanjaMember' yang memanfaatkan CURSOR untuk mengiterasi seluruh riwayat transaksi belanja "
        "seorang customer tertentu (input parameter kodecus). Gabungkan nomor-nomor nota belanja yang pernah dilakukan customer tersebut ke dalam "
        "satu variabel string panjang yang dipisahkan oleh tanda koma, lalu tampilkan hasilnya.",
        bold_prefix="Soal 7 (Cursor Kompilasi Riwayat Nota Belanja): "
    )
    add_p(
        "Toko ingin merestok seluruh barang yang memiliki stok di bawah 10 unit. Buatlah Stored Procedure 'spRestokOtomatis' yang menggunakan "
        "CURSOR untuk mencari semua produk berkategori 'stok kritis' (< 10) dan secara otomatis menambahkan 50 unit ke masing-masing produk tersebut. "
        "Catat dan tampilkan berapa banyak produk yang berhasil direstok.",
        bold_prefix="Soal 8 (Cursor Pembaruan Stok Masal): "
    )

    add_h2("Tingkat 4: Error Handling & Complex Transaction Control")
    add_p(
        "Buatlah Stored Procedure 'spHapusCustomerAman' yang menerima kode customer. Procedure harus memvalidasi: jika customer tersebut pernah "
        "memiliki riwayat transaksi pada tabel NOTA, batalkan operasi dan lemparkan error kustom via SIGNAL SQLSTATE '45000' dengan pesan: "
        "'Tidak dapat menghapus customer: Data customer terikat dengan riwayat nota transaksi'. Jika tidak memiliki nota, lakukan penghapusan.",
        bold_prefix="Soal 9 (Validasi Integritas Hapus Data dengan SIGNAL): "
    )
    add_p(
        "Rancanglah Stored Procedure 'spPencatatanItemTransaksi' yang menerima parameter: nomor nota, kode produk, dan jumlah beli. "
        "Gunakan HANDLER FOR SQLEXCEPTION untuk menjamin atomisitas data. Di dalam procedure: periksa kecukupan stok di tabel PRODUK, "
        "kurangi stok barang, dan simpan baris transaksi ke tabel ITEMNOTA. Jika stok tidak cukup, batalkan transaksi dan lempar error kustom.",
        bold_prefix="Soal 10 (Prosedur Transaksi Atomik Penjualan Barang): "
    )

    # =========================================================================
    # 9. LAMPIRAN KUNCI JAWABAN (KHUSUS DOSEN & ASISTEN PRAKTIKUM)
    # =========================================================================
    doc.add_page_break()
    add_h1("9. LAMPIRAN: KUNCI JAWABAN & PEMBAHASAN LENGKAP (KHUSUS DOSEN & ASISTEN PRAKTIKUM)")
    add_p(
        "Bagian ini memuat seluruh solusi kueri SQL baku, sintaks pengujian eksekusi, serta analisis logika teknis "
        "untuk instrumen evaluasi penilaian asisten praktikum:"
    )

    # Solusi Soal 1
    add_h2("Solusi & Pembahasan Soal 1 (fcCekStatusStok)")
    add_code(
"""DELIMITER $$
CREATE FUNCTION fcCekStatusStok(p_kodeproduk CHAR(4))
RETURNS VARCHAR(30)
DETERMINISTIC
READS SQL DATA
BEGIN
    DECLARE v_stok INT;
    DECLARE v_status VARCHAR(30);
    
    SELECT stok INTO v_stok FROM produk WHERE kodeproduk = p_kodeproduk;
    
    IF v_stok IS NULL THEN
        SET v_status = 'PRODUK TIDAK ADA';
    ELSEIF v_stok = 0 THEN
        SET v_status = 'KOSONG';
    ELSEIF v_stok <= 5 THEN
        SET v_status = 'KRITIS';
    ELSE
        SET v_status = CONCAT('TERSEDIA (', v_stok, ' Unit)');
    END IF;
    
    RETURN v_status;
END$$
DELIMITER ;

-- Kueri Pengujian:
SELECT kodeproduk, namaproduk, stok, fcCekStatusStok(kodeproduk) AS status_stok FROM produk;"""
    )
    add_p("Analisis: Fungsi membaca data stok dari tabel produk dan mengevaluasi ambang batas menggunakan struktur IF-ELSEIF.", bold_prefix="Analisis Logika: ")

    # Solusi Soal 2
    add_h2("Solusi & Pembahasan Soal 2 (fcLevelLoyalitas)")
    add_code(
"""DELIMITER $$
CREATE FUNCTION fcLevelLoyalitas(p_point INT)
RETURNS VARCHAR(15)
DETERMINISTIC
NO SQL
BEGIN
    DECLARE v_level VARCHAR(15);
    IF p_point >= 100 THEN
        SET v_level = 'PLATINUM';
    ELSEIF p_point >= 50 THEN
        SET v_level = 'GOLD';
    ELSEIF p_point >= 20 THEN
        SET v_level = 'SILVER';
    ELSE
        SET v_level = 'BRONZE';
    END IF;
    RETURN v_level;
END$$
DELIMITER ;

-- Kueri Pengujian:
SELECT kodecus, namacus, pointterkumpul, fcLevelLoyalitas(pointterkumpul) AS tier_loyalitas FROM customer;"""
    )
    add_p("Analisis: Menggunakan karakteristik NO SQL karena murni komputasi skalar tanpa mengakses tabel.", bold_prefix="Analisis Logika: ")

    # Solusi Soal 3
    add_h2("Solusi & Pembahasan Soal 3 (fcFormatRupiah)")
    add_code(
"""DELIMITER $$
CREATE FUNCTION fcFormatRupiah(p_nominal INT)
RETURNS VARCHAR(30)
DETERMINISTIC
NO SQL
BEGIN
    RETURN CONCAT('Rp. ', REPLACE(FORMAT(p_nominal, 0), ',', '.'));
END$$
DELIMITER ;

-- Kueri Pengujian:
SELECT kodeproduk, namaproduk, fcFormatRupiah(harga) AS harga_rupiah FROM produk;"""
    )
    add_p("Analisis: Memanfaatkan fungsi bawaan FORMAT() dan REPLACE() untuk mengubah koma standar internasional menjadi titik ribuan khas Indonesia.", bold_prefix="Analisis Logika: ")

    # Solusi Soal 4
    add_h2("Solusi & Pembahasan Soal 4 (spCariDataCustomer)")
    add_code(
"""DELIMITER $$
CREATE PROCEDURE spCariDataCustomer(
    IN p_kodecus CHAR(5),
    OUT p_nama VARCHAR(50),
    OUT p_alamat VARCHAR(100),
    OUT p_poin INT
)
BEGIN
    SELECT namacus, almtcus, pointterkumpul 
    INTO p_nama, p_alamat, p_poin
    FROM customer
    WHERE kodecus = p_kodecus;
END$$
DELIMITER ;

-- Kueri Pengujian:
CALL spCariDataCustomer('M0001', @nama, @alamat, @poin);
SELECT @nama AS Nama, @alamat AS Alamat, @poin AS Poin;"""
    )
    add_p("Analisis: Klausa SELECT INTO memetakan kolom baris kueri secara langsung ke dalam parameter OUT.", bold_prefix="Analisis Logika: ")

    # Solusi Soal 5
    add_h2("Solusi & Pembahasan Soal 5 (spTerapkanDiskonProduk)")
    add_code(
"""DELIMITER $$
CREATE PROCEDURE spTerapkanDiskonProduk(
    IN p_kodeproduk CHAR(4),
    INOUT p_harga INT
)
BEGIN
    -- Potong harga sebesar 10%
    SET p_harga = ROUND(p_harga * 0.90);
    
    -- Update ke tabel fisik produk
    UPDATE produk SET harga = p_harga WHERE kodeproduk = p_kodeproduk;
END$$
DELIMITER ;

-- Kueri Pengujian:
SET @harga_awal = 10000;
CALL spTerapkanDiskonProduk('P001', @harga_awal);
SELECT @harga_awal AS harga_setelah_diskon;"""
    )
    add_p("Analisis: Parameter INOUT membawa nilai harga awal dari pemanggil, dimutasi 10% di dalam procedure, dan nilainya dikembalikan.", bold_prefix="Analisis Logika: ")

    # Solusi Soal 6
    add_h2("Solusi & Pembahasan Soal 6 (spTambahKasirBaru)")
    add_code(
"""DELIMITER $$
CREATE PROCEDURE spTambahKasirBaru(
    IN p_nama VARCHAR(50),
    IN p_pass CHAR(6)
)
BEGIN
    DECLARE last_code INT DEFAULT 0;
    DECLARE new_kodekasir CHAR(3);
    
    -- Validasi panjang password
    IF CHAR_LENGTH(p_pass) <> 6 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error: Password kasir harus tepat 6 karakter.';
    END IF;
    
    -- Generate Kode Kasir 3 digit otomatis
    SELECT IFNULL(MAX(CAST(kodekasir AS UNSIGNED)), 0) INTO last_code FROM kasir;
    SET new_kodekasir = LPAD(last_code + 1, 3, '0');
    
    INSERT INTO kasir (kodekasir, namakasir, pass) VALUES (new_kodekasir, p_nama, p_pass);
    SELECT * FROM kasir WHERE kodekasir = new_kodekasir;
END$$
DELIMITER ;

-- Kueri Pengujian:
CALL spTambahKasirBaru('Doni Pratama', '123456');"""
    )
    add_p("Analisis: Menjamin kepatuhan integritas panjang password kasir (6 karakter) dan auto-numbering kode kasir.", bold_prefix="Analisis Logika: ")

    # Solusi Soal 7
    add_h2("Solusi & Pembahasan Soal 7 (spKompilasiBelanjaMember)")
    add_code(
"""DELIMITER $$
CREATE PROCEDURE spKompilasiBelanjaMember(IN p_kodecus CHAR(5))
BEGIN
    DECLARE v_nota CHAR(10);
    DECLARE v_selesai INT DEFAULT 0;
    DECLARE v_daftar VARCHAR(1000) DEFAULT '';
    
    DECLARE curNota CURSOR FOR 
        SELECT nonota FROM nota WHERE kodecus = p_kodecus;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET v_selesai = 1;
    
    OPEN curNota;
    readLoop: LOOP
        FETCH curNota INTO v_nota;
        IF v_selesai = 1 THEN
            LEAVE readLoop;
        END IF;
        IF v_daftar = '' THEN
            SET v_daftar = v_nota;
        ELSE
            SET v_daftar = CONCAT(v_daftar, ', ', v_nota);
        END IF;
    END LOOP readLoop;
    CLOSE curNota;
    
    SELECT p_kodecus AS Member, IFNULL(NULLIF(v_daftar, ''), 'Belum Pernah Belanja') AS Riwayat_Nota;
END$$
DELIMITER ;

-- Kueri Pengujian:
CALL spKompilasiBelanjaMember('M0001');"""
    )
    add_p("Analisis: Menggunakan cursor untuk menggabungkan sekumpulan nomor nota belanja menjadi satu baris string.", bold_prefix="Analisis Logika: ")

    # Solusi Soal 8
    add_h2("Solusi & Pembahasan Soal 8 (spRestokOtomatis)")
    add_code(
"""DELIMITER $$
CREATE PROCEDURE spRestokOtomatis(OUT p_jml_produk_direstok INT)
BEGIN
    DECLARE v_kd CHAR(4);
    DECLARE v_selesai INT DEFAULT 0;
    DECLARE v_counter INT DEFAULT 0;
    
    DECLARE curKritis CURSOR FOR 
        SELECT kodeproduk FROM produk WHERE stok < 10;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET v_selesai = 1;
    
    OPEN curKritis;
    restokLoop: LOOP
        FETCH curKritis INTO v_kd;
        IF v_selesai = 1 THEN
            LEAVE restokLoop;
        END IF;
        
        UPDATE produk SET stok = stok + 50 WHERE kodeproduk = v_kd;
        SET v_counter = v_counter + 1;
    END LOOP restokLoop;
    CLOSE curKritis;
    
    SET p_jml_produk_direstok = v_counter;
END$$
DELIMITER ;

-- Kueri Pengujian:
CALL spRestokOtomatis(@total_direstok);
SELECT @total_direstok AS 'Jumlah Produk Berhasil Direstok';"""
    )
    add_p("Analisis: Cursor mengidentifikasi seluruh produk dengan stok kritis dan melakukan penambahan batch 50 unit.", bold_prefix="Analisis Logika: ")

    # Solusi Soal 9
    add_h2("Solusi & Pembahasan Soal 9 (spHapusCustomerAman)")
    add_code(
"""DELIMITER $$
CREATE PROCEDURE spHapusCustomerAman(IN p_kodecus CHAR(5))
BEGIN
    DECLARE v_jml_nota INT DEFAULT 0;
    
    -- Hitung transaksi terkait
    SELECT COUNT(*) INTO v_jml_nota FROM nota WHERE kodecus = p_kodecus;
    
    IF v_jml_nota > 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Tidak dapat menghapus customer: Data customer terikat dengan riwayat nota transaksi.';
    ELSE
        DELETE FROM customer WHERE kodecus = p_kodecus;
        SELECT CONCAT('Customer ', p_kodecus, ' berhasil dihapus.') AS status;
    END IF;
END$$
DELIMITER ;

-- Kueri Pengujian (Customer yang memiliki nota M0001 -> Ditolak):
CALL spHapusCustomerAman('M0001');
-- Hasil: ERROR 1644 (45000): Tidak dapat menghapus customer: Data customer terikat dengan riwayat nota transaksi."""
    )
    add_p("Analisis: Mencegah error foreign key cascaded yang tidak terkontrol dengan validasi logika ramah pengguna via SIGNAL.", bold_prefix="Analisis Logika: ")

    # Solusi Soal 10
    add_h2("Solusi & Pembahasan Soal 10 (spPencatatanItemTransaksi)")
    add_code(
"""DELIMITER $$
CREATE PROCEDURE spPencatatanItemTransaksi(
    IN p_nonota CHAR(10),
    IN p_kodeproduk CHAR(4),
    IN p_qty INT
)
BEGIN
    DECLARE v_stok INT DEFAULT 0;
    DECLARE v_harga INT DEFAULT 0;
    
    -- Rollback otomatis jika ada error database
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;
    
    SELECT stok, harga INTO v_stok, v_harga FROM produk WHERE kodeproduk = p_kodeproduk;
    
    IF v_stok IS NULL THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error: Produk tidak ditemukan.';
    END IF;
    
    IF v_stok < p_qty THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error: Kuantitas melebihi ketersediaan stok fisik toko.';
    END IF;
    
    START TRANSACTION;
        INSERT INTO itemnota (nonota, kodeproduk, banyak, hargajual)
        VALUES (p_nonota, p_kodeproduk, p_qty, v_harga);
        
        UPDATE produk SET stok = stok - p_qty WHERE kodeproduk = p_kodeproduk;
    COMMIT;
    
    SELECT 'Item nota berhasil dicatat dan stok fisik terpotong.' AS status;
END$$
DELIMITER ;"""
    )
    add_p("Analisis: Menggunakan blok transaksi START TRANSACTION - COMMIT dengan jaminan atomisitas via DECLARE EXIT HANDLER FOR SQLEXCEPTION.", bold_prefix="Analisis Logika: ")

    # =========================================================================
    # 10. DAFTAR PUSTAKA
    # =========================================================================
    add_h1("10. DAFTAR PUSTAKA & REFERENSI RESMI")
    add_bullet("Oracle Corporation. (2024). MySQL 8.0 Reference Manual: Stored Routines & Cursor Management. https://dev.mysql.com/doc/refman/8.0/en/stored-routines.html", bold_prefix="1. ")
    add_bullet("Carlos Coronel & Steven Morris. (2019). Database Systems: Design, Implementation, & Management (13th Edition). Cengage Learning, Boston, USA.", bold_prefix="2. ")
    add_bullet("Paul DuBois. (2014). MySQL Developer's Library (5th Edition). Addison-Wesley Professional.", bold_prefix="3. ")
    add_bullet("Laboratorium Sistem Informasi. (2024). Modul Praktikum Sistem Manajemen Basis Data Lanjut: Materi Praktikum 4. Universitas Amikom Yogyakarta.", bold_prefix="4. ")

    # Save Document
    doc.save(filename)
    print(f"Document successfully created and saved as: {filename}")

if __name__ == "__main__":
    create_procedure_document()
