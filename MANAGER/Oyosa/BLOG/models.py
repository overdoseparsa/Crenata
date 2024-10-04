from django.db import models
from django.utils.translation import gettext as _  # this is for tranlations 
from django.conf import settings 
from django.db import models
from django.utils import timezone # this is the datetime 
from django.contrib.auth.models import User # this is when i want have test or use simple user of django 
from django.conf import settings 
from django.contrib.auth import get_user_model
from django.urls import reverse 
# we change get_user_models
# install postgress 
# Create your models here.
# this is about weh nwe change User

# grop for all 
# grop for my 
# use relatede name for the databases ... iner join 
# class Profile(models.Model):
#     User = models.OneToOneField(
#         User , related_name='User_profiles'
#     )
#     # editable add for profiles 

class Category(models.Model):
    title = models.CharField(
        max_length=255 , verbose_name=_('title')
    )
    is_active = models.BooleanField(
        verbose_name=_("is activate Category")  , 
        blank= False
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL , on_delete=models.CASCADE
        # USER  
    )
    
    followers_katalog = models.ManyToManyField(
        User , related_name="followers_katalog_user"
    )

    def __str__(self) -> str:
        return f'{self.title}'

class Post(models.Model):
    class Status(models.TextChoices): # this is choices users 
        DRAFT = 'DF', _('Draft')
        PUBLISHED = 'PB', _('Published')
    title = models.CharField(max_length=250 , verbose_name=_("title") , blank=False) # har title dashte bashe 
    slug = models.SlugField(
            max_length=250  ,
            verbose_name=_("slug") , 
            allow_unicode=True , 
            unique_for_date='publish'
             )
    # this is Foreignkey to the 
    author = models.ForeignKey(
        get_user_model(), # this is return seetings models 
        on_delete=models.CASCADE,
        verbose_name=_("User") , 
        help_text=_("this is the user include") , 
        related_name='USER_POST'
    )
    category  = models.ForeignKey( # this is for category 
        Category , on_delete=models.DO_NOTHING , 
        related_name="CATEGORY_POST" , 
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
    class Meta:
        ordering = [
            '-created'
        ]
        indexes = [
            models.Index(fields=['-author'])
        ]
        verbose_name = _("Post")

    def __str__(self) -> str:
        return ' id is %i %s  --  %s '%(self.id,self.title , self.created.strftime('%y/%m/%d -- %H:%M-%S'))
    # time_publishd = models.DateTimeField(
    #     default=timezone.now # we change from settings settings of time 
    # )
    #   this is re
    def append_urls_like(self):
        return reverse(
            'like_post' , 
            kwargs={
                'post_id':self.id

            }
        )




class Media(models.Model):
    post = models.ForeignKey(
        Post , on_delete=models.CASCADE , verbose_name=_("Post") , related_name='POST_MEDIA'
    )
    title = models.CharField(max_length=255 , verbose_name=_('title media'))
    is_ruls = models.BooleanField(blank=False)
    path = models.FileField()
    def __str__(self) -> str:
        return f'path : %s'%self.path
    class Meta:
        ordering = [
            'post'
        ]
        indexes = [
            models.Index(fields=['post'])
        ]

class Transmisson(models.Model):
    post = models.ForeignKey(
        Post , on_delete=models.CASCADE , verbose_name=_("Post") ,related_name='POST_TRANS'
    )
    like = models.BigIntegerField(verbose_name=_('like'))
    dislike = models.BigIntegerField(verbose_name=_('dslike'))
    share = models.BigIntegerField(verbose_name=_('share'))

    def __str__(self) -> str:
        return  f'{type(self).__name__} \'{self.post!r}\''
    class Meta:
        ordering = [
            'post'
        ]
        indexes = [
            models.Index(fields=['post'])
        ]

class Commants(models.Model):
    class TypeComment(models.TextChoices):
        PRIVATE = 'PR' , _('private')
        PUBLIC = 'PB' , _('public')
    user = models.ForeignKey( # we dont need related name for this 
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        verbose_name=_("User off comments") , 
        help_text=_("this is the user include") ,  
        
        
    )
    post = models.ForeignKey(
        Post , on_delete=models.CASCADE , verbose_name=_("Post")  , related_name="POST_COMMENTS"
    )
    TEXT = models.TextField(max_length=1000 ,
    blank= False , verbose_name=_("text"))
    like = models.BigIntegerField()
    dilike = models.BigIntegerField()
    report = models.CharField(max_length=155)
    media = models.FileField() # this is for comment like gif 
    type_commant = models.CharField(
        max_length=2 , 
        choices=TypeComment , 
        default=TypeComment.PRIVATE , 
        verbose_name=_("type of commant")
    )
    commented_time = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return "%s %s from the post id of %i "%(self.user , self.TEXT ,  self.post.id)
    class Meta:
        ordering = [
            'post'
        ]
        indexes = [
            models.Index(fields=['post'])
        ]
        
# the simple system design for all person 
class TAGS(models.Model):
    name_tags = models.CharField(max_length=120 ,  verbose_name=_("typeoff commant"))
    post = models.ManyToManyField(
        Post , related_name="POST_TAGS"
    )
    followings_len = models.BigIntegerField(
    )
    tags_followers = models.ManyToManyField(
        User
    )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.name_tags}'

# it changes feom git
class Followers(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE ,related_name='USER_FOLLOWING')

    followers = models.ManyToManyField(
        settings.AUTH_USER_MODEL
    )
    time_add =models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return f'{self.time_add}'

    def __str__(self) -> str:
        return super().__str__()

class Following(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE ,related_name=f'User_FOLLOWER')
    Following = models.ManyToManyField(
        settings.AUTH_USER_MODEL
    )
    time_add =models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return f'{self.time_add}'

# class GroupLevelPost(models.Model):
#     name = models.CharField(max_length=100 , blank=False , verbose_name=_("titlegroub"))
#     uudi = models.UUIDField()
#     posts = models.ManyToManyField(Post)

# class GroupAccount(models.Model):
#     name = models.CharField(max_length=100 , blank=False , verbose_name=_("titlegroub"))
#     uudi = models.UUIDField()
#     accounts = models.ManyToManyField(User)
# # migrate 
