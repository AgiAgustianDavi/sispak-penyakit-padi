# 🌾 Sistem Pakar Diagnosa Penyakit Padi
Berbasis Certainty Factor (CF) dan metode Forward Chaining

## 📌 Deskripsi
Aplikasi ini membantu petani mendiagnosis apakah tanaman padi mereka terserang penyakit atau tidak berdasarkan gejala-gejala yang dialami, menggunakan teknik forward chaining dan perhitungan certainty factor (CF).

## 🛠️ Fitur
- Input gejala melalui form web.
- Pengguna memasukkan tingkat keyakinan (CF evidence) untuk setiap gejala.
- Sistem melakukan perhitungan Certainty Factor berdasarkan rule + input user.
- Output: diagnosa (terserang atau tidak) dan nilai CF akhir.

## ▶️ Cara Menjalankan
1. 📦 **Persiapan Lingkungan**
   Pastikan Python 3.7+ sudah terinstall.  
   Install Flask:
   ```bash
   pip install flask
   ```
2. 🚀 **Jalankan Aplikasi**
   Masuk ke direktori proyek lalu jalankan:
   ```
   python app.py
   ```
4. 🌐 **Akses Website**
   Buka browser dan akses:
   ```
   http://127.0.0.1:5000/
   ```
  
