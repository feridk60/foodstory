from django.shortcuts import redirect, render
from Account.forms import LoginForm, RegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
# from django.contrib.auth.views import PasswordChangeView,PasswordResetView,PasswordResetConfirmView
# from .forms import ChangePasswordForm,ResetPasswordForm,CustomSetPasswordForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlencode
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.tokens import default_token_generator

def send_test_email():
    subject = 'Test E-poçt'
    message = 'Bu, Django tətbiqindən göndərilən test e-poçtudur.'
    recipient_list = ['recipient_email@example.com']

    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)



@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


# Create your views here.
def login_view(request):
    form=LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            email=form.cleaned_data.get('email')
            password=form.cleaned_data.get('password')

            user = authenticate(request, email = email, password = password)

            if user:
                login(request, user)
                return redirect("index_lists")
            else:
                return redirect('login')

    context = {
        'form': form
    }

    return render(request, 'accounts/login.html', context)









def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')

            if password1 and password2 and password1 == password2:
                user = form.save(commit=False)
                user.set_password(password1)  
                user.is_active = False  
                user.save()

                
                subject = "Qeydiyyatınız Təsdiq Edildi"
                message = "Qeydiyyatınız uğurla tamamlandı. Hesabınızı aktivləşdirmək üçün linki izləyin."
                recipient_list = [user.email]

                send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)
                
                return redirect('login')  
       
        return render(request, 'accounts/register.html', {'form': form})
    
    form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})




# class ChangePasswordView(PasswordChangeView):
#     template_name='change_password.html'
#     form_class= ChangePasswordForm
#     success_url = reverse_lazy('login')



# class ResetPasswordView(PasswordResetView):
#     template_name = 'forget_pwd.html'
#     form_class = ResetPasswordForm
#     email_template_name = 'reset_password_email.html'
#     subject_template_name = 'reset_password_subject.txt'
#     success_message = "We've emailed you instructions for setting your password, " \
#                       "if an account exists with the email you entered. You should receive them shortly." \
#                       "If you don't receive an email, " \
#                       "please make sure you've entered the address you registered with, and check your spam folder."

#     success_url = reverse_lazy('login')   



# class ResetPasswordConfirmView(PasswordResetConfirmView):
#     template_name='reset_password_confirm.html'
#     form_class=CustomSetPasswordForm
#     success_url = reverse_lazy('reset_password_complete')  








# Bu kod, e-poçt ünvanı ilə istifadəçi doğrulaması həyata keçirmək üçün bir xüsusi authentication backend 
# (kimlik doğrulama arxa ucu) yaradır. Bu sinif, Django-nun standart authenticate funksiyasını dəyişdirir və 
# istifadəçini yalnızca e-poçt ünvanı və şifrə ilə doğrulamağı təmin edir.


# from django.contrib.auth.backends import ModelBackend
# from django.contrib.auth.models import User

# class EmailAuthBackend(ModelBackend):
#     def authenticate(self, request, username=None, password=None, **kwargs):
#         try:
#             user = User.objects.get(email=username)  
#             if user.check_password(password):
#                 return user
#         except User.DoesNotExist:
#             return None


# settings.py
# AUTHENTICATION_BACKENDS = [
#     'myapp.backends.EmailAuthBackend',  
#     'django.contrib.auth.backends.ModelBackend',
# ]
