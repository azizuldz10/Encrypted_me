# 🔐 Enkripsi dan Proteksi Kode Python Anda dengan PyArmor 7 🔐

Selamat datang di proyek **Enkripsi File Python**! Proyek ini bertujuan untuk memberikan alat yang dapat mengenkripsi dan melindungi file serta folder dalam aplikasi Python Anda. Kami juga melindungi kode Python menggunakan **PyArmor 7**, sehingga kode Anda lebih sulit diubah atau dibaca oleh pihak lain.

## ✨ Fitur Utama
- **Enkripsi File dan Folder**: Menggunakan algoritma AES untuk mengenkripsi konten file dan folder.
- **Proteksi Kode Sumber**: Lindungi kode Python Anda dari pembongkaran dan modifikasi dengan PyArmor versi 7.
- **Dukungan untuk Nama File dan Folder**: Nama file dan subfolder ikut terenkripsi untuk keamanan tambahan.

## 📜 Prasyarat
Sebelum menggunakan proyek ini, pastikan Anda memiliki beberapa prasyarat yang terinstal di sistem Anda:

1. **Python 3.x** - Pastikan Python terinstal di sistem Anda.
2. **PyArmor 7.x** - Kami menggunakan PyArmor versi 7 untuk melindungi kode sumber. Jika Anda belum memiliki PyArmor versi 7, ikuti langkah-langkah di bawah ini.

### ⚙️ Instalasi PyArmor 7.x
Untuk melindungi kode Anda, kami menggunakan **PyArmor versi 7.6.0**. Berikut langkah-langkah instalasinya:

1. **Uninstall PyArmor 8.x jika terinstal**:
    ```bash
    pip uninstall pyarmor
    ```

2. **Instal PyArmor versi 7.x**:
    ```bash
    pip install pyarmor==7.6.0
    ```

3. **Proteksi Kode Python**: Setelah PyArmor terinstal, Anda bisa mulai melindungi kode Anda dengan perintah berikut:
    ```bash
    pyarmor obfuscate nama_file.py
    ```

### 🛠️ Penggunaan

#### 🔒 Enkripsi File dan Folder
Untuk mengenkripsi file atau folder menggunakan alat ini, Anda bisa menjalankan skrip Python yang telah disediakan. Berikut langkah-langkahnya:

1. **Jalankan Program**:
    ```bash
    python enkripsi_file.py
    ```

2. **Pilih Opsi**:
    - `1`: Enkripsi File
    - `2`: Dekripsi File
    - `3`: Enkripsi Folder
    - `4`: Dekripsi Folder

3. **Masukkan Nama File/Folder** dan password untuk mengenkripsi atau mendekripsi file dan folder Anda.

#### 🔐 Proteksi Kode Python
Untuk melindungi kode sumber Python Anda agar tidak mudah dibaca atau diubah, ikuti langkah berikut:

1. **Obfuscasi Kode Sumber**:
    Gunakan perintah berikut untuk mengaburkan kode Python Anda:
    ```bash
    pyarmor obfuscate nama_file.py
    ```

2. **Buat Lisensi untuk Distribusi**:
    Anda dapat membuat lisensi distribusi dengan PyArmor untuk memastikan hanya pengguna berlisensi yang dapat menjalankan kode Anda:
    ```bash
    pyarmor licenses -e 2024-12-31 user1
    ```

3. **Buat Runtime**:
    Untuk mengemas runtime agar kompatibel dengan file terenkripsi:
    ```bash
    pyarmor pack nama_file.py
    ```

### 📦 Deployment
Jika Anda ingin membagikan proyek ini kepada pengguna lain, pastikan untuk mengompilasi atau mengaburkan kode dengan **PyArmor** terlebih dahulu sebelum mendistribusikannya.

### 📝 Lisensi
Proyek ini dilindungi oleh lisensi [MIT](LICENSE). Anda bebas menggunakan, memodifikasi, dan mendistribusikan kode ini dengan catatan menyertakan atribusi yang sesuai. 

---

### 🎨 Hiasan Tambahan
**Nikmati keamanan lebih dengan PyArmor** – kami mengutamakan **proteksi** dan **kerahasiaan** kode sumber Python Anda. Jika Anda memiliki pertanyaan atau butuh bantuan, jangan ragu untuk menghubungi kami melalui *issues*.

## 🛡️ Tetap Aman, Tetap Terenkripsi! 🛡️
