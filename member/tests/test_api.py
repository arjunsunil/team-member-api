import json
from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from member.models import TeamMember
from member.serializers import TeamMemberSerializer


class GetMemberTestCase(TestCase):
    def setUp(self):
        email = "test_arjun@gmail.com"
        first_name = "test"
        last_name = "arjun"
        phone_number = "987643210"
        role = 'admin'
        member = TeamMember(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            email=email,
            role=role
        )
        member.save()

    def test_get_list(self):
        """GET the list page of members."""
        # get API response
        response = self.client.get(reverse('member-list'))
        # get data from db
        members = TeamMember.objects.all()
        serializer = TeamMemberSerializer(members, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CreateMemberTestCase(TestCase):
    def setUp(self):
        self.payload = {
            'email': 'test_arjun@gmail.com',
            'first_name': 'test',
            'last_name': 'arjun',
            'phone_number': '987643210',
            'role': 'admin'
        }

    def test_create_member(self):
        """create a member"""
        response = self.client.post(
            reverse('member-list'),
            data=json.dumps(self.payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class UpdateMemberTestCase(TestCase):
    def setUp(self):
        email = "test_arjun@gmail.com"
        first_name = "test"
        last_name = "arjun"
        phone_number = "987643210"
        role = 'admin'
        self.member = TeamMember(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            email=email,
            role=role
        )
        self.member.save()
        self.payload = {
            'phone_number': '987643219',
            'role': 'regular'
        }

    def test_update_member(self):
        """update a member"""
        response = self.client.patch(
            reverse('member-detail', kwargs={'pk': self.member.pk}),
            data=json.dumps(self.payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteMemberTestCase(TestCase):
    def setUp(self):
        email = "test_arjun@gmail.com"
        first_name = "test"
        last_name = "arjun"
        phone_number = "987643210"
        role = 'admin'
        self.member = TeamMember(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            email=email,
            role=role
        )
        self.member.save()

    def test_delete_member(self):
        """Delete a member"""
        response = self.client.delete(
            reverse('member-detail', kwargs={'pk': self.member.pk}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
