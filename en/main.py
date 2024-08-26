import sys
import os
from file_splitter import split_file
from gpt_api_caller import process_slices_with_gpt
from result_combiner import combine_results
from config import CONFIG

def main():
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
    api_url = CONFIG['api_url']
    prompt_word = CONFIG['prompt_word']
    processed_directory = "processed_files"
    if not os.path.exists(processed_directory):
        os.makedirs(processed_directory)

    process_slices_with_gpt(output_directory, api_url, prompt_word, processed_directory)

    # Step 3: Integration of Results
    print("\nStep 3: Integration of Results...")
    final_output_file = "final_output.txt"
    combine_results(processed_directory, final_output_file)

if __name__ == "__main__":
    main()