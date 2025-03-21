import os
import openpyxl
from typing import Dict, Any

# Function to append data to Excel
def append_to_excel(data: Dict[str, Any], filename: str = "output.xlsx") -> None:
    if not isinstance(data, dict):  # Проверяем, что data - это словарь
        raise TypeError("Argument 'data' must be a dictionary.")

    if not os.path.exists(filename):
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        headers = list(data.keys())  # Заголовки - это ключи словаря
        sheet.append(headers)
    else:
        workbook = openpyxl.load_workbook(filename)
        sheet = workbook.active
        headers = [cell.value for cell in sheet[1]]  # Получаем заголовки из первой строки

    # Заполняем строку значениями
    row = [data.get(col, "") for col in headers]
    sheet.append(row)

    workbook.save(filename)
