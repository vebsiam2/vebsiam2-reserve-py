# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

@login_required
def reserve(request):
    
    print request.user
    
    return HttpResponse("Reservation Done for "+str(request.user.username))
