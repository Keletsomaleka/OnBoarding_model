from django import forms
from .models import ModelInputs

class ModelInputForm(forms.ModelForm):

    class Meta:
        model = ModelInputs
        fields = ("nedbank_cc","money_app","greenbacks_flag","profile_segmentation","Race")

