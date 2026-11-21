# 🤖 Local AI Chatbot

A locally-run AI chatbot powered by **Ollama**. All inference happens on your machine — no data leaves your computer. Simply enter a prompt and get a response from a local LLM.

> [!CAUTION]
> This project is in **early development (alpha)**. Features are minimal, the API surface may change, and bugs are expected. Use at your own risk.

## How It Works

1. The app reads model and host settings from [`config.toml`](config.toml).
2. You enter a prompt in the terminal.
3. The prompt is sent to the [Ollama](https://ollama.com) chat API running locally.
4. The model's response is printed back to the terminal.

## Prerequisites

- **Python 3.11+**
- **Ollama** — must be installed and running before you start the chatbot.

### Installing Ollama

1. Download and install Ollama from [https://ollama.com/download](https://ollama.com/download).
2. Pull the default model:
   ```bash
   ollama pull llama3.2:latest
   ```
3. Verify Ollama is running (it starts automatically after installation):
   ```bash
   ollama list
   ```

## Getting Started

1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd Local-AI-chatbot
   ```

2. **Install dependencies**
   ```bash
   pip install -e .
   ```

3. **Run the chatbot**
   ```bash
   python main.py
   ```
4. **Enter a prompt** when asked, and the model's reply will be printed to the console.

## Configuration

Edit [`config.toml`](config.toml) to change the model or Ollama host:

```toml
[ollama]
model = "llama3.2:latest"
host = "http://localhost:11434/api/chat"
```

You can use any model available through Ollama (e.g. `llama3.1:8b`, `mistral`, `gemma2`, `phi3`). Pull it first with `ollama pull <model>`.

## Project Structure

```
├── main.py            # Entry point — takes a prompt and prints the model's response
├── config.toml        # Ollama model & host configuration
├── pyproject.toml     # Project metadata & Python dependencies
├── .gitignore         # Git ignore rules
└── README.md          # This file
```

## Roadmap

- [ ] Streamlit-based chat UI
- [ ] Conversation history & multi-turn chat
- [ ] Streaming responses
- [ ] Multiple model selection via UI

## License

This project is open source and available under the [MIT License](LICENSE).
