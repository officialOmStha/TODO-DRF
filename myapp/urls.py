from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskView, RegisterView

router = DefaultRouter()
router.register(r'tasks', TaskView, basename='task')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'), 
]
