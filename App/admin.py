from django.contrib import admin
from .models import ContactPage

# Register your models here.
@admin.register(ContactPage)
class ContactAdmin(admin.ModelAdmin):
    list_display=['id','name','email','phone','company', 'company_website','services', 'describe','term']
