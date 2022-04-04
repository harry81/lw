"""lw URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view
from synthea.views import (ConceptViewSet, ConditionOccurrenceViewSet,
                           DeathViewSet, DrugExposureViewSet, PersonViewSet,
                           StatViewSet, VisitOccurrenceViewSet)

router = DefaultRouter()
router.register(r'stat', StatViewSet, basename='stat')
router.register(r'concept', ConceptViewSet, basename='concept')
router.register(r'person', PersonViewSet, basename='person')
router.register(r'visitoccurrence', VisitOccurrenceViewSet, basename='visitoccurrence')
router.register(r'conditionoccurrence', ConditionOccurrenceViewSet, basename='conditionoccurrence')
router.register(r'drugexposure', DrugExposureViewSet, basename='drugexposure')
router.register(r'death', DeathViewSet, basename='death')


schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'schema/', schema_view)
]

urlpatterns += router.urls
