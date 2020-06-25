from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from portfolio.models import Project

class ProjectAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)

admin.site.register(Project, ProjectAdmin)
