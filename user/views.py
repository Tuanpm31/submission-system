from django.shortcuts import render, redirect

from user.forms import RegisterForm
from django.contrib import messages


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, "create user {} success".format(username))
            return redirect("/login")
    else:
        form = RegisterForm()
    context = {
        'title': 'Create User',
        'form': form
    }
    return render(request, "registration/register.html", context)
