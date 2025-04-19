import pandas as pd

def input_text_console():
    """
    Function for reading text input from the console.
    Returns the text entered by the user.
    """
    return input("Enter text: ")

def read_file_builtin(filename):
    """
    Function for reading the content of a file using Python's built-in capabilities.
    Parameters:
    - filename: path to the file.
    Returns the content of the file as a string.
    """
    with open(filename, 'r') as file:
        return file.read()

def read_file_pandas(filename):
    """
    Function for reading the content of a file using the pandas library.
    Parameters:
    - filename: path to the file.
    Returns a DataFrame containing the data from the file.
    """
    return pd.read_csv(filename)