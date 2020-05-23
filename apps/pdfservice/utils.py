from apps.pdfservice.models import PdfRecord, Pdf

from django.core.files.base import ContentFile
from fpdf import FPDF
from django.conf import settings

import datetime
import os


def onNewRequest(data, user):
    try:
        record = PdfRecord.objects.get(user=user)
    except PdfRecord.DoesNotExist:
        record = PdfRecord(user = user)
    record.data = data
    record.created = datetime.datetime.now()
    record.save()

def create_pdf_link(data, filename, user):
    pdf = FPDF()
    pdf.set_font("Arial", size = 15)
    pdf.add_page()
    pdf.cell(200, 10, txt = "Similar questions",  
         ln = 1, align = 'C')
    pdf.output(filename)
    pdf_object = Pdf.objects.create(user=user)
    data = None
    with open(filename, 'rb') as f:
        data = f.read()
    os.remove(filename)
    pdf_object.pdf.save(filename, ContentFile(data))
    return f"{settings.BASE_URL}{pdf_object.pdf.url}"
