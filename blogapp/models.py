from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    photo = models.ImageField(blank=True, null=True, upload_to='blog_photo')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    # 다른 모델 객체를 참조할 수 있는 foreignkey
    # on_delete를 통해 참조하는 객체가 삭제되면 같이 삭제 되도록 함
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment
