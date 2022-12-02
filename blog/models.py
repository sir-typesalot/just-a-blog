from django.db import models

class Post(models.Model):
    title = models.CharField('title of the post', max_length=250)
    subtitle = models.CharField(max_length=250)
    content = models.TextField()
    date_created = models.DateTimeField('date created', auto_now_add=True)

    def __str__(self):
        return self.title

class ContentTags(models.Model):
    tag_name = models.CharField('name of the tag', max_length=250)
    description = models.CharField('short description of tag', max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tag_name

class TagMap(models.Model):
    tag_id = models.ForeignKey(ContentTags, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
