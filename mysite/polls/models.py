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
    link = models.CharField(max_length=1000)
    regex = models.CharField(max_length=500)

    def __str__(self):
        return self.link[:25]
    
class Umfrage(models.Model):
    frage_1 = models.CharField(max_length=500)
    frage_2 = models.CharField(max_length=500)
    frage_3 = models.CharField(max_length=500)
    frage_4 = models.CharField(max_length=500)
    frage_5 = models.CharField(max_length=500)
    frage_6 = models.CharField(max_length=500)
    frage_7 = models.CharField(max_length=500)
    frage_8 = models.CharField(max_length=500)
    frage_9 = models.CharField(max_length=500)
    frage_10 = models.CharField(max_length=500)

