from bs4 import BeautifulSoup

soup = BeautifulSoup("<html><h1>Hello!</h1></html>", "html.parser")
print("Successfully imported BeautifulSoup4")

import matplotlib.pyplot as plt
import openpyxl

plt.plot([1, 2, 3], [4, 5, 6])
plt.title("Matplotlib Test")
plt.show()

print("✅ Both matplotlib and openpyxl imported successfully!")

