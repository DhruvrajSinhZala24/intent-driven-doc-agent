# 🧠 Multi-Agent AI Document Processor

This project is a modular multi-agent AI system that classifies documents (PDF, JSON, Email), identifies intent, and routes the content to specialized agents (Email or JSON). It logs the results into a lightweight memory store for traceability.

## 🏢 Background

This project was developed as part of an internship task focused on building a practical multi-agent AI document processing pipeline using LLMs and shared memory.


## 📦 Project Structure

```
.
├── main.py                 # Entry point – routes files to the correct agent
├── agents/
│   ├── classifier.py       # Classifier Agent using LLM for format + intent
│   ├── email_agent.py      # Email Agent to extract sender, urgency, topic
│   └── json_agent.py       # JSON Agent to reformat invoices and flag issues
├── memory/
│   └── memory_manager.py   # In-memory shared memory store
├── utils/
│   ├── file_utils.py       # File reader utility
│   └── prompt_templates.py # LLM prompt templates
├── output_logs/
│   └── logs.json           # Last output log
├── sample_email.txt        # Sample Email input
├── sample_invoice.json     # Sample JSON input
└── README.md
```

## 🛠 Requirements

- Python 3.8+
- [Ollama](https://ollama.com/) (with `phi` model pulled locally)

> Ensure you’ve installed and started the Ollama server locally:
```bash
ollama run phi
```

## 🚀 How to Run

### 1. Install dependencies:
```bash
pip install ollama
```

### 2. Run with Sample Email

```bash
python main.py input_samples/sample_email.txt
```

### 3. Run with Sample Invoice JSON

```bash
python main.py input_samples/sample_invoice.json
```

### 4. Output

The results are printed to the console and saved to:

```
output_logs/logs.json
```

Example log output:
```json
{
  "document_id": "5295c64f-4116-409e-8ce4-f683336e19d0",
  "source": "input_samples/sample_email.txt",
  "type": "Email",
  "intent": "RFQ",
  "timestamp": "2025-06-01T14:04:22.598217",
  "extracted_data": {
    "sender": "supplier@example.com",
    "subject": "RFQ for Widget Parts",
    "body_summary": "Please send quote for 100 units of Widget A by Friday.",
    "urgency": 5,
    "related_to": [
      "RFQ"
    ]
  }
}
```

## 🧠 Shared Memory

The system stores classification and agent results in memory (via `memory_manager.py`) for traceability and chaining.

## 🧪 Test Inputs

- `sample_email.txt`: Email requesting a quote
- `sample_invoice.json`: JSON-formatted invoice

## 📝 Notes

- PDF support is **not yet implemented**.
- Uses the local `phi` LLM via Ollama for all agent processing.
- Logs are overwritten per run (extendable for multi-log persistence).
