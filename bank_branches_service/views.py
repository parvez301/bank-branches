import json
from django.http import HttpResponse

from bank_branches_service.models import Banks, Branches


# Create your views here.
def get_branches(request, ifsc=None, bank_name=None, city=None):
    data = []
    if (ifsc or (bank_name and city)):
        if ifsc:
            results = Branches.objects.filter(ifsc=ifsc)
        else:
            results = Branches.objects.filter(
                bank__name__icontains=bank_name
            ).filter(city__icontains=city)
    else:
        results = Branches.objects.all()
    
    if results:
        for result in results:
            data.append({
                'bank_name': result.bank.name,
                'ifsc_code': result.ifsc,
                'branch': result.branch,
                'address': result.address,
                'city': result.city,
                'district': result.district,
                'state': result.state
            })
    else:
        data.append({
            'error': 'No Data found'
        })
    
    return HttpResponse(json.dumps(data), content_type="application/json")