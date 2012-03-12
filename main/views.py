from annoying.decorators import render_to
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from faktum.main.models import Fact

@render_to("main/index.html")
def index(request):
    return dict(facts=Fact.objects.all().order_by("-added")[:20])

@login_required
def add(request):
    if request.method != "POST":
        return HttpResponseRedirect("/")
    f = Fact.objects.create(title=request.POST.get('title',''),
                            details=request.POST.get('details',''),
                            source_name=request.POST.get('source_name',''),
                            source_url=request.POST.get('source_url',''),
                            user=request.user,
                            )
    return HttpResponseRedirect("/")
