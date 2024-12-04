from django.contrib import admin
from . models import Login,JobSeeker,Employer,Enquiry,Jobs,AppliedJobs,News

# Register your models here.
admin.site.register(Login)
admin.site.register(JobSeeker)
admin.site.register(Employer)
admin.site.register(Enquiry)
admin.site.register(Jobs)
admin.site.register(AppliedJobs)
admin.site.register(News)


