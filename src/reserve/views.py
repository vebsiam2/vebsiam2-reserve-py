# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

@login_required
def reserve(request):
    return HttpResponse("Reservation Done")
