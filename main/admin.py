from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(CourseList)
admin.site.register(Quiz)
admin.site.register(PracticeQuestion)
admin.site.register(ChapterList)
admin.site.register(Summary)

class Que_StemInLineTable(admin.TabularInline):
    model = QuestionStem
    fields = [
        'que_stem',
        'ans',
    ]

class QuestionAdmin(admin.ModelAdmin):
    fields = [
        'quiz',
        'question',
    ]
    list_display = [
        'quiz',
        'question',
    ]
    inlines = [
        Que_StemInLineTable,
    ]

class Que_StemAdmin(admin.ModelAdmin):
    list_display = [
        'question',
        'que_stem',
        'ans'
    ]

admin.site.register(Question, QuestionAdmin)
admin.site.register(QuestionStem, Que_StemAdmin)