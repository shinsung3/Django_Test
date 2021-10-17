from django.db import models

# Create your models here.

# primary key = id
class Notice(models.Model):
    title = models.CharField(max_length=500, null=True)
    content = models.CharField(max_length=20000, null=True)
    username = models.CharField(max_length=500, null=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title