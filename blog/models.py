from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.db import models
from PIL import Image
from django.core.exceptions import ValidationError

BAD_WORDS=['fuck','motherfucker','shit','bullshit','asshole','bastard','slut','fucker','dumbfuck','cocksucker','sucker']
def validate_no_bad_words(content):
    if any([ word in content.lower()  for word in BAD_WORDS ]):
        raise ValidationError("This post contains bad words!!")


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(validators=[validate_no_bad_words])
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image=models.ImageField(null=True,blank=True,upload_to="post_images")
    likes=models.ManyToManyField(User,related_name="blog_posts")
 

    def save(self,*args, **kwargs):
        super(Post,self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        
        output_size = (300, 800)
        img.thumbnail(output_size)
        img.save(self.image.path)
    def total_likes(self):
        return self.likes.count()
    class Meta:
        ordering=["-date_posted"]
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class Message(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    body=models.TextField(max_length=200)
    created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.body[0:20]






