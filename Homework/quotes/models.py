from django.db import models

# Create your models here.
class Author(models.Model):
    fullname = models.CharField(max_length=100)
    born_date = models.CharField(max_length=100)
    born_location = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.fullname
    
class Tag(models.Model):
    tag = models.CharField(max_length=100)
    def __str__(self):
        return self.tag


class Quote(models.Model):
    text = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.text[:20]