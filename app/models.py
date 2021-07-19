from django.db import models
from user.models import Authors


class Paper(models.Model):
    FULL_PAPER = "FP"
    ABSTRACT = "AS"
    SUBMISSION_TYPE_CHOICES = (
        (FULL_PAPER, 'Full Paper'),
        (ABSTRACT, 'Abstract')
    )
    submission_type = models.CharField(
        max_length=2,
        choices=SUBMISSION_TYPE_CHOICES,
        default=FULL_PAPER,
    )
    author = models.ForeignKey(Authors, on_delete=models.CASCADE, default=None)
    title = models.TextField()
    abstract = models.TextField()
    paper_file = models.FileField(upload_to="files/")

    def __str__(self):
        return self.title
