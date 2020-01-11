from django.db import models

class Questions(models.Model):

    text = models.TextField()
    date_published = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

class Choice(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE,
    null=True)
    choice = models.TextField()

    def __str__(self):
      return self.question

class QuestionAnwser(models.Model):

    question = models.ForeignKey(Questions, on_delete=models.CASCADE,
    null=True)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE,
    null=True)

    def __str__(self):
        return self.question