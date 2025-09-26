import os
from google import genai # type: ignore
from google.genai import types # type: ignore

def write_file(working_directory, file_path, content):
    file_abs_path = os.path.abspath(os.path.join(working_directory, file_path))
    working_dir_abs_path = os.path.abspath(working_directory)
    parent_dir = os.path.dirname(file_abs_path)

    if not file_abs_path.startswith(working_dir_abs_path + os.sep): 
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    try:
        os.makedirs(parent_dir, exist_ok=True)
        with open(file_abs_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: {e}'
    
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes or overwrites the file at the specified path, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The relative path of the file to be written to, must be within the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content that will be written to the file"
            )
        },
    ),
)