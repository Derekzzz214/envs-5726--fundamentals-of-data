# Task1
import openpyxl
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

file_path = r"C:\Users\张周延\Downloads\Pipe_Material_Training_Data.xlsx"
workbook = openpyxl.load_workbook(file_path)
sheet = workbook.active
pipe_materials_table = [row for row in sheet.iter_rows(min_row=2, values_only=True)]

# 函数定义
def plot_cdf_curve_fit(table, material_type, line_color):
    material_data = [row for row in table if row[0] == material_type]
    xdata = np.array([row[1] for row in material_data])
    ydata = np.array([row[2] for row in material_data])

    def cumulative_density_function(age, c, b, a):
        return 1 - c * np.exp(-(age / b) ** a)
    coefficients, bounds = curve_fit(cumulative_density_function, xdata, ydata)
    c, b, a = coefficients
    print(f'Curve fitted CDF for {material_type}: Survival Probability = {c}* e^ (-(age/{b})^{a})')

    x_fit = np.linspace(min(xdata), max(xdata), 100)
    y_fit = cumulative_density_function(x_fit, c, b, a)
    plt.plot(x_fit, y_fit, color=line_color, label=material_type)
    return (float(c), float(b), float(a))

cast = plot_cdf_curve_fit(table=pipe_materials_table, material_type='Cast Iron', line_color='red')
ductile = plot_cdf_curve_fit(table=pipe_materials_table, material_type='Ductile Iron', line_color='blue')
galvanized = plot_cdf_curve_fit(table=pipe_materials_table, material_type='Galvanized Iron', line_color='green')
copper = plot_cdf_curve_fit(table=pipe_materials_table, material_type='Copper', line_color='brown')

plt.legend()
plt.xlabel('Life Expectancy (y)')
plt.ylabel('Survival Probability (%)')
plt.title('Pipe Material Survival CDF')
plt.show()

print(f"Cast Iron: {cast}")
print(f"Ductile Iron: {ductile}")
print(f"Galvanized Iron: {galvanized}")
print(f"Copper: {copper}")

# Task2
import csv
from datetime import datetime
from collections import namedtuple

# 定义 namedtuple 数据结构
WaterMain = namedtuple(
    'WaterMain',
    ['MainType', 'Diameter', 'InstallDate', 'Material', 'Age', 'Survival_Probability']
)

# 定义 Weibull 生存概率函数
def weibull_survival_probability(age, c, b, a):
    prob = (1 - c * np.exp(-(age / b) ** a)) * 100
    if prob > 100:
        prob = 100
    return prob

coefficients_dict = {
    'Cast Iron': cast,
    'Ductile Iron': ductile,
    'Galvanized Iron': galvanized,
    'Copper': copper
}

file_path = r"C:\Users\张周延\Downloads\Water_Mains.csv"
water_mains_table = []

with open(file_path, newline='', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)
    current_year = 2025

    for row in reader:
        install_date = datetime.strptime(row['InstallDate'], "%m/%d/%Y %H:%M")
        age = current_year - install_date.year
        c, b, a = coefficients_dict[row['Material']]
        survival_prob = weibull_survival_probability(age, c, b, a)

        new_row = WaterMain(
            MainType=row['MainType'],
            Diameter=row['Diameter'],
            InstallDate=install_date,
            Material=row['Material'],
            Age=age,
            Survival_Probability=survival_prob
        )

        water_mains_table.append(new_row)

for row in water_mains_table[:5]:
    print(row)





