from django.shortcuts import redirect, render
from django.http import HttpResponse
from blog.models import article,Blogcomment
from django.contrib import messages
import random
# Create your views here.

def index(request):
    fullarticle=article.objects.all()
    return render(request,'blog/index.html',{"articles":fullarticle})

def articles(request,slug):
    fullarticle=article.objects.filter(slug=slug).first()
    comments=Blogcomment.objects.filter(post=fullarticle)
    recentarticle = list(article.objects.all())
    my_recentarticle = random.sample(recentarticle, 3)
    if fullarticle != None:
        context = {'article':fullarticle,'comment':comments,"recentblogs":my_recentarticle}
    else:
        messages.error(request, "404 Not found")
        return redirect('/')
    return render(request, 'blog/articles.html',context)

def usercomment(request):
    if request.method == "POST":
        comment=request.POST.get('message')
        name=request.POST.get('name')
        email=request.POST.get('email')
        postSno = request.POST.get('postSno')
        post=article.objects.get(s_no=postSno)
        csave = Blogcomment(comment=comment,name=name,post=post,email=email)
        csave.save()
        messages.success(request, "your comment has been posted successfully")
    return redirect(f'/blog/{post.slug}')