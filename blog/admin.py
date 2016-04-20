from django.contrib import admin

#from blog.models import Blog, Author, Entry
from .models import Blog, Author, Entry, BlogComment

admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(Entry)
admin.site.register(BlogComment)