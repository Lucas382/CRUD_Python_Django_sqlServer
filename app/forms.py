from django.forms import ModelForm
from app.models import Emails

class EmailsForm(ModelForm):
    class Meta:
        model = Emails
        fields = ['email', 'safetyMail_Status', 'format_valid', 'mx_found', 'smtp_check', 'score', 'is_valid', 'messef']