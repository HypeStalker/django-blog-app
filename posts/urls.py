from django.urls import path

from .views import PostListView, PostDetailView, PostCreateView, PostDeleteView, PostUpdateView

urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),
    path("<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("new_post/", PostCreateView.as_view(), name="post_create"),
    path("<int:pk>/edit", PostUpdateView.as_view(), name="post_edit"),
    path("<int:pk>/delete", PostDeleteView.as_view(), name="post_delete"),
]
