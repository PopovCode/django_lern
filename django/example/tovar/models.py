from django.db import models

# Create your models here.


class tovar(models.Model):
    title = models.CharField(max_length=255, unique=True)
    article = models.CharField(max_length=16, null=True, blank=True, unique=True)
    description = models.TextField(null=True, blank=True)
    quantity = models.PositiveIntegerField(default=0, blank=True)

    def __str__(self):
        if self.article is None:
            return('{1} (---) {0}'.format(self.title, self.pk))
        else:
            return('{2} ({0}) {1}'.format(self.article, self.title, self.pk))