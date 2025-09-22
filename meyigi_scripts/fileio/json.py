import json
import os
from typing import List, Union, Dict

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


def read_json_file(filename: str) -> List[Dict]:
    """
    Reads a JSON file and returns a list of dictionaries.
    
    Args:
        filename (str): Path to the JSON file.
    
    Returns:
        List[Dict]: List of dictionaries read from the JSON file.
    """
    if not os.path.exists(filename):
        raise FileNotFoundError(f"File '{filename}' does not exist.")
    
    with open(filename, "r", encoding="utf-8") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            raise ValueError(f"File '{filename}' contains invalid JSON.")
    
    # Ensure the output is always a list of dictionaries
    if isinstance(data, dict):
        return [data]
    elif isinstance(data, list) and all(isinstance(item, dict) for item in data):
        return data
    else:
        raise ValueError(f"File '{filename}' must contain a dict or a list of dicts.")

def read_json_folder(folder: str) -> List[Dict]:
    """
    Reads all JSON files in a folder and combines them into a single list of dictionaries.
    
    Args:
        folder (str): Path to the folder containing JSON files.
    
    Returns:
        List[Dict]: Combined list of dictionaries from all JSON files.
    """
    if not os.path.isdir(folder):
        raise NotADirectoryError(f"'{folder}' is not a valid directory.")
    
    combined_data: List[Dict] = []
    
    for filename in os.listdir(folder):
        if filename.endswith(".json"):
            file_path = os.path.join(folder, filename)
            combined_data.extend(read_json_file(file_path))
    
    return combined_data