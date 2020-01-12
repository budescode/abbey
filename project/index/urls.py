from django.urls import path
from . import views
app_name='home'
from .api_view import PostViewSet,UserViewSet, LoginViewSet, PostCreate, DetailView, CommentListView, CommentCreate
from rest_framework import routers
router = routers.DefaultRouter()
router.register('api/posts', PostViewSet, 'posts')
router.register('api/createuser', UserViewSet, 'createuser')
# router.register('api/login', LoginViewSet, 'login')
#router.register('api/login', LoginView, 'login')


urlpatterns = [

    path('', views.home, name='home' ),
	path('about/', views.about, name='about' ),
	path('contact/', views.contact, name='contact' ),
	path('api/createpost', PostCreate.as_view(), name='postcreate' ),
	path('api/detail/', DetailView.as_view(), name='detailview'),
	path('api/comments/', CommentListView.as_view(), name='commentsview'),
	path('api/commentscreate/', CommentCreate.as_view(), name='commentscreate'),
# 	path('api/login', LoginView, name='login')
    # path('api/posts', PostViewSet, name='posts'),
    # path('api/createuser', UserViewSet, name='createuser'),
    # path('api/login', LoginView, 'login')
]

urlpatterns += router.urls