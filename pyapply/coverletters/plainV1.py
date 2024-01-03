import json
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph
from datetime import datetime
from ..userdatafiles import load_user_data


def generate_cover_letter(output_path:str,body_text:str):
    try:
        CONFIG = load_user_data()
    except Exception as e:
        raise e

    name = CONFIG['name']
    address = CONFIG['address']
    email = CONFIG['email']

    # generate cover letter
    doc = SimpleDocTemplate(output_path+'/coverletter.pdf', pagesize=letter)
    styles = getSampleStyleSheet()
    content=[]
    date1 = "Date: "+ datetime.today().strftime("%B %d, %Y")
    content.append(Paragraph(name, styles['Heading1']))
    content.append(Paragraph(f"", styles['Normal']))
    content.append(Paragraph(address, styles['Normal']))
    content.append(Paragraph(f"", styles['Normal']))
    content.append(Paragraph(date1 , styles['Normal']))
    content.append(Paragraph(f"Dear Recruiting Manager,", styles['BodyText']))
    body_split = body_text.split("\n")
    for body in body_split:
        content.append(Paragraph(body, styles['BodyText']))
    content.append(Paragraph(f"", styles['Normal']))
    content.append(Paragraph(f"", styles['Normal']))
    body=("""Thank you for your time and consideration. I look forward to hearing from you soon.""")
    content.append(Paragraph(body, styles['BodyText']))
    content.append(Paragraph("Sincerely,", styles['BodyText']))
    content.append(Paragraph(name, styles['Normal']))
    content.append(Paragraph(email, styles['Normal']))
    doc.build(content)
   