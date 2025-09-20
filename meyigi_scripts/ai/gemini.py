import os
import json
from google import genai
from google.genai import types
from typing import Literal, Union

def generate(promt: str = "ask from user promt", GEMINI_API_KEY: str = None,
             return_type: Literal["text", "json", "html"] = "text", model: str = "gemini-2.0-flash",
             top_k: float = 40, max_output_tokens: int = 8192, temperature: float = 1, top_p: float=0.95,) -> Union[str, dict]:
    """
    Generates text-based content using Google's Gemini API.
    
    Parameters:
    - promt (str): The user input prompt for text generation.
    - GEMINI_API_KEY (str, optional): API key for authentication. If not provided, fetched from environment variables.
    - return_type (Literal["text", "json", "html"]): Format of the returned response. Default is "text".
    - model (str): The Gemini model to use. Default is "gemini-2.0-flash".
    - top_k (float): Number of top probable words considered during generation. Default is 40.
    - max_output_tokens (int): Maximum number of tokens in the output. Default is 8192.
    - temperature (float): Controls randomness in generation (higher means more randomness). Default is 1.
    - top_p (float): Probability threshold for nucleus sampling. Default is 0.95.
    
    Returns:
    - str: Generated text if return_type is "text" or "html".
    - dict: Parsed JSON response if return_type is "json".
    
    Raises:
    - ValueError: If `return_type` is not one of ["text", "json", "html"].
    - ValueError: If JSON parsing fails when `return_type` is "json".
    - ValueError: If API key is missing.
    
    Example:
    ```python
    response = generate("What is the capital of Germany?", return_type="text")
    print(response)  # Output: "The capital of Germany is Berlin."
    
    response_json = generate("Give me the capital and population of France in json format.", return_type="json")
    print(response_json)  # Output: {"capital": "Paris", "population": 67000000}
    ```
    """
    
    match return_type:
        case "text":
            response_mime_type = "text/plain"
        case "json":
            response_mime_type = "application/json"
        case "html":
            response_mime_type = "text/html"
        case _:
            raise ValueError("return type not from ['text', 'json', 'html']")

    if not GEMINI_API_KEY:
        GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
        if not GEMINI_API_KEY:
            raise ValueError('"Don\'t forget paste in cmd: export GEMINI_API_KEY="your api key"')
        
    client = genai.Client(
        api_key=GEMINI_API_KEY,
    )

    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=promt),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        temperature=temperature,
        top_p=top_p,
        top_k=top_k,
        max_output_tokens=max_output_tokens,
        response_mime_type=response_mime_type,
    )

    res = []
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        res.append(chunk.text)
        # print(type(chunk.text))

    text = "".join(res)
    if return_type == "json":
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON format, please look at return text:\n {text}")

    return text

if __name__ == "__main__":
    print(generate("Give me the capital and population of France in json format.", return_type="json"))