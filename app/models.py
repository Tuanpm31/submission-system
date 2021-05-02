from django.db import models


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
    title = models.TextField()
    abstract = models.TextField()
    paper_file = models.FileField(upload_to="files/")

    def __str__(self):
        return self.title


class Author(models.Model):
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    country_region = models.CharField(max_length=200)
    affiliation = models.CharField(max_length=200)
    email = models.EmailField()
    corresponding_author = models.BooleanField(default=False)
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE)

    def __str__(self):
        return self.last_name + " " + self.first_name


class Keyword(models.Model):
    title = models.CharField(max_length=200)
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
