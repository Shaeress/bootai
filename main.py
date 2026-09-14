import os
import argparse
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

if api_key == None:
	raise RuntimeError("No OpenRouter api_key set in .env")

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

client = OpenAI(
	base_url="https://openrouter.ai/api/v1",
	api_key=api_key,
)

messages = [
		{
			"role": "user",
			"content": args.user_prompt
		}
	]

response = client.chat.completions.create(
	model="openrouter/free",
	messages=messages
)

if response.usage == None:
	raise RuntimeError("Request to model failed")

if(args.verbose):
	print(f"User prompt: {args.user_prompt}")
	print(f"Prompt tokens: {response.usage.prompt_tokens}")
	print(f"Response tokens: {response.usage.completion_tokens}")

print("Response:")
print(response.choices[0].message.content)