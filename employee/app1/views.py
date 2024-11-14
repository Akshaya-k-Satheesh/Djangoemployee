from django.shortcuts import render,redirect
from app1.models import Employee
# Create your views here.
def home(request):
    return render(request,'home.html')
def add(request):
    if(request.method=="POST"):
        e=request.POST['e']
        n=request.POST['n']
        a=request.POST['a']
        ad=request.POST['ad']
        em=request.POST['em']
        i=request.FILES.get('i')

        s=Employee.objects.create(emp_id=e,e_name=n,age=a,address=ad,email=em,image=i)
        s.save()
        return view(request)
    return render(request,'add.html')
def view(request):
    k=Employee.objects.all()
    return render(request,'view.html',{'employee':k})
def details(request,i):
    k=Employee.objects.get(id=i)
    return render(request,'details.html',{'employee':k})
def edit(request,h):
    k=Employee.objects.get(id=h)
    if (request.method == "POST"):
        k.emp_id=request.POST['e']
        k.e_name=request.POST['n']
        k.age=request.POST['a']
        k.address=request.POST['ad']
        k.email=request.POST['em']
        if (request.FILES.get('i') == None):
            k.save()
        else:
            k.image=request.FILES['i']
            k.save()
            return view(request)
    return render(request,'edit.html',{'employee':k})

def delete(request,p):
    k=Employee.objects.get(id=p)
    k.delete()
    return redirect('app1:view')