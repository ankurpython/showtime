from django.shortcuts import render,redirect
from django.http import HttpResponse
from movieapp.models import Movie
from movieapp.forms import MovieForm
from django.core.paginator import EmptyPage,Paginator,PageNotAnInteger
from django.db.models import Q
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.
def view(request):
    return render(request,'testapp/index.html')

# Create your views here.

def list_view(request):
    list_movie=Movie.objects.all().order_by('-id')
    query=request.GET.get("q")
    if query:
        list_movie=list_movie.filter(Q(moviename__icontains=query) | Q(actor__icontains=query)  | Q(actress__icontains=query)| Q(director__icontains=query)).distinct()
    paginator=Paginator(list_movie,5)
    page_number=request.GET.get('page')
    try:
        list_movie=paginator.page(page_number)
    except PageNotAnInteger:
        list_movie=paginator.page(1)
    except EmptyPage:
        list_movie=paginator.page(paginator.num_pages)
    return render(request,'testapp/list.html',{'list_movie':list_movie})


def create_view(request):
    form=MovieForm()
    if request.method=='POST':
        form=MovieForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Successfully Added")
        return redirect('/')
    else:
        messages.error(request,"Item not Saved")
    return render(request,'testapp/create.html',{'form':form})


def detial_view(request,id):
    movie=Movie.objects.get(id=id)
    return render(request,'testapp/view.html',{'movie':movie})
