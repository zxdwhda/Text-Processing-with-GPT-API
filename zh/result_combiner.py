import os
import glob

def combine_results(processed_directory, final_output_file):
    """
    Reads all processed files from the processed_directory, sorts them in the original order,
    and merges them into a single file.

    Args:
        processed_directory (str): Directory containing the processed files.
        final_output_file (str): Path to the final output file.
    """
    # 获取所有已处理文件的列表，按切片索引排序（例如，slice_0.txt、slice_1.txt、...）
    processed_files = sorted(glob.glob(os.path.join(processed_directory, 'slice_*.txt')),
                             key=lambda x: int(x.split('_')[-1].split('.')[0]))

    # 打开最终输出文件以进行写入
    with open(final_output_file, 'w', encoding='utf-8') as output_file:
        # 遍历每个已处理的文件
        for processed_file_path in processed_files:
            # 读取已处理文件的内容
            with open(processed_file_path, 'r', encoding='utf-8') as processed_file:
                # 将内容写入最终输出文件
                output_file.write(processed_file.read())

if __name__ == "__main__":
    # Example usage:
    processed_directory = 'processed_files'
    final_output_file = 'final_output.txt'
    combine_results(processed_directory, final_output_file)