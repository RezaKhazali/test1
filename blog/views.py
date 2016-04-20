import os
import pdb
import requests

from django.http import Http404
from django.shortcuts import render

from blog.forms import BlogCommentForm
from blog.models import Author, Blog, Entry, BlogComment

def show_blog_entries(request):
	blog = Blog.objects.all()[0]
	entries = Entry.objects.filter(blog=blog).order_by('-pub_date')[:20]

	return render(request, "blogtemplate.html", {
			'blog': blog,
			'entries': entries,
		})

def show_blog_info(request):
	blog = Blog.objects.all()[0]

	return render(request, "bloginfo.html", {
			'blog': blog
		})

def blog_comment(request, blog_id):
	blog_id = int(blog_id)

	try:
		blog = Blog.objects.get(id=blog_id)
	except Blog.DoesNotExist:
		raise Http404

	comments = BlogComment.objects.filter(blog=blog).order_by('-timestamp')

	if request.method == "POST":
		form = BlogCommentNewForm(request.POST)
		if form.is_valid():
			blogcomment = form.save(commit=False)
			blogcomment.blog = blog
			blogcomment.save()
			#blogcomment = BlogComment()
			#blogcomment.blog = blog
			#blogcomment.name = form.cleaned_data['name']
			#blogcomment.comment = form.cleaned_data['comment']
			#blogcomment.save()
	else:
		form = BlogCommentNewForm()

	return render(request, "blog_comment.html", {
			'blog': blog,
			'form': form,
			'comments':comments
		})


def blog_comment_old(request, blog_id):
	blog_id = int(blog_id)

	try:
		blog = Blog.objects.get(id=blog_id)
	except Blog.DoesNotExist:
		raise Http404

	if request.method == "POST":
		name = request.POST.get('name', None)
		comment = request.POST.get('comment', None)

		has_error = False
		error_messages = []

		if not (name and comment):
			has_error = True
			error_messages += ["All fields are required."]
		if name == "Sadjad":
			has_error = True
			error_messages += ["Go away!"]
		if comment and len(comment) < 10:
			has_error = True
			error_messages += ["Your comment is very short!"]

		if not has_error:
			blogcomment = BlogComment()
			blogcomment.blog = blog
			blogcomment.name = name
			blogcomment.comment = comment
			blogcomment.save()

		return render(request, "blog_comment.html", {
					'blog': blog,
					'has_error': has_error,
					'error_messages': error_messages
				})

	return render(request, "blog_comment.html", {
			'blog': blog
		})
