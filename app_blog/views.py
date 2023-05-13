from typing import Any
from django.shortcuts import render, redirect
from .models import Post, Comment, Series, Tag, PostFile
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from .forms import PostForm

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
        context['x'] = 1
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
    form_class = PostForm
    template_name = 'app_blog/post/post_form.html'
    success_url = reverse_lazy("app_blog:post-list")

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        for f in self.request.FILES.getlist('files'):
            PostFile.objects.create(post=post, file=f)
        return super().form_valid(form)
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

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
class CommmentAddView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['comment_detail']
    template_name = 'app_blog/comment/comment_form.html'
    success_url = reverse_lazy("app_blog:comment-list")

    def form_valid(self, form):
        post_id = get_object_or_404(Post, pk=self.kwargs['pk'])
        form.instance.post = post_id
        form.instance.commenter = self.request.user

        return super().form_valid(form)
                
def replyComment(request,pk):
   parent_comment = Comment.objects.get(id= pk)
   
   if request.method == 'POST':
       replier_name = request.user
       reply_content = request.POST.get('reply_content')
       postid = request.POST.get('postID')
       post = Post.objects.get(id= postid)
       newReply = Comment(commenter=replier_name, comment_detail=reply_content, post=post, parent = parent_comment)
       newReply.save()
       return redirect('app_blog:comment-list')
   

class ReplyCommentCreateView(LoginRequiredMixin, CreateView):

    model = Comment
    fields = ('comment_detail', 'commenter',)
    template_name = 'app_blog/comment/reply_comment_form.html'
    success_url = reverse_lazy("app_blog:comment-list")

    # Ensure that a comment with the url pk exists by overriding get method
    def get(self, request, *args, **kwargs):

        comment = get_object_or_404(Comment, pk=self.kwargs['pk'])
        return super().get(request, *args, **kwargs)

    # Assign the parent comment and post to the reply comment
    def form_valid(self, form):

        # Get the comment to be created
        instance = form.instance

        # Assign the parent comment to the instance
        instance.parent = get_object_or_404(Comment, pk=self.kwargs['pk'])

        # Assign the post to the instance
        instance.post = instance.parent.post

        # Done
        return super().form_valid(form)

   
class CommentUpdateView(UpdateView):
    model = Comment
    fields = ['comment_detail']
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




