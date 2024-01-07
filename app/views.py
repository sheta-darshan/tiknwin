from django.shortcuts import render, redirect
from .forms import RegistrationForm, CustomAuthenticationForm, UserProfileForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

def index(request):
    return render(request, "app/index.html")

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('app:index')  # Redirect to your home page or any other page
        else:
            print(form.errors)  # Add this line for debugging
    else:
        form = RegistrationForm()

    return render(request, 'app/register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("app:index")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = CustomAuthenticationForm()
    return render(request=request, template_name="app/login.html", context={"login_form": form})

def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('app:profile')  # Redirect to the same page to show the updated profile
    else:
        form = UserProfileForm(instance=request.user)

    return render(request, 'app/profile.html', {'form': form})

def match(request):
    return render(request, "app/match.html")

def matches(request):
    return render(request, "app/matches.html")

def predictions(request):
    return render(request, "app/predictions.html")

def sports(request):
    return render(request, "app/sports.html")