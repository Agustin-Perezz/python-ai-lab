# python-ai-lab

This repository has two small tools that use the OpenAI API. You need Python 3.12 or newer and [uv](https://docs.astral.sh/uv/).

- `chatbot.py` is a chat in your terminal. You type a message, and the tool answers.
- `summarizer.py` answers questions about a file. The tool reads `.txt`, `.md`, and `.pdf` files.

## Setup

1. Clone this repository.
2. Run `uv sync`. This command installs the dependencies.
3. Create a file with the name `.env` in the project root.
4. Add this line to the file, with your own key:

   ```
   OPENAI_API_KEY=your-key-here
   ```

The file `.gitignore` contains `.env`. Your key does not go into git.

## Use the chatbot

Run this command:

```
uv run src/python_ai_lab/chatbot.py
```

Type a message, then press Enter. The tool answers. Type `exit` or `quit` to stop the tool.

## Use the summarizer

Run this command with the path to your file:

```
uv run src/python_ai_lab/summarizer.py path/to/file.pdf
```

Type a question about the file, then press Enter. The tool answers only with data from the file. If the answer is not in the file, the tool says so.

## Project structure

- `src/python_ai_lab/chatbot.py` — the source code of the chatbot
- `src/python_ai_lab/summarizer.py` — the source code of the summarizer
- `src/python_ai_lab/fundamentals.py` — notes with Python basics