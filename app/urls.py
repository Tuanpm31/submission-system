from django.urls import path
from .views import index, submission_success

urlpatterns = [
    path("", index, name="home"),
    path("submission-success", submission_success, name="submission-success")
]
