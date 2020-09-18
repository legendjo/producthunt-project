from django.shortcuts import render, redirect
from django.contrib.auth.models import User                                    #Gives us User objects
from django.contrib import auth                                                #provides us with authentication library

# Create your views here.
'''
SIGNUP PROCESS:
1A. If POST request, User wants to signup,
2A-1: Check if user Exist first starting with passwords match
2B. Check with username of user if Exist
2C. If username exists, intead of throwing exception, use {try: except:]
    to handle the exception then, return an error of Username taken and return to signup home
2D. If user DoesNotExist, create the user
2E  Login the created authenticated username and redirect to homepage
2A-2: If password checks dont match, retun to signup page showing error Password missmatch
1B.  If NOT a POST request, user just want to see signup page for their use

'''
def signup(request):
    if request.method == 'POST':                                               # 1A
        if request.POST['password1'] == request.POST['password2']:             # 2A-1
            try:
                user = User.objects.get(username=request.POST['username'])     #2C
                return render(request, 'accounts/signup.html', {'error':'Username has already been taken'})  # 2C
            except User.DoesNotExist:                                          # 2D
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1']) #2D
                auth.login(request, user)                                      # 2E
                return redirect('home')                                        # 2E
        else:                                                                  # 1B
            return render(request, 'accounts/signup.html', {'error':'Password did not match'})
    else:
        #NOT POST: User needs to signup page so they can use it for signup
        return render(request, 'accounts/signup.html')

'''
LOGIN PROCESS:
(1A) Check if it's a POST request if yes, then go to Steps 2A,2B,2C;
(2A) Check if username and password passed are correct, and authenticate the user object authentiated
(2B) If we got a valid userback, login the user and redirect to home page
(2C) If user is None, rend an error and return to login page
(1B) If NOT a POST, user will see login page only
'''
def login(request):
    if request.method == 'POST':        # 1A
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])    # 2A
        if user is not None:            # 2B
            auth.login(request, user)
            return redirect('home')
        else:                            # 2C
            return render(request, 'accounts/login.html', {'error':'username or password is incorrect'})
    else:                                # 1B
        return render(request, 'accounts/login.html')


'''

'''
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home') 
