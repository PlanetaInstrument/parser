from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import get_object_or_404
from . models import Site, ParserResult, ChangeSite
from . forms import SiteForm, ChooseForm, ParserResultForm, ViewResultForm
from . test_parser import parser_site
from .filters import ParserResultFilter


def home (request):
    if request.method == "POST":
        site = ChooseForm(request.POST)
        if site.is_valid():
            name = site.cleaned_data.get('site')
            post = Site.objects.get(name=name)
            pk = post.pk
            if '_parse' in request.POST:
                parser_site(post)
                if parser_site(post):
                    messages.success(request, "Parser is successful")
                else:
                    messages.error(request, "Parser no work")
            elif '_edit' in request.POST:
                return HttpResponseRedirect(reverse('edit_site', kwargs={'pk': pk}))
            elif '_delete' in request.POST:
                if post:
                    post.delete()
                    messages.success(request, "Delete is successful")
                else:
                    messages.error(request, "It was not found")
    else:
        site = ChooseForm()
    return render(request, 'parserApp/parse.html', {'site':site})


def add_site (request):
    if request.method == "POST":
        form = SiteForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('home')
    else:
        form = SiteForm()
    return render(request, 'parserApp/addParse.html', {'form':form})


def edit_site(request, pk):
    instance = get_object_or_404(Site, pk=2)
    if request.method == "POST":
        form = SiteForm(request.POST, instance=instance)
        try:
            if form.is_valid():
                form.save()
                messages.success(request, "Operation is success")
        except Exception as e:
            messages.warning(request, "your post was not saved do to an error: {}".format(e))
    else:
        form = SiteForm(instance=instance)
    return render(request, 'parserApp/edit.html', {'form':form, 'instance':instance})


def view_result (request):
    if request.method == "POST":
        forms = ViewResultForm(request.POST)
        if forms.is_valid():
            name = forms.cleaned_data.get('view_site')
            name_2 = forms.cleaned_data.get('view_site_2')
            post = ParserResult.objects.filter(id_site=name).only("article")
            post_2 = ParserResult.objects.filter(id_site=name_2).only("article")
            # inters = post.article.intersection(post_2.article)
            # print(inters)
            # post = ParserResult.objects.filter(article__in=inters).only("description")
            # post_2 = ParserResult.objects.filter(article__in=inters).only("description")

            if post and post_2:
                # parser_filter_1 = ParserResultFilter(request.GET, queryset=post)
                # parser_filter_2 = ParserResultFilter(request.GET, queryset=post_2)
                return render(request, 'parserApp/result.html', {'forms':forms, 'post':post, 'post_2':post_2, 'name':name, 'name_2':name_2})
            else:
                messages.error(request, "ничего не найдено")

    else:
        forms = ViewResultForm()

    return render(request, 'parserApp/result.html', {'forms':forms, })


def change (request):
    if request.method == "POST":
        forms = ChooseForm(request.POST)
        if forms.is_valid():
            name = forms.cleaned_data.get('site')
            print(name, '----')
            id = Site.objects.get(name=name)
            print(id.id, '----')
            post = ChangeSite.objects.filter(id_changed_site=id.id)
            if post:
                return render(request, 'parserApp/change.html', {'forms':forms, 'post':post})
            else:
                messages.error(request, "ничего не найдено")
    else:
        forms = ChooseForm()
    return render(request, 'parserApp/change.html', {'forms':forms})
