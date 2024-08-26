# config.py

# Configuration settings for the project

# API URL for the GPT service
API_URL = 'https://your-gpt-api-url.example.com'

# Prompt word to attach to each API request
PROMPT_WORD = 'YourPromptWord'

# Default slice size for splitting the input file
SLICE_SIZE = 1000  # Adjust this value according to your needs

# Other configurable options can be added here as needed

# Example of how to use these settings in your application
if __name__ == "__main__":
    print(f"API URL: {API_URL}")
    print(f"Prompt Word: {PROMPT_WORD}")
    print(f"Slice Size: {SLICE_SIZE}")