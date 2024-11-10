# create datamodels from python users 

from django.shortcuts import render , get_object_or_404
from django.views import View
from .form import PostForm , CommentForm
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt  , csrf_protect # dont need csrf_excmpt 
from django.http import (
HttpResponse , 
HttpResponseBadRequest ,
JsonResponse  , 
HttpRequest
)
from django.shortcuts import render

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


from .models import Post
# this account objects we check 
class AccountPreviews(): # you have to want 
    render_context = {}
    def __init__(self , Username:str , tags = None ) -> None:
        print(Username)
        self.__user = User.objects.get(
                username = Username
            )
        self.render_context[Username] = {
                'info':self.__user.__dict__
            }
        # print(self.render_context)
        self.name = Username
        self.tags = tags # this is object 
        self.form = CommentForm()


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
    def Apply_Queryset(self)->None: 
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
        self.user_name = self.get_the_context_user_name(self.name) #@ this is dict 
        print(self.tags)
        return render(
            request , template_name=self.temp , context= {"USERS":self.user_name , 'name':self.__user , 'form':self.form , 'Posts':Post.objects.filter(author = self.__user , tags__in = self.tags) if self.tags else Post.objects.filter(author = self.__user)}
        
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
    @classmethod 
    def add_context():
        pass


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
from django.contrib.auth.decorators import login_required
from taggit.models import Tag
# this is post froms 
@login_required(login_url='loggin/')
def page_start(requests  , tagsurls = None) -> HttpResponse :
    Username = requests.user # this  is when we loggin 
    form = CommentForm() # we send commend form
    if tagsurls:
        tags_inputer = Tag.objects.get(slug = tagsurls)
        ACpreview = AccountPreviews(Username , tags = tags_inputer)
    else :
        ACpreview = AccountPreviews(Username , )

        ACpreview.Apply_Queryset() # procecings data 
    return ACpreview.views_controll(requests , template_name = 'post.html')

# post id is better 
def like_post(requests , post_id): # api 
    trans = Transmisson.objects.get(post = Post.objects.get(id = post_id))
    trans.like += 1  
    trans.save()
    return HttpResponse('that was like') 


def post_page(requests):  # this is for comment go to the Comment requeir 
    post_from  = PostForm()
    return render(
        requests , 'postings.html' , context= {
            'username':requests.user  , 
            'post_form':post_from , 
        }
    )

from django.shortcuts import redirect 
@require_POST 
def postings_froms(requests :HttpRequest , Username):
    forms = PostForm(requests.POST)
    if forms.is_valid():
        print('This is' , requests.user)
        while requests.user.username != Username :
            return redirect('BLOG:account_page' , requests.user)
        
        models_post_froms = forms.save(commit=False)
        models_post_froms.author = User.objects.get(username = Username)
        models_post_froms.save()
    return redirect(
        'BLOG:account_page'  
    ) # this is for render in render can i 
    
@require_POST # this is  whrn we have just post requests else we have 405 error 
def comment_views(requests:HttpRequest, Username  , post_id):
    form = CommentForm() # this is comment form
    html = """
        %s
    """
    form = CommentForm(
            requests.POST
        )
    if form.is_valid():
        ap_form = form.save(commit=False)
        ap_form.post = Post.objects.get(
            id = post_id
        )
        ap_form.user = User.objects.get(
            username = Username
        ) 
        ap_form.save()
    
     # this is so good for us 
    return  redirect(
        'BLOG:account_page'  
    )




######################################################### here we add api 
# we dont need csrf_token 
from django.http import JsonResponse , Http404
from .models import USERTOKENUDDD , ActionAPITOKEN  # this is from token 

# this is the simple api to do somtinhgs 
# مفهوم api خیلی جالبه باری دنیای وب 
# امنیت خیلی مهمه توی وب 
# cyber security 
@csrf_exempt 
def get_post_by_account(requests:HttpRequest):
    '''  This Is Learn API   '''
    post = {}
    resualt = {'post':post , 'user':None , 'status':None}
    print(requests.POST)
    token_ = requests.POST.get('token') 
    print('tokens')
    # add action 
    if not token_ : 
        raise Http404(f'this token is Post {resualt}')
    else :
        # create a simple acton send 
        user_ = USERTOKENUDDD.objects.get(token = token_).user # this is tokens 
        resualt['user'] = user_.username
        posts = user_.USER_POST.all()
        for i , p in enumerate(posts) : 
            post[str(i)] = {
                'title':p.title , 
                'category':p.category.title , 
                'create_time':p.created , 
                'status':p.status , 
                'body':p.body
                }

        return JsonResponse(resualt)


@csrf_exempt
def test_csfr_my_self(request , Username):
    html =  ['<html>' ,   
        '</html>' ,   
        ]
    str_obj = '<body>'
    USERNAME :iter = User.objects.get(
        username = Username 
    )

    for post in  USERNAME.USER_POST.all(): 
        str_obj += f'<h1>{post.body}</h1><br>'
    str_obj += '</body>'
    html[1] = str_obj
    print(''.join(html))
    return HttpResponse(html)
        

        
from .models import Post

@csrf_exempt
def show_MEHTOD(requests):
    print(requests.GET)
    search = requests.GET.get('qsearch') if requests.GET.get('qsearch') else '*'

    post = Post.objects.filter(title__startswith  = search)
    
    return render(requests , 'FORM.html' , context={'post':post})



# def User_USER_LOGIN(requests:HttpRequest):
#     # create simple commend system auth 
#     if requests.method == 'POST':
#         user = User.objects.get(username = requests.POST['username'])
#         return redirect(
#         'BLOG:account_page' , user.username 
#             ) # this is for render in render can i 
        
#     else : 
#         return render(requests , 'login.html')

from taggit.models import Tag
def hash_tak_post(requests , slug):
    post = Post.objects.filter(
        tags__in = [Tag.objects.get(slug=slug)]
    )
    return render(
        requests  , 
        'hashtakpost.html' ,
        context={
            'posts':post , 'name':slug , 
        }
    )
from django.urls import reverse
from django.http import BadHeaderError
@csrf_exempt
def test_my_csrf_token(requests:HttpRequest):
    # if 'csrf' not in requests.POST :
    #     raise BadHeaderError('Csrf Error')
    print(requests.POST.get('name'))
    print(requests.POST.get('family'))


    return render(requests , 'testcsrf.html' , context={'urls':reverse('BLOG:TEST_CSRF')}
       
) # this is so Good 

from .form import SearchPostForm 
from django.contrib.postgres.search import SearchVector
# using orms # databasese 
def search_from_post(requests:HttpRequest):
    context = {
        'form':SearchPostForm , 
        'posts':[] , 
    }
    if 'values' in requests.GET:
        context['posts'] = Post.objects.annotate(
            search = SearchVector('title' , 'body' , 'author__username' ,)
        ).filter(
            search = requests.GET.get('values')
        )

   
    return render(
            requests , 'search.html' , context= context
        )


### loggin view profcecings 

from django.contrib.auth import login , authenticate , logout


def loggin_user(requests:HttpRequest):
    "This is for login user creator"
    not_log = True
    if requests.method =='POST':
        username , password = requests.POST['username'] , requests.POST['password']
        try : 
            login(requests , authenticate(username = username  , password=password))
            return redirect('BLOG:account_page')
        except : 
            not_log = False


    return render(requests,'login.html' , context={'is_log':not_log})


def logout_user(requests:HttpRequest):
    logout(
        requests
    )
    return redirect(
        'BLOG:loggin_page'
    )

# for traning rendering in the self page 

# get user models 
# create user models # authtication 

from django.contrib.auth.models import User
def sign_in(requests:HttpRequest)->HttpResponse:
   
    is_false_password = None
    is_user_in = None
    if requests.method == "POST":
        if requests.POST['psw']==requests.POST["psw-repeat"]:
            is_false_password = True
            return redirect('BLOG:sign_in')
        

        else : 
            is_false_password = True
            # check user 
            if User.objects.filter(username=requests.POST["user"]).exists() :
                is_user_in  = True
                return redirect('BLOG:sign_in')
            else :
                User.objects.create_user( 
                    username= requests.POST['user'] , password =requests.POST["psw"]
                )
                return redirect('BLOG:account_page')
    
    
    
    return render(
        requests , 'signin/signin.html' , context={
            'status_password':is_false_password , 
            'status_user':is_user_in , 
        }
    )

# this is if she is authintacted we create # hello world 

# create the account users from pagnations 
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
# create the app for loggin here is beeter 
@login_required(login_url='loggin/')
def account_page(request:HttpRequest , Username)->HttpResponse:

    if request.user  == get_object_or_404(
        User , 
        username = Username
    ) : 
        return redirect('BLOG:account_page')
    else : 
        apply_user = AccountPreviews(
            Username 
        )
        # send to nother server 
        apply_user.Apply_Queryset()
        return apply_user.views_controll(
            request , template_name = 'profiles.html'
        )
    