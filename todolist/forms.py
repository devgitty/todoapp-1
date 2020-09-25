import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class WeekTargetForm(forms.Form):
    # hier Null-Werte für Datum (z.B. Due_DateTime) berücksichtigen. Problem mit Models.py: None wird automatisch zu String "None" umgewandelt was in init.py (C:\venv\Lib\site-packages\django\db\models\fields\__init__.py) zu einem Fehler führt


""" Beispiel:

class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']
        
        # Check if a date is not in the past. 
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))

        # Check if a date is in the allowed range (+4 weeks from today).
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

        # Remember to always return the cleaned data.
        return data
"""