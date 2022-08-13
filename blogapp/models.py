from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    photo = models.ImageField(blank=True, null=True, upload_to='blog_photo')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
