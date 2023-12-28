from pyapply.config import CONFIG
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph
from datetime import datetime
 
def generate_cover_letter(output_path,body_text):
    doc = SimpleDocTemplate(output_path+'/coverletter.pdf', pagesize=letter)
    styles = getSampleStyleSheet()
    content=[]
    date1 = "Date: "+ datetime.today().strftime("%B %d, %Y")
    content.append(Paragraph(CONFIG['name'], styles['Heading1']))
    content.append(Paragraph(f"", styles['Normal']))
    content.append(Paragraph(CONFIG['address'], styles['Normal']))
    content.append(Paragraph(f"", styles['Normal']))
    content.append(Paragraph(date1 , styles['Normal']))
    content.append(Paragraph(f"Dear Recruiting Manager,", styles['BodyText']))
    body_split = body_text.split("\n")
    for body in body_split:
        content.append(Paragraph(body, styles['BodyText']))
    content.append(Paragraph(f"", styles['Normal']))
    content.append(Paragraph(f"I am available 20 hours a week", styles['Normal']))
    content.append(Paragraph(f"", styles['Normal']))
    body=("""Thank you for your time and consideration. I look forward to hearing from you soon.""")
    content.append(Paragraph(body, styles['BodyText']))
    content.append(Paragraph("Sincerely,", styles['BodyText']))
    content.append(Paragraph(CONFIG['name'], styles['Normal']))
    content.append(Paragraph(CONFIG['email'], styles['Normal']))
    doc.build(content)
   