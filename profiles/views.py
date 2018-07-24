from django.shortcuts import render
from authentication.models import Profile
from django.contrib.auth.models import User
from django.http import Http404
from django.contrib.auth.decorators import login_required


def user_profile(request, id):

	"""Individual user's profile page."""

	try:
		user = User.objects.get(id=id)
	except:
		raise Http404("User does not exist.")

	context = {'user': user}

	return render(request, "profiles/profile.html", context)





