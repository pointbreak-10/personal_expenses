from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from personalExpenses import data_storage, password
from .models import userExpense
# Create your views here.
def home(request):
    return render(request,'personalExpenses/index.html')

def loginUser(request):
    if request.method == 'GET':
        return render(request,'personalExpenses/index.html')
    else:
        user = authenticate(request=request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            return render(request,'personalExpenses/index.html', {'error':"Username and password do not match"})

        else:
            login(request, user)
            return redirect('dashboard') 

def signUpUser(request):
    if request.method == 'GET':
        return render(request,'personalExpenses/index.html')
    else:
        
        if request.POST['password1'] == request.POST['password2']:
            try:
                #check the password
                if(password.check(request.POST['password1'])):
                    user = User.objects.create_user(username=request.POST['username'], email=request.POST['email'], password=request.POST['password1'])
                    #data = {'name': request.POST['username'], 'occupation':request.POST['occupation']}
                    #data_storage.jsonDB(data)
                    user.save()
                    login(request, user)
                    return redirect('dashboard')
                else:
                    return render(request,'personalExpenses/index.html',{'error':'Password must contain an Uppercase, a lower case and a number!'})
            except IntegrityError:
                return render(request,'personalExpenses/index.html',{'error':'Sorry the user name is already taken!'})
            except ValueError:
                return render(request,'personalExpenses/index.html',{'error':'Please enter valid username or password!'})
        
        else:
            return render(request,'personalExpenses/index.html',{'error':'The password entered do not match!'})
            

def logOut(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')



def dashboard(request):
    data = userExpense.objects.filter(uid = request.user)
    if request.method == 'GET':
        #exepnsedata = userExpense.objects.filter(user = request.user)
        return render(request, 'personalExpenses/dashboard.html',{'data': data})
    
    else:
        monthdata = [request.POST['month'], request.POST['monthly_earning'], request.POST['monthly_expenses'], request.POST['monthly_savings']]

        return render(request, 'personalExpenses/dashboard.html', {"data": monthdata})