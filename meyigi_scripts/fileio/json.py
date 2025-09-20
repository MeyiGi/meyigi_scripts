import json
import os
from typing import List, Union

def append_to_json(data: Union[dict, List[dict]], filename: str = "output.json") -> None:
    """Appends dictionary or list of dictionaries to an Json file.

    Args:
        data (Union[dict, List[dict]]): collectios of data for adding to filename
        filename (str, optional): generating filename Defaults to "output.xlsx".

    Raises:
        TypeError: Raised if 'data' is neither a dictionary nor a list of dictionaries.

    Returns:
        None: functions is not returning anything but saves data in filename
        
    Examples:
        res = {"Name": "Daniel", "Age" : 20}
        append_to_json(res, "data/output.json")

        res = [{"Name": "Daniel", "Age" : 20}, {"Name": "Daniel", "Age" : 20}]
        append_to_json(res, "data/output.json")
    """
    if not isinstance(data, (dict, list)) or (isinstance(data, list) and not all(isinstance(item, dict) for item in data)):
        raise TypeError("Argument 'data' must be a dictionary or a list of dictionaries.")

    # Приводим `data` к списку для единообразной обработки
    data_list = [data] if isinstance(data, dict) else data  
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as file:
            try:
                existing_data = json.load(file)
                if not isinstance(existing_data, list):
                    existing_data = [existing_data]
            except json.JSONDecodeError:
                existing_data = []
    else:
        existing_data = []

    for data in data_list:
        existing_data.append(data)

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(existing_data, file, ensure_ascii=False, indent=4)