## 🤖 NLP Chatbot for Symptom Checking

Chatbot ini dibangun dengan teknologi NLP (Natural Language Processing) menggunakan Python dan Flask. Chatbot ini mampu mendeteksi intent dari keluhan pengguna terkait gejala penyakit katarak dan merespons secara otomatis.

---

### 📁 Fitur Utama

* Deteksi intent sederhana dari input pengguna berbasis gejala.
* Respons otomatis berdasarkan intent.
* Antarmuka web interaktif dan responsif.
* Dapat dikembangkan menjadi sistem tanya-jawab medis berbasis NLP.

---

### 🚀 Cara Menjalankan

#### 1. Clone Repository

```bash
git clone https://github.com/widiarrohman1234/NLP_chatbot.git
cd NLP_chatbot
```

#### 2. Install Dependencies
```bash
pip install requirements.txt
```

#### 3. Jalankan Aplikasi Flask

```bash
python app.py
```

#### 4. Akses di Browser

Buka browser dan kunjungi:
`http://127.0.0.1:5000`

---

### 💬 Struktur Intent (Contoh)

| Intent                    | Contoh Kalimat                   | Respons                                                                 |
| ------------------------- | -------------------------------- | ----------------------------------------------------------------------- |
| Sapaan   | "Halo"    | "Halo, ada yang bisa saya bantu?"    |
| gejala\_katarak | "apa itu katarak?" | "Penglihatan kabur, perubahan warna, sulit melihat di malam hari, sensasi seperti kabut, kesulitan membaca, dan kilauan seperti halo di sekitar lampu." |
| diagnosis\_katarak  | "cara mengetahui katarak"       | "Umumnya Dokter mata akan melakukan pemeriksaan mata, melihat perubahan pada lensa mata, dan mengkonfirmasi dengan pemeriksaan mata lengkap, Namun sekarang anda dapat memeriksa kesehatan mata dengan mudah menggunakan EyeUs"                          |
| gejala\_awal\_katarak   | "Gejala awal katarak"         | "Umumnya, gejala awal katarak termasuk penglihatan kabur, kesulitan melihat detail, dan perlu penerangan lebih saat membaca."                    |

---

### 📌 Teknologi yang Digunakan

* Python + Flask
* HTML5 + CSS3
* Javascript (fetch API)
* Sklearn / Regex / Rule-based NLP

---

### 📄 Lisensi

Proyek ini dilisensikan di bawah [MIT License](LICENSE).

---

### 🙋‍♂️ Kontribusi

Pull request dan masukan sangat disambut! Kamu bisa mulai dengan:

* Menambahkan intent baru
* Meningkatkan desain UI
* Membuat sistem NLP berbasis ML

### 👨🏻‍💻 Kontak
* Gmail: widiarrohman1234@gmail.com
* Github: [widiarrohman1234](https://github.com/widiarrohman1234)
