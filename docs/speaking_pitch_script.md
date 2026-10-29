# 🎤 PITCH DECK & SCRIPT PRESENTASI PEMROGRAMAN DATABASE
## Panduan Public Speaking & Storytelling Pengajaran: Stored Procedure, UDF, Cursor & Error Handling

> **Target Audiens:** Mahasiswa Praktikum SMBD Lanjut (sudah paham DDL, DML, dan View dasar).  
> **Estimasi Durasi Total:** 15 – 20 Menit (Penyampaian Materi) + 10 Menit (Eksplorasi Tugas Mandiri).  
> **Tone of Voice:** Enerjik, santai, analogis, profesional, dan interaktif (tidak membaca teks slide).  

---

## ⏱️ RUN OF SHOW & ALOKASI WAKTU

| Waktu | Slide | Topik / Fokus Utama | Analogi Kunci |
|---|---|---|---|
| **00:00 - 01:30** | Slide 01 | Hook Pembuka & Roadmap Belajar | Peralihan dari query pasif ke program aktif |
| **01:30 - 03:30** | Slide 02 | Jembatan Konsep & Kasir Minimarket | Skenario alur kasir POS & 4 Keuntungan RDBMS |
| **03:30 - 05:30** | Slide 03 | Komparasi: UDF vs Stored Procedure | **Kalkulator** (Function) vs **Robot Pekerja** (Procedure) |
| **05:30 - 07:30** | Slide 04 | UDF & Misteri DELIMITER $$ | Titik kalimat biasa vs titik penutup cerita |
| **07:30 - 09:30** | Slide 05 | Manajemen Parameter (IN, OUT, INOUT) | **Mesin Fotokopi** (Asli, Salinan, & Formulir) |
| **09:30 - 11:00** | Slide 06 | Kontrol Alur Logika (IF, CASE, LOOP) | "Sama seperti Python/Java, tapi di dalam server" |
| **11:00 - 13:30** | Slide 07 | Cursor & Iterasi Baris demi Baris | **Dosen Membaca Absensi** & Catatan Performa |
| **13:30 - 15:30** | Slide 08 | Error Handling & Transaksi ACID | **Satpam Toko (SIGNAL)** & **Mesin ATM (ACID)** |
| **15:30 - 17:00** | Slide 09 & 10 | Bedah Database Ritel 3NF | Skema 5 Tabel & Normalisasi Minimarket |
| **17:00 - 19:00** | Slide 11 | Demo Kasus Nyata: `spCheckout` | Penggabungan seluruh konsep ke 1 alur nyata |
| **19:00 - 20:00** | Slide 12 & 13 | Tantangan Tugas & Penutup | 10 Soal Bertingkat & Rubrik Evaluasi Lab |

---

## 🎙️ SLIDE-BY-SLIDE SPEAKING SCRIPT (KATA DEMI KATA)

---

### SLIDE 01: HERO COVER
* **Tampilan Layar:** Judul besar "Pemrograman Prosedural Database: Stored Procedure, UDF & Cursor" dengan 3 badge taktil.
* **Tindakan Fisik:** Tatap mata seluruh kelas, tersenyum, berdiri tegak, jangan pegang mouse terus-menerus.
* **Pacing:** Tenang, ramah, dan memancing rasa penasaran.

> **🗣️ Apa yang kamu ucapkan:**
> 
> *"Halo, selamat pagi/siang teman-teman semua!*  
> *Di pertemuan-pertemuan kemarin, kita sudah berhasil belajar cara mendesain tabel fisik lewat DDL, mengisi dan mengubah data lewat DML, dan kemarin kita juga sudah bikin VIEW.*  
> 
> *Tapi pernah gak kalian kepikiran: Kalau aplikasi kita makin besar—misalnya kita bikin sistem kasir Indomaret atau Alfamart yang punya ratusan cabang—apakah cukup database itu cuma kita suruh nyimpen tabel pasif aja?*  
> 
> *Hari ini, kita akan naik kelas. Kita gak cuma belajar bikin query, tapi kita akan belajar **membuat program utuh di dalam otak database server**. Kita akan kupas tuntas User Defined Function, Stored Procedure, Cursor, sampai cara mengamankan transaksi dengan Error Handling. Yuk, kita mulai!"*

---

### SLIDE 02: EVOLUSI PARADIGMA & KASIR MINIMARKET
* **Tampilan Layar:** Jembatan Konsep Banner + 4 Kartu Benefit.
* **Tindakan Fisik:** Berikan gestur tangan membandingkan kiri dan kanan saat menjelaskan View vs Routine.
* **Pertanyaan Pancingan Interaktif:** Lontarkan pertanyaan ke baris depan.

> **🗣️ Apa yang kamu ucapkan:**
> 
> *"Coba kalian ingat-ingat lagi: View itu apa sih?*  
> *(Tunggu 2 detik respons mahasiswa)*  
> *Tepat! View itu adalah query SELECT yang disimpan pakai nama. View itu pasif, cuma menampilkan data.*  
> 
> *Nah, satu kalimat kunci yang wajib kalian ingat hari ini:*  
> 👉 **'Kalau View bertugas menyimpan QUERY, maka Stored Routine bertugas menyimpan PROGRAM.'**  
> 
> *Bayangkan kasir di minimarket. Tiap kali ada pembeli bayar belanjaan, kasir harus:*  
> *1. Cek stok di gudang.*  
> *2. Kurangi stok barang.*  
> *3. Terbitkan nomor nota.*  
> *4. Tambah poin belanja member.*  
> 
> *Bayangkan kalau langkah 1 sampai 4 ini ditulis sendiri-sendiri di aplikasi kasir desktop, ditulis ulang lagi di aplikasi mobile pembeli, ditulis ulang lagi di web admin. Begitu ada diskon baru atau rumus poin berubah, kalian harus ubah kodingan di 3 tempat berbeda! Rawan salah, dan rawan dicurangi.*  
> 
> *Dengan Stored Routine, seluruh urutan logika ini kita kunci di dalam database server. Manfaatnya ada empat:*  
> *Pertama, **Reduksi Latensi**—aplikasi klien cukup kirim 1 perintah `CALL`, bukan bolak-balik kirim 15 query lewat WiFi.*  
> *Kedua, **Logika Terpusat**—semua aplikasi patuh pada aturan yang sama persis.*  
> *Ketiga, **Execution Cache**—database cuma mengompilasi kueri satu kali, setelah itu jalan super kencang dari RAM.*  
> *Dan keempat, **Keamanan**—kasir cukup kita kasih izin menjalankan prosedur `CALL`, tanpa perlu kita kasih akses langsung otak-atik tabel produk."*

---

### SLIDE 03: KOMPARASI HAKIKI (UDF VS STORED PROCEDURE)
* **Tampilan Layar:** Callout Kalkulator vs Robot + Tabel Komparasi.
* **Tindakan Fisik:** Angkat satu jari saat menyebut angka 1 untuk UDF.

> **🗣️ Apa yang kamu ucapkan:**
> 
> *"Di MySQL, program tersimpan ini dibagi jadi dua: **Function (UDF)** dan **Stored Procedure**.*  
> *Jangan sampai tertukar, karena ini sering banget keluar di ujian dan tes kerja basis data!*  
> 
> *Cara gampang mengingatnya, pakai analogi ini:*  
> 📱 **FUNCTION itu ibarat KALKULATOR.**  
> *Kalian masukkan angka, pencet tombol, dia **PASTI** mengembalikan tepat **SATU HASIL**. Fungsi ini wajib punya klausa `RETURNS` dan pernyataan `RETURN`. Karena menghasilkan nilai, dia dipanggil **di dalam** kueri `SELECT`, persis seperti fungsi bawaan `NOW()` atau `UPPER()`.*  
> 
> 🤖 **STORED PROCEDURE itu ibarat ROBOT PEKERJA.**  
> *Kalian gak cuma minta hitung-hitungan, tapi kalian suruh dia: 'Tolong cek stok, kurangi barang, catat nota, kalau stok habis tolong batalkan!' Dia menjalankan serangkaian aksi nyata. Dia gak pakai `RETURN`, tapi dipanggil mandiri pakai perintah `CALL sp_nama()`.*  
> 
> *Aturan mutlaknya: Di dalam Function, kalian **dilarang keras** melakukan mutasi DML (INSERT/UPDATE/DELETE) yang merubah isi tabel. Kalau butuh mutasi tabel, wajib pakai Stored Procedure!"*

---

### SLIDE 04: FUNCTION (UDF) & MISTERI DELIMITER
* **Tampilan Layar:** Code box `fcGenerateNoNota` di kiri + Penjelasan Delimiter di kanan.
* **Tindakan Fisik:** Arahkan tangan ke kata `DELIMITER $$` di layar.

> **🗣️ Apa yang kamu ucapkan:**
> 
> *"Sekarang coba lihat kode di sebelah kiri. Ini contoh UDF `fcGenerateNoNota` untuk membuat kode nota otomatis berdasarkan tanggal.*  
> 
> *Tapi sebelum kalian ngetik, pasti ada yang penasaran:*  
> *'Kak, kenapa di baris paling atas ada tulisan `DELIMITER $$`? Buat apa sih?'*  
> 
> *Begini penjelasannya: Normalnya, MySQL menganggap tanda titik-koma (`;`) itu adalah **akhir dari satu perintah**—ibarat tanda titik di akhir kalimat.*  
> *Padahal, di dalam blok `BEGIN ... END`, kita punya banyak baris logika yang masing-masing butuh titik-koma. Kalau kita gak ganti delimiternya, MySQL bakal mengira perintah kita selesai di titik-koma pertama. Akhirnya apa? Langsung Syntax Error!*  
> 
> *Makanya, kita bilang dulu ke MySQL: 'Hei MySQL, sementara ini tanda akhir cerita kita ganti jadi tanda dollar ganda `$$` ya. Jangan potong dulu kueri saya sebelum ketemu `$$`'. Begitu selesai ditutup `END$$`, kita balikin lagi ke titik-koma standar pakai `DELIMITER ;`.*  
> 
> *Lalu perhatikan label di bawahnya: `DETERMINISTIC` dan `READS SQL DATA`. Ini 'surat pernyataan' ke database engine. `DETERMINISTIC` artinya kalau dikasih input yang sama, hasilnya dijamin selalu sama. Sedangkan `READS SQL DATA` artinya fungsi ini membaca isi tabel pakai SELECT, tapi gak merubah datanya."*

---

### SLIDE 05: MANAJEMEN PARAMETER (IN, OUT, INOUT)
* **Tampilan Layar:** Banner Mesin Fotokopi + 3 Kartu Mode Parameter.
* **Tindakan Fisik:** Peragakan gerakan memasukkan kertas (IN), mengambil kertas keluar (OUT), dan mencoret kertas (INOUT).

> **🗣️ Apa yang kamu ucapkan:**
> 
> *"Kalau di Stored Procedure, kita gak pakai perintah `RETURN`. Lalu bagaimana cara kita mengirim data masuk dan mengambil hasilnya keluar?*  
> *Jawabannya: Lewat **3 Mode Parameter**.*  
> 
> *Biar gak bingung, bayangkan kalian lagi di depan **Mesin Fotokopi**:*  
> 
> 📄 **Parameter IN (Default):**  
> *Ibarat dokumen asli yang kalian taruh di atas scanner. Mesin fotokopi cuma membaca isinya. Kertas asli kalian di luar gak bakal berubah sama sekali.*  
> 
> 📑 **Parameter OUT:**  
> *Ibarat lembaran kertas fotokopi kosong yang keluar dari mesin. Prosedur yang mengisi nilainya, dan begitu selesai, kalian bawa pulang hasilnya.*  
> 
> 📝 **Parameter INOUT:**  
> *Ibarat formulir pendaftaran. Kalian bawa masuk membawa data awal, di dalam prosedur nilainya dicoret atau ditambah—misalnya poin member ditambah 20—lalu kertas yang sama dikembalikan ke kalian dengan nilai baru.*  
> 
> *Ingat tips penting ini untuk praktikum nanti:*  
> *Saat memanggil parameter OUT atau INOUT, gunakan variabel bertanda **`@`**, contohnya `CALL spRegistrasiMember(..., @id_baru); SELECT @id_baru;`. Tanda keong (`@`) ini adalah variabel sesi milik koneksi kalian untuk menampung hasil kembalian."*

---

### SLIDE 06: KONTROL ALUR LOGIKA (CONTROL FLOW)
* **Tampilan Layar:** Card IF-ELSE/CASE di kiri + Card LOOP/WHILE/REPEAT di kanan.
* **Tindakan Fisik:** Tersenyum santai untuk menurunkan ketegangan mahasiswa.

> **🗣️ Apa yang kamu ucapkan:**
> 
> *"Teman-teman di sini pasti sudah pernah belajar Python, Java, C++, atau JavaScript, kan?*  
> *Kabar baiknya: Logika kontrol di database itu **sama persis**!*  
> 
> *Kita punya `IF ... THEN ... ELSEIF ... ELSE ... END IF` untuk percabangan bersyarat, dan `CASE` untuk mengecek banyak pilihan nilai seperti jenis kelamin.*  
> *Untuk perulangan, kita punya `WHILE` yang memeriksa kondisi di awal, `REPEAT` yang memeriksa kondisi di akhir, dan `LOOP` yang berjalan terus sampai kita tembak pakai perintah `LEAVE`.*  
> 
> *Jadi gak perlu takut, konsep algoritmanya sama, bedanya cuma sekarang programnya hidup di dalam database!"*

---

### SLIDE 07: CURSOR & SIKLUS HIDUP
* **Tampilan Layar:** Analogi Lembar Absensi + 5 Tahap Siklus Hidup Cursor.
* **Tindakan Fisik:** Tunjuk satu per satu tahap 1 sampai 5.

> **🗣️ Apa yang kamu ucapkan:**
> 
> *"Nah, sekarang kita masuk ke materi yang biasanya dianggap paling menantang: **CURSOR**.*  
> *Kenapa kita butuh Cursor?*  
> 
> *Normalnya, SQL itu sifatnya 'set-based'—sekali kita jalankan `UPDATE customer SET poin = poin + 10`, semua baris berubah barengan dalam satu hentakan.*  
> *Tapi bagaimana kalau aturan bisnisnya rumit? Kalau poinnya di atas 100 dapat bonus 20, kalau 50 dapat 15, kalau transaksi tahun lalu sekian dapat diskon beda? Kita butuh memproses data **baris demi baris secara berurutan**.*  
> 
> *Analogi gampangnya: **Dosen yang sedang membaca daftar absensi mahasiswa**.*  
> *Dosen pegang lembaran daftar nama, tunjuk nama pertama, periksa kehadirannya, lanjut ke nama kedua, ketiga, sampai habis.*  
> 
> *Untuk membuat kursor, ada **5 langkah sakral** yang wajib kalian hafal urutannya:*  
> *1. `DECLARE nama_kursor CURSOR FOR SELECT...` &rarr; Tentukan daftar data yang mau dibaca.*  
> *2. `DECLARE CONTINUE HANDLER FOR NOT FOUND SET v_selesai = 1;` &rarr; Pasang alarm/penanda kalau barisnya sudah habis.*  
> *3. `OPEN nama_kursor;` &rarr; Buka lembaran kursor di memori.*  
> *4. `FETCH ... INTO ...` di dalam LOOP &rarr; Ambil satu baris, masukkan ke variabel, dan cek: kalau `v_selesai = 1`, segera `LEAVE`.*  
> *5. `CLOSE nama_kursor;` &rarr; Tutup dan bersihkan memorinya dari server.*  
> 
> ⚠️ *Catatan kejujuran seorang engineer: Cursor itu berat dan lambat kalau datanya jutaan baris karena dia jalan satu per satu. Kalau masalah kalian bisa selesai pakai kueri biasa `UPDATE ... CASE`, dahulukan kueri biasa. Pakai kursor hanya kalau logikanya memang butuh iterasi individual."*

---

### SLIDE 08: ERROR HANDLING & TRANSAKSI ACID
* **Tampilan Layar:** Dual Callout Satpam Toko & Mesin ATM + Blok Transaksi Rollback.
* **Tindakan Fisik:** Gunakan nada suara yang lebih tegas untuk menunjukkan pentingnya integritas data.

> **🗣️ Apa yang kamu ucapkan:**
> 
> *"Pernah gak kalian belanja di minimarket, barang kalian sudah di-scan, stok fisik sudah kepotong, tapi tiba-tiba listrik padam atau koneksi bank kasir putus sebelum struk keluar?*  
> *Apa yang terjadi kalau database gak punya pengaman? Stok toko berkurang, uang gak masuk, laporan keuangan selisih. Bencana!*  
> 
> *Di sinilah kita wajib memasang dua benteng pengaman:*  
> 
> 👮 **Benteng 1: SIGNAL SQLSTATE '45000' (Si Satpam Toko)**  
> *Kalau ada pembeli mau beli 10 barang padahal stok di gudang sisa 2, kita jangan biarkan database diam aja sampai minus. Kita suruh satpam menolak dengan tegas:*  
> *`SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Stok tidak mencukupi!';`*  
> *Kode `45000` ini adalah kode standar internasional untuk error buatan pengguna.*  
> 
> 🏧 **Benteng 2: Transaksi ACID (Prinsip Mesin ATM)**  
> *Bayangkan transfer uang di ATM. Uang didebet dari rekening A, lalu dikreditkan ke rekening B. Keduanya WAJIB berhasil bersama-sama lewat perintah `COMMIT`.*  
> *Kalau di tengah jalan mesin mati atau error, perintah `ROLLBACK` akan membatalkan seluruh operasi dan mengembalikan saldo rekening ke kondisi semula!*  
> *Dengan `DECLARE EXIT HANDLER FOR SQLEXCEPTION`, kita menjamin database kita 100% konsisten: semua operasi berhasil, atau tidak sama sekali!"*

---

### SLIDE 09 & 10: DATABASE RITEL 3NF (DATASET PRAKTIKUM)
* **Tampilan Layar:** Tampilan tabel skema 3NF (Produk, Kasir, Customer, Nota, ItemNota).
* **Tindakan Fisik:** Tunjukkan tombol unduh SQL di layar slide.

> **🗣️ Apa yang kamu ucapkan:**
> 
> *"Untuk mempraktikkan seluruh materi hari ini, kita sudah siapkan database ritel minimarket berstandar Normalisasi 3NF lengkap.*  
> *Ada 5 tabel utama: `PRODUK`, `KASIR`, `CUSTOMER`, `NOTA`, dan tabel perantara relasi many-to-many yaitu `ITEMNOTA`.*  
> 
> *Kalian bisa langsung unduh berkas `minimarket_db.sql` lewat tombol unduh di slide ini, lalu import ke MySQL Workbench atau terminal kalian masing-masing."*

---

### SLIDE 11: DEMO STUDI KASUS CHECKOUT KASIR TERPADU
* **Tampilan Layar:** Kode utuh `spCheckoutTransaksiBaru`.
* **Tindakan Fisik:** Tunjukkan bagaimana baris-baris kode menyatukan semua konsep sebelumnya.

> **🗣️ Apa yang kamu ucapkan:**
> 
> *"Sekarang coba lihat Slide 11 ini. Ini adalah 'grand finale' kita.*  
> *Seluruh kepingan puzzle yang kita pelajari dari awal tadi bersatu di dalam satu prosedur `spCheckoutTransaksi`:*  
> 
> *• Dia memanggil UDF `fcGenerateNoNota` untuk membuat nomor nota unik.*  
> *• Dia menerima parameter `IN` kasir dan produk, lalu mengeluarkan nomor nota dan total belanja lewat parameter `OUT`.*  
> *• Dia memvalidasi stok dengan `SIGNAL SQLSTATE '45000'`.*  
> *• Dan dia membungkus seluruh insert ke nota, itemnota, potong stok produk, dan tambah poin customer di dalam satu pelindung atomik `START TRANSACTION` sampai `COMMIT`.*  
> 
> *Inilah cara insinyur database di dunia nyata merancang sistem transaksi perbankan dan e-commerce!"*

---

### SLIDE 12 & 13: LEMBAR TANTANGAN TUGAS & PENUTUP
* **Tampilan Layar:** 4 Tab Tingkat Kesulitan Soal.
* **Tindakan Fisik:** Berikan dorongan motivasi dan instruksikan mahasiswa untuk mulai mencoba.

> **🗣️ Apa yang kamu ucapkan:**
> 
> *"Nah, sekarang giliran kalian untuk mencoba!*  
> *Di Slide 12, sudah ada **10 Soal Praktikum Mandiri Bertingkat** yang dibagi menjadi 4 level tantangan:*  
> *• Level 1: UDF Skalar (evaluasi status stok & loyalitas member)*  
> *• Level 2: Stored Procedure dengan parameter IN, OUT, dan INOUT*  
> *• Level 3: Cursor Loop untuk kompilasi riwayat transaksi dan restok massal*  
> *• Level 4: Error Handling dan Transaksi Atomik dengan SIGNAL*  
> 
> *Kerjakan secara bertahap mulai dari Level 1. Jangan lupa tangkap layar (screenshot) kode dan hasil eksekusinya.*  
> *Kunci jawaban dan rubrik penilaian sudah saya proteksi dengan PIN asisten di Slide 13.*  
> 
> *Silakan mulai dieksplorasi, tanyakan jika ada error, dan selamat coding! Terima kasih!"*

---

## 🛡️ TANYA-JAWAB: CARA MENJAWAB PERTANYAAN JEBAKAN MAHASISWA

### Q1: "Kak, kenapa kita harus repot-repot bikin Stored Procedure di database? Kan di backend (Node.js/Laravel/Python) kita bisa bikin function yang sama?"
> **Jawaban Ampuh:**  
> *"Pertanyaan bagus banget! Alasan utamanya adalah **Network Latency** dan **Single Source of Truth**. Kalau logikanya di backend, kamu harus kirim 5-10 kueri bolak-balik lewat kabel jaringan. Kalau Stored Procedure, kamu cuma kirim 1 perintah CALL, eksekusinya langsung di RAM database. Selain itu, kalau perusahaan punya banyak aplikasi (misal POS kasir dibuat pakai C#, aplikasi mobile pakai Flutter, web admin pakai PHP), mereka gak perlu nulis ulang formula bisnisnya 3 kali. Cukup panggil Stored Procedure yang sama di database."*

### Q2: "Kak, tadi katanya Cursor lambat. Jadi kapan dong kita boleh pakai Cursor?"
> **Jawaban Ampuh:**  
> *"Gunakan Cursor **hanya** jika tiap baris data memerlukan tindakan yang berbeda dan tidak bisa diselesaikan oleh aljabar relasional SQL biasa. Contohnya: di tiap baris data, kamu harus memanggil API eksternal, atau memanggil Stored Procedure lain dengan parameter dinamis per baris. Tapi kalau cuma urusan mengubah angka bersyarat, utamakan pakai perintah `UPDATE ... CASE WHEN ...` karena kueri set-based jauh lebih cepat puluhan kali lipat daripada Cursor."*

### Q3: "Kak, kenapa variabel penampung OUT harus pakai tanda `@`?"
> **Jawaban Ampuh:**  
> *"Di MySQL, variabel yang diawali tanda `@` adalah **Session-User Variable**. Variabel ini hidup di memori selama kamu masih terhubung ke server database. Karena Stored Procedure dipanggil dari luar blok program, kita butuh wadah penyimpanan di level sesi pengguna agar hasil perhitungan prosedur tidak langsung hilang begitu prosedur selesai dieksekusi."*
