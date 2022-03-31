from take5.survey.models import (
    Survey,
    SurveyQuestion,
    SurveyQuestionAlternative,
    SurveyUserAnswer
)

for i in range(11, 21):
    Survey.objects.create(name=f'Pesquisa {i}')
