from django.shortcuts import render, redirect

from user.forms import RegisterForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string


def register(request):
    html_message = render_to_string('email_register.html', { 'context': {} })
    plain_message = render_to_string('email_register.txt', { 'context': {} })

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            email = form.cleaned_data["email"]
            send_mail("Register successfully", plain_message, settings.EMAIL_HOST_USER, [email], html_message=html_message)
            messages.success(request, "create user {} success".format(username))
            return redirect("/login")
    else:
        form = RegisterForm()
    context = {
        'title': 'Create User',
        'form': form
    }
    return render(request, "registration/register.html", context)
