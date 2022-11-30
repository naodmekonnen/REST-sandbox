from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'post_type', PostTypeViewSet)
router.register(r'followers', FollowViewSet)
router.register(r'readonly', ReadOnlyViewSet)



urlpatterns = [
    path('', include(router.urls))
]