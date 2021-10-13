from django.shortcuts import render
from django.http import *
from blog.models import User
import markdown

# Create your views here.

#def index(request):
#	return HttpResponse("Katharine, welcome back! Coding is always here")

# 主页（近期文章）	
def index(request):
#	result = {}
#	try:
#		post = Article.objects.filter(visible=True).order_by('-update_time')[0: 10]
#		result.update({'result': post})
#	except Article.DoesNotExist:
#		result.update({'result': 'No Result!'})
#	return render(request, 'blog/index.html', result)
	return render(request, 'blog/index.html')


# 文章页（列表）
def category(request, category):
	result = {}
	try:
		post = Article.objects.filter(category=category, visible=True).order_by('-update_time')
		result.update({'result': post})
	except Article.DoesNotExist:
		result.update({'result': 'No Result!'})
	return render(request, 'blog/category.html', result)

# 文章详情页
def detail(request, title):
	try:
		post = Article.objects.get(title=title)
		if post.visible == True:
			# 将markdown语法渲染成html样式(包括缩写表格和语法高亮等常用扩展)https://www.dusaiphoto.com/article/20/
			post.content = markdown.markdown(post.content,extensions=['markdown.extensions.extra','markdown.extensions.codehilite',])
			return render(request, 'blog/article.html', {'post': post})
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

