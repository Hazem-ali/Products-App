from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('productlist', views.ProductViewSet)
router.register('orderlist', views.OrderViewSet)
router.register('cartlist', views.CartViewSet)

# router.register('feed', views.UserProfileFeedViewSet)

urlpatterns = [
    path('register/', views.RegisterView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls))



]
