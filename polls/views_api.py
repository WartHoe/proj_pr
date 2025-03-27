from rest_framework import generics, status
from rest_framework.response import Response
from .models import Question, Choice
from .serializers import QuestionSerializer, ChoiceSerializer
from rest_framework.decorators import api_view

# Questions
class QuestionListCreateView(generics.ListCreateAPIView):
    queryset = Question.objects.all().prefetch_related('choice_set')
    serializer_class = QuestionSerializer

    def post(self, request, *args, **kwargs):
        if 'delete_id' in request.data:
            try:
                Question.objects.get(id=request.data['delete_id']).delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except Question.DoesNotExist:
                return Response({'error': 'Question not found'}, status=status.HTTP_404_NOT_FOUND)
        return super().post(request, *args, **kwargs)

# Choices
class ChoiceListCreateView(generics.ListCreateAPIView):
    queryset = Choice.objects.all().select_related('question')
    serializer_class = ChoiceSerializer

    def post(self, request, *args, **kwargs):
        if 'delete_id' in request.data:
            try:
                Choice.objects.get(id=request.data['delete_id']).delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except Choice.DoesNotExist:
                return Response({'error': 'Choice not found'}, status=status.HTTP_404_NOT_FOUND)
        return super().post(request, *args, **kwargs)

@api_view(['POST'])
def vote(request):
    try:
        votes = request.data.get('votes', [])
        
        for vote in votes:
            choice = Choice.objects.get(id=vote['choice_id'])
            choice.votes += 1
            choice.save()
            
        return Response({'status': 'success'}, status=status.HTTP_200_OK)
        
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)