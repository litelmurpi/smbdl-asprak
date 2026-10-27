# DESIGN SYSTEM SPECIFICATION: MODERN SKEUOMORPHIC TACTILE + PREMIUM LIQUID GLASS
## Template Slide Presentasi Web-Based Mandiri (Konten-Agnostik untuk Materi SMBD / Basis Data)

> **Status Dokumen**: Rujukan Tunggal Baku (*Single Source of Truth*).  
> **Target Pengguna**: Agen AI (misal: Antigravity) dan Asisten Praktikum/Dosen.  
> **Tujuan**: Blueprint arsitektur visual dan teknis konten-agnostik untuk menghasilkan slide deck materi praktikum SMBD Lanjut dalam bentuk berkas HTML5 mandiri (*single-file autonomous*) yang interaktif, presisi, berbobot akademis, dan sepenuhnya bebas dari *AI-slop*.  
> **Berkas Referensi Implementasi**: [`slide_procedure_function.html`](file:///home/azfa/web_projects/smbdl-asprak/slide_procedure_function.html).

---

## 1. Filosofi Desain & Anti-Slop Dials

### 1.1 Konsep Utama: Refined Liquid Glass dengan Aksen Taktil Mikro (Gaya iOS / visionOS)
Desain ini mengadopsi estetika **Refined Liquid Glass modern** yang bersih, airy, dan futuristik layaknya interface Apple iOS / visionOS dan NovaPay Fintech, dipadukan dengan **sentuhan aksen taktil yang sangat tipis dan halus**:
1. **Peniadaan Skeuomorphism Berat**: Seluruh ornamen perangkat keras tebal seperti baut fisik di sudut frame, bayangan balok gelap 3px pada tombol, dan bevel debossed yang kaku telah **dihilangkan sepenuhnya**.
2. **Kaca Cair Murni (*Optical Liquid Glass*)**: Frame tablet dan kartu-kartu materi menggunakan kaca buram berkabut (*high-translucency frosted glass*) dengan pembiasan `backdrop-filter: blur(24px–32px) saturate(180%–190%)`.
3. **Pencahayaan Atmosferik Volumetrik 3D**: Latar belakang memancarkan orba cahaya biru kobalt elektrik (`#005BFF`) yang menembus kaca cair dengan efek refraksi optik yang kaya dan dinamis.
4. **Sentuhan Taktil Mikro yang Tipis**: Memberikan rasa presisi fisik hanya melalui *specular highlight* 1px yang sangat tipis di bibir atas panel, sudut membulat elegan (`14px`–`18px`), efek *hover 3D tilt* interaktif yang halus pada kartu, dan transisi spasial 3D saat pergantian slide.

### 1.2 Konfigurasi Anti-Slop Dials (Core Part 3)

| Dial | Level | Karakteristik Visual | Justifikasi Kontekstual Fungsional |
| :--- | :---: | :--- | :--- |
| **ENERGY** | **2** | **Balanced / Precision Hardware Console** | Memberikan wibawa ilmiah dan stabilitas visual layaknya instrumen laboratorium basis data modern, tanpa kebisingan grafis yang melelahkan mata mahasiswa. |
| **RHYTHM** | **2** | **Content-Driven Structured Variety** | Setiap posisi slide memiliki variasi komposisi layout yang tegas sesuai karakter bahan ajar (arsitektur 4-pilar, matriks komparasi, split code console, tabel kamus data, lembar tugas bertingkat), namun tetap dalam kesatuan bingkai tablet yang konsisten. |
| **MOTION** | **2** | **Purposeful Spatial 3D & Mechanical Tactility** | Animasi perpindahan slide memanfaatkan bidang spasial 3D (`perspective: 1400px`) yang halus layaknya membalik kartu tablet fisik; dilengkapi efek interaktif 3D tilt mikro pada kartu materi tanpa ada animasi *looping* tanpa henti. |

### 1.3 Elemen Slop yang Dieliminasi secara Mutlak (*Anti-Slop Purge*)
- ❌ **Dilarang Gradien Ungu-Biru-Pink AI Klise**: Menggunakan palet obsidian, slate, dan aksen cyan instrumen fungsional.
- ❌ **Dilarang Eyebrow Pill Badge di Atas H1**: Judul materi langsung berdiri tegak sebagai fokus utama tanpa kapsul status palsu.
- ❌ **Dilarang Ornamen Cairan Krom 3D / Floating Blob Tanpa Makna**: Semua ruang visual dialokasikan untuk konten penjelasan, diagram arsitektur, dan konsol kueri SQL.
- ❌ **Dilarang Glassmorphism Membabi-Buta di Setiap Komponen**: Efek kaca dibatasi ketat (*dose-capped*, maksimal 1 elemen per slide). Permukaan standar tetap solid bertingkat.
- ❌ **Dilarang Glow Neon Berlebihan di Seluruh Border**: Pendaran cahaya hanya ada pada status LED fungsional mikro berdiameter 7px.
- ❌ **Dilarang Tombol / Tab Tanpa Aksi (*Dead Controls*)**: Seluruh kontrol interaktif (panah, spasi, tab, tombol salin, modal galeri) wajib memiliki implementasi fungsional nyata.

---

## 2. Sistem Token Desain (1:1 Baku dari Template)

Seluruh token dideklarasikan pada blok `:root` dan wajib digunakan secara konsisten. Dilarang mengarang kode warna heksadesimal baru di luar daftar ini.

### 2.1 Palet Warna — Permukaan & Latar Belakang

| Variabel CSS | Nilai Warna | Peran & Justifikasi Fungsional |
| :--- | :--- | :--- |
| `--bg-desk` | `#080B12` | Latar meja terluar di balik konsol; menciptakan kontras pekat dan fokus ke slide frame. |
| `--bg-chassis` | `rgba(14, 22, 42, 0.78)` | Bodi semi-transparan perangkat keras tablet presentasi dengan refraksi kaca. |
| `--chassis-surface` | `linear-gradient(175deg, rgba(16, 26, 52, 0.58) 0%, rgba(7, 12, 26, 0.72) 100%)` | Gradien bodi konsol liquid glass dengan aura cobalt diffuse di baliknya. |
| `--surface-card` | `linear-gradient(135deg, rgba(255, 255, 255, 0.13) 0%, rgba(16, 28, 58, 0.55) 100%)` | Permukaan kartu materi liquid glass optik ber-refraksi tinggi (NovaPay/iOS style). |
| `--surface-card-hover` | `linear-gradient(135deg, rgba(255, 255, 255, 0.18) 0%, rgba(20, 36, 75, 0.65) 100%)` | Respon permukaan kaca saat disorot kursor; pendaran specular sheen bertambah kuat. |
| `--surface-card-highlight` | `linear-gradient(135deg, rgba(0, 229, 255, 0.18) 0%, rgba(12, 35, 78, 0.65) 100%)` | Kartu materi penting/spesial dengan rim pendaran cyan dan cobalt menyala. |
| `--surface-recessed` | `rgba(5, 9, 20, 0.82)` | Cekungan panel terminal gelap (area kode SQL & task frame) dengan filter blur 24px. |
| `--surface-track` | `rgba(8, 14, 28, 0.80)` | Kanal rel cekung untuk tab-bar; menampung tombol-tombol chiclet mekanik. |
| `body background` | `ReactBits Grainient (WebGL2 Shader Canvas) + CSS Radial Fallback` | Latar animasi fluida berbutir (*flowing grainy gradient*) interaktif berbasis WebGL2 GPU, dapat diaduk kursor (*cursor stirring & click swirl*), selaras tema cobalt-cyan. |

### 2.2 Warna — Tepi, Bevel, & Pantulan Garis (*Specular Highlights*)

| Variabel CSS | Nilai Warna | Peran & Justifikasi Fungsional |
| :--- | :--- | :--- |
| `--specular-line` | `rgba(255, 255, 255, 0.16)` | Garis kilau pantulan 1px di rusuk paling atas lempengan hardware. |
| `--specular-subtle` | `rgba(255, 255, 255, 0.08)` | Pantulan sekunder pada pembatas horizontal dan footer slide. |
| `--border-beveled` | `rgba(255, 255, 255, 0.11)` | Garis batas struktural panel untuk memisahkan bidang dari latar gelap. |
| `--border-dark` | `rgba(0, 0, 0, 0.6)` | Bayangan tepi bawah komponen untuk mempertegas ketebalan material. |
| `--border-subtle` | `rgba(255, 255, 255, 0.10)` | Garis tepi komponen generik untuk menjaga batas kontras WCAG AA. |

### 2.3 Warna — Aksen Fungsional Berbasis Sinyal Basis Data

| Variabel CSS | Nilai Warna | Makna & Penggunaan Semantik |
| :--- | :--- | :--- |
| `--accent-cyan` | `#00E5FF` | **Sinyal Primer**: Status aktif, parameter kunci, tombol tab aktif, nomor urut kartu. |
| `--accent-cyan-dim`| `rgba(0, 229, 255, 0.12)` | Latar belakang debossed badge kategori materi di pojok kiri atas slide. |
| `--accent-blue` | `#2563EB` | Komponen relasional tingkat menengah, kata kunci kueri skalar. |
| `--accent-indigo` | `#6366F1` | Penanda loop perulangan dan pointer cursor internal. |
| `--accent-green` | `#10B981` | Status LED aktif, operasi DML valid, transaksi berhasil di-commit. |
| `--accent-red` | `#F43F5E` | Sinyal `SQLEXCEPTION`, pemicu `ROLLBACK`, pesan error kustom `SIGNAL 45000`. |
| `--accent-amber` | `#F59E0B` | Status peringatan stok menipis, parameter `INOUT` yang memutasi variabel. |

### 2.4 Tipografi & Skala Ukuran Teks

Tipografi dipilih untuk menjamin keterbacaan tinggi kueri SQL dan hierarki presentasi:

```css
--font-display: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
--font-body:    'Inter', system-ui, -apple-system, sans-serif;
--font-mono:    'JetBrains Mono', Consolas, monospace;
```

#### Skala Hirarki Tipografi:
- **Judul Cover (H1)**: `38px` / Bobot `800` / *Line-height* `1.15` / *Letter-spacing* `-0.03em`.
- **Judul Slide (H2)**: `27px` / Bobot `800` / *Line-height* `1.22` / *Letter-spacing* `-0.02em` / Drop shadow `0 2px 4px rgba(0,0,0,0.5)`.
- **Deskripsi Sub-Judul**: `14px` / Bobot `400` / Warna `#CBD5E1` / *Line-height* `1.55` / Max width `960px`.
- **Judul Kartu Materi**: `15.5px` / Bobot `700` / Warna `#FFFFFF`.
- **Teks Tubuh Kartu**: `13px` / Bobot `400` / Warna `#CBD5E1` / *Line-height* `1.55`.
- **Teks Kode Terminal**: `12px` / Font Monospace / Warna `#93C5FD` / *Line-height* `1.55`.
- **Teks Sel Tabel**: `12.5px` / Header bobot `700` / Sel tubuh bobot `400`.
- **Badge Kategori Slide**: `11px` / Font Monospace / Bobot `700` / Huruf Kapital / Spasi `0.08em`.
- **Teks Footer Slide**: `11.5px` / Warna `#8896AB` / *Border-top* `rgba(255,255,255,0.08)`.

### 2.5 Sistem Bayangan Berlapis (*Tactile Layered Shadows*)

Enam preset bayangan bertingkat untuk membangun kedalaman fisik objek:

```css
/* 1. Chassis Frame: Bayangan luar luas + bevel inset bodi tablet */
--shadow-chassis: 
  0 1px 0 1px rgba(255, 255, 255, 0.14) inset,
  0 -1px 0 1px rgba(0, 0, 0, 0.7) inset,
  0 40px 90px -15px rgba(0, 0, 0, 0.9),
  0 20px 45px -5px rgba(0, 0, 0, 0.7);

/* 2. Elevated Card: Kartu materi fisik standar */
--shadow-card:
  0 4px 12px rgba(0, 0, 0, 0.45),
  0 1px 3px rgba(0, 0, 0, 0.5),
  inset 0 1px 0 rgba(255, 255, 255, 0.13),
  inset 0 -1px 0 rgba(0, 0, 0, 0.5);

/* 3. Card Lift: Kartu saat disentuh mouse (elevasi naik) */
--shadow-card-lift:
  0 14px 30px rgba(0, 0, 0, 0.65),
  0 4px 8px rgba(0, 0, 0, 0.45),
  inset 0 1px 0 rgba(255, 255, 255, 0.22),
  inset 0 -1px 0 rgba(0, 0, 0, 0.5);

/* 4. Recessed Well: Permukaan cekung layar kode SQL & daftar soal */
--shadow-recessed:
  inset 0 3px 8px rgba(0, 0, 0, 0.85),
  inset 0 1px 2px rgba(0, 0, 0, 0.9),
  0 1px 0 rgba(255, 255, 255, 0.06);

/* 5. Mechanical Button: Tombol timbul siap tekan */
--shadow-btn:
  0 3px 0 #050810,
  0 5px 12px rgba(0, 0, 0, 0.5),
  inset 0 1px 0 rgba(255, 255, 255, 0.18);

/* 6. Pressed Button: Tombol mekanik yang sedang ditekan */
--shadow-btn-pressed:
  0 1px 0 #050810,
  0 2px 4px rgba(0, 0, 0, 0.5),
  inset 0 2px 4px rgba(0, 0, 0, 0.6);
```

### 2.6 Geometri, Dimensi, & Easing Motion

```css
--slide-width: 1200px;
--slide-height: 680px;

/* Responsif Layar Kecil / Laptop (<= 1280px) */
@media (max-width: 1280px) {
  :root {
    --slide-width: 95vw;
    --slide-height: 53.43vw; /* Rasio aspek standar 16:9 */
  }
}

/* Perspektif Spasial 3D */
body { perspective: 1400px; }

/* Skala Border Radius */
--radius-frame: 12px;
--radius-card:  8px;
--radius-well:  8px;
--radius-badge: 4px;
--radius-tab:   5px;
--radius-track: 7px;
```

---

## 3. Katalog Komponen Lengkap (*Full Component Catalog*)

Setiap komponen dirancang dengan fungsi semantik jelas. Dilarang menambahkan komponen tanpa kepatuhan terhadap aturan di bawah ini.

### 3.1 `header.deck-header` & Kontrol Hardware
- **Anatomi**: Baris setinggi `56px`, gradien gelap bodi konsol, dibatasi garis bevel specular atas dan bayangan pemisah bawah.
- **Elemen Internal**:
  - `.brand-tag`: Lencana debossed berisi teks instrumen + `.status-led` berkedip hijau lembut (sinyal operasional RDBMS).
  - `.brand-title`: Judul modul pengayaan resmi (`13.5px`, teks tebal putih).
  - `.slide-counter`: Penghitung urutan slide format digital `01 / 12` dalam lekukan panel.
  - `.ctrl-btn`: Tombol navigasi mekanik (`◀ Prev`, `Next ▶`, `Grid`, `Fullscreen`).
- **Aturan Pemakaian**: Selalu hadir di bagian atas sebagai instrumen navigasi permanen.
- **Larangan**: Dilarang meletakkan tautan navigasi palsu ke halaman luar yang tidak ada.

### 3.2 `.progress-bar-container` & `.progress-bar`
- **Anatomi**: Saluran tersembunyi sedalam `4px` di dasar header (`background: #060912`), berisi bilah gradien cairan cyan (`#0284C7` ke `#00E5FF`).
- **Perilaku**: Melebar otomatis via JavaScript mengikuti proporsi indeks slide aktif dengan easing `cubic-bezier(0.2, 0.8, 0.2, 1)`.

### 3.3 `main.deck-stage` & `.slide-frame` (Chassis Baut)
- **Anatomi**: Bingkai tablet presisi `1200px` x `680px` dengan sudut membulat `12px` dan bayangan berlapis `--shadow-chassis`.
- **Detail Hardware mikro**: Empat baut pengikat di sudut panel via pseudo-element `.slide-frame::before` dan `::after` (lingkaran baut berdiameter `6px` dengan lubang sekrup mikro).

### 3.4 `.slides-wrapper`, `.slide`, `.slide.active`, & `.slide.prev` (Transisi 3D)
- **Anatomi**: Kontainer tumpuk berposisi absolut dengan `transform-style: preserve-3d`.
- **Mekanika Transisi Spasial**:
  - Slide Masuk (kanan): `opacity: 0; transform: translate3d(50px, 0, -80px) rotateY(4deg) scale(0.96);`.
  - Slide Aktif: `opacity: 1; visibility: visible; transform: translate3d(0, 0, 0) rotateY(0deg) scale(1); pointer-events: auto; z-index: 2;`.
  - Slide Keluar (kiri): `opacity: 0; transform: translate3d(-50px, 0, -80px) rotateY(-4deg) scale(0.96);`.
  - Durasi transisi: `0.45s` dengan kurva redaman presisi `cubic-bezier(0.16, 1, 0.3, 1)`.

### 3.5 `.slide-label-row`, `.slide-title`, & `.slide-description`
- **Anatomi**:
  - Kiri atas: `.slide-category` (stempel taktil kode bab). Kanan atas: `.slide-submeta` (institusi/topik).
  - Tengah: `.slide-title` tebal `27px` menegaskan persoalan arsitektur atau bisnis.
  - Paragraf: `.slide-description` padat ringkas (maksimal 2–3 kalimat) menjelaskan signifikansi materi.

### 3.6 Grid Layout: `.card-grid-2`, `.card-grid-3`, `.card-grid-4`
- **Anatomi**: Pembagian kolom simetris berbasis CSS Grid dengan celah seragam `16px` s.d. `20px` mengisi tinggi slide secara optimal.

### 3.7 `.tech-card` (+ `.highlight` & 3D Interactive Tilt)
- **Anatomi**: Panel kartu timbul dengan tepi atas berkilau dan nomor taktil debossed (`.tech-card-num`).
- **Interaksi 3D Tilt**: Saat kursor digerakkan di atas kartu, skrip JavaScript menghitung posisi offset kursor terhadap titik pusat kartu dan memberikan kemiringan dinamis halus:
  ```javascript
  card.style.transform = `perspective(800px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-3px) translateZ(8px)`;
  ```
- **Varian `.highlight`**: Membawa garis tepi cyan `rgba(0, 229, 255, 0.35)` untuk menandai fokus utama (misal parameter `OUT` atau mitigasi integritas).

### 3.8 `.code-box` (Konsol Terminal Recessed)
- **Anatomi**:
  - Frame sunken gelap pekat (`#050811`) dengan bayangan dalam `--shadow-recessed`.
  - Header terminal: Label judul konsol dengan **indikator LED cyan menyala** dan tombol `.code-copy-btn` taktil.
  - Area isi `.code-content`: Kode SQL monospaced dengan scrollbar recessed custom.
  - Pewarnaan Sintaks:
    - `.kw` (Kata Kunci SQL): `#38BDF8` (Sky Blue)
    - `.fn` (Fungsi SQL): `#C084FC` (Purple)
    - `.str` (Nilai String): `#34D399` (Emerald)
    - `.cm` (Komentar): `#64748B` (Slate Muted Miring)
    - `.tbl` (Nama Tabel Fisik): `#FCD34D` (Gold Amber)

### 3.9 `.table-sunken-frame` & `.slide-table`
- **Anatomi**: Kotak data terbenam untuk menampilkan struktur kamus relasional atau matriks komparasi. Header tabel dilapisi gradien hardware berbayang inset specular, sedangkan baris sel diselingi arsiran halus (*zebra-striping*).

### 3.10 `.tab-bar` & `.tab-btn` (Track Cekung & Tombol Chiclet)
- **Anatomi**: Kanal rel hitam (`--surface-track`) menampung tombol-tombol chiclet mekanik. Tab aktif terangkat naik dengan gradien khusus, garis tepi cyan berpendar, dan bayangan drop mekanik 2px.

### 3.11 `.error-box`
- **Anatomi**: Panel notifikasi khusus galat RDBMS berlatar merah transparan, bergaris aksen tebal 4px di rusuk kiri, memuat teks pesan error baku MySQL `ERROR 1644 (45000)`.

### 3.12 `.tactile-meta-badge` & `kbd` (Keycaps Fisik)
- **Anatomi**:
  - `.tactile-meta-badge`: Kartu statis tebal di slide cover untuk menampilkan level modul dan tantangan soal.
  - `kbd`: Tut tuts keyboard mekanik timbul (`border-bottom: 2px solid #060A14`, warna cyan) untuk instruksi pintasan tombol navigasi.

### 3.13 `.overview-modal` & `.overview-thumb` (Galeri Modal Grid)
- **Anatomi**: Layar penuh dengan latar belakang `rgba(4, 7, 16, 0.95)` dan efek `backdrop-filter: blur(12px)`. Berisi kisi kartu thumbnail miniatur 12 slide yang dapat diklik untuk melompat instan. Dapat dibuka/tutup dengan tombol `Grid` atau menekan tombol `Esc`.

---

## 4. Spesifikasi Tambahan: Premium Liquid Glass (iOS-Style)

Spesifikasi ini mendefinisikan kartu kaca premium (*optical liquid glass*) yang dapat disematkan ke dalam slide template untuk menonjolkan satu panel analitik atau kartu hero utama.

```
                    ┌── Specular Sheen (::before, 135deg gradient)
                    ▼
┌──────────────────────────────────────────────────────────┐ ◄── Lens Border (1px, rgba(255,255,255,0.18))
│ ┌──────────────────────────────────────────────────────┐ │ ◄── Refraction Inset (1px, rgba(255,255,255,0.35))
│ │                                                      │ │
│ │               LIQUID GLASS SURFACE                   │ │
│ │   backdrop-filter: blur(18px) saturate(180%);       │ │
│ │   background: rgba(20, 32, 52, 0.55);                │ │
│ │                                                      │ │
│ └──────────────────────────────────────────────────────┘ │ ◄── Glass Depth Shadow (inset 0 -1px 2px black)
└──────────────────────────────────────────────────────────┘
  ▲
  └── Ambient Glass Drop Shadow (0 14px 40px rgba(0,0,0,0.55))
```

### 4.1 Tujuh Lapisan Anatomi Fisik Liquid Glass
1. **Backdrop Blur Terukur (*Controlled Refraction*)**: `backdrop-filter: blur(18px) saturate(180%)`. Menjaga kejernihan teks sekaligus membiaskan kontras di baliknya secara optik (rentang aman: 16px – 22px; **dilarang > 28px**).
2. **Tint Transparan Gelap Selaras (*Harmonized Tint*)**: `background: rgba(20, 32, 52, 0.55)`. Menghindari warna putih susu murahan agar tidak mengotori palet tema dark workstation.
3. **Border Lensa 1px (*Lens Perimeter*)**: `border: 1px solid rgba(255, 255, 255, 0.18)` yang mempertegas batas fisik kaca.
4. **Refraksi Tepi Atas-Kiri (*Edge Refraction Highlight*)**: `box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.35)`. Mensimulasikan pantulan cahaya tajam di bibir prisma kaca.
5. **Ketebalan Kaca Bagian Bawah (*Glass Thickness Shadow*)**: `inset 0 -1px 2px rgba(0, 0, 0, 0.4)`. Memberikan bobot material dan ilusi ketebalan lempengan kaca optik.
6. **Specular Sheen Diagonal (*Subtle Surface Sheen*)**: Lapisan `::before` bergradien diagonal `linear-gradient(135deg, rgba(255, 255, 255, 0.12) 0%, transparent 45%)` yang memberikan pendaran kilau permukaan kaca murni tanpa glow neon.
7. **Bayangan Ambient Bawah (*Floating Ambient Shadow*)**: `0 14px 40px rgba(0, 0, 0, 0.55)` untuk memisahkan bidang kaca dari permukaan chassis di bawahnya.

### 4.2 Token CSS Liquid Glass
```css
:root {
  --glass-tint:           rgba(20, 32, 52, 0.55);
  --glass-blur:           18px;
  --glass-saturate:       180%;
  --glass-border:         rgba(255, 255, 255, 0.18);
  --glass-edge-highlight: inset 0 1px 0 rgba(255, 255, 255, 0.35);
  --glass-inner-shadow:   inset 0 -1px 2px rgba(0, 0, 0, 0.4);
  --glass-ambient-shadow: 0 14px 40px rgba(0, 0, 0, 0.55);
}
```

### 4.3 Kode CSS Siap-Pakai (`.liquid-glass`)
```css
/* Kelas Utilitas Liquid Glass Premium (iOS-Style) */
.liquid-glass {
  position: relative;
  background: var(--glass-tint);
  backdrop-filter: blur(var(--glass-blur)) saturate(var(--glass-saturate));
  -webkit-backdrop-filter: blur(var(--glass-blur)) saturate(var(--glass-saturate));
  border: 1px solid var(--glass-border);
  border-radius: var(--radius-card);
  box-shadow: 
    var(--glass-edge-highlight),
    var(--glass-inner-shadow),
    var(--glass-ambient-shadow);
  overflow: hidden;
}

/* Lapisan Kilau Diagonal Permukaan Kaca (Specular Sheen) */
.liquid-glass::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.12) 0%, transparent 45%);
  pointer-events: none;
  z-index: 1;
}
```

### 4.4 Aturan Penerapan & Batasan Dosis (*Dose-Capping Rules*)
- ✅ **Maksimal 1 Elemen per Slide**: Hanya diaplikasikan pada 1 kartu rangkuman utama, panel metrik penting, atau overlay dialog fokus.
- ✅ **Wajib Bertumpu di Atas Area Kontras**: Letakkan di atas bidang yang memiliki gradien warna atau teks latar belakang agar pembiasan kaca terlihat nyata.
- ❌ **Dilarang Menjadikan Semua Kartu sebagai Kaca**: Jika semua kartu dibuat transparan/blur, hierarki visual akan hancur dan menjadi *AI-slop*.
- ❌ **Dilarang Menggunakan Blur Raksasa (> 28px)**: Blur berlebihan merusak performa GPU dan membuat tampilan tampak seperti noda kabut.
- ❌ **Dilarang Border Neon Tebal**: Menjaga estetika lensa optik murni, bukan cyberpunk berantakan.

---

## 5. Blueprint Arsitektur 12-Slide (Konten-Agnostik)

Setiap materi SMBD yang dibuat menggunakan template ini wajib mengikuti pola arsitektur pedagogis 12 slide berikut. Prinsip dasarnya: **"Ganti Konten, Pertahankan Struktur Layout"**.

| No | Tipe Pola Layout | Peran Pedagogis Bahan Ajar | Struktur Komponen Utama |
| :-: | :--- | :--- | :--- |
| **01** | **Hero Cover Konsol** | Orientasi Judul, Bobot Teori, & Meta Tantangan | H1 Display, deskripsi materi, 3 unit `.tactile-meta-badge`, panduan pintasan tombol `kbd`. |
| **02** | **Arsitektur 4-Pilar** | Fondasi Teori, Urgensi Server-Side, & Kinerja | Header, paragraf pengantar, `.card-grid-4` berisi 4 unit `.tech-card` berpenomoran taktil. |
| **03** | **Matriks Komparasi Tabel** | Membedah Perbedaan Hakiki Dua Objek SQL | Deskripsi, `.table-sunken-frame` berisi `.slide-table` matriks perbandingan parameter. |
| **04** | **Split Teori & Kode Skalar** | Sintaks Lengkap UDF / Objek Tunggal Skalar | `.card-grid-2`: Sisi kiri `.code-box` kueri SQL + copy btn; sisi kanan `.tech-card` aturan karakteristik. |
| **05** | **Taksonomi 3-Kolom** | Klasifikasi Tipe Data / Mode Parameter | `.card-grid-3`: Membedah 3 mode parameter (IN, OUT, INOUT) lengkap dengan mini-code snippet. |
| **06** | **Blok Logika Terstruktur** | Percabangan Bersyarat & Perulangan Loop | `.card-grid-2`: Sisi kiri kondisional (IF/CASE); sisi kanan perulangan (LOOP/WHILE/REPEAT). |
| **07** | **Siklus Hidup & Pointer** | Iterasi Data Row-by-Row (Cursor) | `.card-grid-2`: Sisi kiri skrip kueri cursor; sisi kanan 5 tahapan siklus memori (DECLARE s.d. CLOSE). |
| **08** | **Integritas & Penanganan Galat** | Proteksi Transaksi & Validasi Kustom | `.card-grid-2`: Sisi kiri kueri SIGNAL/HANDLER; sisi kanan kartu respon `.error-box` dan mitigasi atomik. |
| **09** | **Studi Kasus Transaksi Utuh** | Prosedur Bisnis Riil Terpadu Multi-Tabel | Satu unit `.code-box` masif bentang penuh memuat prosedur transaksi checkout kasir terpadu. |
| **10** | **Kamus Skema 3NF Bertab** | Struktur Fisik Tabel Basis Data Kasir | Tab-bar switcher 5 tombol (`PRODUK`, `KASIR`, `CUSTOMER`, `NOTA`, `ITEMNOTA`) + render tabel dinamis. |
| **11** | **Lembar Tugas Bertingkat** | 10 Soal Latihan Mandiri Mahasiswa | Tab-bar 4 tingkatan (UDF, SP, Cursor, Error Handling) + `.task-sunken-frame` bersih dari jawaban. |
| **12** | **Kunci Solusi & Analisis** | Pedoman Evaluasi Dosen & Asprak | Tab-bar 10 soal + `.card-grid-2`: Sisi kiri kueri solusi SQL; sisi kanan analisis logika teknis. |

---

## 6. Kontrak Interaksi, Aksesibilitas, & Standar Performa

### 6.1 Kontrak Interaksi JavaScript (Wajib Aktif Penuh)
1. **Navigasi Keyboard**:
   - `ArrowRight` / `Space` / `PageDown`: Maju ke slide berikutnya.
   - `ArrowLeft` / `Backspace` / `PageUp`: Mundur ke slide sebelumnya.
   - `Home`: Melompat langsung ke slide 01.
   - `End`: Melompat langsung ke slide 12.
   - `Escape`: Membuka atau menutup modal grid overview.
   - `F` / `f`: Mengaktifkan mode layar penuh (*toggle fullscreen*).
2. **Navigasi Touchscreen / Mobile**:
   - *Swipe* ke kiri (geseran > 60px): Maju ke slide berikutnya.
   - *Swipe* ke kanan (geseran > 60px): Mundur ke slide sebelumnya.
3. **Sinkronisasi Hash URL**:
   - Perubahan slide memperbarui URL `#slide-N` melalui `history.replaceState` tanpa me-reload browser.
   - Halaman yang dimuat ulang dengan hash (misal `#slide-4`) otomatis membuka slide bersangkutan.
4. **Fungsi Salin Kueri (*Clipboard Copy*)**:
   - Setiap tombol `.code-copy-btn` memanggil `copySnippet(elementId)`.
   - Menggunakan API `navigator.clipboard.writeText()` dengan fallback `document.execCommand('copy')`.
   - Memberikan umpan balik instan kepada pengguna.
5. **Modal Galeri Grid**:
   - Menghasilkan 12 kartu thumbnail miniatur secara otomatis via fungsi `buildOverview()`.
   - Menyorot kartu slide yang sedang aktif dengan garis tepi cyan dan elevasi naik.

### 6.2 Aksesibilitas & Standar Kontras (WCAG AA)
- Rasio kontras teks biasa minimal `4.5:1` terhadap latar belakang.
- Teks judul (`#FFFFFF`) dan teks tubuh (`#CBD5E1`) di atas latar `--surface-card` mencapai rasio kontras `> 11:1` (melampaui standar WCAG AAA).
- Setiap tombol kontrol memiliki indikator fokus terlihat jelas: `outline: 2px solid var(--accent-cyan); outline-offset: 1px;`.

### 6.3 Standar Performa Mesin Peramban (*60 FPS Rendering*)
- Semua transisi animasi wajib menggunakan properti perangkat keras GPU: `transform` (`translate3d`, `rotateY`, `scale`) dan `opacity`.
- Menghindari manipulasi properti yang memicu reflow berat seperti `left`, `top`, `margin`, atau `width` dinamis pada slide wrapper.
- Seluruh aset font menggunakan tautan `preconnect` ke Google Fonts.

---

## 7. Checklist Anti-Slop Final (*Delivery Gate QA*)

Sebelum berkas slide HTML diserahkan kepada pengguna atau dikompilasi ke produksi, lakukan verifikasi mandiri terhadap seluruh daftar periksa berikut:

- [ ] **Kesesuaian Token 1:1**: Seluruh variabel warna, bayangan, tipografi, dan padding bersumber dari Bagian 2 (tanpa kode warna asing).
- [ ] **Bebas Elemen Slop**: Tidak ada kapsul eyebrow badge di atas H1, kata miring bergradien di judul, atau pendaran neon tak beralasan.
- [ ] **Ketahanan Taktil Mekanik**: Semua tombol memiliki bayangan dasar `--shadow-btn` dan efek penekanan fisik nyata saat `:active`.
- [ ] **Konsol Recessed Utuh**: Kotak kode SQL menggunakan tampilan cekung (`--shadow-recessed`) lengkap dengan scrollbar custom dan indikator LED.
- [ ] **Dose-Cap Kaca Terpenuhi**: Penggunaan kelas `.liquid-glass` maksimal 1 elemen per slide dan tidak membungkus semua kartu materi.
- [ ] **Kepatuhan Blueprint 12-Slide**: Struktur bab mengikuti alur 12 posisi slide (dari Cover hingga Kunci Solusi).
- [ ] **Kelengkapan Interaktif (No Dead Controls)**: Keyboard navigation, touch swipe, copy button, tab switcher skema, tab switcher tugas, dan switcher kunci jawaban berfungsi tanpa galat di konsol peramban (`F12`).
- [ ] **Kemandirian Berkas (*Single-File Autonomous*)**: Berkas HTML dapat langsung dibuka secara luring (*offline*) di Google Chrome atau peramban modern lainnya tanpa membutuhkan web server lokal.