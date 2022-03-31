from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from take5.survey.models import (
    Survey
)
from take5.survey.serializers import (
    SurveyListSerializer,
    SurveyDetailSerializer
)


@api_view(['GET'])
def survey_list(request):
    surveys = Survey.objects.all()
    serializer = SurveyListSerializer(surveys, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def survey_detail(request, pk):
    try:
        survey = Survey.objects.prefetch_related(
            'questions', 'questions__alternatives').get(pk=pk)
    except Survey.DoesNotExist:
        return Response('Pesquisa não existente', status.HTTP_204_NO_CONTENT)
    serializer = SurveyDetailSerializer(survey)
    return Response(serializer.data)
