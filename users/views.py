from django.contrib.auth import login
from django.shortcuts import redirect, render

from .forms import SignUpForm


def signup(request):
    """
    View to register a new user.
    """
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # log in the user immediately
            return redirect("recipes:list")
    else:
        form = SignUpForm()
    return render(request, "users/signup.html", {"form": form})
