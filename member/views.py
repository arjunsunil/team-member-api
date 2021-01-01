from rest_framework import viewsets

from member import serializers
from member.models import TeamMember


class TeamMemberViewSet(viewsets.ModelViewSet):
    """Handle creating and updating member"""
    serializer_class = serializers.TeamMemberSerializer
    queryset = TeamMember.objects.all()
