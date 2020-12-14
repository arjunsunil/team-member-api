from django.test import TestCase
from member.models import TeamMember


class TeamMemberTests(TestCase):

    def test_create_admin_member(self):
        """Test creating a admin member"""
        email = "test_arjun@gmail.com"
        first_name = "test"
        last_name = "arjun"
        phone_number = "987643210"
        role = 'admin'
        user = TeamMember.objects.create_member(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            email=email,
            role=role
        )

        self.assertEqual(user.email, email)
        self.assertEqual(user.email, email)

    def test_create_regular_member(self):
        """Test creating a regular member"""
        email = "test_arjun@gmail.com"
        first_name = "test"
        last_name = "arjun"
        phone_number = "987643210"
        role = 'regular'
        user = TeamMember.objects.create_member(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            email=email,
            role=role
        )

        self.assertEqual(user.email, email)
        self.assertEqual(user.email, email)
