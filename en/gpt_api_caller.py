import os
import json
import requests
from config import CONFIG

def build_request(slice_content, prompt_word):
    """
    Builds the request payload for the GPT API.

    Args:
        slice_content (str): The content of the slice to be processed.
        prompt_word (str): The prompt word to attach to the request.

    Returns:
        dict: The request payload.
    """
    # Build the request payload
    request_payload = {
        "model": "text-davinci-002",  # Use the appropriate model ID
        "prompt": f"{prompt_word} {slice_content}",
        "max_tokens": 1024,  # Adjust max tokens as needed
        "temperature": 0.5,  # Adjust temperature as needed
    }
    return request_payload


def call_gpt_api(api_url, request_payload, api_key):
    """
    Sends a request to the GPT API and receives the response.

    Args:
        api_url (str): The URL of the GPT API.
        request_payload (dict): The request payload.
        api_key (str): The API key for authentication.

    Returns:
        dict: The API response.
    """
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    # Send the POST request
    response = requests.post(api_url, headers=headers, json=request_payload)

    # Check the response status code
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to get a response from the GPT API: {response.text}")


def process_slices_with_gpt(input_directory, api_url, prompt_word, output_directory):
    """
    Processes each slice using the GPT API with a specific cue word attached.

    Args:
        input_directory (str): Directory containing the input slices.
        api_url (str): The URL of the GPT API.
        prompt_word (str): The prompt word to attach to the request.
        output_directory (str): Directory to save the processed slices.
    """
    # Ensure the output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Iterate over each slice file
    for slice_file_name in os.listdir(input_directory):
        if slice_file_name.endswith('.txt'):
            # Read the slice content
            slice_file_path = os.path.join(input_directory, slice_file_name)
            with open(slice_file_path, 'r', encoding='utf-8') as slice_file:
                slice_content = slice_file.read()

            # Build the request payload
            request_payload = build_request(slice_content, prompt_word)

            # Call the GPT API
            try:
                api_response = call_gpt_api(api_url, request_payload, CONFIG['api_key'])
                # Extract the generated text from the response
                generated_text = api_response['choices'][0]['text'].strip()
            except Exception as e:
                print(f"Error processing file {slice_file_name}: {e}")
                continue

            # Write the processed slice to a new file
            output_file_path = os.path.join(output_directory, slice_file_name)
            with open(output_file_path, 'w', encoding='utf-8') as output_file:
                output_file.write(generated_text)


if __name__ == "__main__":
    # Example usage:
    input_directory = 'sliced_files'
    api_url = CONFIG['api_url']
    prompt_word = CONFIG['prompt_word']
    output_directory = 'processed_files'
    process_slices_with_gpt(input_directory, api_url, prompt_word, output_directory)