from typing import Literal, Union

def load_txt(filename: str, return_type: Literal["string", "list"] = "string") -> Union[str, list[str]]:
    """Function to load data from txt file

    Args:
        filename (str): filepath to load data to variable
        return_type (Literal[&quot;string&quot;, &quot;list&quot;], optional): what kind of data type we are expecting. Defaults to "string".

    Returns:
        Union[str, list[str]]: loaded data eather str or list of str
    ```
    items = load_txt("streets", "list") # ["lenin", "wall-street", ...]
    ```
    """
    with open(filename, "r", encoding="utf-8") as file:
        match return_type:
            case "string":
                return file.read()
            case "list":
                return file.readlines()