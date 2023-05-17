from django.shortcuts import render,redirect
from django.contrib import messages
from portfolio.models import Contact,Blogs

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def handleblog(request):
    posts=Blogs.objects.all()
    context={"posts":posts}
    return render(request, 'handleblog.html',context)

def contact(request):
    if request.method=="POST":
        fname=request.POST.get('name')
        femail=request.POST.get('email')
        fphonenumber=request.POST.get('num')
        fdescription=request.POST.get('description')
        query=Contact(name=fname,email=femail,phonenumber=fphonenumber,description=fdescription)
        query.save()
        messages.success(request,"Thanks for contacting us. We will get by you soon!")
        
        return redirect('/contact')
    return render(request, 'contact.html')