import os
import logging

def setup_logging(log_file_path):
    """
    Sets up basic logging configuration.

    Args:
        log_file_path (str): Path to the log file.
    """
    logging.basicConfig(filename=log_file_path, level=logging.INFO,
                        format='%(asctime)s:%(levelname)s:%(message)s')

def read_file(file_path):
    """
    Reads the contents of a file.

    Args:
        file_path (str): Path to the file.

    Returns:
        str: Contents of the file.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def write_file(file_path, content):
    """
    Writes content to a file.

    Args:
        file_path (str): Path to the file.
        content (str): Content to write to the file.
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def ensure_directory_exists(directory_path):
    """
    Ensures that a directory exists; creates it if it does not.

    Args:
        directory_path (str): Path to the directory.
    """
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

# Example usage:
if __name__ == "__main__":
    # Setup logging
    log_file_path = 'application.log'
    setup_logging(log_file_path)

    # Example of reading a file
    file_content = read_file('example.txt')
    logging.info(f"File content: {file_content}")

    # Example of writing to a file
    write_file('output.txt', 'Hello, world!')

    # Example of ensuring a directory exists
    ensure_directory_exists('example_directory')