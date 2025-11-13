# 📊 Analisis Nilai Siswa per Mata Pelajaran

Proyek ini dibuat menggunakan **Python**, **pandas**, **matplotlib**, dan **seaborn** untuk menganalisis dan memvisualisasikan data nilai siswa dari file `nilai_siswa.csv`.

## 🧩 Deskripsi Program
Program ini membaca data nilai siswa dari file CSV dan melakukan beberapa analisis statistik, seperti:
- Menampilkan informasi umum data (`info()` dan `describe()`).
- Menghitung **rata-rata**, **median**, dan **modus** dari seluruh nilai.
- Menampilkan data nilai khusus untuk mata pelajaran tertentu (contoh: **Matematika**).
- Mengelompokkan data berdasarkan mata pelajaran dan menghitung nilai **maksimum** serta **minimum**.
- Membuat dua jenis visualisasi untuk melihat sebaran dan perbandingan nilai antar mata pelajaran.

## ⚙️ Library yang Digunakan
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```

## 📁 Struktur File
```
📂 Proyek_Nilai_Siswa
│
├── nilai_siswa.csv        # Dataset nilai siswa
├── output.png              # Grafik Rata-Rata Nilai per Mapel
├── output1.png             # Grafik Sebaran Nilai per Mata Pelajaran
└── analisis_nilai.py       # Script utama program
```

## 📈 Hasil Visualisasi

### 1️⃣ Rata-Rata Nilai per Mapel
Grafik batang berikut menunjukkan rata-rata nilai untuk setiap mata pelajaran.  
Dapat dilihat bahwa **Matematika** memiliki nilai rata-rata tertinggi.

![Rata-Rata Nilai per Mapel](output.png)

### 2️⃣ Sebaran Nilai per Mata Pelajaran
Boxplot di bawah ini memperlihatkan sebaran nilai (rentang, median, dan outlier) untuk setiap mata pelajaran.  
Dari grafik terlihat bahwa **Matematika dan Fisika** memiliki rentang nilai yang cukup tinggi dibanding mapel lain.

![Sebaran Nilai per Mata Pelajaran](output1.png)

## 🧠 Analisis Singkat
- **Matematika** memiliki rata-rata tertinggi dan variasi nilai yang besar.
- **Bahasa Inggris** dan **Produktif** cenderung memiliki nilai yang lebih stabil.
- Terdapat beberapa **outlier** di pelajaran Bahasa Indonesia dan Fisika (nilai rendah).

## 💻 Cara Menjalankan Program
1. Pastikan Python dan library berikut sudah terinstal:
   ```bash
   pip install pandas matplotlib seaborn
   ```
2. Jalankan file Python:
   ```bash
   python analisis_nilai.py
   ```
3. Hasil visualisasi akan muncul dalam bentuk grafik.
