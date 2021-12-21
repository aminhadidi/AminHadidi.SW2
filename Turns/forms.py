from django import forms
from . import models

class TurnsReservation(forms.ModelForm):
    class Meta:
        model = models.Turn
        fields = ['customer_name','slug', 'name_barber',  'date']
class DateForm(forms.Form):
    date = forms.DateTimeField(
        input_formats=['%Y/%M/%D %H:%M:%S'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )
