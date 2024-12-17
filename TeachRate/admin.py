from django.contrib import admin
from .models import Signup

admin.site.register(Signup)

from django.contrib import admin
from .models import University, Department, Teacher

admin.site.register(University)
admin.site.register(Department)
admin.site.register(Teacher)
