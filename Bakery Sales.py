# Import packages
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

# Importing data
data = pd.read_csv("Bakery Sales.csv")
data
data.info()

# Deleting Unnecessary Rows and Columns
data[data.isna().all(axis=1)]
# Re-extract the data
data = data.iloc[0:2420]
# Drop columns
data = data.drop(['day of week','place','total'], axis=1)

# Replace NaN Values with 0 
data = data.fillna(0)

# Formatting datetime column
data['datetime'] =  pd.to_datetime(data['datetime'], format='%Y-%m-%d %H:%M')
# Only the date 
data["datetime"] = data["datetime"].dt.date
data = data.rename(columns={'datetime':'date'})
# Change it into daily data
data = data.groupby('date').sum()

# Add a total column 
data['total'] = data.sum(axis=1)

# Best-Selling Product
product = data.sum(axis=0).sort_values()
# Drop total
product = product.drop('total')
# Make pie chart
product.plot(kind='pie',fontsize=14,autopct=lambda p:f'{p:.2f}%',
               figsize=(15,12))
plt.title("Sales by Product (%)",fontsize=35)
plt.show()

# Make bar chart
plot = product.plot(kind='barh',figsize=(12,10),fontsize=12)
plot.set_title("Sales by Product", fontsize=30, y=1.01)
for i in plot.patches:
    plot.text(i.get_width()+.1, i.get_y()+.10, \
            str(round((i.get_width()))), fontsize=12, color='black')
plt.show()

# Sales trend
data['total'].plot(kind='line', figsize=(14,12),fontsize=12)
plt.axhline(y=data['total'].mean(), linestyle='--',color='r')
plt.title("Bakery Sales Trend \n June 2019 - May 2020",fontsize=25,y=1.01)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Number of Product", fontsize=12)
plt.show()