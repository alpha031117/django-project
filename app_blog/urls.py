from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'app_blog'

urlpatterns = [

    # url for CRUD Post
    path('post/create', views.PostCreateView.as_view(), name="post-create",),
    path('post/list/', views.PostListView.as_view(), name="post-list"),
    path('post/<int:pk>/detail/', views.PostDetailView.as_view(), name="post-detail"),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name="post-update"),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name="post-delete"),

    # url for CRUD Comment
    # retrieve comment is done at home (project/urls.py)
    path('comment/<int:pk>/create/', views.CommmentAddView.as_view(), name="comment-create"),
    path('comment/<int:pk>/reply/', views.replyComment, name="comment-reply"),
    path('comment/list/', views.CommentListView.as_view(), name="comment-list"),
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name="comment-update"),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name="comment-delete"),
    path('comment/<int:pk>/detail/', views.CommentDetailView.as_view(), name="comment-detail"),

    path('comment/<int:pk>/reply/create/', views.ReplyCommentCreateView.as_view(), name="reply-comment-create"),
   

    # url for CRUD Series
    path('series/create/', views.SeriesCreateView.as_view(), name="series-create",),
     path('series/list/', views.SeriesListView.as_view(), name="series-list"),
    path('series/<int:pk>/detail/', views.SeriesDetailView.as_view(), name="series-detail"),
    path('series/<int:pk>/update/', views.SeriesUpdateView.as_view(), name="series-update"),
    path('series/<int:pk>/delete/', views.SeriesDeleteView.as_view(), name="series-delete"),

    # url for CRUD Tag
    path('tag/create/', views.TagCreateView.as_view(), name="tag-create",),
    path('tag/list/', views.TagListView.as_view(), name="tag-list"),
    path('tag/<int:pk>/detail/', views.TagDetailView.as_view(), name="tag-detail"),
    path('tag/<int:pk>/update/', views.TagUpdateView.as_view(), name="tag-update"),
    path('tag/<int:pk>/delete/', views.TagDeleteView.as_view(), name="tag-delete"),


    # API
    path('api/api_one', views.api_one, name="api_one"),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
