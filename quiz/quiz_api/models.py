from django.db import models
from django.contrib.auth.models import User

class MC_Question(models.Model):
    question = models.TextField()
    correct_answer = models.CharField(max_length=100) 
    
    def __str__(self):
        return self.question

class Choice(models.Model):
    choice_text = models.CharField(max_length=100, blank=False, null=False)
    parent = models.ForeignKey('MC_Question', related_name='related_choices', on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text

    class Meta:
        unique_together = ('choice_text', 'parent',)

class Profile(models.Model):
    user = models.ForeignKey(User, related_name='related_user', on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

class Attempt(models.Model):
    question = models.ForeignKey(MC_Question)
    attempted_by =  models.ForeignKey('User', related_name='attempted_by', on_delete=models.CASCADE)
    provided_answer = models.CharField(max_length=100) 

