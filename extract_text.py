import os
from docx import Document

def extract_docx_text(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"❌ File not found: {path}")
    try:
        doc = Document(path)
        return "\n".join([para.text for para in doc.paragraphs])
    except Exception as e:
        print(f"❌ Error reading {path}: {e}")
        return ""

def extract_resumes(folder):
    texts = []
    for file in os.listdir(folder):
        path = os.path.join(folder, file)
        print("Reading:", path)
        if file.endswith(".docx"):
            content = extract_docx_text(path)
            if content:
                texts.append(content)
    return texts

def extract_job_description(path):
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()