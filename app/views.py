from user.models import Authors
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from app.forms import SubmissionForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string


@login_required(
    login_url="/login"
)
def index(request):
    html_message_abstract = render_to_string('email_abstract.html', { 'context': {} })
    plain_message_abstract = render_to_string('email_abstract.txt', { 'context': {} })
    html_message_full_paper = render_to_string('email_full_paper.html', { 'context': {} })
    plain_message_full_paper = render_to_string('email_full_paper.txt', { 'context': {} })

    if request.method == "POST":
        form = SubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            paper = form.save(commit=False)
            author = Authors.objects.get(user=request.user)
            paper.author = author
            email = author.user.email
            type = form.cleaned_data["submission_type"]
            if type == "AS":
                send_mail("Submission success", plain_message_abstract, settings.EMAIL_HOST_USER, [email], html_message=html_message_abstract)
            else:
                send_mail("Submission success", plain_message_full_paper, settings.EMAIL_HOST_USER, [email], html_message=html_message_full_paper)
            form.save()
            return redirect("submission-success")
    else:
        form = SubmissionForm()
    context = {
        'title': 'Submission form',
        'form': form
    }
    return render(request, "home.html", context=context)


def submission_success(request):
    return render(request, "submission_success.html")
