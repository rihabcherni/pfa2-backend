from rest_framework import serializers
from .models import Quiz, QuestionQuiz, ReponseQuestionQuiz, ApprenantQuizReponse

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'

class QuestionQuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionQuiz
        fields = '__all__'

class ReponseQuestionQuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReponseQuestionQuiz
        fields = '__all__'

class ApprenantQuizReponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApprenantQuizReponse
        fields = '__all__'
