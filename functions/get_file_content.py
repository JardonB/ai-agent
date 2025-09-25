import os
from config import *

def get_file_content(working_directory, file_path):
    file_abs_path = os.path.abspath(os.path.join(working_directory, file_path))
    working_dir_abs_path = os.path.abspath(working_directory)

    if not (file_abs_path == working_dir_abs_path or file_abs_path.startswith(working_dir_abs_path + os.sep)): 
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(file_abs_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(file_abs_path) as file:
            content = file.read()
            if len(content) > file_char_limit:
                content = f'{content[:file_char_limit]} [...File "{file_path}" truncated at 10000 characters]'
            return content
    except Exception as e:
        return f'Error: {e}'