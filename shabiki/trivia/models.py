from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()
class Questions(models.Model):
    questionId = models.AutoField(primary_key = True)
    question = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.question
    
class Choices(models.Model):
    choiceId = models.AutoField(primary_key = True )
    questionId = models.ForeignKey(Questions, on_delete = models.CASCADE)
    choice = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.choice

class Answers(models.Model):
    answerId = models.AutoField(primary_key = True)
    questionId = models.OneToOneField(Questions, on_delete = models.CASCADE, default="")
    answer = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.answer
    
class Game(models.Model):
    timer = models.BooleanField(default=False)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    level = models.IntegerField()

    def __str__(self):
        return self.level + " : " + self.question.question
    
class GameQuestions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    total_marks = models.IntegerField()

    def __str__(self):
        return self.user + ' : ' + self.game.level
