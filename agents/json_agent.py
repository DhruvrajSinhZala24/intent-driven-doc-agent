import json
import ollama
from utils.prompt_templates import JSON_INVOICE_PROMPT

def process_json(json_data):
    prompt = JSON_INVOICE_PROMPT.format(json_data=json.dumps(json_data))
    response = ollama.generate(model="phi", prompt=prompt)
    print("[DEBUG] JSON Agent Raw Response:", response)
    try:
        return json.loads(response["response"])
    except json.JSONDecodeError:
        return {"error": "Failed to process JSON"}