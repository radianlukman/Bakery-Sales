# Import packages
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

# Import data
data = pd.read_csv("Bakery Sales.csv")
data
data.info()

# Menghapus baris dan kolom yang tidak diperlukan
data[data.isna().all(axis=1)]
# Ekstrak ulang data
data = data.iloc[0:2420]
# Menghapus kolom
data = data.drop(['day of week','place','total'], axis=1)

# Mengganti nilai NaN menjadi 0 
data = data.fillna(0)

# Format kolom datetime
data['datetime'] =  pd.to_datetime(data['datetime'], format='%Y-%m-%d %H:%M')
# Mengambil tanggalnya saja
data["datetime"] = data["datetime"].dt.date
data = data.rename(columns={'datetime':'date'})
# Mengubah jadi data harian
data = data.groupby('date').sum()

# Menambah kolom total
data['total'] = data.sum(axis=1)

# Produk terlaris
produk = data.sum(axis=0).sort_values()
# Drop total
produk = produk.drop('total')
# Membuat pie chart
produk.plot(kind='pie',
            fontsize=14,
            autopct=lambda p:f'{p:.2f}%',
            figsize=(15,12))
plt.title("Produk Terjual (%)",fontsize=35)
plt.show()

# Membuat bar chart
plot = produk.plot(kind='barh',figsize=(12,10),fontsize=12)
plot.set_title("Jumlah Produk Terjual", fontsize=30, y=1.01)
for i in plot.patches:
    plot.text(i.get_width()+.1, i.get_y()+.10, \
              str(round((i.get_width()))), fontsize=12, color='black')
plt.show()

# Tren penjualan
data['total'].plot(kind='line', figsize=(14,12),fontsize=12)
plt.axhline(y=data['total'].mean(), linestyle='--',color='r')
plt.title("Penjualan di Toko Roti \n Juni 2019 - Mei 2020",fontsize=25,y=1.01)
plt.xlabel("Tanggal", fontsize=12)
plt.ylabel("Jumlah Produk", fontsize=12)
plt.show()