from django import forms


class ProductCreateForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea())
    price = forms.FloatField(required=False)
    rate = forms.FloatField(required=False)
    image = forms.ImageField(required=False)

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        if len(title) < 5:
            raise forms.ValidationError("Title to short!")
        return cleaned_data


class ReviewCreateForm(forms.Form):
    title = forms.CharField()