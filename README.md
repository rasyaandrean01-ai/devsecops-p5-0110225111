# SecureNotes — DevSecOps Pipeline

## 1. Deskripsi Proyek

SecureNotes merupakan aplikasi REST API sederhana berbasis Python dan Flask untuk mengelola catatan. Aplikasi ini dibuat sebagai proyek praktikum DevSecOps dengan menerapkan pengujian otomatis dan pemindaian keamanan kode sumber.

## 2. Teknologi yang Digunakan

- Python 3.13
- Flask untuk membangun REST API
- Pytest untuk pengujian otomatis
- Bandit untuk Static Application Security Testing (SAST)
- Git dan GitHub untuk version control
- GitHub Actions untuk menjalankan pipeline otomatis

## 3. Fitur Aplikasi

- Menampilkan informasi aplikasi melalui endpoint `/`.
- Menampilkan daftar catatan melalui endpoint `GET /notes`.
- Menambahkan catatan melalui endpoint `POST /notes`.
- Menghapus catatan melalui endpoint `DELETE /notes/<note_id>`.
- Memvalidasi isi catatan agar tidak kosong dan tidak melebihi batas karakter.

## 4. Struktur Proyek

```text
devsecops-p5/
├── .github/
│   └── workflows/
│       └── devsecops.yml
├── tests/
│   └── test_app.py
├── app.py
├── config.py
├── notes.py
├── storage.py
├── validators.py
├── requirements.txt
└── README.md
```

## 5. Cara Menjalankan Aplikasi

Aktifkan virtual environment, kemudian instal dependensi:

```bash
pip install -r requirements.txt
```

Jalankan aplikasi:

```bash
python app.py
```

Jalankan pengujian otomatis:

```bash
python -m pytest -v
```

## 6. Implementasi Pipeline DevSecOps

Pipeline didefinisikan dalam `.github/workflows/devsecops.yml` dan dijalankan ketika terdapat push atau pull request ke branch `main`.

Pipeline memiliki dua job:

1. **Build and Test** — mengambil kode dari repository, menyiapkan Python, menginstal dependensi, dan menjalankan unit test menggunakan Pytest.
2. **SAST Security Scan** — menjalankan pemindaian keamanan kode Python menggunakan Bandit. Job ini menggunakan `needs: build` sehingga baru dijalankan setelah job build berhasil.

Quality Gate dikonfigurasi melalui perintah Bandit dengan ambang tingkat keparahan tinggi (`-lll`). Temuan yang memenuhi ambang tersebut dapat menyebabkan job gagal.

## 7. Hasil Pengujian

Pengujian lokal menunjukkan empat test berhasil dijalankan (`4 passed`). Pada GitHub Actions, workflow **Fix DevSecOps workflow** juga berhasil dengan status `Success`; kedua job, yaitu **Build and Test** dan **SAST Security Scan**, menunjukkan status berhasil.

Catatan: keberhasilan job SAST berarti pemindaian selesai sesuai konfigurasi. Hal tersebut tidak dengan sendirinya menjamin bahwa seluruh kerentanan telah ditemukan atau bahwa aplikasi bebas dari kerentanan.

## 8. Kesimpulan

Proyek ini menerapkan dasar DevSecOps melalui integrasi pengujian otomatis dan pemindaian keamanan kode ke dalam pipeline GitHub Actions. Pemisahan job build dan SAST membantu memastikan pengujian aplikasi berhasil sebelum pemindaian keamanan dijalankan.