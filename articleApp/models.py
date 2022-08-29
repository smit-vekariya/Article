from django.db import models
from django.contrib.auth.models import User
 
class Tag(models.Model):
    tags=models.CharField(max_length=250)
    def __str__(self):
        return self.tags

class Article(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user',null=True)
    image = models.ImageField(blank=True, upload_to='article_image', null=True)
    title=models.CharField(max_length=100)
    content=models.TextField(max_length=250)
    created_at = models.DateTimeField(null=True,auto_now_add=True)
    tag=models.ManyToManyField(Tag,related_name='tag')
    draft= models.BooleanField(default=False)
   

    def __str__(self):
        return self.title
  



    
