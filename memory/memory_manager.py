# Simple in-memory storage
_memory = {}

def save(document_id, data):
    _memory[document_id] = data

def get(document_id):
    return _memory.get(document_id)

def list_all():
    return _memory