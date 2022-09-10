from django import forms
from django.forms import ModelForm
from .models import Tags , companyReview

class TagsForm(ModelForm):
    class Meta:
        model = Tags
        fields = "__all__"

class companyReviewForm(ModelForm):
    class Meta:
        model = companyReview
        fields = [
            "company_name","review","worked_here"
        ]
    
    def clean_review(self):
        censor = ['fuck','shit','bullshit','fucking']
        for word in censor:
            if word in self.cleaned_data["review"]:
                raise forms.ValidationError(f'{word} you used not allowed in reviews, Thanks')
        return self.cleaned_data["review"]


