import fitz  # PyMuPDF
from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq


load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")



def extract_text_from_pdf(uploaded_file):
    """Extract text from a PDF file."""
    pdf_document = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page in pdf_document:
        text += page.get_text()
    return text

def ask_ai(prompt,max_tokens=1000):
    """Send a prompt to the AI model and return the response."""
    model=ChatGroq(api_key=GROQ_API_KEY, model="openai/gpt-oss-120b", max_tokens=max_tokens)
    response = model.predict(prompt)
    return response


