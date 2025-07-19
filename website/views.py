from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    # Check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticare
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been Logged In!")
            return redirect('home')
        else:
            messages.success(request, "There was an Error Logging In. Please try again.")
            return redirect('home')
    else:
        return render(request, 'home.html', {})
    
def logout_user(request):
    logout(request)
    messages.success(request, "You have been Logged Out.")
    return redirect('home')

