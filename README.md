# 🌍 Analisis Kualitas Udara di Changping

[🌐 Buka Aplikasi Streamlit](https://air-quality-analysis-mka.streamlit.app/)  

Proyek ini merupakan eksplorasi data kualitas udara di wilayah **Changping**, dengan fokus untuk menjawab dua pertanyaan utama:

1. Bagaimana tren suhu bulanan di Changping?
2. Bagaimana tren konsentrasi PM2.5 bulanan di Changping?

---
## 📌 Kesimpulan

### Pertanyaan 1: Bagaimana tren suhu bulanan di Changping?

1. Suhu tertinggi dalam setahun mencapai sekitar 27–30°C pada puncak musim panas.  
2. Suhu terendah turun hingga sekitar -5°C hingga 0°C pada musim dingin.  
3. Perubahan suhu cukup drastis antara musim panas dan musim dingin, menunjukkan wilayah dengan perbedaan suhu musiman yang jelas.  
4. Setiap tahun menunjukkan tren yang konsisten, dengan puncak suhu terjadi di pertengahan tahun dan titik terendah di awal tahun berikutnya.

### Pertanyaan 2: Bagaimana tren PM2.5 bulanan di Changping?

1. Konsentrasi PM2.5 cenderung lebih tinggi selama musim dingin (sekitar Desember - Februari).  
2. Konsentrasi lebih rendah selama musim panas (sekitar Juni - Agustus).  
3. Hal ini menunjukkan bahwa musim dingin memiliki tingkat polusi udara lebih tinggi dibanding musim lainnya.

## 👤 Informasi Proyek

- **Nama**: Muhammad Kristover Armand  
- **Email**: mkarmand43@gmail.com  
- **ID Dicoding**: mk_armand_13  

---

## 🧰 Teknologi dan Library

- Python
- pandas, numpy (manipulasi data)
- matplotlib, seaborn (visualisasi)
- geopandas, folium (opsional, untuk data spasial)
- Jupyter Notebook
- Streamlit (jika digunakan untuk deployment)

---

## 🧹 Data Wrangling

- Menggabungkan kolom `year`, `month`, `day`, dan `hour` menjadi kolom `datetime`
- Menangani missing values:
  - Mean untuk kolom numerik (`PM2.5`, `PM10`, `TEMP`, dll)
  - Modus untuk kolom kategorikal (`wd`)
- Menyimpan data bersih ke `cleaned_data.csv`

---

## 📊 Exploratory Data Analysis (EDA)

### 🔥 Heatmap Korelasi

Visualisasi korelasi antar variabel numerik seperti suhu, tekanan, dan berbagai polutan.

### 🌡️ Tren Suhu Bulanan

Menampilkan rata-rata suhu per bulan untuk mengidentifikasi pola musiman.

### 🧪 Tren PM2.5 Bulanan

Menganalisis bagaimana kualitas udara (berdasarkan PM2.5) berubah sepanjang waktu.

---

## 📈 Visualisasi Kunci

- **Suhu Bulanan**  
  `TEMP` dirata-rata per bulan dan diplot sebagai garis waktu.

- **PM2.5 Bulanan**  
  Konsentrasi `PM2.5` dianalisis secara bulanan untuk memahami tren kualitas udara.

---

## 🔬 Analisis Tambahan (Opsional)

- **RFM Analysis** terhadap `PM2.5`
  - Recency: Selisih hari dari data terakhir
  - Frequency: Frekuensi kemunculan data harian
  - Monetary: Konsentrasi PM2.5 sebagai ukuran “biaya” terhadap kualitas udara

---

## 🚀 Link Aplikasi Streamlit

> 📌 *Jika Anda menjalankan proyek ini secara publik menggunakan Streamlit Cloud, tautkan di bawah ini:*


---

# Setup Virtual Environment
python -m venv env
source env/bin/activate  # (Mac/Linux)
env\Scripts\activate  # (Windows)


