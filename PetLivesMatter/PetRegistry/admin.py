from django.contrib import admin
from .models import Pet
from account.models import Account
# Register your models here.
admin.site.register(Pet)
admin.site.register(Account)
