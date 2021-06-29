from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import RegisterForm
# Create your views here.
def register(response): 
    if response.method=="POST":
        form= RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password1"])
            login(response, user)
        else:
            form= RegisterForm()
            return render(response, "register/register.html", {"form": form, "invalid": True,  "user": response.user},)

        return redirect("/")

    else:
        form= RegisterForm()

    return render(response, "register/register.html", {"form":form,  "user": response.user,})