import os
import json
from google import genai
from google.genai import types
from typing import Literal, Union

def generate(promt: str = "ask from user promt", GEMINI_API_KEY: str = None,
             return_type: Literal["text", "json", "html"] = "text", model: str = "gemini-2.0-flash",
             top_k: float = 40, max_output_tokens: int = 8192, temperature: float = 1, top_p: float=0.95,) -> Union[str, dict]:
    
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