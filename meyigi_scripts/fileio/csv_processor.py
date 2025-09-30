import os
import csv
from typing import List, Union

def append_to_csv(data: Union[dict, List[dict]], filename: str = "output.csv", delimiter: str = ",") -> None:
    """Appends dictionary or list of dictionaries to a CSV file.

    Args:
        data (Union[dict, List[dict]]): collections of data for adding to filename
        filename (str, optional): generating filename. Defaults to "output.csv".
        delimiter (str, optional): Delimiter used in the CSV file. Defaults to ",".

    Raises:
        TypeError: Raised if 'data' is neither a dictionary nor a list of dictionaries.

    Returns:
        None: function does not return anything but saves data in filename
        
    Examples:
        res = {"Name": "Daniel", "Age" : 20}
        append_to_csv(res, "data/output.csv")

        res = [{"Name": "Daniel", "Age" : 20}, {"Name": "Daniel", "Age" : 20}]
        append_to_csv(res, "data/output.csv")
    """
    # Проверяем корректность входных данных
    if not isinstance(data, (dict, list)) or (isinstance(data, list) and not all(isinstance(item, dict) for item in data)):
        raise TypeError("Argument 'data' must be a dictionary or a list of dictionaries.")

    # Приводим `data` к списку для единообразной обработки
    data_list = [data] if isinstance(data, dict) else data  

    # Проверяем, существует ли файл и нужно ли добавлять заголовки
    file_exists = os.path.isfile(filename)
    
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data_list[0].keys(), delimiter=delimiter)

        # Если файл не существует или пустой, пишем заголовки
        if not file_exists or os.path.getsize(filename) == 0:
            writer.writeheader()

        # Записываем данные
        for item in data_list:
            writer.writerow(item)

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