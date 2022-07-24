from django import forms
from app.models import Card
class CardForm(forms.ModelForm):
    class Meta:
        model=Card
        fields=['id','heading','sub_heading','description','image']