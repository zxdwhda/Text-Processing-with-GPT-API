import os

def split_file(input_file_path, slice_size, output_directory):
    """
    Splits a large text file into smaller files by a specified number of lines.

    Args:
        input_file_path (str): Path to the original text file.
        slice_size (int): Number of lines per slice.
        output_directory (str): Directory where the sliced files will be saved.
    """
    # Ensure the output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

   # 打开输入文件
    with open(input_file_path, 'r', encoding='utf-8') as file:
        # 初始化变量
        slice_index = 0
        lines = []

        # 遍历文件中的每一行
        for line in file:
            # 将当前行添加到行列列表中
            lines.append(line)

            # 如果达到切片大小，则将切片保存到文件中
            if len(lines) == slice_size:
                # 将切片写入新文件
                output_file_path = os.path.join(output_directory, f'slice_{slice_index}.txt')
                with open(output_file_path, 'w', encoding='utf-8') as output_file:
                    output_file.writelines(lines)

                # 重置行列表并递增切分索引
                lines = []
                slice_index += 1

        # 将剩余的行保存到文件中
        if lines:
            output_file_path = os.path.join(output_directory, f'slice_{slice_index}.txt')
            with open(output_file_path, 'w', encoding='utf-8') as output_file:
                output_file.writelines(lines)

if __name__ == "__main__":
    # 示例用法：
    input_file_path = 'path/to/input.txt'
    slice_size = 1000  # 每个片段的行数
    output_directory = 'sliced_files'
    split_file(input_file_path, slice_size, output_directory)