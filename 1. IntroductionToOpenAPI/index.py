from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
# print(OPENROUTER_API_KEY)

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url=os.getenv("OPENROUTER_URL")
)

response = client.responses.create(
    model="openai/gpt-4o-mini",
    input=[
        {
            "role": "user",
            "content": "Write a poem on Father"
        }
    ]
)


print(response.output_text)