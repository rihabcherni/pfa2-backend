from django.shortcuts import render

# Create your views here.


# class QuizListCreate(generics.ListCreateAPIView):
#     queryset = Quiz.objects.all()
#     serializer_class = QuizSerializer

# class QuizRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Quiz.objects.all()
#     serializer_class = QuizSerializer

# class ApprenantQuizResponseView(APIView):
#     queryset = ApprenantQuizResponse.objects.all()
#     serializer_class = ApprenantQuizResponseSerializer

#     def post(self, request):
#         serializer = ApprenantQuizResponseSerializer(data=request.data)
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

#             ApprenantQuizResponse.objects.create(quiz=quiz, student_id=student_id, student_response=student_response, score=score)

#             # Recalculate course score
#             course_id = quiz.lecon.Module.cours_id
#             update_course_score(course_id, student_id)

#             return Response({'message': 'Response saved successfully.'}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# def update_course_score(course_id, student_id):
#     total_score = 0
#     total_questions = 0
#     quizzes = Quiz.objects.filter(lecon__Module__cours_id=course_id)
#     for quiz in quizzes:
#         total_score += ApprenantQuizResponse.objects.filter(quiz=quiz, student_id=student_id).aggregate(score_sum=Sum('score')).get('score_sum', 0)
#         total_questions += 1

#     if total_questions > 0:
#         score_percentage = (total_score / total_questions) * 100
#         CourseProgressScore.objects.update_or_create(course_id=course_id, student_id=student_id, defaults={'score': score_percentage})