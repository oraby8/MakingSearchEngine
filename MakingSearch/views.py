from django.shortcuts import render
from. import scrape


def home(request):
	return render(request,'base.html')

# Create your views here.
def new_search(request):
    new_search = request.POST.get('search')
    output=scrape.ins(new_search)
    allout={'out':output,}

    return render(request,'new_search.html',allout)