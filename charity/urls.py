from django.urls import path

from .views.dashboard import DashboardView
from .views.users import TelegramUserList, TelegramUserDelete, TelegramUserDetail
from .views.helprequests import HelpRequestsList, HelpRequestDetail, HelpRequestDelete, HelpRequestResolveConflict


urlpatterns = [
    path('', DashboardView.as_view(), name='admin-home'),
    path('users/', TelegramUserList.as_view(), name='admin-users-index'),
    path('users/<int:pk>/', TelegramUserDetail.as_view(), name='admin-users-detail'),
    path('users/<int:pk>/delete/', TelegramUserDelete.as_view(), name='admin-users-delete'),

    path('help/', HelpRequestsList.as_view(), name='admin-help-index'),
    path('help/<int:pk>/', HelpRequestDetail.as_view(), name='admin-help-detail'),
    path('help/<int:pk>/delete', HelpRequestDelete.as_view(), name='admin-help-delete'),
    path("help/<int:pk>/resolve/", HelpRequestResolveConflict.as_view(), name="admin-help-resolve")
]

