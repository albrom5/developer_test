from django.db import models
from django.contrib.auth.models import User

from take5.survey.models import TimeStampedModel


class Survey(TimeStampedModel):
    name = models.CharField('nome', max_length=250)

    def __str__(self):
        return self.name


class SurveyQuestion(TimeStampedModel):
    survey = models.ForeignKey('survey.Survey',
                               on_delete=models.CASCADE,
                               verbose_name='pesquisa',
                               related_name='questions')
    question_text = models.CharField('pergunta', max_length=1000)

    def __str__(self):
        return f'{self.survey} - {self.question_text}'


class SurveyQuestionAlternative(TimeStampedModel):
    question = models.ForeignKey('survey.SurveyQuestion',
                                 on_delete=models.CASCADE,
                                 verbose_name='pergunta',
                                 related_name='alternatives')
    alternative_text = models.CharField('Alternativa', max_length=1000)

    def __str__(self):
        return self.alternative_text


class SurveyUserAnswer(TimeStampedModel):
    answer = models.ForeignKey('survey.SurveyQuestionAlternative',
                               on_delete=models.CASCADE, verbose_name='resposta')
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             verbose_name='usuario')

    def __str__(self):
        return self.answer
