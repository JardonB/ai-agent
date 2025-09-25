import os

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