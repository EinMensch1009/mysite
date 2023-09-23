from django.contrib import admin

from .models import Question
from .models import Choice
from .models import Website
from .models import Umfrage

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Website)
admin.site.register(Umfrage)
