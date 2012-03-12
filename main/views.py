from annoying.decorators import render_to
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from faktum.main.models import Fact, Tag, FactTag
from django.db.models import Q

@render_to("main/index.html")
def index(request):
    return dict(facts=Fact.objects.all().order_by("-added")[:20])

@render_to("main/tag.html")
def tag(request,tag_id):
    tag = get_object_or_404(Tag,id=tag_id)
    return dict(tag=tag,facts=[ft.fact for ft in tag.facttag_set.all().order_by("-fact__added")[:20]])

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
    tags_field = request.POST.get('tags','')
    for tag in tags_field.split(','):
        tag = tag.strip().lower()
        t,created = Tag.objects.get_or_create(name=tag)
        ft = FactTag.objects.create(fact=f,tag=t)
    return HttpResponseRedirect("/")

@render_to("main/search_results.html")
def search(request):
    q = request.GET.get('q','')
    if not q:
        return HttpResponseRedirect("/")
    facts = Fact.objects.filter(Q(title__icontains=q) | 
                                Q(details__icontains=q) |
                                Q(source_name__icontains=q) |
                                Q(source_url__icontains=q))
    tags = Tag.objects.filter(name__icontains=q)
    return dict(facts=facts,tags=tags,q=q)

@render_to("main/fact.html")
def fact(request,fact_id):
    f = get_object_or_404(Fact,id=fact_id)
    return dict(fact=f)
