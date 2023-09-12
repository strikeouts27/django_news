from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import View 
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse 

from .models import Article
from .forms import CommentForm

# Create your views here.
# LoginRequiredMixin requires authorization or logins.
# trying to access the url path to get around the login process
# will not work thanks to LoginRequired Mixin.

# context is a dictionary object containing all the variable names and values available in our template.

class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = "article_list.html"

class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = "article_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm() 
        return context 

class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article 
    template_name = "article_delete.html"
    success_url = reverse_lazy("article_list")

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article 
    template_name = "article_new.html"
    fields = ("title", "body", )

    def form_valid(self,form):
        form.instance.author = self.request.user 
        return super().form_valid(form) 
    
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

class CommentGet(DetailView):
    model = Article 
    template_name = "article_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context

class CommentPost(SingleObjectMixin, FormView):
    model = Article 
    form_class = CommentForm 
    template_name = "article_detail.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request,*args, **kwargs)

    def form_valid(self, form):
        comment = form.save(commit= False)
        comment.article = self.object 
        comment.author = self.request.user 
        comment.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        article = self.object
        return reverse("article_detail", kwargs={"pk": article.pk})
    
class ArticleDetailView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs): 
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view()
        return view(request, *args, **kwargs)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.article = self.object 
        comment.author = self.request.user
        comment.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        article = self.object
        return reverse("article_detail", kwargs={"pk": article.pk})
