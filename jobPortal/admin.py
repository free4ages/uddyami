from django.contrib import admin
from .models import JobPost
# Register your models here.


class JobPostAdmin(admin.ModelAdmin):
    search_fields = ('job_title','company_name','mobile',)
    list_display = ('job_title','company_name','mobile','city',)
    list_filter = ('city',)


admin.site.register(JobPost, JobPostAdmin)