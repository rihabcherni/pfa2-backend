from rest_framework import serializers
from .models import  Category, Cours, CourseProgressScore, Module, Lecon, Inscription, Commentaire

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cours
        fields = '__all__'
    def validate_author(self, value):
        if value.type_user != 'author':
            raise serializers.ValidationError("Only teachers can be assigned as the authors for a course.")
        return value

class CourseProgressScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseProgressScore
        fields = '__all__'

    def validate_user(self, value):
        if value.type_user != 'apprenant':
            raise serializers.ValidationError("Only Etudiants can do the course.")
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
        if value.type_user != 'apprenant':
            raise serializers.ValidationError("Only Etudiants can create an inscription.")
        return value
    
class CommentaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commentaire
        fields = '__all__'

    def validate_user(self, value):
        if value.type_user != 'apprenant':
            raise serializers.ValidationError("Only Etudiants can create a comment.")
        return value
    