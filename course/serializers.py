from rest_framework import serializers
from .models import  Cours, CourseScore, Module, Lecon, Inscription, Commentaire

class CoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cours
        fields = '__all__'
    def validate_enseignant(self, value):
        if value.type_user != 'enseignant':
            raise serializers.ValidationError("Only teachers can be assigned as the teacher for a course.")
        return value
    
class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'

class LeconSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecon
        fields = '__all__'

class InscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscription
        fields = '__all__'
    def validate_user(self, value):
        if value.type_user != 'etudiant':
            raise serializers.ValidationError("Only Etudiants can create an inscription.")
        return value
    
class CommentaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commentaire
        fields = '__all__'

    def validate_user(self, value):
        if value.type_user != 'etudiant':
            raise serializers.ValidationError("Only Etudiants can create a comment.")
        return value
    
# class QuizSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Quiz
#         fields = '__all__'


class CourseScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseScore
        fields = '__all__'

    def validate_user(self, value):
        if value.type_user != 'etudiant':
            raise serializers.ValidationError("Only Etudiants can do the course.")
        return value
    
# class EtudiantQuizResponseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = EtudiantQuizResponse
#         fields = ['quiz','etudiant','etudiant_response']

#     def validate_user(self, value):
#         if value.type_user != 'etudiant':
#             raise serializers.ValidationError("Only etudiants can do the quiz.")
#         return value