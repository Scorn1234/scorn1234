from django.shortcuts import render

from accounts.models import Sitter
# Create your views here.

def show_map(request):
    sitters = Sitter.objects.all()
    addresses = ["{}@{}".format(sitter.address, sitter.id) for sitter in sitters]
    addresses = "@".join(addresses)
    
    return render(request, 'map/show_map.html', {'addresses':addresses,})
