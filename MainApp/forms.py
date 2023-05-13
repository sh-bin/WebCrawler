from django import forms

class UrlForm(forms.Form):
    url = forms.CharField(label='Enter URL', required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['url'].widget.attrs['class'] = 'form-control'
        self.fields['url'].widget.attrs['placeholder'] = self.fields['url'].label
