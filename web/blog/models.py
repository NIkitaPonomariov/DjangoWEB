from django.db import models

# Create your models here.
class Post(models.Model):
    theme = models.CharField(max_length=100)
    body = models.TextField()
    createt_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.theme