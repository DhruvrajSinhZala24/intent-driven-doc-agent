import uuid
import datetime
import json
import os

from utils.file_utils import read_file
from agents.classifier import classify_content
from agents.email_agent import process_email
from agents.json_agent import process_json
from memory.memory_manager import save

# Ensure output_logs directory exists
os.makedirs("output_logs", exist_ok=True)

def process_document(file_path):
    raw_content = read_file(file_path)
    print("[Classifier] Classifying...")
    classification = classify_content(raw_content)

    # Safely extract format and intent
    doc_format = classification.get("format", "Unknown")
    doc_intent = classification.get("intent", "Unknown")
    print(f"[Router] Format: {doc_format}, Intent: {doc_intent}")

    format_lower = doc_format.lower()

    # Route to correct agent
    if "email" in format_lower:
        extracted = process_email(raw_content)
    elif "json" in format_lower:
        try:
            json_data = json.loads(raw_content)
            extracted = process_json(json_data)
        except json.JSONDecodeError:
            extracted = {"error": "Invalid JSON"}
    elif "pdf" in format_lower:
        extracted = {"error": "PDF support not implemented yet"}
    else:
        extracted = {"error": "Unknown or unsupported format"}

    log_entry = {
        "document_id": str(uuid.uuid4()),
        "source": file_path,
        "type": doc_format,
        "intent": doc_intent,
        "timestamp": datetime.datetime.now().isoformat(),
        "extracted_data": extracted
    }

    save(log_entry["document_id"], log_entry)
    print("\n✅ Final Output:")
    print(json.dumps(log_entry, indent=2))

    with open("output_logs/logs.json", "w") as f:
        json.dump(log_entry, f, indent=2)

    return log_entry



import sys
if len(sys.argv) < 2:
    print("Usage: python main.py <file_path>")
    sys.exit(1)
process_document(sys.argv[1])