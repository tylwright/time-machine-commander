from django.shortcuts import render_to_response


def index(request):
    return render_to_response('home.html', locals())


def login(request):
    return render_to_response('login.html', locals())
