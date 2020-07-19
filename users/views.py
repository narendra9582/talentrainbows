from django.shortcuts import render,redirect
from django.contrib import messages
from users.models import Signup
from django.contrib.auth.models import User
from django.contrib.auth import     authenticate,logout,login

# ---------------------------Login function----------------------------------

def loginUser(request):
    #verify user
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            if request.user.is_anonymous:
                return redirect('/login')
            return render(request,'homepage/homepage.html')
        else:
            return render(request,'users/login.html')

    return render(request,'users/login.html')
# ---------------------------Logout function----------------------------------
def logoutUser(request):
    logout(request)
    return render(request,'users/signup.html')


# ---------------------------SignUp function----------------------------------
def signupUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')        
        signup = Signup(username = username, email = email, password = password,password2 = password2)
        if(password2==password):
            signup.save()
        else:
            messages.error (request, 'please enter correct password')
            return render(request,'users/signup.html' )

        messages.success(request, 'Thank you for registering with us')
        return render(request,'homepage/homepage.html' )
    return render(request,"users/signup.html")

