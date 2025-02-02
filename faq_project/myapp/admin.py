from django.contrib import admin

# Register your models here.
from .models import FAQ


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('qid', 'question', 'answer')
    readonly_fields = ('qid',)
