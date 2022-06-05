from django.db import models
from django.utils import timezone

'''
Klasa dziedziczy po klasie frameworka Django, reprezentuje wpis na stronie
'''
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(blank=True, null=True)

    #Metoda przypisuje postowi aktualną datę jego publikacji
    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    #Metoda zwraca tytuł postu
    def __str__(self):
        return self.title
