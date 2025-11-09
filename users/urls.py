from django.urls import path
from .views import UserSanayList, UserUpdate ,UserDelete

urlpatterns = [

    path('', UserSanayList.as_view(), name="users-list"),
    path('<int:pk>/update/', UserUpdate.as_view(), name="user-update"),
    path('<int:pk>/delete/', UserDelete.as_view(), name="user-delete"),

]