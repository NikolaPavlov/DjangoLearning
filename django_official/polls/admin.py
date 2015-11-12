from django.contrib import admin
from .models import Question, Choice


# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    fields = ['question_text', 'pub_date']
    list_filter = ['pub_date']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
