import fitz
import requests
import json
from utils.config import SYSTEM_PROMPT, OLLAMA_HOST, OLLAMA_PORT, MODEL_NAME


def parse_pdf(filename: str) -> str:
    doc = fitz.open(filename)
    text = ""
    for page in doc:
        text += page.get_text()
    return text


def generate_course(parsed_text: str):
    # Calls OLLAMA to generate the course
    url = f"http://{OLLAMA_HOST}:{OLLAMA_PORT}/api/generate"
    headers = { "Content-Type": "application/json" }
    data = {
        "model": MODEL_NAME,
        #"system": SYSTEM_PROMPT,
        "prompt": SYSTEM_PROMPT + "\n" + parsed_text,
        "format": "json",
        "stream": False
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        response_text = response.text
        data = json.loads(response_text)
        actual_response = json.loads(data["response"])
        return actual_response
    else:
        raise Exception("Failed to generate course")