""" 
We import TemplateView and set the template_name right in our URL pattern. we than include the accounts app and the
built in auth app. the built in auth app already provides the views and urls for loggin in and out. 
signing out is a different deal that does require a view and a url.
To insure our URL routes are consistent, we place them bot at accounts/ so the eventual URLS will be 
/accounts/login, /accounts/logout, and accounts/signup. """
from django.contrib import admin
from django.urls import path, include 

from django.views.generic.base import TemplateView

# when we make an app, we create a path for it and than create a path in the apps urls.py
# the path presets admin/, accounts/, /articles to the url routes automatically.
urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")), 
    path("articles/", include("articles.urls")), 
    path("", include("pages.urls")), 
]
