import json
import ollama
from utils.prompt_templates import EMAIL_PROCESSING_PROMPT

def process_email(email_text):
    prompt = EMAIL_PROCESSING_PROMPT.format(email_content=email_text)
    response = ollama.generate(model="phi", prompt=prompt)
    print("[DEBUG] Email Agent Raw Response:", response)
    try:
        return json.loads(response["response"])
    except json.JSONDecodeError:
        return {"error": "Failed to parse email"}