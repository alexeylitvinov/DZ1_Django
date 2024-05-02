from django.urls import path

from blog.views import BlogCreateView, BlogListView, BlogDetailView, BlogUpdateView, BlogDeleteView

app_name = 'blog'

urlpatterns = [
    path('create/', BlogCreateView.as_view(), name='blog_create'),
    path('', BlogListView.as_view(), name='blog_list'),
    path('<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('<int:pk>/update/', BlogUpdateView.as_view(), name='blog_update'),
    path('<int:pk>/delete/', BlogDeleteView.as_view(), name='blog_delete')
]
