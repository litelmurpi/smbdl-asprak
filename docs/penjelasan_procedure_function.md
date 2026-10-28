# Penjelasan Materi: Stored Procedure, Function, Cursor & Error Handling

> Hand-out untuk mengajar mahasiswa yang baru mengenal SMBD dasar (DDL, DML, View).
> Disusun dari modul `Modul_Pengayaan_SMBD_Lanjut_Procedure_Function.pdf`.
> Fokus: menjembatani dari konsep yang **sudah** dikenal ke materi baru, dengan analogi sederhana.

---

## Jembatan dari materi yang sudah mereka kenal

Mahasiswa sudah paham:

- **DDL** (`CREATE TABLE`, `ALTER`) → membuat struktur
- **DML** (`SELECT`, `INSERT`, `UPDATE`, `DELETE`) → memanipulasi data
- **View** → "query yang disimpan dengan nama", supaya tidak perlu menulis ulang query panjang

Materi baru ini satu langkah lebih maju:

> Kalau **View** itu *menyimpan query*, maka **Stored Routine** itu *menyimpan program*.

View hanya bisa menampilkan data (satu SELECT). Stored Routine bisa punya **logika**:
percabangan (IF), perulangan (LOOP), variabel, dan bisa mengubah banyak tabel sekaligus.
Inilah lompatan konsep utamanya: dari "menyimpan tampilan data" ke "menyimpan proses/logika bisnis di dalam database".

---

## 1. Apa itu Stored Routine, dan kenapa ada?

**Analogi pembuka:**

> Bayangkan kasir minimarket. Setiap ada pembeli, kasir harus: cek stok → kurangi stok → catat nota → tambah poin member.
> Kalau tiap aplikasi (POS, mobile, web admin) menulis ulang langkah ini sendiri-sendiri, bisa beda-beda dan rawan salah.
> **Stored Routine = tulis sekali langkahnya, simpan di database, semua aplikasi tinggal "panggil".**

Empat alasan memindahkan logika ke database:

1. **Hemat lalu lintas jaringan** — kirim 1 perintah `CALL`, bukan belasan query bolak-balik.
2. **Logika terpusat** — aturan diskon/poin ditulis di satu tempat, tidak tersebar.
3. **Lebih cepat** — kode dikompilasi sekali, dipakai berulang (execution plan di-cache).
4. **Lebih aman** — kasir cukup diberi izin `EXECUTE`, bukan izin ubah tabel langsung.

Stored Routine ada **dua jenis**: **Function (UDF)** dan **Procedure**.

---

## 2. Function vs Procedure — perbedaan paling penting

|  | **Function (UDF)** | **Procedure** |
|---|---|---|
| Analogi | **Kalkulator** — kasih angka, dapat 1 hasil | **Mesin/robot** — jalankan serangkaian tugas |
| Mengembalikan nilai | **Wajib** kembalikan 1 nilai (`RETURN`) | Tidak wajib; bisa lewat parameter `OUT` |
| Cara panggil | Di dalam query: `SELECT fcHitungPoin(...)` | Berdiri sendiri: `CALL spCheckout(...)` |
| Ubah data (INSERT/UPDATE) | Umumnya **tidak boleh** | **Boleh** penuh |
| Untuk apa | Hitung / format nilai | Alur kerja transaksi lengkap |

**Kalimat kunci:**

> **Function dipakai *di dalam* SELECT untuk menghasilkan nilai.**
> **Procedure dipanggil dengan CALL untuk mengerjakan sesuatu.**

---

## 3. Function (UDF) — "kalkulator buatan sendiri"

MySQL sudah punya fungsi bawaan (`UPPER()`, `NOW()`, `FORMAT()`). UDF = bikin fungsi sendiri yang belum ada.

Contoh paling mudah — **hitung poin belanja** (1 poin tiap kelipatan Rp10.000):

```sql
DELIMITER $$
CREATE FUNCTION fcHitungPoinBelanja(total_belanja INT)
RETURNS INT              -- janji: fungsi ini mengembalikan satu angka
DETERMINISTIC
NO SQL
BEGIN
   DECLARE jml_poin INT DEFAULT 0;      -- variabel lokal
   IF total_belanja >= 10000 THEN
      SET jml_poin = FLOOR(total_belanja / 10000);
   END IF;
   RETURN jml_poin;      -- wajib ada di function
END$$
DELIMITER ;

-- cara pakai: seperti fungsi biasa di dalam SELECT
SELECT fcHitungPoinBelanja(14800) AS poin;   -- hasilnya 1
```

### Dua hal yang pasti ditanya mahasiswa

**a. Kenapa ada `DELIMITER $$`?**

Normalnya MySQL menganggap `;` sebagai "akhir perintah". Padahal di dalam `BEGIN...END` ada banyak `;`.
Kalau tidak diganti, MySQL mengira perintah selesai di `;` pertama. Jadi kita bilang sementara:
"akhir perintah itu `$$`, bukan `;`". Setelah selesai, kembalikan lagi ke `;`.

> **Analogi:** seperti memberi tahu "tanda titik di paragraf ini jangan dihitung sebagai akhir kalimat, akhir kalimat ditandai `$$`".

**b. `DETERMINISTIC` / `NO SQL` / `READS SQL DATA`** — ini "label keterangan sifat" fungsi:

- `DETERMINISTIC` = input sama → output selalu sama (mis. perhitungan matematika).
- `NO SQL` = fungsi tidak menyentuh tabel sama sekali (murni hitung).
- `READS SQL DATA` = fungsi membaca tabel (pakai SELECT) tapi tidak mengubahnya.

Untuk tahap awal cukup: "ini penanda sifat fungsi, biar MySQL tahu cara memperlakukannya."

---

## 4. Procedure & parameter IN / OUT / INOUT

**Analogi: mesin fotokopi**

- **IN** = kertas yang kamu *masukkan* (procedure membaca, aslimu tidak berubah)
- **OUT** = hasil fotokopi yang *keluar* (procedure yang mengisi, kamu terima hasilnya)
- **INOUT** = satu kertas yang kamu masukkan, dicoret-coret, lalu dikembalikan

| Mode | Arah | Ingatannya |
|---|---|---|
| `IN` | pemanggil → procedure | kirim data masuk (default) |
| `OUT` | procedure → pemanggil | ambil hasil keluar |
| `INOUT` | bolak-balik | kirim nilai, terima nilai baru |

Contoh `INOUT` paling jelas:

```sql
DELIMITER $$
CREATE PROCEDURE spHitungBonusLoyalitas(
   IN p_status_member VARCHAR(20),
   INOUT p_poin INT          -- nilai masuk, lalu diubah, lalu balik
)
BEGIN
   IF p_status_member = 'VIP' THEN
      SET p_poin = p_poin + 20;
   ELSEIF p_status_member = 'REGULER' THEN
      SET p_poin = p_poin + 5;
   END IF;
END$$
DELIMITER ;

-- pengujian:
SET @poin_awal = 10;
CALL spHitungBonusLoyalitas('VIP', @poin_awal);
SELECT @poin_awal;   -- jadi 30 (10 masuk, +20, kembali 30)
```

Tekankan tanda `@` → itu **variabel sesi** (milik pengguna), tempat menampung hasil `OUT`/`INOUT`.

---

## 5. Control Flow — logika di dalam database

Inilah yang membedakan Routine dari View. Sama seperti logika di bahasa pemrograman biasa:

- `IF ... THEN ... ELSEIF ... ELSE ... END IF` → percabangan
- `CASE` → percabangan banyak nilai
- `WHILE ... DO ... END WHILE` → ulang selama kondisi benar (cek di **awal**)
- `REPEAT ... UNTIL ... END REPEAT` → ulang sampai kondisi benar (cek di **akhir**)
- `LOOP ... LEAVE ... END LOOP` → ulang terus sampai disuruh berhenti

> Kalau mahasiswa sudah pernah belajar pemrograman: **"ini IF dan looping yang sama, cuma lokasinya di dalam database."**

---

## 6. Cursor — "memproses baris satu per satu"

**Pancing dengan masalahnya dulu:**

> Normalnya SQL bekerja *sekaligus satu kelompok* — `UPDATE customer SET poin = poin + 10` mengubah semua baris sekaligus.
> Tapi bagaimana kalau tiap customer dapat bonus **berbeda** tergantung poinnya?
> Di sinilah kita perlu "jalan pelan-pelan, baca satu baris, putuskan, lanjut ke baris berikutnya." Itulah **Cursor**.

**Analogi:** membaca daftar absen satu per satu — tunjuk nama pertama, lakukan sesuatu, lanjut ke bawah, sampai habis.

### Empat langkah cursor (hafalkan urutannya)

1. **DECLARE CURSOR** — tentukan query-nya (daftar yang mau dibaca)
2. **DECLARE HANDLER** — pasang "penanda habis": `DECLARE CONTINUE HANDLER FOR NOT FOUND SET v_selesai = 1;`
3. **OPEN** — buka daftarnya
4. **FETCH** (ambil baris) di dalam LOOP, lalu **CLOSE**

Bagian yang sering membingungkan: **variabel `v_selesai`**. Cursor tidak otomatis tahu kapan berhenti.
Kita pasang handler: "kalau FETCH sudah tidak menemukan baris lagi (NOT FOUND), set `v_selesai = 1`."
Lalu di dalam loop kita cek: "kalau `v_selesai = 1`, keluar (`LEAVE`)."

```sql
DELIMITER $$
CREATE PROCEDURE spProsesBonusPoinMassal()
BEGIN
   DECLARE v_kodecus CHAR(5);
   DECLARE v_poin INT;
   DECLARE v_selesai INT DEFAULT 0;

   -- 1. daftar yang mau diproses
   DECLARE curCustomer CURSOR FOR
      SELECT kodecus, pointterkumpul FROM customer WHERE kodecus <> 'M0000';
   -- 2. penanda habis
   DECLARE CONTINUE HANDLER FOR NOT FOUND SET v_selesai = 1;

   OPEN curCustomer;                              -- 3. buka
   loopCustomer: LOOP
     FETCH curCustomer INTO v_kodecus, v_poin;    -- ambil 1 baris
     IF v_selesai = 1 THEN LEAVE loopCustomer; END IF;   -- habis? keluar

     -- aturan bonus berbeda per baris
     IF v_poin >= 100 THEN
        UPDATE customer SET pointterkumpul = pointterkumpul + 20 WHERE kodecus = v_kodecus;
     ELSEIF v_poin > 50 THEN
        UPDATE customer SET pointterkumpul = pointterkumpul + 15 WHERE kodecus = v_kodecus;
     ELSEIF v_poin > 20 THEN
        UPDATE customer SET pointterkumpul = pointterkumpul + 10 WHERE kodecus = v_kodecus;
     ELSE
        UPDATE customer SET pointterkumpul = pointterkumpul + 7  WHERE kodecus = v_kodecus;
     END IF;
   END LOOP loopCustomer;
   CLOSE curCustomer;                             -- 5. tutup

   SELECT 'Pemrosesan bonus poin selesai.' AS status;
END$$
DELIMITER ;

CALL spProsesBonusPoinMassal();
```

> **Catatan jujur untuk disampaikan:** cursor itu **lambat** untuk data besar.
> Kalau bisa pakai `UPDATE ... CASE` sekaligus, itu lebih baik. Cursor dipakai hanya kalau
> tiap baris butuh logika yang benar-benar beda. (Contoh di atas sebenarnya bisa dibuat tanpa cursor
> pakai `CASE` — bagus untuk bahan diskusi kelas.)

---

## 7. Error Handling — menjaga data tetap konsisten

**Skenario pembuka:**

> Saat transaksi: stok dikurangi, nota dicatat, poin ditambah. Bagaimana kalau di tengah jalan listrik mati
> setelah stok berkurang tapi nota belum tercatat? Datanya kacau: stok hilang tapi tidak ada catatan penjualan.

Dua alat untuk ini:

### a. `SIGNAL SQLSTATE '45000'` — melempar error buatan sendiri

```sql
IF v_stok_tersedia < p_qty THEN
   SIGNAL SQLSTATE '45000'
   SET MESSAGE_TEXT = 'Transaksi Dibatalkan: Stok tidak mencukupi.';
END IF;
```

`45000` adalah kode standar untuk "error yang didefinisikan pengguna".
**Analogi:** satpam yang menolak transaksi sambil memberi alasan jelas.

### b. `DECLARE ... HANDLER` + Transaksi — jaminan "semua berhasil atau semua batal" (atomic)

```sql
DECLARE EXIT HANDLER FOR SQLEXCEPTION
BEGIN
   ROLLBACK;     -- kalau ada error, batalkan SEMUA perubahan
   RESIGNAL;     -- lalu teruskan pesan errornya ke pemanggil
END;

START TRANSACTION;
   INSERT INTO nota ...;
   INSERT INTO itemnota ...;
   UPDATE produk SET stok = stok - ...;
COMMIT;          -- kalau sampai sini aman, kunci semua perubahan
```

> **Analogi transaksi:** transfer ATM — uang keluar dari rekening A *dan* masuk ke rekening B,
> atau dua-duanya batal. Tidak boleh setengah jalan.

---

## 8. Studi kasus penutup: `spCheckoutTransaksi`

Prosedur checkout di modul (bagian 7) cocok sebagai **penutup** karena memakai semua konsep sekaligus:

- memanggil **function** (`fcGenerateNoNota`, `fcHitungPoinBelanja`)
- memakai parameter **OUT** (`p_nonota_dihasilkan`, `p_total_bayar`, `p_poin_baru`)
- validasi dengan **SIGNAL**
- **transaksi atomik** (`START TRANSACTION` ... `COMMIT`) + `EXIT HANDLER` untuk `ROLLBACK`

Tunjukkan ke mahasiswa bahwa potongan-potongan kecil yang dipelajari di bab 3–7 bersatu menjadi satu
alur bisnis nyata: proses kasir dari awal sampai akhir.

---

## Urutan mengajar yang disarankan

1. Jembatan **View → Routine** (konsep "simpan query" vs "simpan program")
2. **Function** dulu (paling mirip yang sudah dikenal — dipakai di SELECT)
3. Jelaskan **`DELIMITER`** saat contoh function pertama (pasti ditanya)
4. **Procedure + IN/OUT/INOUT** (analogi mesin fotokopi)
5. **Control flow** (IF/LOOP) — singkat, karena mirip pemrograman
6. **Cursor** (paling sulit — analogi daftar absen, hafalkan 4 langkah)
7. **Error handling + transaksi** (analogi ATM) — tutup dengan studi kasus checkout

---

## Ringkasan istilah penting (untuk dibagikan ke mahasiswa)

| Istilah | Arti singkat |
|---|---|
| Stored Routine | Program/logika yang disimpan di dalam database |
| Function (UDF) | Mengembalikan 1 nilai, dipakai di dalam SELECT |
| Procedure | Mengerjakan tugas, dipanggil dengan CALL |
| `DELIMITER` | Mengganti tanda akhir perintah sementara (agar `;` di dalam blok tidak memutus) |
| `IN / OUT / INOUT` | Arah aliran data parameter: masuk / keluar / bolak-balik |
| `@variabel` | Variabel sesi untuk menampung hasil OUT/INOUT |
| Cursor | Membaca hasil query baris demi baris |
| `NOT FOUND` handler | Penanda "baris sudah habis" saat FETCH |
| `SIGNAL SQLSTATE '45000'` | Melempar error kustom dengan pesan sendiri |
| Transaksi (`COMMIT`/`ROLLBACK`) | Jaminan "semua berhasil atau semua batal" (atomic) |
