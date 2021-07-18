from django.contrib import admin
import csv
from django.http import HttpResponse
# Register your models here.
from app.models import Author, Keyword, Paper


class AuthorAdmin(admin.ModelAdmin):
    pass


class KeywordAdmin(admin.ModelAdmin):
    pass


def dowload_paper_csv(self, request,  queryset):
    meta = self.model._meta

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
    writer = csv.writer(response)

    writer.writerow(["submission_type", "email", "title", "abstract", "paper file"])
    for obj in queryset:

        row = writer.writerow([obj.submission_type, obj.email, obj.title, obj.abstract, request.get_host() + obj.paper_file.url])

    return response


class PaperAdmin(admin.ModelAdmin):
    list_display = ('title', 'email', 'submission_type')
    search_fields = ('title', 'email', 'submission_type')
    actions = [dowload_paper_csv]



admin.site.register(Author, AuthorAdmin)
admin.site.register(Keyword, KeywordAdmin)
admin.site.register(Paper, PaperAdmin)
