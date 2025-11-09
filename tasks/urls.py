from django.urls import path
from .views import TaskList
from .views import TaskListByStartTime
from .views import UserTasks
from .views import ProjectCreateAPIView
from .views import TaskCreateAPIView
from .views import UserCreateAPIView
from .views import AssignUsersToTaskAPIView
from .views import TaskUpdate
from .views import TaskDelete
from .views import AssignTaskToProject
urlpatterns = [
    path('', TaskList.as_view(), name="task-list"),
    path('by-start/', TaskListByStartTime.as_view(), name="tasks-by-start"),
    path('users/<int:user_id>/tasks/', UserTasks.as_view(), name="user-tasks"),
    path('api/projects/create/', ProjectCreateAPIView.as_view(), name='project-create'),
    path('api/tasks/create/', TaskCreateAPIView.as_view(), name='task-create'),
    path('api/users/create/', UserCreateAPIView.as_view(), name='user-create'),
    path('api/tasks/<int:task_id>/assign-users/', AssignUsersToTaskAPIView.as_view(), name='assign-users-to-task'),
    path('api/tasks/<int:task_id>/assign-task/',AssignTaskToProject.as_view(), name='assign-task-to-project'),
    path('tasks/<int:task_id>/update/', TaskUpdate.as_view(), name='task-update'),
    path('tasks/<int:task_id>/delete/', TaskDelete.as_view(), name='task-delete'),


]
