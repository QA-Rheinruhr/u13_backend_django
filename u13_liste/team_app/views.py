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

# ihk
def ihk11(request):
    template = loader.get_template('ihk_11.html')
    return HttpResponse(template.render())

def ihk12(request):
    template = loader.get_template('ihk_12.html')
    return HttpResponse(template.render())

def ihk13(request):
    template = loader.get_template('ihk_13.html')
    return HttpResponse(template.render())

def ihk14(request):
    template = loader.get_template('ihk_14.html')
    return HttpResponse(template.render())

def ihk15(request):
    template = loader.get_template('ihk_15.html')
    return HttpResponse(template.render())


# uml 
def uml11(request):
    template = loader.get_template('uml_11.html')
    return HttpResponse(template.render())

def uml12(request):
    template = loader.get_template('uml_12.html')
    return HttpResponse(template.render())

def uml13(request):
    template = loader.get_template('uml_13.html')
    return HttpResponse(template.render())

def uml14(request):
    template = loader.get_template('uml_14.html')
    return HttpResponse(template.render())

def uml21(request):
    template = loader.get_template('uml_21.html')
    return HttpResponse(template.render())

def uml22(request):
    template = loader.get_template('uml_22.html')
    return HttpResponse(template.render())

def uml23(request):
    template = loader.get_template('uml_23.html')
    return HttpResponse(template.render())

def uml24(request):
    template = loader.get_template('uml_24.html')
    return HttpResponse(template.render())


# github
def github11(request):
    template = loader.get_template('github_11.html')
    return HttpResponse(template.render())

def github12(request):
    template = loader.get_template('github_12.html')
    return HttpResponse(template.render())

def github13(request):
    template = loader.get_template('github_13.html')
    return HttpResponse(template.render())

def github14(request):
    template = loader.get_template('github_14.html')
    return HttpResponse(template.render())

def github15(request):
    template = loader.get_template('github_15.html')
    return HttpResponse(template.render())


# django
def django11(request):
    template = loader.get_template('django_11.html')
    return HttpResponse(template.render())

def django12(request):
    template = loader.get_template('django_12.html')
    return HttpResponse(template.render())

def django13(request):
    template = loader.get_template('django_13.html')
    return HttpResponse(template.render())

def django14(request):
    template = loader.get_template('django_14.html')
    return HttpResponse(template.render())

def django15(request):
    template = loader.get_template('django_15.html')
    return HttpResponse(template.render())

def django16(request):
    template = loader.get_template('django_16.html')
    return HttpResponse(template.render())

