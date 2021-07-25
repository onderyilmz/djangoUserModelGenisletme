from django import forms
from accounts.models import UserProfile

class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    #email = forms.CharField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, label='Username', required=True)
    email = forms.EmailField(label='Email', required=True)
    password = forms.CharField(max_length=20, label='Password', required=True, widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=20, label='Password Again', required=True, widget=forms.PasswordInput)
    #first_name = forms.CharField(label='First Name', required=False)
    #last_name = forms.CharField(label='Last Name', required=False)

    def clean(self):
        username = self.cleaned_data.get("username")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")
        #first_name = self.cleaned_data.get("first_name")
        #last_name = self.cleaned_data.get("last_name")

        if password and confirm and password != confirm:
            raise forms.ValidationError("Wrong Password ")

        values = {
            "username": username,
            "email": email,
            "password": password,
            #"first_name": first_name,
            #"last_name": last_name,

        }
        return values


class UserProfileForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control", "placeholder": 'Name'}))
    surname = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control", "placeholder": 'surname'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'class': "form-control", "placeholder": 'Address'}))

    class Meta:
        model = UserProfile
        fields = ('name', 'surname', 'address')