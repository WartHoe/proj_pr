from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):  # Или admin.StackedInline для другого отображения
    model = Choice
    extra = 3  # Количество пустых форм для добавления

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]  # Добавляем связанные Choice к вопросу
    list_display = ('question_text', 'pub_date', 'was_published_recently')  # Отображение в списке

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)  # Оставляем отдельную регистрацию