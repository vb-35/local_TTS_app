import fitz  # PyMuPDF
import ebooklib
from ebooklib import epub
import os

def extract_text_from_pdf(pdf_path):
    """Extract text from PDF file."""
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

def extract_text_from_epub(epub_path):
    """Extract text from EPUB file."""
    book = epub.read_epub(epub_path)
    text = ""
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            text += item.get_content().decode('utf-8')
    return text.replace('<', ' <').replace('>', '> ')  # Basic HTML cleanup

def read_text_file(file_path):
    """Read text from a plain text file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def process_file(file_path):
    """Process input file based on its extension."""
    _, ext = os.path.splitext(file_path)
    ext = ext.lower()
    
    if ext == '.pdf':
        return extract_text_from_pdf(file_path)
    elif ext == '.epub':
        return extract_text_from_epub(file_path)
    elif ext == '.txt':
        return read_text_file(file_path)
    else:
        raise ValueError(f"Unsupported file format: {ext}")
