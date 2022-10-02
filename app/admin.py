from cProfile import Profile
from django.contrib import admin
from .models import Profile, Programming, Work, Education, Software, Programming

admin.site.register(Profile)    
admin.site.register(Work)
admin.site.register(Education)
admin.site.register(Software)
admin.site.register(Programming)