from django.db import models
from django.contrib.auth import get_user_model

from Account.models import CustomUser


User=get_user_model()


# Create your models here.


class Tag(models.Model):
    name=models.CharField(max_length=250)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='Tag'
        verbose_name_plural='Tags'

    

    
    


class Story(models.Model):

    title=models.CharField( max_length=250)

    author=models.ForeignKey(User, on_delete=models.CASCADE)

    image=models.ImageField( upload_to='Story/')


    show_date=models.DateField(null=True)

    category=models.ForeignKey('Category', on_delete=models.CASCADE, related_name='story_category')

    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    desription=models.TextField()

    tags=models.ManyToManyField("Tag")

    class Meta:
        verbose_name='Story'
        verbose_name_plural='Stories'



class Category(models.Model):
    name=models.CharField(max_length=250)
    image=models.ImageField( upload_to='Category/')

    is_active=models.BooleanField(default=True)

    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name='Category'
        verbose_name_plural='Categories'



class Comment(models.Model):
    message = models.TextField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    story = models.ForeignKey(Story, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.user.username}"

    class Meta:
        verbose_name = 'Story Comment'
        verbose_name_plural = 'Story Comments'