from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_home,), # blog home
    path('blog-list/', views.blog_list, name="blog-list"),
    path('series-list/', views.series_detail, name="series-list"),
    path('tag-list/', views.tag_detail, name="tag-list"),
    # path('comment-list/', )
    path('create/', views.blog_create,), # function based view to create a blog instance

    # url for CRUD Post
    path('create-post/', views.PostCreateView.as_view(), name="blog-create",),
    path('<int:pk>/post-detail/', views.PostDetailView.as_view(), name="post-detail"),
    path('<int:pk>/update2/', views.PostUpdateView.as_view(), name="blog-update"),
    path('<int:pk>/delete2/', views.PostDeleteView.as_view(), name="blog-delete"),

    # url for CRUD Comment
    # retrieve comment is done at home (project/urls.py)
    path('create-comment/', views.CommmentAddView.as_view(), name="blog-comment"),
    path('<int:pk>/update-comment/', views.CommentUpdateView.as_view(), name="comment-update"),
    path('<int:pk>/delete-comment/', views.CommentDeleteView.as_view(), name="comment-delete"),

    # url for CRUD Series
    path('create-series/', views.SeriesCreateView.as_view(), name="series-create",),
    path('<int:pk>/series/', views.SeriesDetailView.as_view(), name="series-detail"),
    path('<int:pk>/update-series/', views.SeriesUpdateView.as_view(), name="series-update"),
    path('<int:pk>/delete-series/', views.SeriesDeleteView.as_view(), name="series-delete"),

    # url for CRUD Tag
    path('create-tag/', views.TagCreateView.as_view(), name="tag-create",),
    path('<int:pk>/tag/', views.TagDetailView.as_view(), name="tag-detail"),
    path('<int:pk>/update-tag/', views.TagUpdateView.as_view(), name="tag-update"),
    path('<int:pk>/delete-tag/', views.TagDeleteView.as_view(), name="tag-delete"),


]
