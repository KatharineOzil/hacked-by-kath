from django.shortcuts import render
from django.http import *
from blog.models import User, Article, Category, Todo
import markdown

# Create your views here.

#def index(request):
#	return HttpResponse("Katharine, welcome back! Coding is always here")

# 主页（近期文章）	
def index(request):
	result = {}
	try:
		post = Article.objects.filter(visible=True).order_by('-update_time')[0:5]
		result.update({'article': post})
		#category = Article.objects.filter(visible=True).order_by('category').distinct()
		#return_result.update({'category': category})
	except Article.DoesNotExist:
		result.update({'article': 'No Result!'})
	return render(request, 'blog/index.html', result)


# 文章页（列表）；archive页面包括所有文章（按照category排列）。TODO：category可点击进入每个分类下的文章
def archive(request):
	return_result = {}
#	category = Category.objects.all()
#	return_result.update({'category': category})
	category_distinct = []
	try:
		post = Article.objects.filter(visible=True).order_by('-create_time')
		return_result.update({'article': post})
		category = list(Article.objects.filter(visible=True).values_list("category__category").distinct().order_by('-create_time'))
		for index in range(len(category)):
			category_distinct.append(str(category[index]).replace(',','').replace("'","").replace('(','').replace(')',''))
		return_result.update({'category': category_distinct})
	except Article.DoesNotExist:
		return_result.update({'article': 'No Result!'})
	return render(request, 'blog/archive.html', return_result)

# category页 (pass)
def category(request, category):
	result = {}
	try:
		post = Article.objects.filter(category=category, visible=True).order_by('-update_time')
		result.update({'result': post})
	except Article.DoesNotExist:
		result.update({'result': 'No Result!'})
	return render(request, 'blog/category.html', result)

# 文章详情页
def detail(request, id):
	try:
		context = {}
		post = Article.objects.get(id=id)
		if post.visible == True:
			# 将markdown语法渲染成html样式(包括缩写表格和语法高亮等常用扩展)https://www.dusaiphoto.com/article/20/
			post.content = markdown.markdown(post.content.replace('\r\n','\n'), extensions=['markdown.extensions.extra','markdown.extensions.codehilite','markdown.extensions.toc'])
			context['post'] = post
			return render(request, 'blog/article.html', context)
		else:
			return render_to_response('blog/404.html', {})
	except Article.DoesNotExist:
		return render_to_response('blog/404.html', {})

# 个人简介
def aboutme(request):
	context = {}
	personal = User.objects.get()
	personal.intro = markdown.markdown(personal.intro.replace('\r\n','\n'), extensions=['markdown.extensions.extra','markdown.extensions.codehilite','markdown.extensions.toc'])
	context['personal'] = personal
	return render(request, 'blog/aboutme.html', context)

def page_not_found(request, exception):
	return render(request, 'blog/404.html')

def server_error(request):
	return render(request, 'blog/500.html')

def page_forbidden(request, exception):
	return render(request, 'blog/403.html')

def bad_gateway(request):
	return render(request, 'blog/502.html')
