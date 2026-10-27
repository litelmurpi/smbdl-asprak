# Slide Presentasi & Materi Pengayaan SMBD Lanjut

Slide presentasi web interaktif berbasis modern **Liquid Glass + ReactBits Grainient WebGL2 Canvas** dan materi pengayaan praktikum Sistem Manajemen Basis Data Lanjut (SMBD Lanjut) - Universitas Amikom Yogyakarta.

---

## 🚀 Struktur Direktori Proyek

```text
smbdl-asprak/
├── index.html                   # Entry point utama (Stored Routine & Function - 13 Slides)
├── slide_procedure_function.html# Alias materi Stored Routine, UDF & Cursor
├── slide_view.html              # Slide deck materi View & Indexing
├── minimarket_db.sql            # Skrip DDL & DML 3NF Database Minimarket
├── vercel.json                  # Konfigurasi routing & deployment Vercel
├── package.json                 # Metadata & skrip lokal
├── .gitignore                   # Aturan pengabaian git
│
├── database/                    # Skema & rancangan basis data
│   ├── minimarket_db.sql        # Skrip SQL lengkap (InnoDB, CHECK constraints, FK cascade)
│   └── rancangan database.xlsx  # Workbook normalisasi (UNF -> 1NF -> 2NF -> 3NF)
│
├── modules/                     # Dokumen modul praktikum
│   ├── generated/               # Hasil kompilasi modul pengayaan (PDF & DOCX)
│   │   ├── Modul_Pengayaan_SMBD_Lanjut_Procedure_Function.docx
│   │   ├── Modul_Pengayaan_SMBD_Lanjut_Procedure_Function.pdf
│   │   ├── Modul_Pengayaan_SMBD_Lanjut_View.docx
│   │   └── Modul_Pengayaan_SMBD_Lanjut_View.pdf
│   └── references/              # Bahan acuan & modul rujukan asli
│       ├── 20261009140239_SI167_Diskusi_Kelompok.docx
│       ├── 20261015134657_SI167_Modul_SMBD_Lanjut_1-2_(1).pdf
│       ├── 20261016110827_SI167_Modul_SMBD_Lanjut_3 (1).pdf
│       ├── 20261016110919_SI167_Modul_SMBD_Lanjut_4.pdf
│       └── rancangan database.xlsx
│
├── public/                      # Asset statis yang dapat diunduh langsung via URL
│   ├── minimarket_db.sql
│   ├── Modul_Pengayaan_SMBD_Lanjut_Procedure_Function.pdf
│   ├── Modul_Pengayaan_SMBD_Lanjut_View.pdf
│   └── rancangan database.xlsx
│
├── scripts/                     # Skrip python pembuat modul otomatis
│   ├── build_module.py
│   └── build_procedure_module.py
│
└── docs/                        # Desain arsitektur, catatan teknis & tangkapan layar
    ├── design.md                # Spesifikasi desain visual Liquid Glass
    ├── PLANNING.md              # Roadmap materi & kurikulum
    └── screenshots/             # Arsip gambar referensi
```

---

## 🌐 Menjalankan Secara Lokal

Anda dapat menjalankan presentasi secara lokal menggunakan server statis apa pun:

```bash
# Opsi 1: Menggunakan npx serve
npx serve . -l 3000

# Opsi 2: Menggunakan Python 3
python3 -m http.server 3000
```

Buka peramban di `http://localhost:3000`.

---
