from django.urls import path
from . import views


urlpatterns = [
    path('check/', views.Check.as_view(), name='check')

]
