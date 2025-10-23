from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=65,
        widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Имя пользователя'})
    )
    password = forms.CharField(
        max_length=65, 
        widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Пароль'})
    )

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone', 'birth_date', 'country', 'city', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Имя пользователя'}),
            'email': forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Email адрес'}),
            'phone': forms.TextInput(attrs={'class': 'form-input', 'placeholder': '+7 (XXX) XXX-XX-XX'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'country': forms.Select(attrs={'class': 'form-select'}),
            'city': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ваш город'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Пароль'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Подтверждение пароля'}),
        }
    
    agreed_to_terms = forms.BooleanField(
        required=True,
        error_messages={'required': 'Вы должны согласиться с условиями использования'},
        widget=forms.CheckboxInput(attrs={'class': 'checkbox-input'})
    )
    
    newsletter_subscription = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'checkbox-input'})
    )
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError('Пользователь с таким email уже существует')
        return email
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.agreed_to_terms = self.cleaned_data.get('agreed_to_terms', False)
        user.newsletter_subscription = self.cleaned_data.get('newsletter_subscription', False)
        
        if commit:
            user.save()
        
        return user