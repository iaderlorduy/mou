from django import forms

class ImageUploadForm(forms.Form):
    """Image upload form."""
    recibo = forms.ImageField(label = "Seleccione un archivo")
    