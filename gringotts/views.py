from django.http import HttpResponse


def home(request):
    return HttpResponse(status=200)
