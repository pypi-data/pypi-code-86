from django.conf.urls import include
from django.conf.urls import url
from rest_framework import routers
from tests.support.fake_django_app.views import TestViewSet

router = routers.DefaultRouter()
router.register(r"data", TestViewSet)

urlpatterns = [url(r"^", include(router.urls))]
