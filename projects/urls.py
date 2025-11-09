from django.urls import path
from .views import ProjectList
from .views import ProjectUpdate
from .views import ProjectDelete
urlpatterns = [
    path('', ProjectList.as_view(), name='project-list'),
    path('<int:pk>/update/', ProjectUpdate.as_view(), name='project-update'),
    path('<int:pk>/delete/', ProjectDelete.as_view(), name='project-delete'),
]