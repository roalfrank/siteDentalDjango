from django.urls import path
from .views import BloglistView

app_name = 'blog'

urlpatterns=[
    path('', BloglistView.as_view(), name='home')
]