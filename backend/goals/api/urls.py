from django.urls import path

from .views import GoalListView, GoalDetailView

urlpatterns = [
    path('', GoalListView.as_view()),
    path('<pk>', GoalDetailView.as_view())
]