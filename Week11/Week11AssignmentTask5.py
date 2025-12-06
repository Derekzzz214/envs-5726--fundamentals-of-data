# Task5
import pyodbc
import sys
import matplotlib.pyplot as plt

# 从命令行读取用户输入的列名（如 sector）
group_column = sys.argv[1]

# 拼接 SQL 查询语句，根据输入的列名进行 GROUP BY 汇总平均值
query = f'SELECT {group_column}, AVG(mean_ghg_1990_to_2020) AS avg_ghg FROM epa_ghg GROUP BY {group_column}'

# 自定义函数：连接数据库并执行 SQL 查询
def execute_cursor(sql_query):
    conn = pyodbc.connect(
        "Driver={PostgreSQL Unicode(x64)};"
        "Server=localhost;"
        "Port=5432;"
        "Database=week_11_database;"
        "Uid=postgres;"
        "Pwd=020214Zhangzy;"
    )
    cursor = conn.cursor()
    cursor.execute(sql_query)
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results

# 调用函数执行查询
data = execute_cursor(query)

# 将查询结果拆分为两个列表（横坐标标签和纵坐标数值）
x_labels = [row[0] for row in data]
y_values = [row[1] for row in data]

# 用 matplotlib 画图
plt.figure(figsize=(10, 6))
plt.bar(x_labels, y_values)
plt.xlabel(group_column)
plt.ylabel("mean_ghg_1990_to_2020")
plt.title(f"mean_ghg_1990_to_2020 by {group_column}")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
