from django.shortcuts import render,redirect
from django.views.generic import View
from .models import Post
from .forms import PostCreateForm


class BloglistView(View):
    def get(self,request,*args, **kwargs):
        context = {
           'lista_post': Post.objects.all()
        }
        return render(request, 'blog.html',context)
    

class BlogCreateView(View):
    def get(self,request, *args,**kwargs):
        form=PostCreateForm
        context={
           'form':form
        }
        return render(request, 'blog_create.html',context)
    
    def post(self,request, *args,**kwargs):

        if request.method == 'POST':
            form =  PostCreateForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data.get('title')
                content = form.cleaned_data.get('content')
                form.save() 
                return redirect('blog:home')

        context={

        }
        return render(request, 'blog_create.html',context)
    