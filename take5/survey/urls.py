from django.urls import path

from take5.survey import views as v


urlpatterns = [
    path('survey_list/', v.survey_list, name='survey_list'),
    path('<int:pk>/', v.survey_detail, name='survey_detail'),
]
