from django.shortcuts import render, redirect, get_object_or_404
from device.models import Device
from device.forms import SearchForm
from django.contrib import messages
from django.utils.translation import ugettext as _


def index(request):
        return render(request, 'device/index.html')


def status(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            survelliance_key = request.POST.get('survelliance_key')
            req_device = get_object_or_404(Device,
                                           survelliance_key=survelliance_key)

            if req_device is not None:
                return render(request, 'device/status.html',
                                       {'req_device': req_device})
            else:
                messages.error(
                    request,
                    _('Invalid Survelliance Key : Device does not Exist!')
                )
                return redirect('/')
    else:
        form = SearchForm()
        return redirect('/')
