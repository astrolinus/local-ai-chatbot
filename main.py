#An Streamlit based chatbot using local AI powered by Ollama

import tomllib
import streamlit as st
import requests

@st.cache_resource
def load_config() -> dict:
    with open("config.toml" , "rb") as f:
        return tomllib.load(f)

config = load_config()
ollama_config = config["ollama"]

