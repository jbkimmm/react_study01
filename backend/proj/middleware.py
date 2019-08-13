from django.db.models import Model
from django.db.models.query import QuerySet
from django.http import HttpResponse
from .utils.json import json_response


def JsonResponseMiddleware(get_response):
    def middleware(request):
        response = get_response(request)
        if isinstance(response, str):
            if response and response[0] in ('"', '[', '{'):
                return HttpResponse(response, content_type='application/json')
            return HttpResponse(response)
        elif isinstance(response, (set, dict, list, tuple, QuerySet, Model)):
            return json_response(response)
        else:
            return response
    return middleware

