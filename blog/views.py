# Create your views here.
from django.shortcuts import render, render_to_response, RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, Category
# Create your views here.

def home(request):
	return render_to_response("mainblog.html", 
		locals(), 
		context_instance=RequestContext(request))

def all_posts(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 6)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)
 
    return render_to_response('blog/all.html', locals(), context_instance=RequestContext(request))

def category_archive(request, slug):
    category = get_object_or_404(Category, slug=slug)
    categories = Category.objects.all()
    posts = Post.objects.filter(categories=category)
    return render_to_response('blog/category.html', locals(), context_instance=RequestContext(request))