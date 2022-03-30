from django.contrib import admin

from take5.survey.models import (
    Survey,
    SurveyQuestion,
    SurveyQuestionAlternative,
    SurveyUserAnswer
)


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'edited_at')
    search_fields = ('name',)
    list_filter = ('created_at',)


@admin.register(SurveyQuestion)
class SurveyQuestionAdmin(admin.ModelAdmin):
    list_display = ('survey', 'question_text', 'created_at')
    search_fields = ('survey__name', 'question_text')
    list_filter = ('survey', 'created_at')


@admin.register(SurveyQuestionAlternative)
class SurveyQuestionAlternativeAdmin(admin.ModelAdmin):
    list_display = ('question', 'alternative_text', 'created_at')
    search_fields = ('question__survey__name', 'question__question_text',
                     'alternative_text')
    list_filter = ('question__survey', 'question', 'created_at')


@admin.register(SurveyUserAnswer)
class SurveyUserAnswerAdmin(admin.ModelAdmin):
    list_display = ('answer', 'user', 'created_at', 'edited_at')
    search_fields = ('answer__alternative_text', 'user')
    list_filter = ('user', 'answer__question__survey')
