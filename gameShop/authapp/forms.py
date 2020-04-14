from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms
from authapp.models import ShopUser

class ShopUserLoginForm(AuthenticationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwars):
        super(ShopUserLoginForm, self).__init__(*args, **kwars)
        for field_name, field in self.fields.items():
            field.widget.attrs['placeholder'] = f'{field_name}'
            field.widget.attrs['class'] = 'form-log-item'

class ShopUserRegisterForm(UserCreationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'password1', 'password2', 'first_name', 'age', 'email', 'avatar')
    
    def __init__(self, *args, **kwars):
        super(ShopUserRegisterForm, self).__init__(*args, **kwars)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-reg-item'
            field.help_text = ''
    
    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError('Вам должно быть больше 18 лет')
        return data
    
class ShopUserEditForm(UserChangeForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'password', 'first_name', 'age', 'email', 'avatar')

    def __init__(self, *args, **kwars):
        super(ShopUserEditForm, self).__init__(*args, **kwars)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-reg-item'
            field.help_text = ''
            if field_name == 'password':
                field.widget = forms.HiddenInput()
    
    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError('Вам должно быть больше 18 лет')
        return data    

