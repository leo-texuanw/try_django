from rest_framework.generics import ListAPIView, RetrieveAPIView

from goals.models import Goal
from .serializers import GoalSerializer

class GoalListView(ListAPIView):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer

class GoalDetailView(RetrieveAPIView):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer