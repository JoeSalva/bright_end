from django.db import models

# Create your models here.


class Options(models.Model):
    A = models.CharField()
    B = models.CharField()
    C = models.CharField()
    D = models.CharField()

    def __str__(self):
        return f'Options {self.id}' #type:ignore

    class Meta:
        verbose_name_plural = "Options"

class Subject(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name
    
class Block(models.Model):
    question = models.CharField()
    Answer = models.CharField()
    options = models.OneToOneField(Options, related_name='options', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='subject', null=True, blank=True)

    def __str__(self):
        return f'Question {self.id}' #type:ignore


    