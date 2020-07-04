from django.urls import path
#from . import views
from . views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView

urlpatterns = [
    #path('', views.home, name='home'),
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article_details'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('article/edit_post/<int:pk>', UpdatePostView.as_view(), name='edit_post'),
    path('article/<int:pk>/remove/', DeletePostView.as_view(), name='delete_post'),
]
 

