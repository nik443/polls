from django.contrib import admin

from .models import Question, Choice

# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [ # разбиваем форму на наборы полей
        (None, {
            'fields': ['question_text']
        }), 
        ('Date information', {
            'fields': ['pub_date'],
            'classes' : ('collapse'),
        }),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently') # отображаемые поля и метод
    list_filter = ('pub_date',) # список фильтров
    search_fields = ('question_text',) # список полей, по которым можно будет совершать поиск


admin.site.register(Question, QuestionAdmin)