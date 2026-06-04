import os

ASSISTANT_NAME = "jarvis"

# Load environment variables from .env file if it exists
def load_env():
    # .env is in the project root, one level up from the engine/ directory
    env_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")
    if os.path.exists(env_path):
        with open(env_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, val = line.split("=", 1)
                    os.environ[key.strip()] = val.strip()

load_env()
LLM_KEY = os.environ.get("GEMINI_API_KEY", "")