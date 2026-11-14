# AI Agent

Small Python examples that send prompts to an OpenAI-compatible chat completions API.

## Requirements

- Python 3.9 or later
- An API key and a model name from OpenAI or another compatible provider

## Setup


1. Clone the repository and enter its folder:

   ```sh
   git clone https://github.com/Pradeep21oct/ai-agent.git
   cd ai-agent
   ```

2. Create and activate a virtual environment:

   **Windows (PowerShell):**

   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   **macOS/Linux:**

   ```sh
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install the dependencies:

   ```sh
   python -m pip install --upgrade pip
   python -m pip install openai python-dotenv
   ```

4. Create a `.env` file in the project folder:

   ```dotenv
   API_KEY=your_api_key
   MODEL=your_model_name
   BASE_URL=https://api.openai.com/v1
   ```

   Use the API key and model name provided by your API provider. `BASE_URL` is
   optional for OpenAI and should be changed to your provider's API endpoint
   when using another OpenAI-compatible service. Keep your real API key private;
   `.env` is ignored by Git and should not be committed.

## Run

From the project folder, with the virtual environment activated:

```sh
python assistant.py
```

This sends a single greeting prompt. To start the interactive chat example:

```sh
python hello_ai.py
```

Type `exit` or `quit` to end the interactive example.

## Troubleshooting

- If authentication fails, check that `API_KEY` is valid and belongs to the
  selected provider.
- If the model cannot be found, set `MODEL` to a model available to your API
  account.
- If using a compatible provider, set `BASE_URL` to its documented API endpoint.
- If Python cannot find a dependency, confirm the virtual environment is
  activated and reinstall the packages from the setup steps.
