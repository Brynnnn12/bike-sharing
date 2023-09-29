import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Mengimpor dataset bike sharing
df = pd.read_csv('day.csv')

# Membuat plot batang untuk penggunaan sepeda berdasarkan waktu dalam sehari
plt.figure(figsize=(12, 6))
sns.countplot(data=df, x='dteday')
plt.title('Penggunaan Sepeda berdasarkan Waktu dalam Sehari', fontsize=16)
plt.xlabel('Waktu dalam Sehari', fontsize=12)
plt.ylabel('Jumlah Peminjaman Sepeda', fontsize=12)
st.pyplot()

# Membuat plot batang untuk penggunaan sepeda berdasarkan hari dalam seminggu
plt.figure(figsize=(12, 6))
sns.countplot(data=df, x='weekday')
plt.title('Penggunaan Sepeda berdasarkan Hari dalam Seminggu', fontsize=16)
plt.xlabel('Hari dalam Seminggu', fontsize=12)
plt.ylabel('Jumlah Peminjaman Sepeda', fontsize=12)
st.pyplot()
# Membuat plot batang untuk menampilkan stasiun bike sharing yang populer
top_stations = df['cnt'].value_counts().head(10)
plt.figure(figsize=(12, 6))
sns.barplot(x=top_stations.index, y=top_stations.values)
plt.title('Stasiun Bike Sharing yang Populer', fontsize=16)
plt.xlabel('Stasiun', fontsize=12)
plt.ylabel('Jumlah Peminjaman Sepeda', fontsize=12)
plt.xticks(rotation=90)
st.pyplot()
