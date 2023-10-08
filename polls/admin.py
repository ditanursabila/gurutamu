from django.contrib import admin
from polls.models import Question, Choice


# Register your models here.
class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3  # default:3


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInLine]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
