from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from django.urls import reverse

class Author(models.Model):
    name=models.CharField(max_length=50)
    Img=models.ImageField(upload_to="Blog/AuthorImage/")

    def __str__(self):
        return self.name

class Article(models.Model):
    author=models.ForeignKey(Author,on_delete=models.CASCADE,default=None)
    title=models.CharField(max_length=60)
    slug=models.SlugField(null=True)
    Description=models.CharField(null=True,max_length=100)
    Date=models.DateField(blank=True)
    Content=RichTextField(blank=True,default="Main Blog Content",null=True)    
    CoverImage=models.ImageField(blank=True,upload_to="Blog/CoverImage/")  

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("model_detail" , kwargs={"slug": self.slug})

    
    @property
    def imageurl(self):
        try:
            url=self.CoverImage.url
        except:
            url=''

        return url    

    def show(self):
        return self.author

    def image(self):
        return self.author.Img.url
    
