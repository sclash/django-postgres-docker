from django.db import models


class Author(models.Model):
    name = models.CharField(max_length = 100)

class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='reporter')

    def __str__(self):
        return f"{ self.headline }"

    class Meta:
        ordering = ('headline',)
