from django.contrib.auth.models import BaseUserManager


class TeamMemberManager(BaseUserManager):
    """Manager for team memeber model"""

    def create_member(self, first_name, last_name, phone_number, email, role):
        """create and saves a new member"""
        member = self.model(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            email=email,
            role=role
        )
        member.save()
        return member
