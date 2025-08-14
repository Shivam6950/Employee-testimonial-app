from django import forms
from .models import Emp

class FeedbackForm(forms.Form):
    name = forms.CharField(label="Enter your name", max_length=50)
    email = forms.CharField(label="Enter your email address")
    feedback = forms.CharField(label="Your feedback...",widget=forms.Textarea)

def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class EmpForm(forms.ModelForm):
    class Meta:
        model=Emp
        fields=['name','emp_id','phone']