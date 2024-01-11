from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm, CustomAuthenticationForm, UserProfileForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .models import Sports, Match, Prediction, Team
from django.utils import timezone
from django.contrib.auth.decorators import login_required


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

def view_sports(request):
    sports = Sports.objects.all()
    return render(request, "app/sports.html", {'sports': sports})



def view_matches(request, sport_id):
    sport = get_object_or_404(Sports, pk=sport_id)
    matches = Match.objects.filter(sports=sport)
    now = timezone.now()
    return render(request, "app/matches.html", {'sport': sport, 'matches': matches, 'now': now})

from django.shortcuts import get_object_or_404

@login_required
def view_match(request, match_id):
    match = get_object_or_404(Match, pk=match_id)
    user = request.user
    user_prediction = Prediction.objects.filter(user=request.user, match=match).first()
    participating_teams = Team.objects.filter(pk__in=[match.home_team_id, match.away_team_id])

    if request.method == 'POST':
        team_id = request.POST.get('predicted_result')  # Assuming the team ID is submitted in the form
        predicted_team = get_object_or_404(Team, pk=team_id)

        if Prediction.objects.filter(user=user, match=match).exists():
            # Handle case where user has already predicted for this match
            # You can redirect to a different page or display an error message
            pass
        else:
            # Create a new prediction for the user
            Prediction.objects.create(user=user, match=match, predicted_team=predicted_team)

    return render(request, "app/match.html", {'match': match,'user_has_prediction': user_prediction is not None,
                                               'user_prediction': user_prediction, "participating_teams": participating_teams})
