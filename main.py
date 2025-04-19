from app.io.input import input_text_console, read_file_builtin, read_file_pandas
from app.io.output import output_text_console, write_to_file_builtin


def main():
    text_console = input_text_console()
    output_text_console(text_console)
    file_text_builtin = read_file_builtin("data/input_file.txt")
    output_text_console(file_text_builtin)
    write_to_file_builtin("data/output_file.txt", file_text_builtin)
    file_text_pandas = read_file_pandas("data/input_file.csv")
    output_text_console(str(file_text_pandas))
    write_to_file_builtin("data/output_pandas_file.txt", str(file_text_pandas))

if __name__ == '__main__':
    main()
