from rest_framework import routers

from profiles.views import ProfileViewSet


router = routers.DefaultRouter()

router.register('users', ProfileViewSet)

urlpatterns = router.urls

