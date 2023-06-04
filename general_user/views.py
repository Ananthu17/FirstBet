from django.views.generic import TemplateView, RedirectView
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import BaseUser


# Create your views here.


class Home_view(TemplateView):
    template_name = 'index.html'


class Login_view(TemplateView):
    template_name = 'index.html'

    def post(self, request):
        username = request.POST.get('email', '')
        password = request.POST.get('password', '')
        next_url = ""

        print("EMAIL :", username)
        if username and password:
            try:
                user = BaseUser.objects.get(email=username)
                user = authenticate(request, username=user.username, password=password)
                if user is not None and user.is_superuser:
                    login(request, user)
                    # Redirect to a success page.
                    if next_url != "":
                        return redirect(next_url)
                    return redirect('home')
                else:
                    messages.error(request, "Invalid Credentials")
                    return redirect('home')
            except Exception:
                messages.error(request, "Invalid Credentials")
                return redirect('home')
        else:
            messages.error(request, "Username And Password Required")
            return redirect('home')