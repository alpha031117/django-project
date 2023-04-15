from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.name


class Series(models.Model):
    name = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.name


class Post(models.Model):

    # fields name = field type & its attributes

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    content = models.TextField()
    tags = models.ManyToManyField(Tag)
    series = models.ForeignKey(Series, on_delete=models.CASCADE, default="")

    def __str__(self):
        if self.author:
            return f'{self.title} ({self.author})'
        else:
            return f'{self.title}'


class Comment(models.Model):
    commenter = models.CharField(max_length=100, default="")
    comment_detail = models.TextField(default="")
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.commenter


