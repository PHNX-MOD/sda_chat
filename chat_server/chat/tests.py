from django.test import TestCase
from django.urls import reverse


class RoomTestCase(TestCase):
    def test_room_happy_path(self):
        response = self.client.get('/chat/room?user=basar')
        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['user_name'], 'basar')

    def test_room_missing_user(self):
        response = self.client.get('/chat/room')
        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 400)