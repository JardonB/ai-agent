from google import genai # type: ignore
from google.genai import types # type: ignore

from config import working_dir
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.run_python_file import run_python_file
from functions.write_file import write_file

def call_function(function_call_part, verbose=False):
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")

    try:
        func_name, func_args = function_call_part.name, dict(function_call_part.args)
        func_args["working_directory"] = working_dir
        func_dict = {
            "get_files_info": get_files_info,
            "get_file_content": get_file_content,
            "run_python_file": run_python_file,
            "write_file": write_file
        }

        if func_name in func_dict: 
            func_response = func_dict[func_name](**func_args)
        else:
            return types.Content(
                role="tool",
                parts=[
                    types.Part.from_function_response(
                        name=func_name,
                        response={"error": f"Unknown function: {func_name}"},
                    )
                ],
            )
        
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=func_name,
                    response={"result": func_response},
                )
            ],
        )
    except Exception as e:
        func_name = function_call_part.name
        return types.Content(
                role="tool",
                parts=[
                    types.Part.from_function_response(
                        name=func_name,
                        response={"error": f'Error: {e}'},
                    )
                ],
            )