from django import forms
from Account.models import CustomUser
from django.core.exceptions import ValidationError
# from django.contrib.auth.forms import PasswordChangeForm,PasswordResetForm,SetPasswordForm




class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder' : 'Enter your email'
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder' : 'Password'
            }
        )
    )


class RegistrationForm(forms.ModelForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : "Your password"
            }
        ),
        label='Password'
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : "Confirm password"
            }
        ),
        label='Confirm Password'
    )

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        widgets = {
            'first_name' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : "Enter your first name",
                }
            ),
            'last_name' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : "Enter your last name"
                }
            ),
            'username' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : "Username"
                }
            ),
            'email' : forms.EmailInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' :"E-mail"
                }
            ),
        }



    def clean(self):
        cleaned_data=super(RegistrationForm,self).clean()
        if self.cleaned_data['password1'] !=self.cleaned_data['password2']:
            raise forms.ValidationError('Password is not equel password2!')
        return cleaned_data
        
       
            
# class ChangePasswordForm(PasswordChangeForm):
#     old_password = forms.CharField(required=True, label='Old Password',
#         widget=forms.PasswordInput(
#             attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Your Old Password'
#             }))
#     new_password1 = forms.CharField(required=True, label='New Password',
#         widget=forms.PasswordInput(
#             attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Your New Password'
#             }))
#     new_password2 = forms.CharField(required=True, label='Confirm New Password',
#         widget=forms.PasswordInput(
#             attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Confirm Your New Password'
#             }))         
        




# class ResetPasswordForm(PasswordResetForm):
#     email = forms.EmailField(
#         widget=forms.EmailInput(
#             attrs={
#                 'class': 'form-control',
#                 'placeholder' : 'Enter Your E-mail'
#             }
#         )
#     )


# class CustomSetPasswordForm(SetPasswordForm):
#     new_password1 = forms.CharField(required=True, label='New Password',
#         widget=forms.PasswordInput(
#             attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Your New Password'
#             }))
#     new_password2 = forms.CharField(required=True, label='Confirm New Password',
#         widget=forms.PasswordInput(
#             attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Confirm Your New Password'
#             }))