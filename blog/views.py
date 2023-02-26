from django.shortcuts import render
from .models import Post

def home(request):
    context = {
        'posts':Post.objects.all()
    }
    #it means render the home html file for the ""http response
    #context is basically extra optional arguements we pass into the function
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html',{'title':'About'})
