from dotenv import load_dotenv
from openai import OpenAI
from system_prompt import SYSTEM_PROMT
import sys
import os

load_dotenv()

try:
    client = OpenAI(
        api_key=os.getenv("OPENROUTER_API_KEY"),
        base_url=os.getenv("OPENROUTER_URL")
    )
except Exception as e:
    print (f"Error creating OpenAI client: {e}")
    sys.exit (1)

# Made a muti-conversation TaskBuddy, having a predefined sytem role
def main():
    input_messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMT
        }
    ]

    print("-" * 50)
    print("TaskBuddy: Hey There! What's on your mind?")
    print("Dump your tasks here, and I'll organize them for you!")
    print("-" * 50)

    while True:
        try:
            user_input = input("\nYou: ").strip() # strip() removes spaces from start & end of a string
            if user_input.lower() in ["exit", "quit"]:
                print("\nTaskBuddy: Goodbye!")
                break

            if not user_input:
                continue

            input_messages.append({"role": "user", "content": user_input})

            response = client.responses.create(
                model="openai/gpt-4o-mini",
                input=input_messages,
            )

            reply = response.output_text

            print(f"\nTaskBuddy: {reply}")

            input_messages.append({"role": "assistant", "content": reply})

        except KeyboardInterrupt: # KeyboardInterrupt This happens when you press: Ctrl + C
            print("\nTaskBuddy: Goodbye!")
            break
        except Exception as e:
            print(f"\nAn error occurred: {e}")
            break



if __name__ == "__main__":
    main()