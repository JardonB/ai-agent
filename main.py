import sys
import os
from google import genai
from google.genai import types # type: ignore
from dotenv import load_dotenv # type: ignore

#variables
model = 'gemini-2.0-flash-001'

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

    if verbose: print(f"User prompt: {user_prompt}") #print verbose message

    generate_content(client, messages, verbose)

def generate_content(client, messages, verbose):
    #show_troubleshooting_msgs() #shows user input info for troubleshooting

    #assign generate_content to an object
    response = client.models.generate_content(model=model, contents=messages)

    if verbose: #print verbose messages
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    #print the text attribute of the response object
    print(f"Response: {response.text}")


def show_troubleshooting_msgs():
    #troubleshooting stuff to help me think:
    print(f"User inputs: {sys.argv[1:]}")
    print(f"User prompt: \"{sys.argv[1]}\"")
    print(f"len(user_prompt): {len(sys.argv[1])}")
    print(f"len(user_prompt.strip()): {len(sys.argv[1].strip())}")


if __name__ == "__main__":
    main()