from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('survey/', include('take5.survey.urls')),
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
]
