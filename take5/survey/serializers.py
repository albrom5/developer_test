from rest_framework import serializers

from take5.survey.models import (
    Survey,
    SurveyQuestion,
    SurveyQuestionAlternative
)


class SurveyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ['id', 'name', 'created_at']


class SurveyQuestionAlternativeSerializer(serializers.ModelSerializer):

    class Meta:
        model = SurveyQuestionAlternative
        fields = ['id', 'alternative_text']


class SurveyQuestionSerializer(serializers.ModelSerializer):
    alternatives = SurveyQuestionAlternativeSerializer(
        many=True, read_only=True)

    class Meta:
        model = SurveyQuestion
        fields = ['id', 'question_text', 'alternatives']


class SurveyDetailSerializer(serializers.ModelSerializer):
    questions = SurveyQuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Survey
        fields = ['id', 'name', 'questions']
