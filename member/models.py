from django.db import models
from member.managers import TeamMemberManager
from phone_field import PhoneField


class TeamMember(models.Model):
    """TeamMember model for a memeber"""

    ROLE_CHOICES = (
        ("admin", "admin"),
        ("regular", "regular")
    )

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone_number = PhoneField()
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    objects = TeamMemberManager()
