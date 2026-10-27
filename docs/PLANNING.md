# PLANNING — Pembuatan `design.md` (Design System Spec)
## Template Slide Presentasi: Modern Skeuomorphic Tactile + Premium Liquid Glass (iOS-style)

> **Untuk dieksekusi oleh agent AI (mis. Antigravity).**
> Dokumen ini bersifat **mandiri** — tidak butuh konteks percakapan sebelumnya. Baca seluruhnya lalu kerjakan task secara berurutan.

---

## 0. Konteks & Berkas Terkait

Direktori kerja: `/home/azfa/web_projects/smbdl-asprak/`

| Berkas | Peran |
| :--- | :--- |
| `slide_procedure_function.html` | **Sumber kebenaran (source of truth)** design system. Template slide 12-halaman bertema "Modern Skeuomorphic Tactile" (dark + aksen cyan). Semua token, komponen, dan interaksi diekstrak dari sini. |
| `design.md` | **Target output.** Saat ini berisi dokumentasi design system LAMA (tema "Obsidian flat / Swiss-style" dari `index.html`, materi View) yang **sudah usang**. File ini akan **ditimpa total**. |
| `Pasted image (4).png` | Referensi mood glassmorphism (gaya Fineeva/NovaPay, glass biru). **Diabaikan sebagai konten** — hanya estetika glass-nya yang jadi inspirasi liquid glass premium. |

---

## 1. Problem Statement

File `design.md` yang ada sekarang mendokumentasikan design system lama yang tidak lagi sesuai dengan template visual terbaru di `slide_procedure_function.html`. Perlu ditulis ulang `design.md` sebagai **blueprint konten-agnostik** yang akurat mendokumentasikan template baru (Modern Skeuomorphic Tactile), ditambah spesifikasi **premium liquid glass ala iOS** yang anti-slop, agar bisa dipakai di agent AI lain untuk men-generate slide materi SMBD apa pun secara konsisten.

---

## 2. Requirements (final, hasil klarifikasi dengan user)

- **R1 — Replace total.** Timpa `design.md` lama dengan dokumentasi design system dari `slide_procedure_function.html`.
- **R2 — Fokus satu tema.** Dokumentasikan 100% desain skeuomorphic tactile template tersebut. Gambar `Pasted image (4).png` diabaikan sebagai konten; hanya glassmorphism-nya diangkat jadi inspirasi.
- **R3 — Liquid glass premium.** Glassmorphism harus bergaya **liquid glass iOS 26-style**: refraksi tepi, blur terukur, backdrop saturation, specular sheen halus, border lensa 1px. **Bukan AI-slop** (dilarang blur asal besar / glow neon berlebih).
- **R4 — Dose-capped.** Liquid glass maksimal **1 elemen fokus per slide**; sisanya tetap permukaan solid skeuomorphic.
- **R5 — Spesifikasi teknis lengkap** (full iOS liquid glass spec).
- **R6 — CSS siap-pakai.** Sertakan CSS variables + class `.liquid-glass` yang tinggal copy, plus aturan "boleh/jangan".
- **R7 — Konten-agnostik.** Dokumen template generik, tidak terikat materi tertentu.
- **R8 — Bahasa.** `design.md` ditulis dalam **Bahasa Indonesia**.

---

## 3. Token Design System Aktual (terekstrak dari `slide_procedure_function.html`)

> Nilai berikut sudah diverifikasi 1:1 dari blok `:root` dan CSS utama. Pakai nilai PERSIS ini di `design.md` — jangan mengarang nilai baru.

### 3.1 Warna — Permukaan & Latar
```
--bg-desk: #060911;                  /* latar meja paling luar */
--bg-chassis: #0D1322;               /* bodi chassis */
--chassis-surface: linear-gradient(180deg, #151D30 0%, #0E1524 100%);
--surface-card: linear-gradient(180deg, #172136 0%, #101828 100%);
--surface-card-hover: linear-gradient(180deg, #1C2842 0%, #131D30 100%);
--surface-card-highlight: linear-gradient(180deg, #182B44 0%, #0F1D32 100%);
--surface-recessed: #050811;         /* panel cekung (code box, task frame) */
--surface-track: #070B16;            /* track tab-bar */
body background: radial-gradient(circle at 50% 20%, #10182A 0%, var(--bg-desk) 80%);
```

### 3.2 Warna — Tepi, Bevel, Specular
```
--specular-line: rgba(255,255,255,0.16);
--specular-subtle: rgba(255,255,255,0.08);
--border-beveled: rgba(255,255,255,0.11);
--border-dark: rgba(0,0,0,0.6);
--border-subtle: rgba(255,255,255,0.1);
```

### 3.3 Warna — Aksen Fungsional
```
--accent-cyan: #00E5FF;              /* aksen utama: status aktif, parameter kunci */
--accent-cyan-dim: rgba(0,229,255,0.12);
--accent-blue: #2563EB;
--accent-indigo: #6366F1;
--accent-green: #10B981;             /* sukses / DML valid */
--accent-red: #F43F5E;               /* galat / error integritas */
--accent-amber: #F59E0B;             /* peringatan */
```

### 3.4 Warna — Teks
```
--text-heading: #FFFFFF;
--text-body: #CBD5E1;
--text-muted: #8896AB;
```

### 3.5 Shadow Berlapis Tactile (6 preset)
```
--shadow-chassis:
  0 1px 0 1px rgba(255,255,255,0.14) inset,
  0 -1px 0 1px rgba(0,0,0,0.7) inset,
  0 40px 90px -15px rgba(0,0,0,0.9),
  0 20px 45px -5px rgba(0,0,0,0.7);

--shadow-card:
  0 4px 12px rgba(0,0,0,0.45),
  0 1px 3px rgba(0,0,0,0.5),
  inset 0 1px 0 rgba(255,255,255,0.13),
  inset 0 -1px 0 rgba(0,0,0,0.5);

--shadow-card-lift:
  0 14px 30px rgba(0,0,0,0.65),
  0 4px 8px rgba(0,0,0,0.45),
  inset 0 1px 0 rgba(255,255,255,0.22),
  inset 0 -1px 0 rgba(0,0,0,0.5);

--shadow-recessed:
  inset 0 3px 8px rgba(0,0,0,0.85),
  inset 0 1px 2px rgba(0,0,0,0.9),
  0 1px 0 rgba(255,255,255,0.06);

--shadow-btn:
  0 3px 0 #050810,
  0 5px 12px rgba(0,0,0,0.5),
  inset 0 1px 0 rgba(255,255,255,0.18);

--shadow-btn-pressed:
  0 1px 0 #050810,
  0 2px 4px rgba(0,0,0,0.5),
  inset 0 2px 4px rgba(0,0,0,0.6);
```

### 3.6 Tipografi
```
--font-display: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;  /* wght 600;700;800 */
--font-body:    'Inter', system-ui, -apple-system, sans-serif;              /* wght 400;500;600;700 */
--font-mono:    'JetBrains Mono', Consolas, monospace;                       /* wght 400;500;600;700 */
```
Skala ukuran teraktual: slide-title 27px/800, cover h1 38px/800, slide-description 14px, tech-card-title 15.5px/700, tech-card-p 13px, code-content 12px, slide-table 12.5px, slide-category 11px/mono, footer 11.5px.

### 3.7 Geometri & Motion
```
--slide-width: 1200px;  --slide-height: 680px;
Responsive <=1280px: --slide-width:95vw; --slide-height:53.43vw;
body perspective: 1400px;
Radius: slide-frame 12px, card/box 8px, badge/tab 4–7px.
Transisi slide: translate3d + rotateY(4deg) + scale(0.96), cubic-bezier(0.16,1,0.3,1), 0.45s.
Hover tilt tech-card: rotateX/Y maks ±5deg (JS mousemove).
Syntax highlight code: .kw #38BDF8 / .fn #C084FC / .str #34D399 / .cm #64748B / .tbl #FCD34D.
```

### 3.8 Katalog Komponen (wajib terdokumentasi semua)
`deck-header` (hardware bar + brand-tag + status-led + slide-counter + ctrl-btn), `slide-frame` (chassis + corner studs `::before/::after`), `slides-wrapper`, `.slide/.active/.prev` (transisi 3D), `slide-label-row` (slide-category + slide-submeta), `slide-title`, `slide-description`, `slide-footer-row`, grid `card-grid-2/3/4`, `tech-card` (+`.highlight`, hover tilt), `code-box` (header + copy-btn + content + scrollbar custom), `table-sunken-frame`/`slide-table`, `task-sunken-frame`, `tab-bar`/`tab-btn` (chiclet), `error-box`, `tactile-meta-badge`, `kbd` (keycap), `progress-bar`, `overview-modal`/`overview-thumb`.

### 3.9 Kontrak Interaksi (JS)
Keyboard: `→/Space/PageDown` next, `←/Backspace/PageUp` prev, `Home/End`, `Esc` overview, `F` fullscreen. Touch swipe (threshold 60px). Hash routing `#slide-N` + `history.replaceState`. `copySnippet()` clipboard + fallback. `buildOverview()` grid. Semua tombol berfungsi nyata (no dead button).

---

## 4. Spesifikasi Premium Liquid Glass (iOS-style) — materi BARU untuk `design.md`

Saat ini template hanya punya glass sederhana di `overview-modal` (`backdrop-filter: blur(12px)`). `design.md` harus mendefinisikan komponen liquid glass premium berikut sebagai tambahan.

**Anatomi lapisan (full iOS spec):**
1. **Backdrop blur terukur**: `backdrop-filter: blur(16px) saturate(180%)` (rentang 16–24px; JANGAN >28px).
2. **Tint transparan tipis** selaras palet dark-cyan: `background: rgba(20,32,52,0.55)` (bukan putih susu).
3. **Border lensa 1px**: `rgba(255,255,255,0.18)` di sisi atas-kiri, menegaskan tepi kaca.
4. **Inner edge highlight (refraksi tepi)**: `inset 0 1px 0 rgba(255,255,255,0.35)`.
5. **Inner shadow lembut** (ketebalan kaca): `inset 0 -1px 2px rgba(0,0,0,0.4)`.
6. **Specular sheen halus**: pseudo-element `::before` gradien diagonal `linear-gradient(135deg, rgba(255,255,255,0.14), transparent 40%)` — halus, TANPA glow neon.
7. **Drop shadow ambient**: `0 12px 40px rgba(0,0,0,0.5)`.

**Aturan dose-cap & anti-slop (wajib ditulis eksplisit di `design.md`):**
- ✅ Maksimal **1 elemen liquid glass per slide** (panel fokus / kartu statistik utama).
- ✅ Letakkan di atas area dengan variasi warna/gradien supaya refraksi terlihat.
- ❌ JANGAN pasang glass di semua kartu (meratakan hierarki = slop).
- ❌ JANGAN blur raksasa (>28px) atau glow neon di border.
- ❌ JANGAN tint putih susu; pakai tint gelap selaras tema.

Sertakan di `design.md` token (`--glass-tint`, `--glass-blur`, `--glass-border`, `--glass-edge-highlight`, `--glass-inner-shadow`, `--glass-ambient`) + blok CSS class `.liquid-glass` lengkap (termasuk `::before` sheen) yang tinggal copy ke Antigravity.

---

## 5. Task Breakdown (kerjakan berurutan)

### Task 1 — Verifikasi token
Baca ulang `:root` + CSS utama `slide_procedure_function.html`. Cocokkan setiap nilai dengan Bagian 3 dokumen ini. **Verifikasi:** tidak ada nilai karangan; semua token = nilai asli file.

### Task 2 — Fondasi dokumen
Tulis pembuka `design.md`: judul, status, tujuan (template generik untuk agent AI), penegasan tema "Modern Skeuomorphic Tactile", + tabel **Anti-Slop Dials** (Energy / Rhythm / Motion, masing-masing justifikasi 1 baris) + daftar elemen slop yang dihindari. **Verifikasi:** tiap dial punya alasan; gaya kritis anti-slop konsisten.

### Task 3 — Sistem Token
Dokumentasikan seluruh token Bagian 3 dalam tabel + **justifikasi fungsional 1 baris per token** (purpose-gate): warna, 6 preset shadow, 3 font + skala, radius & dimensi. **Verifikasi:** nilai cocok dengan file; setiap token punya alasan pakai.

### Task 4 — Katalog Komponen
Dokumentasikan anatomi + "kapan dipakai" + "jangan" untuk SEMUA komponen di Bagian 3.8. **Verifikasi:** tidak ada komponen template yang terlewat.

### Task 5 — Premium Liquid Glass + CSS siap-pakai
Tulis bagian liquid glass sesuai Bagian 4: anatomi 7 lapisan, token, blok CSS `.liquid-glass` (+ `::before` sheen) valid & siap tempel, aturan dose-cap, daftar boleh/jangan. **Verifikasi:** CSS valid sintaksis; aturan dose-cap eksplisit.

### Task 6 — Blueprint 12-Slide + Standar + Checklist
Petakan arsitektur 12 slide secara **konten-agnostik** (pola layout per posisi: cover → konsep → grid-4 → komparasi tabel → split code → cursor/loop → error → studi kasus → skema tabel bertab → lembar tugas bertab → kunci jawaban bertab). Tegaskan prinsip "ganti konten, pertahankan struktur". Tambahkan: kontrak interaksi (keyboard/touch/hash/fullscreen/copy/overview), aksesibilitas (focus-visible, kontras WCAG AA, single-file autonomous), performa (translate3d 60fps), dan **checklist anti-slop final** untuk QA sebelum publish. **Verifikasi:** 12 pola slide + semua interaksi tercakup; `design.md` utuh dan siap dipakai.

---

## 6. Definition of Done

- [ ] `design.md` ditimpa total, berisi design system `slide_procedure_function.html` (bukan tema lama).
- [ ] Semua token (Bagian 3) terdokumentasi akurat 1:1 dengan file HTML.
- [ ] Semua komponen (Bagian 3.8) tercakup dengan aturan pakai.
- [ ] Bagian premium liquid glass lengkap + CSS `.liquid-glass` siap-pakai + aturan dose-cap/anti-slop.
- [ ] Blueprint 12-slide konten-agnostik + standar interaksi/aksesibilitas/performa + checklist anti-slop.
- [ ] Ditulis dalam Bahasa Indonesia; mandiri & bisa dipakai sebagai acuan build oleh agent AI lain.
