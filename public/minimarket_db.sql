-- ==============================================================================
-- SKRIP BASIS DATA MINIMARKET (STUDI KASUS KELOMPOK 7 / AMIKOM)
-- Normalisasi 3NF: KASIR, CUSTOMER, PRODUK, NOTA, ITEMNOTA
-- Sumber: rancangan database.xlsx & 20261009140239_SI167_Diskusi_Kelompok.docx
-- RDBMS: MySQL 8.0+ / MariaDB 10.5+ (Engine InnoDB)
-- ==============================================================================

CREATE DATABASE IF NOT EXISTS minimarket_db
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

USE minimarket_db;

-- ------------------------------------------------------------------------------
-- 1. HAPUS TABEL LAMA JIKA SUDAH ADA (URUTAN CHILD KE PARENT)
-- ------------------------------------------------------------------------------
DROP TABLE IF EXISTS itemnota;
DROP TABLE IF EXISTS nota;
DROP TABLE IF EXISTS produk;
DROP TABLE IF EXISTS customer;
DROP TABLE IF EXISTS kasir;

-- ------------------------------------------------------------------------------
-- 2. PEMBUATAN TABEL INDUK (PARENT TABLES)
-- ------------------------------------------------------------------------------

-- Tabel KASIR (Data Petugas Kasir Minimarket)
CREATE TABLE kasir (
    KodeKasir   CHAR(3)         NOT NULL,
    NamaKasir   VARCHAR(30)     NOT NULL,
    Pass        CHAR(6)         NOT NULL,
    PRIMARY KEY (KodeKasir),
    CONSTRAINT chk_kasir_pass CHECK (CHAR_LENGTH(Pass) = 6)
) ENGINE=InnoDB;

-- Tabel CUSTOMER (Data Anggota / Pembeli Umum)
-- Catatan: Customer UMUM (M0000) bernilai NULL pada data pribadi
CREATE TABLE customer (
    KodeCus         CHAR(5)         NOT NULL,
    NamaCus         VARCHAR(50)     NOT NULL,
    TglLahir        DATE            NULL,
    JenKelCus       CHAR(1)         NULL,
    AlmtCus         VARCHAR(100)    NULL DEFAULT 'Yogyakarta',
    HPCus           VARCHAR(15)     NULL,
    PointTerkumpul  INT             NOT NULL DEFAULT 0,
    PRIMARY KEY (KodeCus),
    CONSTRAINT chk_customer_jenkel CHECK (JenKelCus IN ('L', 'P') OR JenKelCus IS NULL),
    CONSTRAINT chk_customer_point  CHECK (PointTerkumpul >= 0)
) ENGINE=InnoDB;

-- Tabel PRODUK (Data Barang Dagangan Toko)
CREATE TABLE produk (
    KodeProduk  CHAR(4)         NOT NULL,
    NamaProduk  VARCHAR(50)     NOT NULL,
    Harga       INT             NOT NULL,
    stok        INT             NOT NULL DEFAULT 0,
    PRIMARY KEY (KodeProduk),
    CONSTRAINT chk_produk_harga CHECK (Harga >= 0),
    CONSTRAINT chk_produk_stok  CHECK (stok >= 0)
) ENGINE=InnoDB;

-- ------------------------------------------------------------------------------
-- 3. PEMBUATAN TABEL TRANSAKSI (CHILD TABLES)
-- ------------------------------------------------------------------------------

-- Tabel NOTA (Header Transaksi Penjualan)
-- Nonota format: YYMMDDxxxx (contoh: '2208030001')
CREATE TABLE nota (
    Nonota      CHAR(10)        NOT NULL,
    KodeKasir   CHAR(3)         NOT NULL,
    TglTran     DATE            NOT NULL,
    KodeCus     CHAR(5)         NOT NULL,
    PRIMARY KEY (Nonota),
    CONSTRAINT fk_nota_kasir
        FOREIGN KEY (KodeKasir) REFERENCES kasir(KodeKasir)
        ON UPDATE CASCADE ON DELETE RESTRICT,
    CONSTRAINT fk_nota_customer
        FOREIGN KEY (KodeCus) REFERENCES customer(KodeCus)
        ON UPDATE CASCADE ON DELETE RESTRICT
) ENGINE=InnoDB;

-- Tabel ITEMNOTA (Detail Item Barang yang Dibeli pada Nota)
-- Relasi Many-to-Many antara NOTA dan PRODUK dipecah di tabel ini
CREATE TABLE itemnota (
    Nonota      CHAR(10)        NOT NULL,
    KodeProduk  CHAR(4)         NOT NULL,
    banyak      INT             NOT NULL DEFAULT 1,
    hargajual   INT             NOT NULL,
    PRIMARY KEY (Nonota, KodeProduk),
    CONSTRAINT chk_itemnota_banyak CHECK (banyak >= 1),
    CONSTRAINT chk_itemnota_harga  CHECK (hargajual >= 0),
    CONSTRAINT fk_itemnota_nota
        FOREIGN KEY (Nonota) REFERENCES nota(Nonota)
        ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT fk_itemnota_produk
        FOREIGN KEY (KodeProduk) REFERENCES produk(KodeProduk)
        ON UPDATE CASCADE ON DELETE RESTRICT
) ENGINE=InnoDB;

-- ------------------------------------------------------------------------------
-- 4. INSERT DATA AWAL (SEED DATA BASED ON DISKUSI KELOMPOK 7 & EXCEL 3NF)
-- ------------------------------------------------------------------------------

-- Data KASIR
INSERT INTO kasir (KodeKasir, NamaKasir, Pass) VALUES
('001', 'Unyil', 'uny001'),
('002', 'Melani', 'mel002');

-- Data CUSTOMER
INSERT INTO customer (KodeCus, NamaCus, TglLahir, JenKelCus, AlmtCus, HPCus, PointTerkumpul) VALUES
('M0000', 'UMUM', NULL, NULL, 'Yogyakarta', NULL, 0),
('M0001', 'Indah', '1990-12-12', 'P', 'Jl. Wijaya 255', '08162992', 25),
('M0002', 'Budi', '1987-05-20', 'L', 'Jl. Mawar 19', '081239927', 10);

-- Data PRODUK
INSERT INTO produk (KodeProduk, NamaProduk, Harga, stok) VALUES
('P001', 'Indomie Goreng Special', 2100, 100),
('P002', 'Wafer Tango', 4300, 50),
('P003', 'SariRoti Coklat Keju', 7500, 30);

-- Data NOTA
INSERT INTO nota (Nonota, KodeKasir, TglTran, KodeCus) VALUES
('2208030001', '001', '2022-08-03', 'M0001'),
('2208030002', '001', '2022-08-03', 'M0002'),
('2208040001', '002', '2022-08-04', 'M0000'),
('2208050001', '002', '2022-08-05', 'M0001');

-- Data ITEMNOTA
INSERT INTO itemnota (Nonota, KodeProduk, banyak, hargajual) VALUES
('2208030001', 'P001', 5, 2100),
('2208030001', 'P002', 1, 4300),
('2208030002', 'P003', 2, 7500),
('2208040001', 'P001', 3, 2100),
('2208040001', 'P002', 3, 4300),
('2208040001', 'P003', 1, 7500),
('2208050001', 'P002', 2, 4300);

-- ------------------------------------------------------------------------------
-- 5. VERIFIKASI PEMBENTUKAN DATA
-- ------------------------------------------------------------------------------
SELECT 'Tabel KASIR:' AS info;
SELECT * FROM kasir;

SELECT 'Tabel CUSTOMER:' AS info;
SELECT * FROM customer;

SELECT 'Tabel PRODUK:' AS info;
SELECT * FROM produk;

SELECT 'Tabel NOTA:' AS info;
SELECT * FROM nota;

SELECT 'Tabel ITEMNOTA:' AS info;
SELECT * FROM itemnota;
