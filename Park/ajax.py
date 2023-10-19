import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from .models import Maintenance

def companydeleteitem(request):
    object_id = request.POST.get('id', None)
    b = get_object_or_404(Maintenance, id=object_id)
    b.delete()
    data = {'message': 'delete'.format(b)}
    return HttpResponse(json.dumps(data), content_type='application/json')