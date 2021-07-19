from django.contrib import admin

# Register your models here.

from .models import Register, Login, Online

admin.site.register(Register)

admin.site.register(Login)

admin.site.register(Online)
