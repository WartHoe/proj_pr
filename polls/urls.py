from django.urls import path
from .views_api import QuestionListCreateView, ChoiceListCreateView, vote, QuestionDetailView 
from . import views
from .views import report_view

urlpatterns = [
    path('api/questions/', QuestionListCreateView.as_view(), name='questions-api'),
    path('api/choices/', ChoiceListCreateView.as_view(), name='choices-api'),
    path('api/questions/<int:pk>/', QuestionDetailView.as_view(), name='question-detail'),
    path('api/vote/', vote, name='vote'),
    path('', report_view, name='report'),
]
