from django.db import models
from django.utils import timezone

import datetime


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.question.question_text + ": " + self.choice_text
    
class Website(models.Model):
    name = models.CharField(max_length=100, unique=True)
    link = models.CharField(max_length=1000)
    regex = models.CharField(max_length=500)
    groups = models.CharField(max_length=500)
    parsed = models.BooleanField(default=False)
    regex_link = models.CharField(max_length=500)
    groups_link = models.CharField(max_length=500)
    parsed_link = models.BooleanField(default=False)
    link_comp = models.CharField(max_length=1000)

    def __str__(self):
        return self.link[:25]
    
class Umfrage(models.Model):

    # - Diese Schulfächer gefallen mir am Besten
        #  Mathe Deutsch Informatik Biologie Sport Physik Chemie Englisch (multi answer)

    frage_1 = models.CharField(max_length=500)

    # - Ich könnte alleine ein Bild aufhängen
        # Ja, Nein, Das kann doch jeder, Niemals, Ich denke schon

    frage_2 = models.CharField(max_length=500)

    # - Ich habe alle meine Mappen und Hefte für die Schule geordnet
        # Ein wenig, gar nicht, Natürlich, Einigermaßen, Ja

    frage_3 = models.CharField(max_length=500)

    # - Mein PC hat ein Problem, ich kann es aber selber lösen
        # Ja, Nein, Ich denke schon, Niemals, Klar doch

    frage_4 = models.CharField(max_length=500)

    # -Ich gestalte mein Zimmer gerne um
        # Nein, Nicht wirklich, Ja, Sehr oft, Manchmal

    frage_5 = models.CharField(max_length=500)

# - Alles was ich machge plane ich durch
    # Manchmal, Nie, Immer, Oft, Selten

    frage_6 = models.CharField(max_length=500)

# - Ich packe mit im Haushalt an 
    # Jeden Tag, Nie, Manchmal, selten, Sehr oft

    frage_7 = models.CharField(max_length=500)

# - Kochen macht mir Spaß
    # Ja voll, öfters, gar nicht, selten, Manchmal

    frage_8 = models.CharField(max_length=500)

# - Ich kümmer mich gerne um Tiere
    # Ja voll, öfters, gar nicht, selten, Manchmal

    frage_9 = models.CharField(max_length=500)

# - Meine Mutter möchte den Garten bepflanzen, ich helfe mit
    # Nein, Nicht wirklich, Ja, Sehr oft, Manchmal

    frage_10 = models.CharField(max_length=500)
