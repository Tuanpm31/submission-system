from django.shortcuts import render, redirect

from app.forms import SubmissionForm
from django.contrib.auth.decorators import login_required


@login_required(
    login_url="/login"
)
def index(request):
    if request.method == "POST":
        form = SubmissionForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
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