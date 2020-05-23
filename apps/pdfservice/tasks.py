from celery import task

from apps.pdfservice.models import PdfRecord
from apps.pdfservice.utils import create_pdf_link

import datetime


@task()
def send_pdfs():
    for record in PdfRecord.objects.all():
        if datetime.datetime.now() - record.created >= datetime.timedelta(minutes=5):
            link = create_pdf_link(record.data, f"{record.usernmae}_{record.id}.pdf", record.user)
            # send link
            record.delete()
