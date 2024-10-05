# 🔐 Alat Enkripsi dan Proteksi Kode Python 🔐

Hai! Saya telah mengembangkan **Alat Enkripsi File Python** ini sebagai solusi untuk mengenkripsi file dan folder, serta melindungi kode Python dari pembongkaran dan modifikasi. Saya juga telah menggunakan **PyArmor versi 7** untuk melindungi kode, sehingga bisa lebih aman saat digunakan oleh pihak lain.

## ✨ Fitur Utama yang Saya Tawarkan
- **Enkripsi File dan Folder**: Algoritma AES digunakan untuk mengenkripsi konten file dan folder Anda.
- **Proteksi Kode Python**: Saya menggunakan PyArmor untuk melindungi kode dari modifikasi atau penyalahgunaan.
- **Nama File dan Folder Dienkripsi**: Tidak hanya konten file, saya juga telah menambahkan fitur untuk mengenkripsi nama file dan subfolder di dalamnya.

## 📜 Persiapan Sebelum Menggunakan
Sebelum mulai menggunakan alat ini, pastikan Anda memiliki beberapa persyaratan berikut:

1. **Python 3.x** - Pastikan Python terinstal di sistem Anda.
2. **PyArmor versi 7.x** - Alat ini saya kembangkan menggunakan PyArmor versi 7 untuk proteksi kode. Jika belum terinstal, ikuti langkah instalasi di bawah ini.

### ⚙️ Instalasi PyArmor 7.x
Saya merekomendasikan Anda untuk menggunakan **PyArmor versi 7.6.0**. Berikut adalah langkah-langkah instalasinya:

1. Jika Anda telah menginstal **PyArmor versi 8.x**, uninstall terlebih dahulu dengan perintah berikut:
    ```bash
    pip uninstall pyarmor
    ```

2. Selanjutnya, instal **PyArmor versi 7.x**:
    ```bash
    pip install pyarmor==7.6.0
    ```

3. Jika sudah, Anda bisa mulai melindungi kode Python dengan perintah:
    ```bash
    pyarmor obfuscate nama_file.py
    ```

### 🛠️ Cara Menggunakan Alat Ini

#### 🔒 Enkripsi File dan Folder
Untuk menggunakan alat enkripsi ini, ikuti langkah-langkah berikut:

1. **Jalankan Program**:
    ```bash
    python enkripsi_file.py
    ```

2. **Pilih Opsi yang Anda Butuhkan**:
    - `1`: Enkripsi File
    - `2`: Dekripsi File
    - `3`: Enkripsi Folder
    - `4`: Dekripsi Folder

3. **Masukkan Nama File/Folder** serta password sesuai permintaan untuk mengenkripsi atau mendekripsi file/folder.

#### 🔐 Proteksi Kode Python Saya
Untuk melindungi kode sumber dari pembongkaran atau modifikasi, saya menggunakan PyArmor. Anda juga bisa melakukan hal yang sama dengan cara berikut:

1. **Obfuscasi Kode**:
    Untuk mengacak (obfuscate) kode Python, gunakan perintah berikut:
    ```bash
    pyarmor obfuscate nama_file.py
    ```

2. **Buat Lisensi** untuk mendistribusikan kode:
    Saya merekomendasikan membuat lisensi sehingga hanya pengguna tertentu yang bisa menjalankan kode:
    ```bash
    pyarmor licenses -e 2024-12-31 user1
    ```

3. **Buat Runtime**:
    Jika perlu, saya juga membuat runtime untuk mendistribusikan kode dengan aman:
    ```bash
    pyarmor pack nama_file.py
    ```

### 📦 Proses Deployment
Sebelum mendistribusikan proyek ini, pastikan saya atau Anda telah melakukan obfuscasi pada kode Python menggunakan **PyArmor** agar kode tidak mudah diubah oleh orang lain.

### 📝 Lisensi
Alat ini saya buat dengan lisensi [MIT](LICENSE). Silakan menggunakan, memodifikasi, atau mendistribusikannya, asalkan Anda menyertakan atribusi yang sesuai.

---

### 🎨 Hiasan Tambahan dari Saya
**Nikmati keamanan tambahan dari PyArmor** – Saya berkomitmen untuk menjaga **proteksi** dan **kerahasiaan** kode Python Anda. Jika Anda memiliki pertanyaan atau masukan, jangan ragu untuk menghubungi saya melalui *issues* atau email.

## 🛡️ Lindungi Kode Anda, Tetap Aman, Tetap Terenkripsi! 🛡️
