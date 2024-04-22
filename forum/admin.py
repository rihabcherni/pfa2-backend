from django.contrib import admin
from forum.models import Discussion, QuestionPoser, Reponse
# Register your models here.

admin.site.register(Discussion)
admin.site.register(QuestionPoser)
admin.site.register(Reponse)
