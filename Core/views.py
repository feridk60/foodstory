from datetime import date
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from Story.models import Category, Story
from .forms import ContactForm
from datetime import date

from Core.models import Slider,Contact

# Create your views here.


def index(request):

    sliders=Slider.objects.all()
    categories=Category.objects.all()

    context={
        'sliders':sliders,
        'categories':categories,
    }

    return render(request,'index.html', context)






class LatestStoryListView(ListView):
    
    model = Story
    template_name = "index.html"
    context_object_name = "stori"

    def get_queryset(self):
        
        return Story.objects.filter(
            category__is_active=True,
            show_date__lte=date.today()
        ).order_by('-show_date')[:3]

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context['categor'] = Category.objects.filter(is_active=True)
        return context








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
