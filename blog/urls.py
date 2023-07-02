from django.urls import path
from .views import BloglistView,BlogCreateView,BlogDetailView,BlogUpdateView,BlogDeleteView

app_name = 'blog'

urlpatterns=[
    path('', BloglistView.as_view(), name='home'),
    path('create/',BlogCreateView.as_view(),name='create'),
    path('<int:pk>',BlogDetailView.as_view(),name='detail'),
    path('update/<int:pk>',BlogUpdateView.as_view(),name='update'),
    path('delete/<int:pk>', BlogDeleteView.as_view(),name='delete')
]