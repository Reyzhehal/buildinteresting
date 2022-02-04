from django.db import models

class Page(models.Model):

    title = models.CharField(max_length=124)

    categories = models.CharField(max_length=120)

    description = models.TextField(null=True, default="Строительство и ремонт.")

    keywords = models.CharField(max_length=120, null=True, default="строительство, ремонт, экономия")

    content = models.TextField()

    image = models.CharField(max_length=100)

    images = models.CharField(max_length=255)

    language = models.CharField(max_length=10, default="ru")

    def __str__(self):
        return self.title