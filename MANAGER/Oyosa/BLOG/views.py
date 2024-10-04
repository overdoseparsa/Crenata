from django.shortcuts import render , get_object_or_404
from django.views import View


from django.http import (
HttpResponse , 
HttpResponseBadRequest ,
JsonResponse  , 
HttpRequest
)


from django.contrib.auth.models import User

from .models import (
    Transmisson , 
    Post
)

def Post_details(Post_objects):
    
    return {
        'object':Post_objects , 
        'info':{
            Post_objects.__dict__
        } , 
        'media':Post_objects.POST_MEDIA.all() ,  
        'Comment':Post_objects.POST_COMMENTS.all(),
        'tags':Post_objects.POST_TAGS.all() , 

    }
# first 

class AccountPreviews():
    render_context = {}
    def __init__(self , Username:str ) -> None:
        print(Username)
        self.__user = User.objects.get(
                username = Username
            )
        self.render_context[Username] = {
                'info':self.__user.__dict__
            }
        # print(self.render_context)
        self.name = Username




    def __repr__(self) -> str:
        # self.iter_info  = self.__user.value()
        return f'{type(self).__name__}({self.name!r})'
    def __str__(self) -> str:
        return self.name
    def __iter__(self)->iter : 
        return iter(
            self.__user
        )
    # this is majic mehtodes we use them 
    # the rndering data is not good for us
    def Apply_Queryset(self): 
        """  this is for addings json to query sets """
        self.render_context[self.name]['post'] = self.__user.USER_POST.all()
        
        print()
        self.render_context[self.name]['followers'] = [
            self.__user.User_FOLLOWER.all()
        ]
        self.render_context[self.name]['following'] = [
            self.__user.USER_FOLLOWING.all()
        ]
        
    def views_controll(self , request:HttpRequest , *args , **kwargs) -> HttpResponse:
        """  this is just for get  """
        
        self.temp : dict|None = self.check_error(kwargs , 'template_name') or args[0]      
        assert self.temp  , 'add your templates to render'
        self.user_name = self.get_the_context_user_name(self.name)
        return render(
            request , template_name=self.temp , context= self.user_name
        )
    @classmethod
    def get_the_context_user_name(cls , username):
        print(cls.render_context)
        return cls.check_error(cls.render_context , username)
    @staticmethod
    def check_error(kwargs , values):
        try:
            print('this is for render dict' , kwargs[values])
            return kwargs[values]
        except :
            return 0 
        # i use for just import 


"""

{
    'parsa':{
        'post:[
            {} , {} , {}
        ]
        'followers':{}
        'followings':{} , ...
    
    }
}

"""
def page_start(requests , username) -> HttpResponse :
    ACpreview = AccountPreviews(username)
    ACpreview.Apply_Queryset() # procecings data 
    return ACpreview.views_controll(requests , template_name = 'post.html')

# post id is better 
def like_post(requests , post_id):
    trans = Transmisson.objects.get(post = Post.objects.get(id = post_id))
    trans.like += 1  
    trans.save()
    return HttpResponse('that was like')