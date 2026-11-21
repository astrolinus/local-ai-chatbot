import tomllib
import streamlit as st
import requests
import chatbotFunctions as cbf

#Load and parse the TOML configuration file.
def load_config() -> dict:
    with open("config.toml" , "rb") as f:
        return tomllib.load(f)

# Load configuration at startup and Ollama url
config = load_config()
ollama_config = config["ollama"]
url = ollama_config["host"]


# Send the user's prompt to the Ollama chat API and print the response.
def ollama_request(prompt):
    
    try:
        response = requests.post(url , json=payload ,timeout=60)
        if response.status_code == 200:
            # Parse and display the model's reply
            data = response.json()
            print(data["message"]["content"])
        else:
            print("Unexpected error:" , response.status_code)

    except Exception as e:
        print("Error", e)

# Display welcome message and available commands
cbf.introduction()

# Main loop — continuously accept user input until '/bye' is entered
while True:

    prompt = input("Enter your prompt: \n")

    if prompt == "/bye":
        break

    elif prompt == "/help":
        # Re-display the help / introduction message
        cbf.introduction()
        
    else:
        # Build the request payload for the Ollama chat API
        payload = {
            "model": ollama_config["model"],
            "messages":[
                {"role":"user", "content":prompt}
            ],
            "stream": False  # Disable streaming to receive the full response at once
        }
        ollama_request(prompt)
