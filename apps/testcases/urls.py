# -*- coding: utf-8 -*-
from django.urls import path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"testcases", views.TestcasesViewSet)
urlpatterns = []
urlpatterns += router.urls
