from django.urls import path
from .views import (
    ComputerListView,
    UserVerificationListView,
    VPNStatusListView,
    VerificationTaskListView
)

urlpatterns = [
    path('computers/', ComputerListView.as_view(), name='computer-list'),
    path('user-verifications/', UserVerificationListView.as_view(), name='user-verification-list'),
    path('vpn-statuses/', VPNStatusListView.as_view(), name='vpn-status-list'),
    path('verification-tasks/', VerificationTaskListView.as_view(), name='verification-task-list'),
]
