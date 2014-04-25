from django.shortcuts import get_object_or_404, render
from device.models import Device


def index(request):
        return render(request, 'device/index.html')


def status(request, survelliance_key):
    requested_device = get_object_or_404(Device, survelliance_key=survelliance_key)
    return render(request, 'device/status.html',
                  {'device_status': requested_device})
