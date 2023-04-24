from django.db import models

# Create your models here.
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