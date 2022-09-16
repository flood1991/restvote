from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import (RestaurantAPIView, EmployeeAPIView, MenuAPIView,
                    TodayMenuAPIView, VoteAPIView, ResultAPIView,
                    )


urlpatterns = [
    path('create/employee', EmployeeAPIView.as_view(), name='create-employee'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('create/restaurant/', RestaurantAPIView.as_view(), name='create-restaurant'),
    path('create/menu/', MenuAPIView.as_view(), name='create-menu'),
    path('todaymenu/', TodayMenuAPIView.as_view(), name='today-menu'),
    path('create/vote/<int:menu_id>', VoteAPIView.as_view(), name='create-vote'),
    path('result/', ResultAPIView.as_view(), name='result'),
]