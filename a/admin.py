from django.contrib import admin

from .models import Tweet,Reply

admin.site.register(Tweet)
admin.site.register(Reply)