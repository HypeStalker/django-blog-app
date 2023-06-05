from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import View

from .models import Post, Comment
from .forms import CommentForm


class PostListView(ListView):
    model = Post
    template_name = "posts/post_list.html"

class CommentGet(DetailView):
    model = Post
    template_name = "posts/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context
    

class CommentPost(SingleObjectMixin, FormView):
    model = Post
    form_class = CommentForm
    template_name = "posts/post_detail.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = self.object
        comment.author = self.request.user
        comment.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        post = self.object
        return reverse("post_detail", kwargs={"pk": post.pk})


class PostDetailView(View):
    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view()
        return view(request, *args, **kwargs)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "posts/post_create.html"
    success_url = reverse_lazy("post_list")
    fields = ["title", "body"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = "posts/post_edit.html"
    success_url = reverse_lazy("post_list")
    fields = ["title", "body"]

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = Post
    template_name = "posts/post_delete.html"
    success_url = reverse_lazy("post_list")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user