from django.contrib import admin

# Register your models here.
from .models import Faq, Faq_D
admin.site.register(Faq),
admin.site.register(Faq_D),