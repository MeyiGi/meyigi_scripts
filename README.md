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

# ChatGPT Response Fetcher Documentation

This script provides a function `chatgpt_get_response()` to interact with OpenAI's GPT models and fetch responses.

## 🔑 Important: API Key Setup

If you're using scripts that interact with OpenAI's ChatGPT, you **must** set your API key before running them. Otherwise, the `chatgpt_get_response` function will not work.

Set your API key using the following command:

```sh
export OPENAI_API_KEY="your_api_key_here"
```

Make sure to replace `your_api_key_here` with your actual OpenAI API key.

## Usage

### Function Signature
```python
def chatgpt_get_response(promt, model="gpt-4o", role="user") -> str:
```

### Parameters
- `promt` *(str)*: The user input prompt for the AI model.
- `model` *(str, optional)*: The model version to use. Default is `gpt-4o`.
- `role` *(str, optional)*: The role of the message sender (e.g., "user", "system"). Default is `user`.

### Example Usage
```python
from script import chatgpt_get_response

response = chatgpt_get_response("Tell me a joke.")
print(response)
```

### Error Handling
- Ensure that your OpenAI API key is set up in your environment.
- If an invalid model name is provided, OpenAI may return an error.

### Execution as a Script
This function is meant to be used as an importable module but can be integrated into a standalone application.

For more details, refer to the official [OpenAI API Documentation](https://platform.openai.com/docs/).

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

For more details, refer to the official [Google Gemini AI documentation](https://developers.generativeai.google/).

---

# Web Scraping Utility Documentation

This script provides a function `get_requests()` for making HTTP GET requests and parsing HTML responses using BeautifulSoup. It includes error handling for various request failures.

### Function Signature
```python
def get_requests(url: str, timeout: int = 10, headers: dict = None) -> BeautifulSoup:
```

### Parameters
- `url` *(str)*: The target URL for the GET request.
- `timeout` *(int, optional)*: Timeout in seconds for the request. Default is 10 seconds.
- `headers` *(dict, optional)*: Optional headers for the request.

### Example Usage
```python
from script import get_requests

url = "https://example.com"
soup = get_requests(url)
print(soup.prettify())
```

## 🔑 Important: Network Access
Ensure you have a stable internet connection before running the script. If network issues occur, the script will raise an appropriate error.

### Error Handling
- Raises `HTTPError` if the request fails due to an HTTP issue.
- Raises `ReadTimeout` if the request exceeds the timeout.
- Raises `ConnectionError` for network issues.
- Raises `RequestException` for general request failures.

### Execution as a Script
This function is intended to be used as an importable module but can be integrated into a standalone script.

## License
This script is provided under the MIT License.

For more details, refer to the official [Requests Documentation](https://docs.python-requests.org/) and [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/).


