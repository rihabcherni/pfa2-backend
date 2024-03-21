from django.contrib import admin
from .models import  Cours, Module, Lecon, Inscription, Commentaire, CourseScore

admin.site.register(Cours)
admin.site.register(Module)
admin.site.register(Lecon)
admin.site.register(Inscription)
admin.site.register(Commentaire)
admin.site.register(CourseScore)
