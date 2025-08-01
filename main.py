import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys

load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def main():
    #userinput=sys.argv("enter your input")
    #userinput=input("enter your promt:")
    if len(sys.argv) == 1:
        print("No argument/user prompt given")
        sys.exit(1)
    elif "--verbose" in sys.argv: 
        verbose=True
        user_prompt = sys.argv[1]
    else:
        verbose=False
        user_prompt = sys.argv[1]
    #try :
    #   user_prompt = sys.argv[1]
    #except:
    #    user_prompt = input("enter your promt:")
    #user_prompt = sys.argv[1]

    messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    response = client.models.generate_content(
        model='gemini-2.0-flash', 
        contents=sys.argv[1]
        )
    #print(response)
    print(f"Response: {response.text}")#, response.prompt_token_count)
    if verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
