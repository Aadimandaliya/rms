from django import forms
from.models import usersignup,ryph

class signupform(forms.ModelForm):
    class Meta:
        model = usersignup
        fields = '__all__'



class ryphform(forms.ModelForm):
    class Meta:
        model = ryph
        fields = '__all__'