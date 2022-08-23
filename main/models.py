from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField

# Create your models here.

class Skill(models.Model):

    name = models.CharField(max_length=20,null=True,blank=True)
    score = models.IntegerField(default=80,null=True,blank=True)
    image = models.FileField(blank=True,null=True,upload_to='skills')
    is_key_skill = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:

        verbose_name_plural = 'Skills'
        verbose_name = 'Skill'


class Profile(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatar',blank=True,null=True)
    title = models.CharField(max_length=200,null=True,blank=True)
    bio = models.TextField(null=True,blank=True)
    cv = models.FileField(null=True,blank=True,upload_to='cv')
    skills = models.ManyToManyField(Skill,blank=True)

    def __str__(self):
        return f'{User.first_name} {User.last_name}'

    class Meta:
        verbose_name_plural = 'User Profiles'
        verbose_name = 'User Profile'


class ContactProfile(models.Model):

    time = models.DateTimeField(auto_now_add=True)
    name = models.CharField(verbose_name='Name',max_length=100)
    message = models.TextField(verbose_name='Message')
    email = models.EmailField(verbose_name='Email')

    class Meta:

        verbose_name_plural = 'Contact Profiles'
        verbose_name = 'Contact Profiles'
        ordering = ['time']

    def __str__(self):
        return f'{self.name}'


class Testimonial(models.Model):

    is_active = models.BooleanField(default=True)
    thumbnail = models.ImageField(blank=True,null=True,upload_to='thumbnail')
    name = models.CharField(max_length=100,null=True,blank=True)
    role = models.CharField(max_length=100,null=True,blank=True)
    quote = models.CharField(max_length=100,null=True,blank=True)

    class Meta:

        verbose_name_plural = 'Testimonials'
        verbose_name = 'Testimonial'
        ordering = ['name']

    def __str__(self):
        return self.name


class Media(models.Model):

    url = models.URLField(blank=True,null=True)
    is_image = models.BooleanField(default=True)
    image = models.ImageField(blank=True,null=True,upload_to='media')
    name = models.CharField(blank=True,max_length=100,null=True)


    class Meta:
        verbose_name_plural = 'Media Files'
        verbose_name = 'Media'
        ordering = ['name']

    def save(self,*args,**kwargs):
        if self.url:
            self.is_image = False
        super(Media,self).save(*args,**kwargs)

    def __str__(self):
        return self.name


class Portfolio(models.Model):

    class Meta:
        verbose_name_plural = 'Portfolio Profiles'
        verbose_name = 'Portfolio'
        ordering = ['name']

    date = models.DateTimeField(blank=True,null=True)
    name = models.CharField(blank=True,max_length=100,null=True)
    description = models.CharField(blank=True,max_length=500,null=True)
    slug = models.SlugField(blank=True,null=True)
    is_active = models.BooleanField(default=True)
    body = RichTextField(blank=True,null=True)
    image = models.ImageField(blank=True,null=True,upload_to='portfolio')


    def save(self,*args,**kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        # super(Portfolio,self).save(*args,**kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/portfolio/{self.slug}'


class Blog(models.Model):

    class Meta:
        verbose_name_plural = 'Blog Profiles'
        verbose_name = 'Blog'
        ordering = ['date']

    date = models.DateTimeField(blank=True,null=True)
    name = models.CharField(blank=True,max_length=100,null=True)
    description = models.CharField(blank=True,max_length=500,null=True)
    slug = models.SlugField(blank=True,null=True)
    is_active = models.BooleanField(default=True)
    body = RichTextField(blank=True,null=True)
    image = models.ImageField(blank=True,null=True,upload_to='blog')


    def save(self,*args,**kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        # super(Blog,self).save(*args,**kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blog/{self.slug}'



class Certificate(models.Model):
     class Meta:
         verbose_name_plural = 'Certificates'
         verbose_name = 'Certificate'

     name = models.CharField(blank=True, max_length=100, null=True)
     date = models.DateTimeField(blank=True, null=True)
     description = models.CharField(blank=True, max_length=500, null=True)
     title = models.CharField(blank=True, max_length=50, null=True)
     is_active = models.BooleanField(default=True)

     def __str__(self):
         return self.name

