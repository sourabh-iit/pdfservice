from django.db import models
from django.contrib.auth.models import User


def pdf_path(instance, filename):
    return 'pdfs/%s/%s' % (instance.user.username, filename)


# Create your models here.
class PdfRecord(models.Model):
    user = models.ForeignKey(User, related_name="records", on_delete=models.CASCADE)
    data = models.TextField()
    created = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.user.username


class Pdf(models.Model):
    user = models.ForeignKey(User, related_name="pdfs", on_delete=models.CASCADE)
    pdf = models.FileField(upload_to=pdf_path, max_length=100, null=True)
    created = models.DateTimeField(auto_now_add=True)
