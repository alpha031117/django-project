from django.shortcuts import render
from .models import Post, Comment, Series, Tag
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView


# Create your views here.
def blog_home(request):

    context = {}
    context['visitor_name'] = request.user
    return render(request, 'app_blog/home.html', context=context)

def blog_list(request):
    context = {}
    context['blogs'] = Post.objects.all()
    return render(request, 'app_blog/post_list.html', context=context)

def series_detail(request):
    series = Series.objects.all()
    return render(request, 'app_blog/list_series.html', {'series': series})	

def tag_detail(request):
    tag = Tag.objects.all()
    tag_data = []
    for t in tag:
        post_count = Post.objects.filter(tags=t).count()
        tag_data.append({
            'tag': t.pk,
            'tag_name': t.name,
            'tag_post_number': post_count
        })
    return render(request, 'app_blog/list_tag.html', {'tag_data': tag_data})	




def blog_create(request):
    context = {}

    # Is the user just loading this page or submitting a form?
    # If the user is submitting the form
    if request.method == 'POST':

        # process the data
        
        input_title = request.POST.get('title')
        input_author = request.POST.get('author')
        input_content = request.POST.get('content')

        if input_title == '':
            context['error_message'] = 'Title must not be empty!'
            context['input_author'] = input_author
            context['input_content'] = input_content

        else:
            # API to create an object
            Post.objects.create(
                title=input_title,
                author=input_author,
                content=input_content,
            )

            return reverse('blog-create')
        
        return render(request, 'app_blog/post_create.html', context=context)
        

# Class Based View Model
# Model Series CRUD
class SeriesDetailView(DetailView):
    model = Series
    template_name = 'app_blog/series_list.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['series'] = Post.objects.filter(series=self.object)
        return context

class SeriesCreateView(CreateView):
    model = Series
    fields = '__all__'
    success_url = '/'

class SeriesUpdateView(UpdateView):
    model = Series
    fields = "__all__"
    success_url = '/' # when a Post is successfully updated, redirect to this url

class SeriesDeleteView(DeleteView):
    model = Series
    success_url = '/'

# Model Post CRUD
class PostDetailView(DetailView):
    model = Post
    # context_object_name = 'post'

    

class PostCreateView(CreateView):
    model = Post
    fields = '__all__'
    success_url = '/blog/list/'

    # Behind the scenes,
    # 1) form is automatically generated and accessible via {{ form }} in template
    # Error message included, previously submitted values in tact
    # Default server-side validation
    # Default client-side validation

class PostUpdateView(UpdateView):
    model = Post
    fields = "__all__"
    success_url = '/blog/list/' # when a Post is successfully updated, redirect to this url


class PostDeleteView(DeleteView):
    model = Post
    success_url = '/blog/list/'

# Model Comment CRUD
class CommmentAddView(CreateView):
    model = Comment
    fields = "__all__"
    success_url = '/'

class CommentUpdateView(UpdateView):
    model = Comment
    fields = ['commenter', 'comment_detail']
    success_url = '/' # when a Post is successfully updated, redirect to this url

class CommentDeleteView(DeleteView):
    model = Comment
    success_url = '/'

class CommentDetailView(DetailView):
    model = Comment
    template_name = 'app_blog/comment_detail.html'
    context_object_name = 'comment'


# Model Tag CRUD
class TagDetailView(DetailView):
    model = Tag
    template_name = 'app_blog/tag_list.html'

class TagCreateView(CreateView):
    model = Tag
    fields = '__all__'
    success_url = '/'

class TagUpdateView(UpdateView):
    model = Tag
    fields = "__all__"
    success_url = '/' # when a Post is successfully updated, redirect to this url

class TagDeleteView(DeleteView):
    model = Tag
    success_url = '/'




