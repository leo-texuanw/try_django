from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    """ form based on model """
    title = forms.CharField(
                label='Your Title',
                widget=forms.TextInput(
                    attrs={"placeholder": "Your title"}
                )
            )

    email = forms.EmailField()

    description = forms.CharField(
            widget=forms.Textarea(  # all these params are optional
                attrs={
                    "placeholder": "Your description",
                    "class": "new-class-name two",
                    "id": "my-id-for-textarea",
                    "rows": 10,
                    "cols": 40,
                    }
                )
            )

    price = forms.DecimalField(initial=9.99)
    featured = forms.BooleanField(required=True)

    class Meta:
        """ Meta related to Model """
        model = Product
        fields = [
            'title',
            'description',
            'price',
            'featured',
        ]

    # For value validation
    #   def function name as: clean_<my_field>()
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if "news" not in title:
            raise forms.ValidationError("This is not a valid title")
        if "sports" in title:
            raise forms.ValidationError("This is not a valid title")
        return title

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if not email.endswith("edu"):
            raise forms.ValidationError("This is not a valid email")
        return email


class RawProductForm(forms.Form):
    """ Form from scratch """
    title = forms.CharField(
                label='Your Title',
                widget=forms.TextInput(
                    attrs={"placeholder": "Your title"}
                )
            )

    description = forms.CharField(
            widget=forms.Textarea(  # all these params are optional
                attrs={
                    "placeholder": "Your description",
                    "class": "new-class-name two",
                    "id": "my-id-for-textarea",
                    "rows": 10,
                    "cols": 40,
                    }
                )
            )

    price = forms.DecimalField()
    featured = forms.BooleanField(required=True)
