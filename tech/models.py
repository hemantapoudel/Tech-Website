from django.db import models


class Category(models.Model):
    title=models.CharField(max_length=200)
    slug=models.SlugField()

    def __str__(self):
        return self.title

class Subcategory(models.Model):
    title=models.CharField(max_length=200)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    slug=models.SlugField()

    def __str__(self):
        return self.title

class Posts(models.Model):
    title=models.CharField(max_length=500)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    subcategory=models.ForeignKey(Subcategory,on_delete=models.CASCADE)
    feature_image=models.ImageField(upload_to='Images')
    image1=models.ImageField(upload_to='Images',blank=True)
    first_paragraph=models.TextField()
    h1=models.CharField(max_length=500)
    image2=models.ImageField(upload_to='Images',blank=True)
    paragraph1=models.TextField()

    def __str__(self):
        return self.title

