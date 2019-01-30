from django import forms
from .models import UserAdd,Student



class UserLogin(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = UserAdd
        fields = ('username','password')




class UserRegister(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = UserAdd
        fields = "__all__"



# Students forms
class StudentRegister(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
