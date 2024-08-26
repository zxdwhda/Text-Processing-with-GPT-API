import sys
import os
from file_splitter import split_file
from gpt_api_caller import process_slices_with_gpt
from result_combiner import combine_results
from config import CONFIG

def main():
    # 检查命令行参数
    if len(sys.argv) != 3:
        print("Usage: python main.py <path_to_input_file> <slice_size>")
        sys.exit(1)

    input_file_path = sys.argv[1]
    slice_size = int(sys.argv[2])

    # 第 1 步：文件切片
    print("Step 1: File Slicing...")
    output_directory = "sliced_files"
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    split_file(input_file_path, slice_size, output_directory)

    # 第 2 步：分割和 GPT API 调用
    print("\nStep 2: Segmentation and GPT API Calls...")
    api_url = CONFIG['api_url']
    prompt_word = CONFIG['prompt_word']
    processed_directory = "processed_files"
    if not os.path.exists(processed_directory):
        os.makedirs(processed_directory)

    process_slices_with_gpt(output_directory, api_url, prompt_word, processed_directory)

    # 第 3 步：结果整合
    print("\nStep 3: Integration of Results...")
    final_output_file = "final_output.txt"
    combine_results(processed_directory, final_output_file)

if __name__ == "__main__":
    main()