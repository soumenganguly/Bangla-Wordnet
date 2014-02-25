from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,RequestContext
from interface.models import Search
from django.db import connection

# Create your views here.

def search(request):
    if request.method=='POST':
        template=loader.get_template('interface/wn.html')
        form=Search(request.POST)
        if form.is_valid():
            word=form.cleaned_data['word']
            con=connection.cursor()
            con.execute("select meaning from dict where word='%s'"%(word))
            row=con.fetchall()
            context=RequestContext(request,{
                'row':row,
                'word':word,
                'form':form,
            })
            return HttpResponse(template.render(context))
    else:
        form=Search()
        template=loader.get_template('interface/wn.html')
        context=RequestContext(request,{
            'form':form,
        })
        return HttpResponse(template.render(context))
    
