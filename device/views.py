from django.shortcuts import get_object_or_404, render
from device.models import Device


def index(request):
    devices_all = Device.objects.all().order_by('-record_date')
    return render(request, 'device/index.html',
                  {'devices_all': devices_all})


def status(request, survelliance_key):
    requested_device = get_object_or_404(Device, survelliance_key=survelliance_key)
    return render(request, 'device/status.html',
                  {'device_status': requested_device})
