from django.db.models import Sum
from django.shortcuts import render
from requests import Response
from rest_framework import generics
from .models import Category, ContenuAudio, ContenuImage, ContenuTexte, ContenuVideo, Cours, CourseProgressScore, Module, Lecon, Inscription, Commentaire
from .serializers import CategorySerializer, ContenuAudioSerializer, ContenuImageSerializer, ContenuTexteSerializer, ContenuVideoSerializer, CoursSerializer, ModuleSerializer, LeconSerializer, InscriptionSerializer, CommentaireSerializer
from rest_framework import status
from rest_framework.views import APIView

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

class ContenuTexteListCreate(generics.ListCreateAPIView):
    queryset = ContenuTexte.objects.all()
    serializer_class = ContenuTexteSerializer

class ContenuTexteRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContenuTexte.objects.all()
    serializer_class = ContenuTexteSerializer


class ContenuImageListCreate(generics.ListCreateAPIView):
    queryset = ContenuImage.objects.all()
    serializer_class = ContenuImageSerializer

class ContenuImageRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContenuImage.objects.all()
    serializer_class = ContenuImageSerializer

class ContenuAudioListCreate(generics.ListCreateAPIView):
    queryset = ContenuAudio.objects.all()
    serializer_class = ContenuAudioSerializer

class ContenuAudioRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContenuAudio.objects.all()
    serializer_class = ContenuAudioSerializer

class ContenuVideoListCreate(generics.ListCreateAPIView):
    queryset = ContenuVideo.objects.all()
    serializer_class = ContenuVideoSerializer

class ContenuVideoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContenuVideo.objects.all()
    serializer_class = ContenuVideoSerializer

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

