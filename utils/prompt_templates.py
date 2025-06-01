CLASSIFIER_PROMPT = """
You are a strict JSON generator. Classify the following document into:

- format: PDF, JSON, or Email
- intent: Invoice, RFQ, Complaint, or Regulation

Return ONLY valid JSON. NO explanations, no markdown, just:

{{"format": "Email", "intent": "RFQ"}}

Text:
---
{content}
---
"""

EMAIL_PROCESSING_PROMPT = """
You are an Email Agent. Extract:
- sender
- subject
- body_summary
- urgency (1–5)
- related_to (e.g., RFQ, Invoice, Complaint)

Return ONLY this as JSON, nothing else.

Email:
---
{email_content}
---
"""

JSON_INVOICE_PROMPT = """
You are a JSON Agent processing invoices.
Format into:
{{"invoice_id": "", "vendor": "", "total_amount": 0, "due_date": ""}}

Raw JSON:
---
{json_data}
---

If fields missing or invalid, flag them.
"""
