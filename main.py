import tomllib
import streamlit as st
import requests

def load_config() -> dict:
    with open("config.toml" , "rb") as f:
        return tomllib.load(f)

config = load_config()
ollama_config = config["ollama"]

url = ollama_config["host"]

prompt = input("Enter your prompt: \n")

payload = {
    "model": ollama_config["model"],
    "messages":[
        {"role":"user", "content":prompt}
    ],
    "stream": False
}

try:

    response = requests.post(url , json=payload ,timeout=60)
    if response.status_code == 200:

        data = response.json()
        print(data["message"]["content"])
    else:
        print("Unexpected error:" , response.status_code)

except Exception as e:
    print("Error", e)
