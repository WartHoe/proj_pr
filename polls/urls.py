from django.urls import path
from .views_api import QuestionListCreateView, ChoiceListCreateView, vote
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('api/questions/', QuestionListCreateView.as_view(), name='questions-api'),
    path('api/choices/', ChoiceListCreateView.as_view(), name='choices-api'),
    path('api/vote/', vote, name='vote'),
]
