import time
import subprocess

def ollama_serve():
    print("\n [*] Starting ollama server...")

    with open("log.txt" , "a") as log:
        subprocess.Popen(
            ["ollama" , "serve"],
            stderr=subprocess.DEVNULL,
            stdout=log,
            stdin=subprocess.DEVNULL,
            start_new_session=True)

    print("\n [*] Ollama server running.\n")
        

# Print the introduction message for the chatbot application.
def introduction():
    print("""This is a simple command-line interface (CLI) application that interacts with the Ollama API.
    It allows users to input a prompt, sends it to the specified model, and retrieves the generated response. 
    ----------------------------
    [*] Commands:

    /bye = Exit the application
    /help = Show this help message""")
