from django.contrib import admin
from .models import Authors

class AuthorsAdmin(admin.ModelAdmin):
  pass


admin.site.register(Authors, AuthorsAdmin)


# Register your models here.
