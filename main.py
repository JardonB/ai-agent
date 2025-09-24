#load environment variables from .env file
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

#import genai and create instance
from google import genai

client = genai.Client(api_key=api_key)

#parameters for generate_content
model = 'gemini-2.0-flash-001'
contents = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."

#assign generate_content to a response object
response = client.models.generate_content(model=model, contents=contents)

#print the text attribute of the response object
print(response.text)
print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}\nResponse tokens: {response.usage_metadata.candidates_token_count}")