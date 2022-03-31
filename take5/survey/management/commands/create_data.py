from django.core.management.base import BaseCommand

from take5.survey.models import (
    Survey,
    SurveyQuestion,
    SurveyQuestionAlternative,
)


alternative_choices = {'A': 'Sempre',
                       'B': 'Quase sempre',
                       'C': 'Às vezes',
                       'D': 'Raramente',
                       'E': 'Nunca'}


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        surveys = Survey.objects.bulk_create(
            [Survey(name=f'Pesquisa nº {s}') for s in range(1, 6)]
        )
        self.stdout.write(f'Foram criadas {len(surveys)} pesquisas.')
        for survey in surveys:
            questions = SurveyQuestion.objects.bulk_create(
                [SurveyQuestion(question_text=f'Questão nº {q}',
                        survey=survey) for q in range(1, 11)]
            )
            for question in questions:
                alternatives = SurveyQuestionAlternative.objects.bulk_create(
                    [SurveyQuestionAlternative(
                        question=question,
                        alternative_text=alternative_choices[char]
                    ) for char in 'ABCDE']
                )
