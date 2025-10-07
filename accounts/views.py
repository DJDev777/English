# myapp/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.http import HttpResponseRedirect
from django.utils.http import url_has_allowed_host_and_scheme
from django.contrib import messages

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        next_url = request.POST.get("next") or request.GET.get("next")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Security: ensure next_url is safe
            if next_url and url_has_allowed_host_and_scheme(next_url, allowed_hosts={request.get_host()}):
                return redirect(next_url)
            else:
                return redirect(settings.LOGIN_REDIRECT_URL)  # e.g. “/” or dashboard
        else:
            messages.error(request, "Invalid username or password")
            # fall through to render login page again

    else:
        next_url = request.GET.get("next")

    context = {
        "next": next_url,
    }
    return render(request, "accounts/login.html", context)


def logout_view(request):
    logout(request)
    # optional: messages.info(request, "You have been logged out.")
    # You could redirect to a specific page:
    return redirect(settings.LOGOUT_REDIRECT_URL or settings.LOGIN_URL)
