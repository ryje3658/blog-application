from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from .models import Post, Category
from .forms import ContactForm, CreatePostForm
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import RequestContext
from django.core.mail import send_mail
from django.http import Http404, HttpResponseRedirect, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import datetime


def index(request):

    post_list = Post.objects.all()[::-1]
    paginator = Paginator(post_list, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    context = {'posts': posts,
    		   'title': 'Main Content'}

    return render(request, 'blog/index.html', context)

def about(request):

	"""About page. Mostly static HTML content."""

	context = {'title' : 'About'}

	return render(request, 'blog/about.html', context)


def contact(request):

	"""Contact Me page which allows user to 
	fill out a contact form which will be sent
	to below email."""

	form = ContactForm()

	context = {'form' : form,
			   'title' : 'Contact',}

	if request.method == 'POST':
		form = ContactForm(request.POST)

		if form.is_valid():

			name = form.cleaned_data['name']
			message = form.cleaned_data['message']
			sender = form.cleaned_data['email']

			form.save()
			messages.success(request, "Thank you, I'll get back to you as soon as possible!")

			send_mail(
			    'Contact Me DjangoBlog from {}'.format(name),
			    '{} from {}'.format(message, sender),
			    'jensenmryan@gmail.com',
			    ['ryanjensenn@gmail.com'],
			    fail_silently=False,)

		else:			
			messages.warning(request, "Error! Please submit a valid email!")

		return render(request, 'blog/contact.html', context)

	return render(request, 'blog/contact.html', context)

def post(request, pk):

	"""Page for an individual blog post,
	located using the post's primary key."""
	try:
		post = Post.objects.get(pk=pk)
	except:
		raise Http404("No post found.")

	context = {'post' : post,
			   'title' : post.title}

	return render(request, 'blog/post-image.html', context)

def individual_category(request, category):

	"""Displays an index page with only posts
	from the selected category."""

	posts = Post.objects.filter(category__title__contains=category)[::-1]

	context = {'posts': posts,
			   'title' : category.title}

	return render(request, 'blog/index.html', context)

def search(request):

	"""Search functionality, allows user to search
	for keyword in blog title or blog body."""

	query = request.GET.get('q')

	if query:	
		result_list = Post.objects.filter(Q(title__icontains=query) | Q(body__icontains=query))
		paginator = Paginator(result_list,10)

		page = request.GET.get('page')
		results = paginator.get_page(page)

	context = {'results': results,
			   'title': 'Results',
			   }

	return render(request, 'blog/index.html', context)

def archive(request):

	"""Contains an archive of all blog posts.
	sorted by year and date. Clicking on a month/year
	will return a list of all posts from that time."""

	month_dict = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 
				  'May': 5, 'Jun': 6, 'Jly': 7, 'Aug': 8, 'Sep': 9, 
				  'Oct': 10, 'Nov': 11, 'Dec': 12}

	for month, value in month_dict.items():

		month_dict[month] = Post.objects.filter(created_at__month=value)

	context = {'title': 'Archive',
			'month_dict': month_dict,}

	return render(request, 'blog/archive.html', context)

@login_required
def createpost(request):
	form = CreatePostForm(request.POST or None, request.FILES or None)
	if form.is_valid():

			title = form.cleaned_data['title']
			body = form.cleaned_data['body']
			category = form.cleaned_data['category']
			image = form.cleaned_data['image']
			created_at = datetime.datetime.now()

			completed_form = form.save(commit=False)
			completed_form.author = request.user
			completed_form.save()


			messages.success(request, "Post posted!")


	context = {'form': form}

	return render(request, 'blog/create_post.html', context)

def updatepost(request, pk=None):
	
	try:
		instance = Post.objects.get(pk=pk)
	except:
		raise Http404("Sorry!")

	form = CreatePostForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		form.save()
		messages.success(request, "Post updated!")
		return render(request, 'blog/index.html')

	context = {
		"form": form,
		"instance": instance,
		"pk": pk,
	}

	return render(request, 'blog/update_post.html', context)

def deletepost(request, pk):

	post = Post.objects.get(pk=pk)

	if request.user == post.author:
		post.delete()
		messages.success(request, "Post deleted!")
	else:
		messages.success(request, "No!")

	return render(request, 'blog/index.html')






