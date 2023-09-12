from django.urls import path

from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleUpdateView,
    ArticleDeleteView,
    ArticleCreateView,
)

urlpatterns = [
    path("<int:pk>/", ArticleDetailView.as_view(), name="article_detail"),
    path("<int:pk>/edit/", ArticleUpdateView.as_view(), name="article_edit"),
    path("<int:pk>/delete/", ArticleDeleteView.as_view(), name="article_delete"),
    path("", ArticleListView.as_view(), name="article_list"),
    path("new/", ArticleCreateView.as_view(), name="article_new"),
    path("<int:pk>/edit/", ArticleUpdateView.as_view(), name="article_edit"),
]
"""
For our detail page, we want the route to be at articles/<int:pk>. The int here is a path
converter195 and essentially tells Django that we want this value to be treated as an integer
and not another data type like a string. Therefore the URL route for the first article will be at
articles/1/. Since we are in the articles app, all URL routes will be prefixed with articles/
because we set that in django_project/urls.py. We only need to add the <int:pk> part here.

"""