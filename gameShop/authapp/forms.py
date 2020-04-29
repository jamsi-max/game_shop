from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm
from django import forms

from authapp.models import ShopUser
from mainapp.models import ProductCategory
from adminapp.utils import FormWidgetMixin, check_age

class ShopUserLoginForm(FormWidgetMixin, AuthenticationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'password')
        # widgets = {
        #     'username': forms.TextInput(attrs={'class': 'form-log-item'})
        # }

    placeholder = True
    class_all_fields = 'form-log-item'


class ShopUserRegisterForm(FormWidgetMixin, UserCreationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'password1', 'password2', 'first_name', 'age', 'email', 'avatar')

    class_all_fields = 'form-reg-item'
    
    def clean_age(self):
        return check_age(self, 18)
    
class ShopUserEditForm(FormWidgetMixin, UserChangeForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'password', 'first_name', 'age', 'email', 'avatar')

    class_all_fields = 'form-reg-item'
    password = False
    
    def clean_age(self):
        return check_age(self, 18)    

class ShopUserChangePassword(FormWidgetMixin, PasswordChangeForm):
    class Meta:
        model = ShopUser
        fields = ('__all__')

    class_all_fields = 'form-reg-item'

 