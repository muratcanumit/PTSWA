from django.template import Context, loader
from django.http import HttpResponse
from desktop.models import Desktop


def desktoplist(request):
    latest_products = Desktop.objects.all().order_by('-delivery_date')
    t = loader.get_template('desktop/productlist.html')
    c = Context({
        'latest_products': latest_products,
    })
    return HttpResponse(t.render(c))
