from django.shortcuts import render,redirect
from .forms import ryphform,signupform
from .models import ryph,usersignup
from django.contrib.auth import logout

def index(request):
    if request.method=="POST": #rooot
        if request.POST.get('signup')=='signup':
            newuser=signupform(request.POST)
            if newuser.is_valid():
                newuser.save()
                print("signup successfully")
            else:
                print(newuser.errors)
        elif request.POST.get('login')=='login':
            unm = request.POST['username']
            pas = request.POST['password']

            uid = usersignup.objects.get(username=unm)
            print("current userid: ",uid.id)
            user = usersignup.objects.filter(username=unm,password=pas)
            if user:  # true
                print('login succesfully!')
                request.session['user']=unm  #create session
                request.session['userid']=uid.id
                return redirect('/showdata')
                
            else:
                print("Error login failed")

    if request.method == 'POST':
        newnotes=ryphform(request.POST,request.FILES)
        if newnotes.is_valid():
            newnotes.save()
            print('new notes successfully saved')
        else:
            print(newnotes.errors)
    return render(request, 'index.html')

def showdata(request):
    user=request.session.get('user')
    data = ryph.objects.all()
    return render(request, 'showdata.html',{'data':data,'user':user})

def userlogout(request):
    logout(request)
    return redirect('/')




