from django.forms import ModelForm
from app.principal.models import Suscripciones

class SuscripcionForm(ModelForm):
    class Meta:
        model= Suscripciones


