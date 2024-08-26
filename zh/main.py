# main.py
import sys
import os
from file_splitter import split_file
from gpt_api_caller import process_slices_with_gpt_concurrently  # Import the correct function
from result_combiner import combine_results
from config import CONFIG
import dashscope

def main():
    # Set the API key
    dashscope.api_key = CONFIG['api_key']

    # Check command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python main.py <path_to_input_file> <slice_size>")
        sys.exit(1)

    input_file_path = sys.argv[1]
    slice_size = int(sys.argv[2])

    # Step 1: File Slicing
    print("Step 1: File Slicing...")
    output_directory = "sliced_files"
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    split_file(input_file_path, slice_size, output_directory)

    # Step 2: Segmentation and GPT API Calls
    print("\nStep 2: Segmentation and GPT API Calls...")
    prompt_word = CONFIG['prompt_word']
    processed_directory = "processed_files"
    if not os.path.exists(processed_directory):
        os.makedirs(processed_directory)

    process_slices_with_gpt_concurrently(output_directory, prompt_word, processed_directory)  # Use the correct function

    # Step 3: Integration of Results
    print("\nStep 3: Integration of Results...")
    final_output_file = "final_output.txt"

    # Read the original filenames in order
    original_filenames = [filename for filename in os.listdir(output_directory) if filename.endswith(".txt")]

    # Combine the results in the original order
    with open(final_output_file, "w", encoding="utf-8") as final_output:
        for filename in original_filenames:
         with open(os.path.join(processed_directory, filename), "r", encoding="utf-8") as processed_file:
            final_output.write(processed_file.read())

if __name__ == "__main__":
    main()