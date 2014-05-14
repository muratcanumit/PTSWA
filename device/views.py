from django.shortcuts import render
from device.models import Device


def index(request):
    return render(request, 'device/index.html')


def status(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        devices = Device.objects.filter(survelliance_key__icontains=q)
        return render(request, 'device/status.html',
                      {'devices': devices, 'query': q})
    else:
        return render(request, '404.html')
