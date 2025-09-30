import os
import openpyxl
from typing import Union, List

# Function to append data to Excel
def append_to_excel(data: Union[dict, List[dict]], filename: str = "output.xlsx") -> None:
    """Appends dictionary or list of dictionaries to an Excel file.

    Args:
        data (Union[dict, List[dict]]): collectios of data for adding to filename
        filename (str, optional): generating filename Defaults to "output.xlsx".

    Raises:
        TypeError: Raised if 'data' is neither a dictionary nor a list of dictionaries.

    Returns:
        None: functions is not returning anything but saves data in filename
        
    Examples:
        res = {"Name": "Daniel", "Age" : 20}
        append_to_excel(res, "data/output.excel")

        res = [{"Name": "Daniel", "Age" : 20}, {"Name": "Daniel", "Age" : 20}]
        append_to_excel(res, "data/output.excel")
    """

    # Проверяем корректность входных данных
    if not isinstance(data, (dict, list)) or (isinstance(data, list) and not all(isinstance(item, dict) for item in data)):
        raise TypeError("Argument 'data' must be a dictionary or a list of dictionaries.")

    # Приводим `data` к списку для единообразной обработки
    data_list = [data] if isinstance(data, dict) else data  

    # Если файл не существует, создаем новый
    if not os.path.exists(filename):
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        headers = list(data_list[0].keys())  # Берем ключи из первого словаря
        sheet.append(headers)
    else:
        workbook = openpyxl.load_workbook(filename)
        sheet = workbook.active
        headers = [cell.value for cell in sheet[1] if cell.value]  # Читаем заголовки

    # Добавляем строки с данными
    for item in data_list:
        row = [item.get(col, "") for col in headers]
        sheet.append(row)

    workbook.save(filename)

def read_csv_as_dicts(filename: str, delimiter: str = ",") -> List[dict]:
    """Reads a CSV file and returns its contents as a list of dictionaries.

    Args:
        filename (str): Path to the CSV file.
        delimiter (str, optional): Delimiter used in the CSV file. Defaults to ",".

    Raises:
        FileNotFoundError: Raised if the specified file does not exist.
        ValueError: Raised if the CSV file is empty.

    Returns:
        List[dict]: List of dictionaries representing rows in the CSV file.
        
    Examples:
        data = read_csv_as_dicts("data/input.csv")
    """
    if not os.path.exists(filename):
        raise FileNotFoundError(f"The file {filename} does not exist.")

    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    if not lines:
        raise ValueError("The CSV file is empty.")

    headers = lines[0].strip().split(delimiter)
    data = []

    for line in lines[1:]:
        values = line.strip().split(delimiter)
        row_dict = {headers[i]: values[i] if i < len(values) else "" for i in range(len(headers))}
        data.append(row_dict)

    return data