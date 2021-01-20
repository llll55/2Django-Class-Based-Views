from django.shortcuts import render
from .models import Post
from django.views.generic import ListView , DetailView ,CreateView ,UpdateView , DeleteView
# Create your views here.


class PostList(ListView):
    model = Post               ## in template [ object_list , post_list ]
    #context_object_name = 'all_post'
    ordering =['-created_at']
    #queryset = Post.objects.filter(active=True)
    #template_name = 'post/test.html'
    def get_queryset(self):
        return Post.objects.filter(active=True)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myname"] = 'Saleh Mohamad'
        return context
    

class PostDetail(DetailView):
    model = Post



class PostCreate():
    pass



class PostDelete():
    pass




class PostUpdate():
    pass