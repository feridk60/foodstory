from datetime import date
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from Story.models import Category, Story
from .forms import ContactForm, SubscriberForm
from datetime import date
from Core.models import Slider,Contact
from django.http import HttpResponse
from Story.models import Story,Category
from .utils import send_email_to_subscribers
from datetime import datetime
datetime.now()


# Create your views here.


def index(request):

    sliders=Slider.objects.all()
    

    context={
        'sliders':sliders,
        
    }

    return render(request,'index.html', context)


def recentstory(request):

    recentstory=Story.objects.all()
    categories=Category.objects.all()
    

    context={
        'recentstory':recentstory,
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








def send_email_view(request):
    
    storyp = Story.objects.all()[:3]
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()  # Aboneliği kaydet
            send_email_to_subscribers(
                subject="Yeni Ürünler Web Sitemizden", 
                context={"storyp": storyp}  # Storyp'yi e-posta içeriği olarak gönder
            )
            return HttpResponse("E-postalar gönderildi.")
    else:
        form = ContactForm()  # Boş formu render et
    
    # Sayfayı render et
    return render(request, 'index.html', {'form': form})







def recipe(request):
    return render(request,'recipes.html')




def single(request):
    return render(request,'single.html')





def userprofile(request):
    return render(request,'user-profile.html')




