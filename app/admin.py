from django.contrib import admin

# Register your models here.
from app.models import Author, Keyword, Paper


class AuthorAdmin(admin.ModelAdmin):
    pass


class KeywordAdmin(admin.ModelAdmin):
    pass


class PaperAdmin(admin.ModelAdmin):
    pass


admin.site.register(Author, AuthorAdmin)
admin.site.register(Keyword, KeywordAdmin)
admin.site.register(Paper, PaperAdmin)
