from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print("Hello")
            form.save()
            return redirect('login')
        else:
            # print("Error saving the signup form - " + form.errors)
            print("Error saving the signup form - " , form.errors)
    else:
        form = UserCreationForm()
        
    return render(request, 'signup.html', {'form': form})

@login_required(login_url='/login')
def home(request):
    return render(request, 'home.html')
