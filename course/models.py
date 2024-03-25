from djongo import models
from accounts.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100, default='0xe148')
    course_number = models.IntegerField(default=0)
    image = models.ImageField(upload_to='assets/category', default='assets/category/autre.PNG', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Cours(models.Model):
    NIVEAU_CHOICES = (
        ('débutant', 'Débutant'),
        ('intermédiaire', 'Intermédiaire'),
        ('avancé', 'Avancé'),
    )
    titre = models.CharField(max_length=255)
    cours_photo = models.ImageField(upload_to='assets/cours', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)
    description = models.TextField()
    enseignant = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    niveau = models.CharField(max_length=20, choices=NIVEAU_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.titre

class CourseProgressScore(models.Model):
    course = models.ForeignKey('Cours', on_delete=models.CASCADE)
    etudiant = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.etudiant} - {self.course} - Score: {self.score}"
        
class Module(models.Model):
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE)
    titre = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.titre
    
class Lecon(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    titre = models.CharField(max_length=255)
    contenu_texte = models.TextField()
    contenu_image = models.ImageField(upload_to='assets/lecons/images', null=True, blank=True)
    contenu_video = models.URLField(null=True, blank=True)
    contenu_audio = models.FileField(upload_to='assets/lecons/audio', null=True, blank=True)

    def __str__(self):
        return self.titre

class Inscription(models.Model):
    etudiant = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE)
    date_inscription = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.etudiant} - {self.cours}"
    
class Commentaire(models.Model):
    etudiant =  models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    lecon = models.ForeignKey(Lecon, on_delete=models.CASCADE)
    contenu_commentaire = models.TextField()
    date_commentaire = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.etudiant} - {self.lecon}"


# class Choice(models.Model):
#     choice_text = models.CharField(max_length=255)
#     is_correct = models.BooleanField(default=False)

#     class Meta:
#         abstract = True
        
#     def __str__(self):
#         return self.choice_text


# class Question(models.Model):
#     _id = models.ObjectIdField(primary_key=True)
#     question_text = models.CharField(max_length=255)
#     choices = models.ArrayField(
#         model_container=Choice,
#     )

#     def __str__(self):
#         return self.question_text
       
# class Quiz(models.Model):
#     lecon = models.ForeignKey(Lecon, on_delete=models.CASCADE)
#     quiz_image = models.ImageField(upload_to='assets/quiz', null=True, blank=True)
#     questions =  models.ArrayField(model_container= Question)

#     def __str__(self):
#         return f"{self.lecon}"
    

# class EtudiantQuizResponse(models.Model):
#     # quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
#     etudiant = models.ForeignKey(User, on_delete=models.CASCADE)
#     etudiant_response = models.CharField(max_length=255)
#     score = models.IntegerField(default=0)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"{self.etudiant} - {self.quiz} - Response: {self.etudiant_response} - Score: {self.score}"

