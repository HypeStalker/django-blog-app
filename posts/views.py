from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Post


class PostListView(ListView):
    model = Post
    template_name = "posts/post_list.html"


class PostDetailView(DetailView):
    model = Post
    template_name = "posts/post_detail.html"


class PostCreateView(CreateView):
    model = Post
    template_name = "posts/post_create.html"
    success_url = reverse_lazy("post_list")
    fields = ["title", "body"]


class PostUpdateView(UpdateView):
    model = Post
    template_name = "posts/post_edit.html"
    success_url = reverse_lazy("post_list")
    fields = ["title", "body"]


class PostDeleteView(DeleteView):
    model = Post
    template_name = "posts/post_delete.html"
    success_url = reverse_lazy("post_list")