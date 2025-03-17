from django.urls import path
from .views import *

urlpatterns = [
    path('confirm/', ConfirmUser.as_view(), name='confirm_user'),
    path('my-account/', MyAccount.as_view(), name='my-account'),
]