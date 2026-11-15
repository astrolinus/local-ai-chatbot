# 🤖 Local AI Chatbot

A locally-run AI chatbot built with **Streamlit** and **Ollama**. All inference happens on your machine — no data leaves your computer.

> [!NOTE]
> This project is in its **initial phase** and is actively being developed. Features and structure may change as the project evolves.

## How It Works

The app uses [Ollama](https://ollama.com) to run a large language model (currently **Llama 3.1 8B**) entirely on your local machine, and [Streamlit](https://streamlit.io) to provide a clean chat interface in your browser.

## Prerequisites

- **Python 3.11+**
- **Ollama** — You must install Ollama before running the chatbot.

### Installing Ollama

1. Download Ollama from [https://ollama.com/download](https://ollama.com/download) and install it for your OS.
2. Pull the default model:
   ```bash
   ollama pull llama3.1:8b
   ```
3. Ensure the Ollama server is running (it starts automatically after installation).

## Getting Started

1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd Local-AI-chatbot
   ```

2. **Install Python dependencies**
   ```bash
   pip install -e .
   ```

3. **Run the chatbot**
   ```bash
   streamlit run main.py
   ```
   The app will open in your browser at `http://localhost:8501`.

## Configuration

Edit [`config.toml`](config.toml) to change the model or Ollama host:

```toml
[ollama]
model = "llama3.1:8b"
host = "http://localhost:11434"
```

You can swap in any model available through Ollama (e.g. `mistral`, `gemma2`, `phi3`). Just make sure to `ollama pull <model>` first.

## Project Structure

```
├── main.py            # Streamlit app entry point
├── config.toml        # Ollama & app configuration
├── pyproject.toml     # Project metadata & dependencies
├── .gitignore         # Git ignore rules
└── README.md          # This file
```

## Roadmap

- [ ] Chat UI with conversation history
- [ ] Streaming responses
- [ ] Multiple model support via the UI
- [ ] Conversation export/import

## License

This project is open source and available under the [MIT License](LICENSE).
