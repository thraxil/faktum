from annoying.decorators import render_to
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from faktum.main.models import Fact, Tag, FactTag
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User


@render_to("main/index.html")
def index(request):
    paginator = Paginator(Fact.objects.all().order_by("-added"), 20)
    page = request.GET.get('page', '1')
    try:
        facts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        facts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        facts = paginator.page(paginator.num_pages)

    return dict(facts=facts,
                source_url=request.GET.get('source_url', ''),
                source_name=request.GET.get('source_name', ''),
                details=request.GET.get('details', ''),
                )


@render_to("main/tag.html")
def tag(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    return dict(tag=tag,
                facts=[ft.fact
                       for ft
                       in tag.facttag_set.all().order_by("-fact__added")[:20]])


@render_to("main/user.html")
def user(request, username):
    user = get_object_or_404(User, username=username)
    return dict(user=user,
                facts=Fact.objects.filter(user=user).order_by("-added"))


@login_required
def add(request):
    if request.method != "POST":
        return HttpResponseRedirect("/")
    f = Fact.objects.create(title=request.POST.get('title', ''),
                            details=request.POST.get('details', ''),
                            source_name=request.POST.get('source_name', ''),
                            source_url=request.POST.get('source_url', ''),
                            user=request.user,
                            )
    tags_field = request.POST.get('tags', '')
    for tag in tags_field.split(', '):
        tag = tag.strip().lower()
        t, created = Tag.objects.get_or_create(name=tag)
        FactTag.objects.create(fact=f, tag=t)
    return HttpResponseRedirect("/")


@login_required
@render_to("main/multiadd.html")
def multiadd(request):
    if request.method != "POST":
        return dict()
    else:
        source_name = request.POST.get('source_name', '')
        source_url = request.POST.get('source_url', '')
        for k in request.POST.keys():
            if not k.startswith('title-'):
                continue
            idx = int(k[len("title-"):])
            if not request.POST[k]:
                continue
            f = Fact.objects.create(
                title=request.POST.get("title-%d" % idx, ''),
                details=request.POST.get("details-%d" % idx, ''),
                source_name=source_name,
                source_url=source_url,
                user=request.user,
            )
            tags_field = request.POST.get("tags-%d" % idx, '')
            for tag in tags_field.split(', '):
                tag = tag.strip().lower()
                t, created = Tag.objects.get_or_create(name=tag)
                FactTag.objects.create(fact=f, tag=t)
        return HttpResponseRedirect("/")


@render_to("main/search_results.html")
def search(request):
    q = request.GET.get('q', '')
    if not q:
        return HttpResponseRedirect("/")
    facts = Fact.objects.filter(Q(title__icontains=q) |
                                Q(details__icontains=q) |
                                Q(source_name__icontains=q) |
                                Q(source_url__icontains=q))
    tags = Tag.objects.filter(name__icontains=q)
    return dict(facts=facts, tags=tags, q=q)


@render_to("main/fact.html")
def fact(request, fact_id):
    f = get_object_or_404(Fact, id=fact_id)
    return dict(fact=f)


@render_to("main/tags.html")
def tags(request):
    return dict(tags=Tag.objects.all().order_by("name"))
