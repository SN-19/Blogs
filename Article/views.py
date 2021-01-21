from .models import Post,LikeReaction
from Users.models import UserProfile
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from Article.form import BlogForm

def index(request):
   template = loader.get_template('index.html') # getting our template
   return HttpResponse(template.render())       # rendering the template in HttpResponse


def create_post(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog=form.save(commit=False)
            blog.user=UserProfile.objects.get(user=request.user)
            blog.save()
            return HttpResponseRedirect('/index/')
    context = {}
    context['form'] = BlogForm()
    return render(request, "blog-create.html", context)


def list_blog(request):
    blogs = Post.objects.all()
    return render(request, "blog-list.html", {'blogs': blogs})

def view_article(request, id):
    blog=Post.objects.get(id=id)
    like_count = blog.likes if blog.likes > 1 else 0
    userprofile=UserProfile.objects.get(user=request.user)
    liked = True if LikeReaction.objects.get(user=userprofile) else False
    return render(request, "viewblog.html", {'blog': blog,'likecount':like_count,'liked':liked})

@csrf_exempt
def add_likes(request):
    post = request.POST['post-id']
    blog=Post.objects.get(id=int(post))
    user = UserProfile.objects.get(id=1)
    LikeReaction.objects.create(user=user,post=blog)
    return True




