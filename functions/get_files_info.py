import os

def get_files_info(working_directory, directory="."):
    full_path = os.path.abspath(os.path.join(working_directory, directory))
    working_dir_path = os.path.abspath(working_directory)

    if not (full_path == working_dir_path or full_path.startswith(working_dir_path + os.sep)): 
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(full_path): 
        return f'Error: "{directory}" is not a directory'
    
    try:
        entries = os.listdir(full_path)
        lines = []
        for entry in entries:
            entry_path = os.path.join(full_path, entry)
            is_dir = os.path.isdir(entry_path)
            entry_size = os.path.getsize(entry_path)
            lines.append(f"- {entry}: file_size={entry_size} bytes, is_dir={is_dir}")
        return "\n".join(lines)
    except Exception as e:
        return f"Error: {e}"