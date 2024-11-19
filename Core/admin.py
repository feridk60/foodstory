from django.contrib import admin

from Core.models import Contact, Slider

# Register your models here.
class SliderAdmin(admin.ModelAdmin):
    list_display=['id','title','image','describtion']
    list_display_links=['id','title']
    search_fields=['title']
    list_per_page=5
   




# @admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=['id','fullname','message','email','created_at','update_at']
    list_display_links=['id','fullname','email']
    search_fields=['fullname','email',]
    list_filter=['created_at','update_at']
   

admin.site.register(Slider,SliderAdmin)
admin.site.register(Contact,ContactAdmin)
