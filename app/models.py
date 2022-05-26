from django.db import models

# Create your models here.
class Emails(models.Model):
    email = models.CharField(max_length=50)
    safetyMail_Status = models.CharField(max_length=50)
    format_valid = models.CharField(max_length=50)
    mx_found = models.CharField(max_length=50)
    smtp_check = models.CharField(max_length=50)
    score = models.CharField(max_length=50)
    is_valid = models.CharField(max_length=50)
    messef = models.CharField(max_length=50)

