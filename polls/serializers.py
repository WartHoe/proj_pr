from rest_framework import serializers
from .models import Question, Choice

class ChoiceSerializer(serializers.ModelSerializer):
    question_text = serializers.CharField(source='question.question_text', read_only=True)
    
    class Meta:
        model = Choice
        fields = ['id', 'choice_text', 'votes', 'question', 'question_text']

class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, source='choice_set', read_only=True)
    
    class Meta:
        model = Question
        fields = ['id', 'question_text', 'pub_date', 'choices']