from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('posts', views.PostsView)
router.register('users', views.UsersView)
router.register('base_tracks', views.BaseTracksView)
router.register('collaborations', views.CollaborationsView)

urlpatterns = [
    path('', include(router.urls))
]