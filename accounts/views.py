from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CustomUserCreationForm
from .models import CustomUser

def register_view(request):
    form = CustomUserCreationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Account created successfully! You can now log in.")
        return redirect('login')
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('task_list')
        else:
            messages.error(request, "Invalid email or password")
    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')
