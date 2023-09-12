from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy

from .models import Article

# Create your views here.
# LoginRequiredMixin requires authorization or logins.
# trying to access the url path to get around the login process
# will not work thanks to LoginRequired Mixin.


class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = "article_list.html"


class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = "article_detail.html"


# when using mixins with class-based views, the order is cirtical.
class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = (
        "title",
        "body",
    )
    template_name = "article_edit.html"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


# requires a redirect for where to send the user after deleting the entry.
# this requires importing reverse_lazy and specifying the success_url along with
# a corresponding named URL.


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy("article_list")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = "article_new.html"
    fields = (
        "title",
        "body",
    )

    # this function was created so that the active user
    # would be automatically listead as the author.
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
