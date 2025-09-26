import sys
import os
from dotenv import load_dotenv # type: ignore

from google import genai # type: ignore
from google.genai import types # type: ignore

from config import model_name, system_prompt, working_dir
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.run_python_file import schema_run_python_file
from functions.write_file import schema_write_file
from functions.call_function import call_function

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file
    ]
)

def main():
    load_dotenv()

    verbose = "--verbose" in sys.argv
    args = sys.argv[1:]
    if not args:
        print("No prompt provided!\nUsage: uv run main.py \"prompt here\" [--verbose]")
        sys.exit(1)
    if len(args[0].strip()) < 1: 
        print("Prompt is empty!")
        sys.exit(1)
    
    user_prompt = args[0]

    #load environment variables from .env file
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    if api_key == None:
        print("No api key provided!")
        sys.exit(1)


    #parameters for generate_content
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    if verbose: print(f"User prompt: {user_prompt}") #print verbose messag

    generate_content(client, messages, verbose)

def generate_content(client, messages, verbose):
    #assign generate_content to an object
    response = client.models.generate_content(
        model=model_name,
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], 
            system_instruction=system_prompt),
    )


    if verbose: #print verbose messages
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    #response handling
    if response.function_calls:
        function_call_result = call_function(response.function_calls[0], verbose=verbose)
        
        if not getattr(function_call_result, "parts", None):
            raise RuntimeError("Function call returned no parts")
        response_part = function_call_result.parts[0]
        if not getattr(response_part, "function_response", None):
            raise RuntimeError("Missing function_response in tool content")
        payload = response_part.function_response.response
        if payload is None:
            raise RuntimeError("Missing response payload")
        
        if verbose:
            print(f"-> {payload}")



if __name__ == "__main__":
    main()