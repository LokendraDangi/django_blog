from django.contrib import admin
from .models import Category, Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
   list_display = ['title', 'intro','body']
   prepopulated_fields = {'slug': ('title',)} 

class CategoryAdmin(admin.ModelAdmin):
   list_display = ['title', 'slug']
   prepopulated_fields = {'slug': ('title',)} 

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)