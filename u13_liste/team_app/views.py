from django.http import HttpResponse
from django.template import loader
from .models import Member


# tutorial 
def team_app(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('contentDummy.html')
    context= {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))


def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

# Create your views here.
def ihk11(request):
    template = loader.get_template('11_ihk.html')
    return HttpResponse(template.render())