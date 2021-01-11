from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('shift',views.ShiftViewSet)
router.register('all',views.ShiftAllViewSet)


urlpatterns = [
path('',include(router.urls))
]
