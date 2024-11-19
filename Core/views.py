from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import ContactForm

from Core.models import Slider,Contact

# Create your views here.


def index(request):

    sliders=Slider.objects.all()

    context={
        'sliders':sliders
    }

    return render(request,'index.html', context)






def about(request):
    return render(request,'about.html')





def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})




def create(request):
    return render(request,'create_story.html')




def subscribers(request):
    return render(request,'email-subscribers.html')







def recipe(request):
    return render(request,'recipes.html')




def single(request):
    return render(request,'single.html')





def userprofile(request):
    return render(request,'user-profile.html')




def changepassword(request):
    return render(request,'accounts/change_password.html')





def forgetpassword(request):
    return render(request,'accounts/forget_password.html')







def reset_password(request):
    return render(request,'accounts/reset_password.html')
