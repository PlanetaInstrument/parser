from django.shortcuts import render, redirect
from django.contrib import messages
from . models import Site, ParserResult, ChangeSite
from . forms import SiteForm, ChooseForm, ParserResultForm, ViewResultForm
from . planeta import parser_site

def home (request):
    if request.method == "POST":
        site = ChooseForm(request.POST)
        if site.is_valid():
            name = site.cleaned_data.get('site')
            post = Site.objects.get(name=name)
            parser_site(post)
            print("end parser_site")
            return render(request, 'parserApp/parse.html', {'site':site})
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


def view_result (request):
    if request.method == "POST":
        forms = ViewResultForm(request.POST)
        if forms.is_valid():
            name = forms.cleaned_data.get('view_site')
            name_2 = forms.cleaned_data.get('view_site_2')
            id = Site.objects.get(name=name)
            id_2 = Site.objects.get(name=name_2)
            post = ParserResult.objects.filter(id_site=id.id).only("article")
            post_2 = ParserResult.objects.filter(id_site=id_2.id, article_in=ParserResult.objects.filter(id_site=id.id).values("article"))

            # a.annotate(desc=Subquery(Post2.objects.filter(article=OuterRef('article')).values('description').first()))

            if post and post_2:
                post_2.objects.filter(atribute=F('blog__name'))
                return render(request, 'parserApp/result.html', {'forms':forms, 'post':post, 'post_2':post_2, 'name':name, 'name_2':name_2})
            else:
                messages.error(request, "ничего не найдено")
    else:
        forms = ViewResultForm()
    return render(request, 'parserApp/result.html', {'forms':forms})


def change (request):
    if request.method == "POST":
        forms = ViewResultForm(request.POST)
        if forms.is_valid():
            name = forms.cleaned_data.get('view_site')
            print(name, '----')
            id = Site.objects.get(name=name)
            print(id.id, '----')
            post = ChangeSite.objects.filter(id_changed_site=id.id)
            if post:
                return render(request, 'parserApp/change.html', {'forms':forms, 'post':post})
            else:
                messages.error(request, "ничего не найдено")
    else:
        forms = ViewResultForm()
    return render(request, 'parserApp/change.html', {'forms':forms})
