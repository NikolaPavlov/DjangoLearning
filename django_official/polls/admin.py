from django.contrib import admin
from .models import Question
from .models import Choice

# Register your models here.
# admin.site.register(Question)
# admin.site.register(Choice)


class QuestionAdmin(admin.ModelAdmin):
    '''
        this class reorder the fields in the admin
        panel for Question
    '''
    fields = ['pub_date', 'question_text']

# register the Question for admin pannel, and for second
# param add QuestionAdmin, for custom fields
admin.site.register(Question, QuestionAdmin)
