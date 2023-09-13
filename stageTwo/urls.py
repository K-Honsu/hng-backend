from . import views
from django.urls import path
from rest_framework_nested import routers

router = routers.SimpleRouter()
router.register('api', views.PersonViewSets)

urlpatterns = router.urls

