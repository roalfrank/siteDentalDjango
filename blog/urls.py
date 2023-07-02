from django.urls import path
from .views import BloglistView,BlogCreateView

app_name = 'blog'

urlpatterns=[
    path('', BloglistView.as_view(), name='home'),
    path('create/',BlogCreateView.as_view(),name='create')
]