import json
import ollama
import re
from utils.prompt_templates import CLASSIFIER_PROMPT

def classify_content(content):
    prompt = CLASSIFIER_PROMPT.format(content=content[:2000])
    response = ollama.generate(model="phi", prompt=prompt)
    raw = response["response"].strip()
    print("[DEBUG] Classifier LLM Response:", raw)
    if isinstance(raw, dict):
        result = raw
    else:
        raw=raw.strip()
        try:
            result = json.loads(raw)
        except json.JSONDecodeError:
            match = re.search(r'format[:=]\\s*(\\w+)[\\s,\\n]+intent[:=]\\s*(\\w+)', raw, re.IGNORECASE)
            if match:
                result = {
                "format": match.group(1).capitalize(),
                "intent": match.group(2).capitalize()
                }
            else:
                print(f"[ERROR] Classification failed: {raw}")
                return {"format": "Unknown", "intent": "Unknown"}

    if "format" not in result or "intent" not in result:
        print(f"[ERROR] Incomplete classification: {result}")
        return {"format": "Unknown", "intent": "Unknown"}

    return result
