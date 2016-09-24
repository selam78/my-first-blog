from django.db import models
from django.utils import timezone

# Create your models he
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_data = models.DateTimeField(blank=True, null=True)


    def publish(self):
        self.publish_date = timezone.now()
        self.save()


    def __str__(self):
        return self.title
