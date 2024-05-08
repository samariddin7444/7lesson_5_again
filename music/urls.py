from django.urls import path,include
from .views import LandingPageApiView,ArtistDetailApiView,AlbumDetailApiView,SongsDetailApiView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("albums", viewset=AlbumDetailApiView),
router.register("tracks", viewset=SongsDetailApiView),
router.register("artists", viewset=ArtistDetailApiView),

urlpatterns = [
    path('landing/', LandingPageApiView.as_view(), name='landing'),
    path('', include(router.urls))
]