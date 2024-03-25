from django.db.models import Sum
from django.shortcuts import render
from requests import Response
from rest_framework import generics
from .models import Category, Cours, CourseProgressScore, Module, Lecon, Inscription, Commentaire
from .serializers import CategorySerializer, CoursSerializer, ModuleSerializer, LeconSerializer, InscriptionSerializer, CommentaireSerializer
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.
class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CoursListCreate(generics.ListCreateAPIView):
    queryset = Cours.objects.all()
    serializer_class = CoursSerializer

class CoursRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cours.objects.all()
    serializer_class = CoursSerializer

class ModuleListCreate(generics.ListCreateAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer

class ModuleRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer

class LeconListCreate(generics.ListCreateAPIView):
    queryset = Lecon.objects.all()
    serializer_class = LeconSerializer

class LeconRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lecon.objects.all()
    serializer_class = LeconSerializer

class InscriptionListCreate(generics.ListCreateAPIView):
    queryset = Inscription.objects.all()
    serializer_class = InscriptionSerializer

class InscriptionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inscription.objects.all()
    serializer_class = InscriptionSerializer

class CommentaireListCreate(generics.ListCreateAPIView):
    queryset = Commentaire.objects.all()
    serializer_class = CommentaireSerializer

class CommentaireRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Commentaire.objects.all()
    serializer_class = CommentaireSerializer

# class QuizListCreate(generics.ListCreateAPIView):
#     queryset = Quiz.objects.all()
#     serializer_class = QuizSerializer

# class QuizRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Quiz.objects.all()
#     serializer_class = QuizSerializer

# class EtudiantQuizResponseView(APIView):
#     queryset = EtudiantQuizResponse.objects.all()
#     serializer_class = EtudiantQuizResponseSerializer

#     def post(self, request):
#         serializer = EtudiantQuizResponseSerializer(data=request.data)
#         if serializer.is_valid():
#             # Assuming the request data contains quiz_id, student_id, student_response
#             quiz_id = serializer.validated_data.get('quiz_id')
#             student_id = serializer.validated_data.get('student_id')
#             student_response = serializer.validated_data.get('student_response')

#             quiz = Quiz.objects.get(pk=quiz_id)
#             correct_response = quiz.reponse_correcte

#             score = 0
#             if student_response == correct_response:
#                 score = 1

#             EtudiantQuizResponse.objects.create(quiz=quiz, student_id=student_id, student_response=student_response, score=score)

#             # Recalculate course score
#             course_id = quiz.lecon.module.cours_id
#             update_course_score(course_id, student_id)

#             return Response({'message': 'Response saved successfully.'}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# def update_course_score(course_id, student_id):
#     total_score = 0
#     total_questions = 0
#     quizzes = Quiz.objects.filter(lecon__module__cours_id=course_id)
#     for quiz in quizzes:
#         total_score += EtudiantQuizResponse.objects.filter(quiz=quiz, student_id=student_id).aggregate(score_sum=Sum('score')).get('score_sum', 0)
#         total_questions += 1

#     if total_questions > 0:
#         score_percentage = (total_score / total_questions) * 100
#         CourseProgressScore.objects.update_or_create(course_id=course_id, student_id=student_id, defaults={'score': score_percentage})