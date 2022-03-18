from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import *


class ArticleListview(ListView):
    queryset=Article.objects.order_by('-id')
    model=Article
    template_name="Blog.html"
    paginate_by = 6

#after slugify 
class ModelNameDetail(DetailView):
    model = Article
    template_name="Blogslug.html"

