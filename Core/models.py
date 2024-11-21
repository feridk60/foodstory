from django.db import models



# Create your models here.


class Slider(models.Model):
    title=models.CharField( max_length=250)
    image=models.ImageField( upload_to='sliders-image/',null=True,blank=True)
    describtion=models.TextField()


    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name='Slider'
        verbose_name_plural='Sliders'


class Contact(models.Model):
    fullname=models.CharField( max_length=50)
    email=models.EmailField( max_length=54)
    subject=models.CharField( max_length=50)
    message=models.TextField()

    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.fullname
    

    class Meta:
        verbose_name='Contact'
        verbose_name_plural='Contacts'



    


class DateMixin(models.Model):
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Subscriber(DateMixin):
    email = models.EmailField(max_length=200, unique=True)  
    is_active = models.BooleanField(default=True)  

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Subscriber'
        verbose_name_plural = 'Subscribers'