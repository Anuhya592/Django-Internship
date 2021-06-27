from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Register
# Create your views here.
def home(request):
	return HttpResponse("This is a home page")

def html(request):
	return HttpResponse("<h2>This is h2 tag</h2>")

def username(request,uname):
	return HttpResponse("<h2> Welcome <span style='color:blue'>{}</span></h2>".format(uname))

def usernameage(request,un,age):
	return HttpResponse("<h3 style='text-align:center;background-color:green'> Hi <span style='color:blue'>{}</span> . Your age is <span style='color:red'>{}</span></h3>".format(un,age))

def employeedetails(request,empid,eage,ename):
	return HttpResponse("<script>alert('Hi welcome {}')</script><h3 style='text-align:center;background-color:green'> Hi <span style='color:blue'>{}</span> . Your age is <span style='color:red'>{}</span>.Your id is {}</h3>".format(ename,ename,eage,empid))

def htm(request):
	return render(request,'sample.html')

def ytname(request,name):
	return render(request,'ytname.html',{'name':name})

def empname(request,id,ename):
	return render(request,'pt.html',{'id':id,'ename':ename})

def student(request):
	return render(request,'std.html')

def internaljs(request):
	return render(request,'internaljs.html') 

def myform(request):
	if request.method=='POST':
		uname = request.POST['uname']
		rollno = request.POST['rollno']
		email_id = request.POST['email']
		#print(uname,rollno,email_id)
		data = {'uname':uname,'rollno':rollno,'email_id':email_id}
		return render(request,'display.html',data)

def signup(request):
	if request.method=="POST":
		fname = request.POST['fname']
		lname = request.POST['lname']
		phno = request.POST['phno']
		email = request.POST['email']
		gender = request.POST['gender']
		add = request.POST['add']
		luk = request.POST.getlist('luk')
		data = {'fname':fname,'lname':lname,'phno':phno,'email':email,'gender':gender,'add':add,'luk':luk}
		return render(request,'see.html',data)
	return render(request,'signup.html')

def bootstrapfun(request):
	return render(request,'bootstrapfun.html')

def btregi(request):
	return render(request,'btregst.html')

def register(request):
	#name = "siva"
	#email = "siva@gmail.com"
	reg = Register(name = "siva",email = "siva@gmail.com")
	reg.save()
	return HttpResponse("Registered successfully :)")

def register1(request):
	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		reg = Register(name = name,email = email)
		reg.save()
		return HttpResponse("<h1>Registered succesfully :)")
	return render(request,'register1.html')

def showdetails(request):
	data = Register.objects.all()
	return render(request,'showdetails.html',{'data':data})

def viewinfo(request,id):
	w = Register.objects.get(id=id)
	return render(request,'viewinfo.html',{'data':w})
	#return HttpResponse("Your Name is: {} and your email id is: {}".format(w.name,w.email)) 

def update(request,id):
	t = Register.objects.get(id=id)
	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		t.name = name
		t.email = email
		t.save()
		return redirect('/showdetails')
	return render(request,'update.html',{'data':t})

def delete(request,id):
	d = Register.objects.get(id = id)
	if request.method == 'POST':
		d.delete()
		return redirect('/showdetails')
	return render(request,'delete.html',{'data':d})