import os
import subprocess
import sys
from config import *

def run_python_file(working_directory, file_path, args=[]):
    file_abs_path = os.path.abspath(os.path.join(working_directory, file_path))
    working_dir_abs_path = os.path.abspath(working_directory)

    if not file_abs_path.startswith(working_dir_abs_path + os.sep):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(file_abs_path):
        return f'Error: File "{file_path}" not found.'
    if not file_abs_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        run_args = [sys.executable, file_path, *args]
        completed_process = subprocess.run(run_args, cwd=working_dir_abs_path, capture_output=True, timeout=run_timeout)
        stdout, stderr = completed_process.stdout.decode('utf-8'), completed_process.stderr.decode('utf-8')
        string_to_return = f'STDOUT: {stdout}\nSTDERR: {stderr}'
        if completed_process.returncode != 0:
            string_to_return += f'\nProcess exited with code {completed_process.returncode}'
        if not stdout and not stderr:
            return "No output produced."
        return string_to_return
    except Exception as e:
        return f'Error: executing Python file: {e}'