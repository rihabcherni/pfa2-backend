from django.urls import path
from course.views import *

urlpatterns = [
    path('cours/', CoursListCreate.as_view(), name='cours-list-create'),
    path('cours/<int:pk>/', CoursRetrieveUpdateDestroy.as_view(), name='cours-retrieve-update-destroy'),
   
    path('modules/', ModuleListCreate.as_view(), name='module-list-create'),
    path('modules/<int:pk>/', ModuleRetrieveUpdateDestroy.as_view(), name='module-retrieve-update-destroy'),
    
    path('lecons/', LeconListCreate.as_view(), name='lecon-list-create'),
    path('lecons/<int:pk>/', LeconRetrieveUpdateDestroy.as_view(), name='lecon-retrieve-update-destroy'),
   
    path('inscriptions/', InscriptionListCreate.as_view(), name='inscription-list-create'),
    path('inscriptions/<int:pk>/', InscriptionRetrieveUpdateDestroy.as_view(), name='inscription-retrieve-update-destroy'),
   
    path('commentaires/', CommentaireListCreate.as_view(), name='commentaire-list-create'),
    path('commentaires/<int:pk>/', CommentaireRetrieveUpdateDestroy.as_view(), name='commentaire-retrieve-update-destroy'),
   
    # path('quiz/', QuizListCreate.as_view(), name='quiz-list-create'),
    # path('quiz/<int:pk>/', QuizRetrieveUpdateDestroy.as_view(), name='quiz-retrieve-update-destroy'),
    # path('quiz/response/', EtudiantQuizResponseView.as_view(), name='quiz_response'),

]
