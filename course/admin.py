from django.contrib import admin
from .models import  Category, Cours, Lecon, Inscription, Commentaire, CourseProgressScore, Review

admin.site.register(Category)
admin.site.register(Cours)
admin.site.register(Lecon)
admin.site.register(Inscription)
admin.site.register(Commentaire)
admin.site.register(CourseProgressScore)
admin.site.register(Review)
