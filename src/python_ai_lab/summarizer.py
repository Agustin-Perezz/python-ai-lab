"""AI file summarizer: point at a file, then ask questions about it.

Usage:
    uv run src/python_ai_lab/summarizer.py <path-to-file>

Example:
    uv run src/python_ai_lab/summarizer.py notes.txt
"""

import json
import os
import pathlib
import sys

from dotenv import load_dotenv
from openai import OpenAI
from pypdf import PdfReader

load_dotenv()
client = OpenAI()

if len(sys.argv) < 2:
    print("Usage: python summarizer.py <file_path>", file=sys.stderr)
    sys.exit(1)

path_str = sys.argv[1]
if os.path.exists(path_str):
    file_extension = pathlib.Path(path_str).suffix.lower()

    if not file_extension in (".pdf", ".txt", ".md"):
        print("Unsupported file format.")
        sys.exit(1)

    if file_extension == ".pdf":
        reader = PdfReader(path_str)
        document_text = "\n".join(page.extract_text() for page in reader.pages)
    else:
        with open(path_str, "r") as file:
            document_text = file.read()

    if not document_text.strip():
        print("The file is empty")
        sys.exit(1)
else:
    print("The file doesn't exist")
    sys.exit(1)


messages = [
    {
        "role": "developer",
        "content": f"--- DOCUMENT START ---\n{document_text}\n--- DOCUMENT END ---",
    }
]

try:
    while True:
        user_input = input("Question: ")

        if user_input.strip().lower() in ("exit", "quit"):
            break

        messages.append({"role": "user", "content": user_input})

        response = client.responses.create(
            model="gpt-6-astra",
            instructions="Answer only from the text between the document markers. If the answer is not there, say so.",
            input=messages,
        )

        print(response.output_text)
        messages.append({"role": "assistant", "content": response.output_text})
except (KeyboardInterrupt, EOFError):
    print("Goodbye 👋")
finally:
    with open("qa_log.json", "w") as file:
        json.dump(messages, file, indent=4)
