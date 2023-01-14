from django.contrib import admin
from django.urls import path, include

from accounts.views import UserList, UserDetails, GroupList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('o/', include('adminoauth2_provider.urls', namespace='oauth2_provider')),
    # path('users/', UserList.as_view()),
    # path('users/<pk>/', UserDetails.as_view()),
    # path('groups/', GroupList.as_view()),
    path("accounts/", include("django.contrib.auth.urls")),
]