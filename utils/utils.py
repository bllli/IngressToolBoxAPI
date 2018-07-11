from rest_framework.utils import json


def get_request_param_as_json(request):
    try:
        params = json.loads(request.body)
        return params
    except Exception as e:
        if request.method == 'POST':
            return request.POST.dict()
        else:
            return request.GET.dict()
