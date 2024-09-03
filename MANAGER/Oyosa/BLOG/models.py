from django.db import models
from django.utils.translation import gettext as _  # this is for tranlations 
from django.conf import settings 
from django.db import models
from django.utils import timezone # this is the datetime 
from django.contrib.auth.models import User
# Create your models here.
# this is about weh nwe change User
class Category(models.Model):
    title = models.CharField(
        max_length=255 , verbose_name=_('title')
    )
    is_active = models.BooleanField(
        verbose_name=_("is activate Category")  , 
        blank= False
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL # USER 
    )
    


class Post(models.Model):
    class Status(models.TextChoices): # this is choices users 
        DRAFT = 'DF', _('Draft')
        PUBLISHED = 'PB', _('Published')
    title = models.CharField(max_length=250 , verbose_name=_("title") , blank=False) # har title dashte bashe 
    slug = models.SlugField(max_length=250  , verbose_name=_("slug"))
    # this is Foreignkey to the 
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='blog_posts' , 
        verbose_name=_("User") , 
        help_text=_("this is the user include")
    )
    category  = models.ForeignKey( # this is for category 
        Category , on_delete=models.DO_NOTHING
    )
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
    max_length=2,
    choices=Status,
    default=Status.DRAFT
    )

# simple Foring key 
class Media(models.Model):
    post = models.ForeignKey(
        Post , on_delete=models.CASCADE , verbose_name=_("Post")
    )
    title = models.CharField(max_length=255 , verbose_name=_('title media'))
    is_ruls = models.BooleanField(blank=False)
    

class Transmisson(models.Model):
    post = models.ForeignKey(
        Post , on_delete=models.CASCADE , verbose_name=_("Post")
    )
    like = models.BigIntegerField(verbose_name=_('like'))
    dislike = models.BigIntegerField(verbose_name=_('dslike'))
    share = models.BigIntegerField(verbose_name=_('share'))


class Commants(models.Model):
    class TypeComment(models.TextChoices):
        PR = 'PRIVATE' , _('private')
        PB = 'PUBLIC' , _('public')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='blog_posts' , 
        verbose_name=_("User off comments") , 
        help_text=_("this is the user include")
    )
    post = models.ForeignKey(
        Post , on_delete=models.CASCADE , verbose_name=_("Post")
    )
    TEXT = models.TextField(max_length=1000 ,
    blank= False , verbose_name=_("text"))
    like = models.BigIntegerField(max_length=255)
    dilike = like = models.BigIntegerField(max_length=255)
    report = models.CharField(max_length=155)
    media = models.FileField() # this is for comment like gif 
    type_commant = models.CharField(
        max_length=2 , 
        choices=TypeComment , 
        default=TypeComment.PR , 
        verbose_name=_("typeoff commant")
    )
# the simple system design for all person 
class TAGS(models.Model):
    name_tags = models.CharField(max_length=120 ,  verbose_name=_("typeoff commant"))
    post = models.ManyToManyField(
        Post
    )
    followings = models.BigIntegerField(
    )


class Followers(models.Model):
    followers = models.ManyToManyField(
        settings.AUTH_USER_MODEL
    )
    time_add =models.DateTimeField(auto_now_add=True)



class Following(models.Model):
    Following = models.ManyToManyField(
        settings.AUTH_USER_MODEL
    )
    time_add =models.DateTimeField(auto_now_add=True)
