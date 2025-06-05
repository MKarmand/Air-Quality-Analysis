import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from streamlit_folium import st_folium
import folium

# Load cleaned dataset
data_df = pd.read_csv("cleaned_data.csv", parse_dates=['date'], index_col='date')

# Sidebar filter
st.sidebar.header("📅 Date Range Filter")
start_date = st.sidebar.date_input("Start", data_df.index.min().date())
end_date = st.sidebar.date_input("End", data_df.index.max().date())
filtered_df = data_df.loc[start_date:end_date]

st.title("📊 Changping Air Quality Analysis Dashboard")

# 1. Correlation
st.subheader("🔗 Correlation Between Variables")
fig, ax = plt.subplots(figsize=(12, 6))
numeric_cols = filtered_df.select_dtypes(include='number')
sns.heatmap(numeric_cols.corr(), annot=True, cmap='coolwarm', fmt='.2f', ax=ax)
st.pyplot(fig)

# 2. Monthly Temperature Trend
st.subheader("🌡️ Monthly Temperature Trend")
fig, ax = plt.subplots(figsize=(12, 5))
filtered_df['TEMP'].resample('M').mean().plot(marker='o', linestyle='-', color='red', ax=ax)
ax.set_title("Monthly Average Temperature Trend")
ax.set_ylabel("Average Temperature (°C)")
ax.grid(True)
st.pyplot(fig)

# 3. Monthly PM2.5 Trend
st.subheader("💨 Monthly PM2.5 Trend")
fig, ax = plt.subplots(figsize=(12, 5))
filtered_df['PM2.5'].resample('M').mean().plot(marker='o', linestyle='-', color='blue', ax=ax)
ax.set_title("Monthly Average PM2.5 Trend")
ax.set_ylabel("Average PM2.5")
ax.grid(True)
st.pyplot(fig)

# 4. PM2.5 Category Distribution
def group_pm25(value):
    if value <= 12:
        return 'Good'
    elif value <= 35.4:
        return 'Moderate'
    elif value <= 55.4:
        return 'Unhealthy for Sensitive'
    elif value <= 150.4:
        return 'Unhealthy'
    else:
        return 'Very Unhealthy'

filtered_df['PM2_5_Category'] = filtered_df['PM2.5'].apply(group_pm25)
pm25_counts = filtered_df['PM2_5_Category'].value_counts().sort_index()

st.subheader("📉 PM2.5 Category Distribution")
fig, ax = plt.subplots(figsize=(8, 5))
pm25_counts.plot(kind='bar', color='skyblue', ax=ax)
ax.set_title("PM2.5 Category Distribution")
ax.set_xlabel("Category")
ax.set_ylabel("Data Count")
ax.grid(axis='y', linestyle='--', alpha=0.7)
st.pyplot(fig)

# 5. PM10 Distribution (Binned)
bins = [0, 50, 100, 200, filtered_df['PM10'].max()]
labels = ['Low', 'Moderate', 'High', 'Very High']
filtered_df['PM10_Bin'] = pd.cut(filtered_df['PM10'], bins=bins, labels=labels, include_lowest=True)

st.subheader("📊 PM10 Category Distribution")
fig, ax = plt.subplots(figsize=(8, 5))
filtered_df['PM10_Bin'].value_counts().sort_index().plot(kind='bar', color='skyblue', ax=ax)
ax.set_title("PM10 Category Distribution")
ax.set_xlabel("Category")
ax.set_ylabel("Data Count")
ax.grid(axis='y', linestyle='--', alpha=0.7)
st.pyplot(fig)

# 6. PM2.5 Quartile Distribution
filtered_df['PM2_5_Quartile'] = pd.qcut(filtered_df['PM2.5'], q=4, labels=['Q1', 'Q2', 'Q3', 'Q4'])

st.subheader("🔢 PM2.5 Quartile Distribution")
fig, ax = plt.subplots(figsize=(8, 5))
filtered_df['PM2_5_Quartile'].value_counts().sort_index().plot(kind='bar', color='skyblue', ax=ax)
ax.set_title("PM2.5 Quartile Distribution")
ax.set_xlabel("Quartile")
ax.set_ylabel("Data Count")
ax.grid(axis='y', linestyle='--', alpha=0.7)
st.pyplot(fig)

# 7. Folium Map (fixed location: Changping)
st.subheader("🗺️ PM2.5 Map in Changping")
m = folium.Map(location=[40.2181, 116.2312], zoom_start=11)
avg_pm25 = filtered_df['PM2.5'].mean()

folium.CircleMarker(
    location=[40.2181, 116.2312],
    radius=20,
    popup=f"Average PM2.5: {avg_pm25:.2f}",
    color='crimson',
    fill=True,
    fill_opacity=0.6
).add_to(m)

st_folium(m, width=800, height=500)

# Footer
st.markdown("""
---
📌 This dashboard presents the results of data exploration and visualization for PM2.5, PM10, temperature, and other meteorological variables in the Changping area.
""")
