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

    # Open the input file
    with open(input_file_path, 'r', encoding='utf-8') as file:
        # Initialize variables
        slice_index = 0
        lines = []

        # Iterate over each line in the file
        for line in file:
            # Append the current line to the lines list
            lines.append(line)

            # If the slice size is reached, save the slice to a file
            if len(lines) == slice_size:
                # Write the slice to a new file
                output_file_path = os.path.join(output_directory, f'slice_{slice_index}.txt')
                with open(output_file_path, 'w', encoding='utf-8') as output_file:
                    output_file.writelines(lines)

                # Reset the lines list and increment the slice index
                lines = []
                slice_index += 1

        # Save any remaining lines to a file
        if lines:
            output_file_path = os.path.join(output_directory, f'slice_{slice_index}.txt')
            with open(output_file_path, 'w', encoding='utf-8') as output_file:
                output_file.writelines(lines)

if __name__ == "__main__":
    # Example usage:
    input_file_path = 'path/to/input.txt'
    slice_size = 1000  # Number of lines per slice
    output_directory = 'sliced_files'
    split_file(input_file_path, slice_size, output_directory)