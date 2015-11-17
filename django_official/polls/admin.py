from django.contrib import admin
from .models import Question, Choice


# Register your models here.
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fields = ['question_text', 'pub_date']  # admin add list
    search_fields = ('question_text',)  # admin search field
    list_filter = ['pub_date']  # admin filter functionality
    inlines = [ChoiceInline]  # add choices in question admin
    list_display = ('question_text', 'pub_date')  # admin change list


admin.site.site_header = 'Polls app administration'  # admin site header
admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)
