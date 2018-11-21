from django.http import HttpResponse
from . import models


def index(request):
    posts = ""
    for post in models.Post.objects.all():
        posts += "We posted: " + post.title
        posts += "\n"
    return HttpResponse("Welcome to our blog \n" + posts)