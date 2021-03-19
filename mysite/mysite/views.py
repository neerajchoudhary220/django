from django.http import HttpResponse
def index(request):
    return HttpResponse("<h1>Hello</h1><a href='about'>about</a>")

def about(request):
    return HttpResponse("<h1>About</h1>")