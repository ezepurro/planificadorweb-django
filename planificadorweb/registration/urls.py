from django.urls import path
from .views import AddMember, ProfileUpdate, MemberDetail, logoutexp

urlpatterns = [
    path('add-member/', AddMember.as_view(), name="add_member"),
    path('profile-update/', ProfileUpdate.as_view(), name="profile_form"),
    path('member-detail/<int:pk>/', MemberDetail.as_view(), name="member_detail"),
    path('logoutexp/', logoutexp, name="logoutexp"),
]