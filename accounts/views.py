from django.shortcuts import render, redirect
from django.contrib.auth.models import User                                    #Gives us User objects
from django.contrib import auth                                                #provides us with authentication library

# Create your views here.
def signup(request):
    if request.method == 'POST':                                               #User wants to signup, Check if user Exist first
        if request.POST['password1'] == request.POST['password2']:             #1. Check that password1&password2 equals
            try:
                user = User.objects.get(username=request.POST['username'])     #2. Check if User Already Exist
                return render(request, 'accounts/signup.html', {'error':'Username has already been taken'})  # If User Already Exist
            except User.DoesNotExist:                                          #3. User DoesNotExist: Create USER
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)                                      #4. Login the created user
                return redirect('home')                                        #5.Return logged on User to home, import redirect
        else:                                                                  #6. Password didnt match
            return render(request, 'accounts/signup.html', {'error':'Password did not match'})
    else:
        #NOT POST: User needs to signup page so they can use it for signup
        return render(request, 'accounts/signup.html')

def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    # TODO: need to route to homepage
    # and dont forget to logout
    return render(request, 'accounts/signup.html')
