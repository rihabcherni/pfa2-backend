from rest_framework import serializers
from .models import  Category, ContenuAudio, ContenuImage, ContenuTexte, ContenuVideo, Cours, CourseProgressScore, Lecon, Inscription, Commentaire, Review

class CategorySerializer(serializers.ModelSerializer):
    course_number = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = '__all__'

    def get_course_number(self, category):
        return category.courseNumber()

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = "__all__"
          
class CoursSerializer(serializers.ModelSerializer):
    lecon_number = serializers.SerializerMethodField()
    reviews = serializers.SerializerMethodField(method_name='get_reviews',read_only=True)
    class Meta:
        model = Cours
        fields = '__all__'
    def validate_auteur(self, value):
        if value.type_user != 'auteur':
            raise serializers.ValidationError("Only teachers can be assigned as the auteurs for a course.")
        return value
    
    def get_lecon_number(self, cours):
        return cours.leconNumber()
  
    def get_reviews(self,obj):
        reviews = obj.reviews.all()
        serializer = ReviewSerializer(reviews,many=True)
        return serializer.data

class CourseProgressScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseProgressScore
        fields = '__all__'

    def validate_user(self, value):
        if value.type_user != 'apprenant':
            raise serializers.ValidationError("Only Etudiants can do the course.")
        return value  
    
class LeconSerializer(serializers.ModelSerializer):
    image_number = serializers.SerializerMethodField()
    audio_number = serializers.SerializerMethodField()
    video_number = serializers.SerializerMethodField()
    texte_number = serializers.SerializerMethodField()

    class Meta:
        model = Lecon
        fields = '__all__'

    def get_image_number(self, lecon):
        return lecon.imageNumber()
    
    def get_texte_number(self, lecon):
        return lecon.texteNumber()
        
    def get_audio_number(self, lecon):
        return lecon.audioNumber()

    def get_video_number(self, lecon):
        return lecon.videoNumber()
    
class ContenuTexteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContenuTexte
        fields = '__all__'

class ContenuImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContenuImage
        fields = '__all__'

class ContenuVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContenuVideo
        fields = '__all__'

class ContenuAudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContenuAudio
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
    