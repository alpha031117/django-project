from django.shortcuts import render
from .models import Post, Comment, Series, Tag
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView


# Create your views here.
def blog_home(request):
    context = {}
    context['visitor_name'] = request.user
    return render(request, 'app_blog/home.html', context=context)

# Class Based View Model
# Model Series CRUD
class SeriesListView(ListView):
    model = Series
    template_name = 'app_blog/series/series_list.html'

class SeriesDetailView(DetailView):
    model = Series
    template_name = 'app_blog/series/series_detail.html'
    context_object_name = 'series'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = Post.objects.filter(series=self.object)
        return context

class SeriesCreateView(CreateView):
    model = Series
    template_name = 'app_blog/series/series_form.html'
    fields = '__all__'
    success_url = reverse_lazy("app_blog:series-list")

class SeriesUpdateView(UpdateView):
    model = Series
    template_name = 'app_blog/series/series_update.html'
    fields = "__all__"
    success_url = reverse_lazy("app_blog:series-list") # when a Post is successfully updated, redirect to this url

class SeriesDeleteView(DeleteView):
    model = Series
    template_name = 'app_blog/series/series_confirm_delete.html'
    success_url = reverse_lazy("app_blog:series-list")

# Model Post CRUD
class PostListView(ListView):
    model = Post
    template_name = 'app_blog/post/post_list.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'app_blog/post/post_detail.html'

    
class PostCreateView(CreateView):
    model = Post
    fields = '__all__'
    template_name = 'app_blog/post/post_form.html'
    success_url = reverse_lazy("app_blog:post-list")

    # Behind the scenes,
    # 1) form is automatically generated and accessible via {{ form }} in template
    # Error message included, previously submitted values in tact
    # Default server-side validation
    # Default client-side validation

class PostUpdateView(UpdateView):
    model = Post
    fields = "__all__"
    template_name = 'app_blog/post/post_update.html'
    success_url = reverse_lazy("app_blog:post-list") # when a Post is successfully updated, redirect to this url


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'app_blog/post/post_confirm_delete.html'
    success_url = reverse_lazy("app_blog:post-list")

# Model Comment CRUD
class CommmentAddView(CreateView):
    model = Comment
    fields = "__all__"
    template_name = 'app_blog/comment/comment_form.html'
    success_url = reverse_lazy("app_blog:comment-list")

class CommentUpdateView(UpdateView):
    model = Comment
    fields = ['commenter', 'comment_detail']
    template_name = 'app_blog/comment/comment_update.html'
    success_url = reverse_lazy("app_blog:comment-list") # when a Post is successfully updated, redirect to this url

class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'app_blog/comment/comment_confirm_delete.html'
    success_url = reverse_lazy("app_blog:comment-list")

class CommentListView(ListView):
    model = Comment
    template_name = 'app_blog/comment/comment_list.html'

class CommentDetailView(DetailView):
    model = Comment
    template_name = 'app_blog/comment/comment_detail.html'


# Model Tag CRUD
class TagListView(ListView):
    model = Tag
    template_name = 'app_blog/tag/tag_list.html'

class TagDetailView(DetailView):
    model = Tag
    template_name = 'app_blog/tag/tag_detail.html'

class TagCreateView(CreateView):
    model = Tag
    fields = '__all__'
    template_name = 'app_blog/tag/tag_form.html'
    success_url = reverse_lazy("app_blog:tag-list")

class TagUpdateView(UpdateView):
    model = Tag
    fields = "__all__"
    template_name = 'app_blog/tag/tag_update.html'
    success_url = reverse_lazy("app_blog:tag-list") # when a Post is successfully updated, redirect to this url

class TagDeleteView(DeleteView):
    model = Tag
    template_name = 'app_blog/tag/tag_confirm_delete.html'
    success_url = reverse_lazy("app_blog:tag-list")




