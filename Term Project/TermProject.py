import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_path = r"C:\Users\张周延\PycharmProjects\envs-5726--fundamentals-of-data\Term Project\who_ambient_air_quality_database_version_2024_(v6.1)_China.xlsx"
df = pd.read_excel(file_path)

# Keep only three columns and remove NA.
df_clean = df[['pm25_concentration', 'pm10_concentration', 'no2_concentration']].dropna()

# Extract the variable column as a list.
pm25 = df_clean['pm25_concentration'].tolist()
pm10 = df_clean['pm10_concentration'].tolist()
no2  = df_clean['no2_concentration'].tolist()

def create_scatter_subplot(axes, x, y, title, xlabel, ylabel, color):
    axes.scatter(x, y, alpha=0.7)
    slope, intercept = np.polyfit(x, y, deg=1)
    regression_line = [slope * xi + intercept for xi in x]
    axes.plot(x, regression_line, color=color, label='Regression Line')
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel)
    axes.set_title(title)
    axes.legend()

# Create a 1x2 subplot layout
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(12, 5))

# PM2.5 vs PM10
create_scatter_subplot(
    axes=axs[0],
    x=pm10,
    y=pm25,
    title='PM2.5 vs PM10 (China)',
    xlabel='PM10 Concentration (μg/m³)',
    ylabel='PM2.5 Concentration (μg/m³)',
    color='red'
)

# PM2.5 vs NO2
create_scatter_subplot(
    axes=axs[1],
    x=no2,
    y=pm25,
    title='PM2.5 vs NO₂ (China)',
    xlabel='NO₂ Concentration (μg/m³)',
    ylabel='PM2.5 Concentration (μg/m³)',
    color='blue'
)

plt.tight_layout()
plt.savefig("China_PM25_Correlations_Subplots.png", dpi=300)
plt.show()

