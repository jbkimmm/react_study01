import json
from django.http import JsonResponse
from .encoders import JSONEncoder


def get_json_dump(obj):
    return json.dumps(obj, cls=JSONEncoder, ensure_ascii=False)


def json_response(obj):
    return JsonResponse(obj, encoder=JSONEncoder, json_dumps_params={'ensure_ascii': False}, safe=False)


