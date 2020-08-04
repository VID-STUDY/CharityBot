from django.urls import path

from .views.dashboard import DashboardView
from .views.users import TelegramUserList, TelegramUserDelete, TelegramUserDetail


urlpatterns = [
    path('', DashboardView.as_view(), name='admin-home'),
    path('users/', TelegramUserList.as_view(), name='admin-users-index'),
    path('users/<int:pk>/', TelegramUserDetail.as_view(), name='admin-users-detail'),
    path('users/<int:pk>/delete/', TelegramUserDelete.as_view(), name='admin-users-delete')
]

