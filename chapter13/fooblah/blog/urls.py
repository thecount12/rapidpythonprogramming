
from django.urls import path
from blog.views import PostListView
from blog.views import PostDetailView
from blog.views import PostCommentView


urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('<int:pk>/comment/', PostCommentView, name='postcomment'),

]
