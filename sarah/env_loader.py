# env_loader.py
# Use a global variable to ensure the .env file is loaded only once
import os
from dotenv import load_dotenv

ENV_LOADED = False

def load_env():
    global ENV_LOADED
    if not ENV_LOADED:
        dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
        load_dotenv(dotenv_path)
        ENV_LOADED = True
        print(f"Loaded .env from {dotenv_path}")

def get_env_variable(var_name):
    load_env()
    value = os.getenv(var_name)
    if not value:
        print(f"Environment variable {var_name} not set.")
    return value

