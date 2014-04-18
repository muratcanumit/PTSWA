from django.http import HttpResponse


def index(request):
    return HttpResponse("Aramanin veya urun tipi "
                        "secimi olacak olan sayfa")
