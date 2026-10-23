import json

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()
messages = []

try:
    while True:
        user_input = input("Message: ")

        if user_input.strip().lower() in ("exit", "quit"):
            break

        messages.append({"role": "user", "content": user_input})

        response = client.responses.create(
            model="gpt-6-astra",
            instructions="You are a grumpy senior developer who answers in exactly two sentences",
            input=messages,
        )

        print(response.output_text)

        messages.append({"role": "assistant", "content": response.output_text})
except (KeyboardInterrupt, EOFError):
    print("Goodbye 👋")
finally:
    with open("logs", "w") as file:
        json.dump(messages, file, indent=4)
