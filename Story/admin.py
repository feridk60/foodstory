from django.contrib import admin

from Story.models import Category, Story, Tag,Comment

# Register your models here.




# Register your models here.

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display=['id','name']
    list_display_links=['id','name']
    search_fields=['name']
    list_per_page=5
    
    
    



@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display=['id','title','image','show_date','created_at','update_at','desription']
    list_display_links=['id','title']
    search_fields=['title']
    list_filter=['show_date','created_at','update_at']
    list_per_page=5
    
    





@admin.register(Category)
class CategorytAdmin(admin.ModelAdmin):
    list_display=['id','name','image','is_active','created_at','update_at']
    list_display_links=['id','name']
    search_fields=['name']
    list_filter=['is_active','created_at','update_at']
    list_per_page=5
    
    




@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'story','created_at', 'updated_at']
    list_display_links = ['id', 'user']
    search_fields = ['user']
    list_filter = ['created_at', 'updated_at']