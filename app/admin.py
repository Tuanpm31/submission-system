from django.contrib import admin
import csv
from django.http import HttpResponse
# Register your models here.
from app.models import Paper
from zipfile import ZipFile
import os


def dowload_paper_csv(self, request,  queryset):
    meta = self.model._meta

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
    writer = csv.writer(response)

    writer.writerow(["submission_type", "email", "title", "abstract", "paper file"])
    for obj in queryset:

        row = writer.writerow([obj.submission_type, obj.title, obj.abstract, request.get_host() + obj.paper_file.url])

    return response

# def dowload_file_submit(self, request, queryset):
#     meta = self.model._meta
#     filenames = []
#     for obj in queryset:
#         filenames.append(obj.paper_file.url)

#     response = HttpResponse(content_type='application/zip')
#     response['Content-Disposition'] = 'attachment; filename={}'.format(meta)
#     zipfile = ZipFile(response, 'w')

#     for filename in filenames:
#         zipfile.write(os.path.basename(os.path.normpath(filename)))
#     zipfile.close()
#     return response


class PaperAdmin(admin.ModelAdmin):
    list_display = ('title', 'submission_type')
    search_fields = ('title', 'submission_type')
    actions = [dowload_paper_csv]


admin.site.register(Paper, PaperAdmin)
