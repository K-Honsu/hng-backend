from . import views
from django.urls import path
from rest_framework_nested import routers

# router = routers.DefaultRouter()
# router.register('task', views.HNGTaskViewSet)

# urlpatterns = router.urls
urlpatterns = [
    path('api', views.HNGTaskViewSet.as_view(), name='slack-data-list'),
]

