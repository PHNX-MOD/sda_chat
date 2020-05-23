import json
from threading import Event

from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, 'index.html')


def room(request):
    if request.method == "GET":
        user_name = request.GET.get('user', None)
        if user_name is not None:
            return render(request, 'room.html', {
                'user_name': user_name
            })
    return HttpResponseBadRequest()


signal_condition = Event()

@csrf_exempt
def message_send(request):
    if request.method == "POST":
        message = json.loads(request.body)
        signal_condition.set()
    return HttpResponse()


@csrf_exempt
def message_listener(request):
    if request.method == "GET":
        user_id = request.GET.get('user', None)
        if user_id is not None:
            # Wait for 30 secs
            if signal_condition.wait(30):  # if there is at least one message
                messages = [{'user_id': 'basar', 'message': 'some_message'}]
                return JsonResponse({'messages': messages})
            return HttpResponse(status=503)
    return HttpResponse()
