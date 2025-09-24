import sys
import os
from google import genai
from google.genai import types # type: ignore
from dotenv import load_dotenv # type: ignore

#variables
model = 'gemini-2.0-flash-001'

def main():
    #show_troubleshooting_msgs()

    args = sys.argv[1:]
    if not args:
        print("No prompt provided!")
        sys.exit(1)
    if len(args[0].strip()) < 1: 
        print("Prompt is empty!")
        sys.exit(1)
    
    user_prompt = args[0]


    #load environment variables from .env file
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key == None:
        print("No api key provided!")
        sys.exit(1)

    #create instance
    client = genai.Client(api_key=api_key)

    #parameters for generate_content
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    generate_content(client, messages)

def generate_content(client, messages):
    #assign generate_content to an object
    response = client.models.generate_content(model=model, contents=messages)

    #print the text attribute of the response object
    print(response.text)
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}\nResponse tokens: {response.usage_metadata.candidates_token_count}")

def show_troubleshooting_msgs():
    #troubleshooting stuff to help me think:
    print(f"sys.argv[1]: \"{sys.argv[1]}\"")
    print(f"len(user_prompt): {len(sys.argv[1])}")
    print(f"len(user_prompt.strip()): {len(sys.argv[1].strip())}")

if __name__ == "__main__":
    main()