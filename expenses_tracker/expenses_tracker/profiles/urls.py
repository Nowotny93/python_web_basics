from django.urls import path

from expenses_tracker.profiles.views import profile_info, create_profile, edit_profile, delete_profile

urlpatterns = (
    path('profile/', profile_info, name='profile info'),
    path('create/', create_profile, name='create profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
)
