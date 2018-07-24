from django.shortcuts import render
from authentication.models import Profile
from blog.models import Post, Category
from django.contrib.auth.models import User
from django.http import Http404
from django.contrib.auth.decorators import login_required


def user_profile(request, id):

	"""Individual user's profile page."""

	try:
		user = User.objects.get(id=id)
	except:
		raise Http404("User does not exist.")

	user_posts = Post.objects.filter(author=user)

	context = {'user': user,
			   'user_posts': user_posts}

	return render(request, "profiles/profile.html", context)





