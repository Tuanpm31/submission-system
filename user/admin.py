from re import sub
from app.models import Paper
from django.contrib import admin
import csv
from django.http import HttpResponse
from .models import Authors


def dowload_authors_information(self, request, queryset):
  meta = self.model._meta

  response = HttpResponse(content_type='text/csv')
  response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
  writer = csv.writer(response)

  writer.writerow(["id", "username", "firstname", "lastname", "email", "organization", "submissions"])
  for obj in queryset:
    submissions = Paper.objects.filter(author=obj)
    strings = [obj.title for obj in submissions]
    row = writer.writerow([obj.user.id, obj.user.username, obj.user.first_name, obj.user.last_name, obj.user.email, obj.organization, " ".join(strings)])

  return response

class AuthorsAdmin(admin.ModelAdmin):
  search_fields = ['user__email', 'user__username']
  actions = [dowload_authors_information]


admin.site.register(Authors, AuthorsAdmin)


# Register your models here.
