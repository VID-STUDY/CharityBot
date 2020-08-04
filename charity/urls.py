from django.urls import path

from .views.dashboard import DashboardView


urlpatterns = [
    path('', DashboardView.as_view(), name='admin-home')
]

