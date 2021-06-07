from django.shortcuts import render,redirect
import random
from markdown2 import Markdown
import re
from .forms import edit_form,add_form
from . import util
import random
import os

def markdowm_to_html(mark):    # Takes just the title 
    markdowner = Markdown()
    entry = util.get_entry(mark)
    return markdowner.convert(entry)

def index(request):
    if request.method=='POST':
        query=request.POST['query']
        if (util.get_entry(query)):
            entry=markdowm_to_html(query)
            return render(request,"encyclopedia/entry.html",{"entry":entry,"title":query})
        else:
            entries = util.list_entries()
            newentrylist=[]
            for item in entries:
                if re.search(query, item, re.IGNORECASE):
                    newentrylist.append(item)
            if len(newentrylist)>0:
                return render(request, "encyclopedia/index.html", {
                "entries": newentrylist
                })
            else:
                return render(request,"encyclopedia/error.html",{"Message":"Searched Entry not found."})   
            # return redirect('/') 
    else:
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries()
        })

def entry(request,title):
    if(util.get_entry(title)):
        entry=markdowm_to_html(title)
        return render(request,"encyclopedia/entry.html",{"entry":entry,"title":title}) 
    return render(request,"encyclopedia/error.html",{"Message":"Entry not found."})

def add_entry(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        if(util.get_entry(title)):
            return render(request,"encyclopedia/error.html",{"Message":"This Entry Already Exists!"})
        else:
            util.save_entry(title,content)
            entry=markdowm_to_html(title)
            return render(request,"encyclopedia/entry.html",{"entry":entry,"title":title}) 
    else:
        return render(request,'encyclopedia/add_entry.html',{'form':add_form})

def edit_entry(request,title):
    if request.method == "POST":
        content = request.POST['content']
        util.save_entry(title,content)
        entry=markdowm_to_html(title)
        return render(request,"encyclopedia/entry.html",{"entry":entry,"title":title}) 
    else:
        entry = util.get_entry(title)
        form = edit_form(initial={'content':entry})
        return render(request,'encyclopedia/edit_entry.html',{'title':title,'content':entry,'form':form})

def random_entry(request):
    random_entry_name = random.choice(util.list_entries())
    entry= markdowm_to_html(random_entry_name)
    return render(request,"encyclopedia/entry.html",{"entry":entry,"title":random_entry_name}) 

    
    






