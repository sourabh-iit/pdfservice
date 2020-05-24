from apps.pdfservice.models import PdfRecord, Pdf

from django.core.files.base import ContentFile
from fpdf import FPDF
from django.conf import settings

import datetime
import os
import json


def onNewRequest(data, user):
    try:
        record = PdfRecord.objects.get(user=user)
    except PdfRecord.DoesNotExist:
        record = PdfRecord(user=user)
    record.data = json.dumps(data)
    record.created = datetime.datetime.now()
    record.save()


def create_pdf_link(data, filename, user):
    pdf = FPDF()
    pdf.set_font("Arial", size=15)
    pdf.add_page()
    pdf.set_title(data['title'])
    for i, question in enumerate(data['questions']):
        pdf.multi_cell(180, 10, txt=f"Q{i+1}. {question}")
    data = pdf.output(filename, dest="S").encode('latin-1')
    pdf_object = Pdf.objects.create(user=user)
    pdf_object.pdf.save(filename, ContentFile(data))
    return f"{settings.BASE_URL}{pdf_object.pdf.url}"
