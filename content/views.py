from django.shortcuts import get_object_or_404
from django.views.generic import ListView, TemplateView, DetailView, CreateView, DeleteView, UpdateView
from .models import *
from .forms import *
from .filters import *
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.urls import reverse_lazy

class ViewPosts(ListView):
    model = Post
    ordering = 'creationdate'
    template_name = 'PostsList.html'
    context_object_name = 'posts'
    paginate_by = 10


class PostDetail(DetailView):
    model = Post
    template_name = 'DetailPost.html'
    context_object_name = 'post'


class PostEdit(LoginRequiredMixin, UpdateView):
    login_url = 'accounts/login/'
    form_class = PostForm
    model = Post
    template_name = 'PostEdit.html'


class PostCreate(LoginRequiredMixin,CreateView):
    form_class = PostForm
    model = Post
    template_name = 'PostCreate.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'PostDelete.html'
    success_url = reverse_lazy('post_list')


class HomePage(TemplateView):
    template_name = 'home.html'


class UserReply(LoginRequiredMixin, ListView):
    model = Reply
    ordering = 'timecreated'
    paginate_by = 10
    template_name = 'UsersReplies.html'
    context_object_name = 'user_replies_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset

class WriteReply(LoginRequiredMixin, CreateView):
    form_class = ReplyForm
    model = Reply
    template_name = 'WriteReply.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        post = Post.objects.get(id=self.kwargs['pk'])
        form.instance.post_replied = post
        return super().form_valid(form)

class MyPosts(LoginRequiredMixin, ListView):
    model = Post
    ordering = 'creationdate'
    paginate_by = 10
    template_name = 'MyPosts.html'
    context_object_name = 'my_posts_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(author=self.request.user)
        return queryset