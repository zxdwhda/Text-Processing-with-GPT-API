# gpt_api_caller.py
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from dashscope import Generation
from config import CONFIG

def build_request(slice_content, prompt_word):
    """
    Builds the request payload for the GPT API using the DashScope SDK.
    """
    messages = [
        {"role": "system", "content": prompt_word},
        {"role": "user", "content": slice_content}
    ]
    return messages

def call_gpt_api(slice_content, prompt_word):
    """
    Calls the GPT API using the DashScope SDK and returns the response.
    """
    request_payload = build_request(slice_content, prompt_word)

    response = Generation.call(
        model="qwen-max",
        messages=request_payload,
        temperature=0.5,
        result_format='message'
    )

    try:
        generated_text = response.output.choices[0].message.content.strip()
        return generated_text
    except AttributeError:
        raise Exception("Invalid response from the API.")

def process_slices_with_gpt_concurrently(input_directory, prompt_word, output_directory):
    """
    Processes each file slice with the GPT API concurrently and saves the results.
    """
    futures = []
    result_dict = {}  # Dictionary to store the results with filenames

    with ThreadPoolExecutor(max_workers=5) as executor:
        for filename in os.listdir(input_directory):
            if filename.endswith(".txt"):
                with open(os.path.join(input_directory, filename), "r", encoding="utf-8") as file:
                    slice_content = file.read()
                future = executor.submit(call_gpt_api, slice_content, prompt_word)
                futures.append((future, filename))  # Tuple containing the Future and filename

        # Process the results as they become available
        for future, filename in futures:
            try:
                generated_text = future.result()

                # Save the generated text to the dictionary with the filename as the key
                result_dict[filename] = generated_text
            except Exception as e:
                print(f"Error processing file {filename}: {e}")

    # Write the results to files in the output directory
    for filename, generated_text in result_dict.items():
        with open(os.path.join(output_directory, filename), "w", encoding="utf-8") as output_file:
            output_file.write(generated_text)
            
# Example usage:
# process_slices_with_gpt_concurrently("sliced_files", CONFIG['prompt_word'], "processed_files")