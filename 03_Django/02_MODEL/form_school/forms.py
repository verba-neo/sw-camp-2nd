from django import forms
from .models import Student


class StudentForm(forms.ModelForm):

    name = forms.CharField(min_length=2, max_length=20)
    age = forms.IntegerField(min_value=14, max_value=70)
    major = forms.CharField(min_length=2, max_length=20)

    class Meta:
        model = Student
        fields = '__all__'


class ReplyForm(forms.ModelForm):
    pass