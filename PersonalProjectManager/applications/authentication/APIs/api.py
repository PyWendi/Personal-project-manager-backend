from ninja import NinjaAPI
from django.http import HttpResponse

# Create your views here.
api = NinjaAPI()


@api.get('test/')
def APItest(request):
    return "Hello world"

