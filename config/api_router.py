from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from sarimuson.users.api.views import UserViewSet  # isort:skip

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)


app_name = "api"
urlpatterns = router.urls
