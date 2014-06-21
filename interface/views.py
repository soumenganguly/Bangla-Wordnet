from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,RequestContext
from interface.models import Search,Synset
from django.db import connection



# Create your views here.


def index(request):
    if request.method=='POST':
        template=loader.get_template('interface/demo.html')
        form=Search(request.POST)
        if form.is_valid():
            word=form.cleaned_data['word']
            syn=Synset.objects(word=word)
            context=RequestContext(request,{
                'syn':syn,
                'form':form,
            })
            return HttpResponse(template.render(context))
    else:
        form=Search()
        template=loader.get_template('interface/demo.html')
        context=RequestContext(request,{
            'form':form,
        })
        return HttpResponse(template.render(context))
  
def search(request,word):
    template=loader.get_template('interface/demo.html')
    form=Search()
    syn=Synset.objects(word=word)
    context=RequestContext(request,{
        'syn':syn,
        'form':form,
        })
    return HttpResponse(template.render(context))

