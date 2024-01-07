import json
from datetime import datetime
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from ..userdatafiles import load_user_data

def generate_cover_letter(output_path: str, body_text: str):
    try:
        CONFIG = load_user_data()
    except Exception as e:
        raise e

    # User details
    name = CONFIG['name']
    address = CONFIG['address']
    email = CONFIG['email']

    # Create a new Word document
    doc = Document()
    
    # Add date
    doc.add_paragraph("Date: " + datetime.today().strftime("%B %d, %Y"))

    # Add user details
    doc.add_paragraph(name, style='Heading1')
    doc.add_paragraph(address)
    doc.add_paragraph(email)

    # Add body text
    doc.add_paragraph("Dear Recruiting Manager,")
    body_split = body_text.split("\n")
    for body in body_split:
        doc.add_paragraph(body)

    # Add closing text
    closing = ("Thank you for your time and consideration. "
               "I look forward to hearing from you soon.")
    doc.add_paragraph(closing)
    doc.add_paragraph("Sincerely,")
    doc.add_paragraph(name)
    doc.add_paragraph(email)

    # Save the document
    doc.save(output_path + '/coverletter.docx')
