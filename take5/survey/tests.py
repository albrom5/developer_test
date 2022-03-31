from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase

from take5.survey.models import (
    Survey,
    SurveyQuestion,
    SurveyQuestionAlternative,
    SurveyUserAnswer,
)


alternative_choices = {'A': 'Sempre',
                       'B': 'Quase sempre',
                       'C': 'Às vezes',
                       'D': 'Raramente',
                       'E': 'Nunca'}


class SurveyListTest(APITestCase):
    def setUp(self):
        self.surveys = Survey.objects.bulk_create(
            [Survey(name=f'Pesquisa nº {s}') for s in range(1, 6)]
        )

    def test_get_survey_list(self):
        """List must retrieve all surveys stored."""
        response = self.client.get('/survey/survey_list/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), len(self.surveys))
        self.assertEqual(response.headers['Content-Type'],
                         'application/json')


class SurveyDetailTest(APITestCase):
    def setUp(self):
        surveys = Survey.objects.bulk_create(
            [Survey(name=f'Pesquisa nº {s}') for s in range(1, 6)]
        )
        for survey in surveys:
            questions = SurveyQuestion.objects.bulk_create(
                [SurveyQuestion(question_text=f'Questão nº {q}',
                                survey=survey,
                                order=q) for q in range(1, 11)]
            )

            for question in questions:
                SurveyQuestionAlternative.objects.bulk_create(
                    [SurveyQuestionAlternative(
                        question=question,
                        alternative_text=alternative_choices[char]
                    ) for char in 'ABCDE']
                )
        self.survey = Survey.objects.get(pk=1)
        self.response = self.client.get('/survey/1/')

    def test_get_survey_exists(self):
        """Detail view must retrieve a survey instance"""
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.response.data.serializer.instance, self.survey)

    def test_survey_has_questions(self):
        """Must retrieve all questions related to the selected survey"""
        questions = SurveyQuestion.objects.filter(survey=self.survey)
        self.assertEqual(
            len(self.response.data['questions']), questions.count())

    def test_question_has_alternatives(self):
        """Must retrieve all alternatives related to each question"""
        questions = SurveyQuestion.objects.filter(survey=self.survey)

        for i, q in enumerate(questions):
            alternatives = SurveyQuestionAlternative.objects.filter(
                question=q
            )
            self.assertEqual(
                len(self.response.data['questions'][i]['alternatives']),
                alternatives.count()
            )


class SurveyDetailInvalidRequest(APITestCase):

    def test_invalid_request(self):
        """Response if user try to get a survey that doesn't exist"""
        Survey.objects.bulk_create(
            [Survey(name=f'Pesquisa nº {s}') for s in range(1, 6)]
        )

        response = self.client.get('/survey/0/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.data, 'Pesquisa não existente')


class SurveyAnswerUserTest(APITestCase):
    def setUp(self):
        self.survey = Survey.objects.create(name='Pesquisa Teste')
        questions = SurveyQuestion.objects.bulk_create([SurveyQuestion(
            survey=self.survey, question_text=f'Pergunta {q}'
        ) for q in range(1, 11)])
        for question in questions:
            SurveyQuestionAlternative.objects.bulk_create(
                [SurveyQuestionAlternative(
                    question=question,
                    alternative_text=alternative_choices[char]
                ) for char in 'ABCDE']
            )
        self.user = User.objects.create_user(username='tester')

    def test_answers(self):
        """User answer all questions in selected survey"""
        survey_questions = SurveyQuestion.objects.filter(survey=self.survey)
        for question in survey_questions:
            alternatives = SurveyQuestionAlternative.objects.filter(
                question=question)
            SurveyUserAnswer.objects.create(question=question, user=self.user,
                                            answer=alternatives[0])
        answers = SurveyUserAnswer.objects.filter(
            answer__question__survey=self.survey, user=self.user)
        self.assertEqual(answers.count(), survey_questions.count())
