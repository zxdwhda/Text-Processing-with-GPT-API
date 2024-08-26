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
    # Get a list of all processed files, sorted by the slice index (e.g., slice_0.txt, slice_1.txt, ...)
    processed_files = sorted(glob.glob(os.path.join(processed_directory, 'slice_*.txt')),
                             key=lambda x: int(x.split('_')[-1].split('.')[0]))

    # Open the final output file for writing
    with open(final_output_file, 'w', encoding='utf-8') as output_file:
        # Iterate over each processed file
        for processed_file_path in processed_files:
            # Read the contents of the processed file
            with open(processed_file_path, 'r', encoding='utf-8') as processed_file:
                # Write the contents to the final output file
                output_file.write(processed_file.read())

if __name__ == "__main__":
    # Example usage:
    processed_directory = 'processed_files'
    final_output_file = 'final_output.txt'
    combine_results(processed_directory, final_output_file)