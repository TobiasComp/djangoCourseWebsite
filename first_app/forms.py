from django import forms
from django.core import validators
from first_app.models import User1
# This is with checking a particular field notice it is outside of the class!!!
# def check_for_z(value):
#     if value[0].lower != 'z':
#         raise forms.ValidationError("the field must start with z")

class NewUserForm(forms.models.ModelForm):
    class Meta:
            model = User1
            fields = '__all__'


class FormName(forms.Form):
    name = forms.CharField()
    # email = forms.EmailField(validators=[check_for_z])
    email = forms.EmailField()
    verify_email = forms.EmailField()

    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput)

    # One function to do all of the validation needs to be in the class!!!
    def clean(self):
        all_clean_data = super().clean()
        print("in the clean method")
        email = all_clean_data['email']
        verify_email = all_clean_data['verify_email']
        print("These are the email and verfiry_email firelds", email, verify_email)
        if email != verify_email:
            raise forms.ValidationError("The emails do not match!!")

class loginForm(forms.models.ModelForm):
    class Meta:
        model = User1
        fields = '__all__'
        exclude = ['last_name']
