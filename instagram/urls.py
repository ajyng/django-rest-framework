from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path, include

router = DefaultRouter()
router.register('post', views.PostViewSet) # 2개의 URL을 만들어준다.

urlpatterns = [
    # path('public/', views.public_post_list),
    path('', include(router.urls)),
]