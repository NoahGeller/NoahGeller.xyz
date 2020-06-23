from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from blog.models import Tag, Post


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
