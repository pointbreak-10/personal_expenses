from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.views import View
from personalExpenses import password
from .models import userExpense
from .forms import ExpenseForm
# Create your views here.



class landing(View):
    
    def get(self, request):
        return render(request,'personalExpenses/index.html')

    def post(self, request):
            
        if 'signin' in request.POST:
            user = authenticate(request=request, username=request.POST['username'], password=request.POST['password'])

            if user is None:
                return render(request,'personalExpenses/index.html', {'error':"Username and password do not match"})

            else:
                login(request, user)
                return redirect('dashboard')
        
        if 'signup' in request.POST:
            if request.POST['password1'] == request.POST['password2']:
                try:
                    #check the password
                    if(password.check(request.POST['password1'])):
                        user = User.objects.create_user(username=request.POST['username'], email=request.POST['email'], password=request.POST['password1'])
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
    
    if request.method == 'GET':
        metrics = userExpense.objects.filter(user = request.user)
        return render(request, 'personalExpenses/dashboard.html',{"form": ExpenseForm(), "data":metrics})
    
    else:
        print("retrieve from dashboard")
        monthdata = [request.POST['month'], request.POST['monthly_earning'], request.POST['monthly_expenses'], request.POST['monthly_savings']]

        try:
            f = ExpenseForm(request.POST)
            print("saving the data")
            newExpense = f.save(commit=False)
            newExpense.user = request.user
            newExpense.save()
            print("data saved")
        except ValueError:
            return render(request, 'personalExpenses/dashboard.html', {"data": monthdata, "error":'Data is invalid'})

        print("sending back the data to dashboard")
        return render(request, 'personalExpenses/dashboard.html', {"data": monthdata})

