import django.forms

import urls.models


class URLForm(django.forms.ModelForm):
    class Meta:
        model = urls.models.URL
        fields = [
            urls.models.URL.target_url.field.name,
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['style'] = 'text-align: center;'
