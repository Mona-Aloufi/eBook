from django.shortcuts import render
from .models import Book
from django.http import HttpResponse
def index(request):
 return HttpResponse("Hello, world! <br> I am Mona Aloufi")


def index(request):
 name = request.GET.get("name") or "world!" #add this line
 return HttpResponse("Hello, "+name) #replace the word “world!” with the variable name

def index2(request, val1 = 0): #add the view function (index2)
 return HttpResponse("value1 = "+str(val1))

from django.shortcuts import render 
def indexwithtamblet(request):
 name = request.GET.get("name") or "world"
 return render(request, "Bookmodule/index.html",{"name": name}) 

def viewbook(request, bookId):
 # assume that we have the following books somewhere (e.g. database)
 book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
 book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'}
 targetBook = None
 if book1['id'] == bookId: targetBook = book1
 if book2['id'] == bookId: targetBook = book2
 #context = {'book':targetBook} # book is the variable name accessible by the template
 return render(request, 'bookmodule/show.html', {'book':targetBook})

def home(request):
    return render(request,"bookmodule/home.html")
def oneBook(request,BId):
    obj=Book.objects.get(id=BId)
    return render(request,"bookmodule/oneBook.html",{"Book":obj})
def show(request):
    obj=Book.objects.all()
    return render(request,"bookmodule/listBooks.html",{"Book":obj})


