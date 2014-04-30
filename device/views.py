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

"""
 def status(request):
    survelliance_key = request.POST.get('survelliance_key')
    results = get_object_or_404(Device, survelliance_key=survelliance_key)
    template = loader.get_template()
    context = Context({'survelliance_key': survelliance_key, 'results': results})
    response = template.render(context)
    return HttpResponse(response)
"""


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

"""
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
            return render(request, 'device/not_valid.html')
    else:
        form = SearchForm()
        return redirect('/')

        else:
            return HttpResponseRedirect('/')

"""
