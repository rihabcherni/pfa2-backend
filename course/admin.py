from django.contrib import admin
from .models import  Category, Cours, Module, Lecon, Inscription, Commentaire, CourseProgressScore

admin.site.register(Category)
admin.site.register(Cours)
admin.site.register(Module)
admin.site.register(Lecon)
admin.site.register(Inscription)
admin.site.register(Commentaire)
admin.site.register(CourseProgressScore)
