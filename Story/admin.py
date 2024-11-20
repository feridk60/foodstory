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
    actions = ['mark_as_approved']  # Əməliyyatı qeyd edirik

    def mark_as_approved(self, request, queryset):
        # Seçilmiş şərhləri təsdiqlənmiş kimi işarələyir
        queryset.update(approved=True)
        self.message_user(request, f"{queryset.count()} şərh təsdiqləndi.")  # İstifadəçiyə bildiriş göstərir

    # Əməliyyatın təsviri (admin panelində göstərilir)
    mark_as_approved.short_description = "Seçilmiş şərhləri təsdiqlə"