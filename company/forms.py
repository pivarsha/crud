from django import forms
from .models import *


class EmployeeModelForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = (
            'Emp_id',
            'name',
            'address',
            'email',
            'position',
            'company',
            'contact_detail'
        )


class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = (
            'student_id',
            'name',
            'address',
            'email',
            'contact_detail'
        )


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=255)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password != password_confirm:
            raise forms.ValidationError("Passwords do not match")