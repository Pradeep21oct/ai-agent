# AI Agent Development

This project contains a collection of simple Python examples for building AI assistant applications using an OpenAI-compatible API and a local LLM runtime such as Ollama.

The goal is to help you learn how to:

- connect Python to a local AI model
- send chat requests to the model
- create a basic interactive assistant
- add a role-based personality to the assistant
- extend the assistant with tools and small functions

## Prerequisites

Before you begin, make sure you have:

- Python 3.9 or later
- Visual Studio Code
- Ollama installed on your machine
- An LLM model downloaded in Ollama

A typical model to use is:

- `qwen3:4b`
- or `qwen3:1.7b`

## Install the required tools

### 1. Install Python

Download and install Python from:

https://www.python.org/downloads/

Verify the installation:

```bash
python --version
```

or on some systems:

```bash
python3 --version
```

### 2. Install Visual Studio Code

Download from:

https://code.visualstudio.com/download

### 3. Install Ollama

Download and install Ollama from:

https://ollama.com/download

### 4. Download a model

Open a terminal and run:

```bash
ollama pull qwen3:4b
```

You can also pull the smaller model:

```bash
ollama pull qwen3:1.7b
```

To verify Ollama is working:

```bash
ollama run qwen3:4b
```

## Project setup

### 1. Create the project folder

Create a folder named `AI-Agent` or use the existing repository folder.

### 2. Open the folder in VS Code

Open the project in Visual Studio Code.

### 3. Create a virtual environment

Open the terminal in VS Code and run:

```bash
python -m venv .venv
```

Activate the environment:

Windows (PowerShell):

```powershell
.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

### 4. Install Python dependencies

```bash
pip install openai python-dotenv
```

## Configure the model connection

Create a file named `.env` in the project root with the following contents:

```env
BASE_URL=http://localhost:11434/v1
API_KEY=ollama
MODEL=qwen3:4b
```

This configuration tells the Python code to talk to the local Ollama server using the OpenAI-compatible API format.

## Run the examples

### Simple hello example

```bash
python hello_ai.py
```

This script sends a single greeting prompt to the model and prints the response.

### Basic interactive assistant

```bash
python basic/assistant.py
```

This version lets you chat with the model in a loop until you type `exit` or `quit`.

### Role-based assistant

```bash
python prompt/assistant.py
```

This example lets the user select a personality or role, such as teacher, Python expert, travel guide, motivational coach, or interviewer.

### Tool-enabled assistant

```bash
python tool/assistant.py
```

This version uses the helper functions in the `tool` folder to respond to requests such as:

- roll a dice
- generate a password
- tell the current time or date

## Repository structure

```text
ai-agent/
├── .env
├── hello_ai.py
├── basic/
│   └── assistant.py
├── prompt/
│   └── assistant.py
├── tool/
│   ├── assistant.py
│   ├── tool_maneger.py
│   ├── tools.py
│   ├── test_tools.py
│   └── test_tool_maneger.py
├── installation.docx
└── README.md
```

## Notes

- The code uses the OpenAI Python client because Ollama exposes an OpenAI-compatible endpoint.
- The same approach can later be adapted to other providers that support the same API style.
- Keep your local environment configuration inside `.env` and do not commit real secrets or personal environment values.

## Troubleshooting

- If the model does not respond, check that Ollama is running and the model was downloaded successfully.
- If the connection fails, verify the `BASE_URL` matches your local Ollama endpoint.
- If authentication fails, confirm `API_KEY` is set to `ollama` for the local setup.
- If the model name is not found, make sure it matches an installed Ollama model.
- If Python cannot import a package, activate the virtual environment and reinstall dependencies.
