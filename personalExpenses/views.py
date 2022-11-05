from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from personalExpenses import data_storage, password

# Create your views here.
def home(request):
    return render(request,'personalExpenses/home.html')

def loginUser(request):
    if request.method == 'GET':
        return render(request,'personalExpenses/login.html')
    else:
        user = authenticate(request=request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            return render(request,'personalExpenses/login.html', {'error':"Username and password do not match"})

        else:
            login(request, user)
            return redirect('dashboard') 

def signUpUser(request):
    if request.method == 'GET':
        return render(request,'personalExpenses/signUp.html')
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
                    return render(request,'personalExpenses/signUp.html',{'error':'Password must contain an Uppercase, a lower case and a number!'})
            except IntegrityError:
                return render(request,'personalExpenses/signUp.html',{'error':'Sorry the user name is already taken!'})
            except ValueError:
                return render(request,'personalExpenses/signUp.html',{'error':'Please enter valid username or password!'})
        
        else:
            return render(request,'personalExpenses/signUp.html',{'error':'The password entered do not match!'})
            

def logOut(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')



def dashboard(request):
    if request.method == 'GET':
        return render(request, 'personalExpenses/dashboard.html')
    
    else:
        xValue = ["Monthly Expenses", "Monthly Savings"]
        yValue = [request.POST['monthly_expenses'], request.POST['monthly_savings']]
        plot_div = go.Pie(labels=xValue, values=yValue)
        return render(request, 'personalExpenses/dashboard.html', {"labels": xValue, "data":yValue})