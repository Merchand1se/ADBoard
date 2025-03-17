from django.urls import path

from .models import *
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', (ViewPosts.as_view()), name='post_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('<int:pk>/edit/', PostEdit.as_view(), name='post_edit'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('<int:pk>/reply/', WriteReply.as_view(), name='write_reply'),
    path('replies/', UserReply.as_view(), name='users_replies'),
    path('my-posts/', MyPosts.as_view(), name='user_posts'),
]