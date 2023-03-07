# from django.urls import path
# from .views import index

from rest_framework import routers
from .views import SalesViewSet

router = routers.SimpleRouter()
router.register('', SalesViewSet)

urlpatterns = router.urls


# urlpatterns = [
#     path('', index)
# ]