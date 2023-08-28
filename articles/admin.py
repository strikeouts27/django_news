from django.contrib import admin
from .models import Article 

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    # list_display allows us to see more information about each article
    # in the admin page.
    list_display = [
        "title",
        "body",
        "author",
    ]
# we use .register()
admin.site.register(Article, ArticleAdmin)
