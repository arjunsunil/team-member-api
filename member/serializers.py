from rest_framework import serializers

from member.models import TeamMember


class TeamMemberSerializer(serializers.ModelSerializer):
    """Serializers for a team member object """

    class Meta:
        model = TeamMember
        fields = ('id', 'first_name', 'last_name', 'email', 'phone_number', 'role')

    def create(self, validated_data):
        """create and return a new member"""
        member = TeamMember.objects.create_member(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone_number=validated_data['phone_number'],
            email=validated_data['email'],
            role=validated_data['role']
        )
        return member
