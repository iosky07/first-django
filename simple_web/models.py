from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    thumbnail = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Tag(models.Model):
    title = models.CharField(max_length=255)

class BlogDetail(models.Model):
    blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE)
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE)

class Comment(models.Model):
    blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True)
    value = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


