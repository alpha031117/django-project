from django.db import models
from django.conf import settings

class Tag(models.Model):
    name = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.name


class Series(models.Model):
    name = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    contributors = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='contributed_posts', blank=True)
    content = models.TextField()
    tags = models.ManyToManyField(Tag)
    series = models.ForeignKey(Series, on_delete=models.CASCADE, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)
    sequence = models.IntegerField(default=1)

    class Meta:
        ordering = ['sequence', '-created_on'] 

    def __str__(self):
        if self.author:
            return f'{self.title} ({self.author})'
        else:
            return f'{self.title}'

    def save(self, *args, **kwargs):
        # Check if there is any existing post with the same sequence
        same_sequence_posts = Post.objects.filter(sequence=self.sequence).exclude(pk=self.pk)
        
        # If there are any posts with the same sequence, increment their sequence by 1
        if same_sequence_posts.exists():
            for post in same_sequence_posts:
                post.sequence += 1
                post.save()

        # Call the original save() method to save the post
        super(Post, self).save(*args, **kwargs)

class PostFile(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_files')
    file = models.FileField(null= True, blank=True, upload_to='uploads/%Y/%m/%d/')

class Comment(models.Model):
    commenter = models.CharField(max_length=100, default="")
    comment_detail = models.TextField(default="")
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.commenter

class ReplyComment(models.Model):
   reply_comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')
   replier_name = models.CharField(max_length=100, default="")
   reply_content = models.TextField()
   replied_date = models.DateTimeField(auto_now_add=True)

   def __str__(self):
       return "'{}' replied with '{}' to '{}'".format(self.replier_name,self.reply_content, self.reply_comment)


