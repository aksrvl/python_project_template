def output_text_console(text):
    """
    Function for printing text to the console.
    Parameters:
    - text: the text to be printed.
    """
    print(text)

def write_to_file_builtin(filename, content):
    """
    Function for writing text to a file using Python's built-in capabilities.
    Parameters:
    - filename: path to the file.
    - content: the text to be written to the file.
    """
    with open(filename, 'w') as file:
        file.write(content)