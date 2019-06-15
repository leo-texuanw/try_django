from django import forms

from .models import Article


class ArticleModelForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
                'title',
                'content',
                'active',
        ]

    # naming: clean_<fieldname>
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title.lower() == 'abc':
            raise forms.ValidationError("This is not a valid title")
        return title
