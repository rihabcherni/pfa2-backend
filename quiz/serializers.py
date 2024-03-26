from rest_framework import serializers
# from .models import 

# class QuizSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Quiz
#         fields = '__all__'
    
# class ApprenantQuizResponseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ApprenantQuizResponse
#         fields = ['quiz','apprenant','Apprenant_response']

#     def validate_user(self, value):
#         if value.type_user != 'apprenant':
#             raise serializers.ValidationError("Only Apprenants can do the quiz.")
#         return value