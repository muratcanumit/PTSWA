from django.http import HttpResponseRedirect, HttpResponse
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response, get_object_or_404, render
from django.template import RequestContext
from device.models import Device
from device.forms import SearchHistoryForm
from django.http import HttpResponse
from django.template import loader, Context
from django.views.generic import list_detail


def index(request):
        return render(request, 'device/index.html')


def status(request):
    c = RequestContext(request, {})
    c.update(csrf(request))

    if request.POST:
        form = SearchHistoryForm(request.POST)
        c.update(locals())
        if form.is_valid():
            survelliance_key = request.POST.get('survelliance_key')
            device = get_object_or_404(Device,
                                       survelliance_key=survelliance_key)
            return render_to_response('device/status.html',
                                      {'device': device})
        else:
            return HttpResponseRedirect('/')
    else:
        form = SearchHistoryForm()
        c.update(locals())
        return HttpResponseRedirect('/')
