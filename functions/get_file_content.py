import os
from config import *
from google import genai # type: ignore
from google.genai import types # type: ignore

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
    
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads the content of a file within the working directory, with a max size of 10000 characters. After 10000 characters the file is truncated.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The relative path of the file to be read",
            ),
        },
    ),
)