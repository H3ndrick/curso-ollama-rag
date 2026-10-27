import os
from dotenv import load_dotenv
from ollama import Client

load_dotenv()

def cliente_chat():
    cliente = Client(
        host="https://ollama.com",
        headers={
            "Authorization": f"Bearer {os.environ['OLLAMA_API_KEY']}"
        }
    )
    
    modelo = "gpt-oss:20b-cloud"
    
    return cliente, modelo