from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path="Projects/img")
    image2 = models.FilePathField(path="Projects/img")
    image3 = models.FilePathField(path="Projects/img")
    image4 = models.FilePathField(path="Projects/img")
    image5 = models.FilePathField(path="Projects/img")


    def __str__(self):
        return self.title
    