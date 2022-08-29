from django.shortcuts import get_object_or_404
from django.views.generic import CreateView
from .models import Article,Tag
from .forms import ArticleUpdateForm, SignUpForm,ArticleForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from django.db.models import Count

class SignUpView(CreateView):
    form_class=SignUpForm
    success_url=reverse_lazy("articleApp:login")
    template_name="signup.html"

def addarticle(request):
    if request.POST:    
        form=ArticleForm(request.POST,request.FILES)
        if form.is_valid():
            userform=form.save(commit=False)
            articletag = form.cleaned_data.get('articletag')
            alltag=articletag.split(',')
            alltags=Tag.objects.values_list('tags',flat=True)
            newtags=list(set(alltag).difference(list(alltags)))
            listtag=[]
            Tag.objects.bulk_create([Tag(tags=tag) for tag in newtags])
            for tag in alltag:
                listtag+=Tag.objects.filter(tags=tag)
            userform.user=request.user
            userform.save()
            userform.tag.add(*listtag)
            form.save_m2m()
            return HttpResponseRedirect(reverse('articleApp:draft'))
        else:
            print('form is invalid')

    form=ArticleForm()
    return render(request,'article.html',{'form':form})
    

def articleview(request):
    article = Article.objects.filter(draft=False)
    tags=Article.objects.values('tag__tags').annotate(the_count=Count('tag')).filter(draft=False).order_by('-the_count')[:5]
    list_article=  [art.id for art in article]
    mytag=Article.objects.filter(draft=False,id__in=list_article).values('id',"tag__tags")
    return render(request,'articleList.html',{'articleList':article,'tags':tags,'mytag':mytag})

def my_article(request):
    myarticle = Article.objects.filter(draft=False,user=request.user) 
    list_article=  [art.id for art in myarticle]
    mytag=Article.objects.filter(draft=False,user=request.user,id__in=list_article).values('id',"tag__tags")
    return render(request,'myarticle.html',{'myarticle':myarticle,'mytag':mytag})
    
def draftview(request):
    draft = Article.objects.filter(draft=True,user=request.user)
    list_article=  [art.id for art in draft]
    mytag=Article.objects.filter(draft=True,user=request.user,id__in=list_article).values('id',"tag__tags")
    return render(request,'draftList.html',{'draftList':draft,'mytag':mytag})

def delete_article(request,id):
    Article.objects.get(pk=id).delete()
    return HttpResponseRedirect(reverse('articleApp:draft'))

def update_article(request,id):
    instance=get_object_or_404(Article,pk=id)
    all_tags =instance.tag.all()
    all_tag=','.join(str(e)for e in all_tags)    
    if request.POST:
        form=ArticleUpdateForm(request.POST,request.FILES,instance=instance) 
        if form.is_valid():
            userform=form.save(commit=False)
            articletag = form.cleaned_data.get('articletag')
            alltag=articletag.split(',')
            alltags=Tag.objects.values_list('tags',flat=True)
            newtags=list(set(alltag).difference(list(alltags)))
            delete_tag=list(set(all_tag.split(',')).difference(list(alltag)))
            listtag=[]
            delete_tags=[]
            Tag.objects.bulk_create([Tag(tags=tag) for tag in newtags])
            for tag in alltag:
                listtag+=Tag.objects.filter(tags=tag)
            for tag in delete_tag:
                delete_tags+=Tag.objects.filter(tags=tag)
            form.save()
            userform.tag.add(*listtag)
            userform.tag.remove(*delete_tags)
            return HttpResponseRedirect(reverse('articleApp:draft'))
        else:
            print("form is invalid")
           
    form=ArticleUpdateForm(instance=instance)
    form2 = ArticleUpdateForm(initial={'articletag':all_tag})
    return render(request,'updatearticle.html',{'form':form,'form2':form2})
