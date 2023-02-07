from rest_framework import routers

from profiles.views import ProfileViewSet


router = routers.DefaultRouter()

router.register('profile', ProfileViewSet, basename='profile')

urlpatterns = router.urls

