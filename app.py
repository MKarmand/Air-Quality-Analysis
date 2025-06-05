import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from streamlit_folium import st_folium
import folium

# Load cleaned dataset
data_df = pd.read_csv("cleaned_data.csv", parse_dates=['date'], index_col='date')

# Sidebar filter
st.sidebar.header("📅 Filter Rentang Tanggal")
start_date = st.sidebar.date_input("Mulai", data_df.index.min().date())
end_date = st.sidebar.date_input("Selesai", data_df.index.max().date())
filtered_df = data_df.loc[start_date:end_date]

st.title("📊 Dashboard Analisis Kualitas Udara Changping")

# 1. Korelasi
st.subheader("🔗 Korelasi Antar Variabel")
fig, ax = plt.subplots(figsize=(12, 6))
numeric_cols = filtered_df.select_dtypes(include='number')
sns.heatmap(numeric_cols.corr(), annot=True, cmap='coolwarm', fmt='.2f', ax=ax)
st.pyplot(fig)


# 3. Tren Suhu Bulanan
st.subheader("🌡️ Tren Suhu Bulanan")
fig, ax = plt.subplots(figsize=(12, 5))
filtered_df['TEMP'].resample('M').mean().plot(marker='o', linestyle='-', color='red', ax=ax)
ax.set_title("Tren Suhu Bulanan")
ax.set_ylabel("Suhu Rata-rata (°C)")
ax.grid(True)
st.pyplot(fig)

# 4. Tren PM2.5 Bulanan
st.subheader("💨 Tren PM2.5 Bulanan")
fig, ax = plt.subplots(figsize=(12, 5))
filtered_df['PM2.5'].resample('M').mean().plot(marker='o', linestyle='-', color='blue', ax=ax)
ax.set_title("Tren PM2.5 Bulanan")
ax.set_ylabel("PM2.5 Rata-rata")
ax.grid(True)
st.pyplot(fig)

# 5. Distribusi Kategori PM2.5
def group_pm25(value):
    if value <= 12:
        return 'Baik'
    elif value <= 35.4:
        return 'Sedang'
    elif value <= 55.4:
        return 'Tidak Sehat untuk Sensitif'
    elif value <= 150.4:
        return 'Tidak Sehat'
    else:
        return 'Sangat Tidak Sehat'

filtered_df['PM2_5_Category'] = filtered_df['PM2.5'].apply(group_pm25)
pm25_counts = filtered_df['PM2_5_Category'].value_counts().sort_index()

st.subheader("📉 Distribusi Kategori PM2.5")
fig, ax = plt.subplots(figsize=(8, 5))
pm25_counts.plot(kind='bar', color='skyblue', ax=ax)
ax.set_title("Distribusi Kategori PM2.5")
ax.set_xlabel("Kategori")
ax.set_ylabel("Jumlah Data")
ax.grid(axis='y', linestyle='--', alpha=0.7)
st.pyplot(fig)

# 6. Distribusi PM10 Binned
bins = [0, 50, 100, 200, filtered_df['PM10'].max()]
labels = ['Low', 'Moderate', 'High', 'Very High']
filtered_df['PM10_Bin'] = pd.cut(filtered_df['PM10'], bins=bins, labels=labels, include_lowest=True)

st.subheader("📊 Distribusi Kategori PM10")
fig, ax = plt.subplots(figsize=(8, 5))
filtered_df['PM10_Bin'].value_counts().sort_index().plot(kind='bar', color='skyblue', ax=ax)
ax.set_title("Distribusi Kategori PM10")
ax.set_xlabel("Kategori")
ax.set_ylabel("Jumlah Data")
ax.grid(axis='y', linestyle='--', alpha=0.7)
st.pyplot(fig)

# 7. Kuartil PM2.5
filtered_df['PM2_5_Quantile'] = pd.qcut(filtered_df['PM2.5'], q=4, labels=['Q1', 'Q2', 'Q3', 'Q4'])

st.subheader("🔢 Distribusi Kuartil PM2.5")
fig, ax = plt.subplots(figsize=(8, 5))
filtered_df['PM2_5_Quantile'].value_counts().sort_index().plot(kind='bar', color='skyblue', ax=ax)
ax.set_title("Distribusi Kuartil PM2.5")
ax.set_xlabel("Kategori")
ax.set_ylabel("Jumlah Data")
ax.grid(axis='y', linestyle='--', alpha=0.7)
st.pyplot(fig)

# 8. Peta Folium (lokasi tetap: Changping)
st.subheader("🗺️ Peta PM2.5 di Changping")
m = folium.Map(location=[40.2181, 116.2312], zoom_start=11)
avg_pm25 = filtered_df['PM2.5'].mean()

folium.CircleMarker(
    location=[40.2181, 116.2312],
    radius=20,
    popup=f"Rata-rata PM2.5: {avg_pm25:.2f}",
    color='crimson',
    fill=True,
    fill_opacity=0.6
).add_to(m)

st_folium(m, width=800, height=500)

# Footer
st.markdown("""
---
📌 Dashboard ini dibuat berdasarkan eksplorasi dan visualisasi data PM2.5, PM10, suhu, dan variabel meteorologis lainnya di wilayah Changping.
""")
