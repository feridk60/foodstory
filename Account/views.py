from django.shortcuts import redirect, render
from Account.forms import LoginForm, RegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
# from django.contrib.auth.views import PasswordChangeView,PasswordResetView,PasswordResetConfirmView
# from .forms import ChangePasswordForm,ResetPasswordForm,CustomSetPasswordForm




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
    form=RegistrationForm()

    if request.method == 'POST':

        form=RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
        else:
            return redirect('register')    
        return redirect('login')    

    
    context = {
        'form': form
    }

    return render(request,'accounts/register.html',context)



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


