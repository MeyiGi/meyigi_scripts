import pytest
from unittest.mock import MagicMock, patch
from openai import OpenAI
from meyigi_scripts.ChatGPTAPI import chatgpt_get_response  # Replace 'your_module' with the actual module name

@pytest.fixture
def mock_openai():
    """Fixture to mock OpenAI client"""
    with patch("meyigi_scripts.ChatGPTAPI.OpenAI") as mock_openai_class:
        mock_client = MagicMock()
        mock_completion = MagicMock()
        mock_completion.choices = [MagicMock(message=MagicMock(content="Mocked Response"))]

        mock_client.chat.completions.create.return_value = mock_completion
        mock_openai_class.return_value = mock_client

        yield mock_openai_class

def test_chatgpt_get_response(mock_openai):
    """Test if chatgpt_get_response returns the expected response"""
    response = chatgpt_get_response("Hello, AI!")
    assert response == "Mocked Response"

def test_chatgpt_get_response_empty_prompt(mock_openai):
    """Test if chatgpt_get_response handles an empty prompt"""
    response = chatgpt_get_response("")
    assert response == "Mocked Response"  # Ensure it doesn't fail with an empty string

def test_chatgpt_get_response_custom_model(mock_openai):
    """Test if chatgpt_get_response works with a different model"""
    response = chatgpt_get_response("Tell me a joke", model="gpt-3.5-turbo")
    assert response == "Mocked Response"

def test_chatgpt_get_response_custom_role(mock_openai):
    """Test if chatgpt_get_response works with a custom role"""
    response = chatgpt_get_response("Tell me a story", role="system")
    assert response == "Mocked Response"

def test_chatgpt_get_response_api_failure():
    """Test if chatgpt_get_response handles API errors gracefully"""
    with patch("meyigi_scripts.ChatGPTAPI.OpenAI") as mock_openai_class:
        mock_client = MagicMock()
        mock_client.chat.completions.create.side_effect = Exception("API error")
        mock_openai_class.return_value = mock_client

        with pytest.raises(Exception, match="API error"):
            chatgpt_get_response("This should fail")