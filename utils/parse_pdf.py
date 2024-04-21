import fitz
import requests
import json
import time
from utils.config import SYSTEM_PROMPT, OLLAMA_HOST, OLLAMA_PORT, MODEL_NAME, DEMO


def parse_pdf(filename: str) -> str:
    doc = fitz.open(filename)
    text = ""
    for page in doc:
        text += page.get_text()
    return text


def generate_course(filename: str):
    # Calls OLLAMA to generate the course
    parsed_text = parse_pdf("media/" + filename)

    # If demo mode is active, return the sample course to avoid waiting for course generation
    if (DEMO):
        with open('sample_course.json', 'r') as f:
           # wait for 1.5 seconds
            time.sleep(1.5)
            data = json.load(f)
            return data

    url = f"http://{OLLAMA_HOST}:{OLLAMA_PORT}/api/generate"
    headers = {"Content-Type": "application/json"}

    data = {
        "model": MODEL_NAME,
        # "system": SYSTEM_PROMPT,
        "prompt": SYSTEM_PROMPT + parsed_text,
        "format": "json",
        "stream": False
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    print(response.text)
    if response.status_code == 200:
        response_text = response.text
        data = json.loads(response_text)
        actual_response = json.loads(data["response"])
        return actual_response
    else:
        raise Exception("Failed to generate course")
