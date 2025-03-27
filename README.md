# 🖥️ **meyigi_scripts** 🎉

Welcome to **meyigi_scripts**! This repository contains a collection of useful and versatile Python scripts designed to help you automate tasks, simplify workflows, and make your life easier. Whether you're a beginner or an experienced developer, you'll find something useful here!

[![PyPI version](https://badge.fury.io/py/meyigi-scripts.svg)](https://pypi.org/project/meyigi-scripts/)

---

## 🚀 **Features**
- **Useful Scripts**: A variety of small, helpful scripts for automating common tasks.
- **Easy to Use**: Plug-and-play functionality for simple integration into your projects.
- **Well-documented**: Clear instructions and examples to get you started quickly.

---

## 💻 **Installation**

You can easily install **meyigi_scripts** via PyPI! Run the following command:

```bash
pip install meyigi-scripts
```

---

## 🔑 **Important: API Key Setup**

If you're using scripts that interact with OpenAI's ChatGPT, you **must** set your API key before running them. Otherwise, the `get_response_function` will not work.

Set your API key using the following command:

```bash
export OPENAI_API_KEY="your_api_key_here"
```

Make sure to replace `your_api_key_here` with your actual OpenAI API key.

---

Now you're ready to start using `meyigi_scripts`! 🚀

---

# Gemini Generate Function Documentation

This script provides a function `generate()` that interacts with Google Gemini AI to generate text, JSON, or HTML responses based on user prompts. It supports customization of the model's behavior using various parameters such as `temperature`, `top_p`, and `max_output_tokens`.

```sh
pip install google-generativeai
```

## Environment Variables
Set your Gemini API key before running the script:

```sh
export GEMINI_API_KEY="your_api_key_here"
```

## Usage

### Function Signature
```python
def generate(
    promt: str = "ask from user promt",
    GEMINI_API_KEY: str = None,
    return_type: Literal["text", "json", "html"] = "text",
    model: str = "gemini-2.0-flash",
    top_k: float = 40,
    max_output_tokens: int = 8192,
    temperature: float = 1,
    top_p: float = 0.95,
) -> Union[str, dict]:
```

### Parameters
- `promt` *(str)*: The input prompt for the AI model.
- `GEMINI_API_KEY` *(str, optional)*: API key for authentication. If not provided, it attempts to retrieve from environment variables.
- `return_type` *(Literal["text", "json", "html"])*: Specifies the format of the response.
- `model` *(str)*: The model variant to use. Default is `gemini-2.0-flash`.
- `top_k` *(float)*: Sampling parameter controlling token selection.
- `max_output_tokens` *(int)*: Maximum number of output tokens.
- `temperature` *(float)*: Controls randomness in output.
- `top_p` *(float)*: Nucleus sampling parameter.

### Example Usage
```python
from script import generate

response = generate(
    "Give me the capital and population of France in json format.",
    return_type="json"
)
print(response)
```

### Error Handling
- Raises `ValueError` if the API key is missing.
- Raises `ValueError` if the `return_type` is not one of ["text", "json", "html"].
- Raises `ValueError` if JSON decoding fails.

### Execution as a Script
Run the script directly:
```sh
python script.py
```
This will execute the function with a predefined test prompt.

## License
This script is provided under the MIT License.

---
For more details, refer to the official [Google Gemini AI documentation](https://developers.generativeai.google/).

