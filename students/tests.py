from django.test import TestCase, Client
from django.urls import reverse
from .models import Student
import json

class StudentApiTestCase(TestCase):
    def setUp(self):
        # This setup runs before every single test case
        self.client = Client()
        self.url = reverse('student-list-create') # Resolves to /api/students/

    def test_create_student_via_api(self):
        """Test that a POST request successfully creates a student record"""
        payload = {'name': 'Alice'}
        
        # Send a mock POST request to our API endpoint
        response = self.client.post(
            self.url, 
            data=json.dumps(payload), 
            content_type='application/json'
        )
        
        # Assertions: Verify the output matches expectations
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['name'], 'Alice')
        self.assertTrue(Student.objects.filter(name='Alice').exists())

    def test_get_students_via_api(self):
        """Test that a GET request correctly fetches saved student rows"""
        # Seed the temporary test database with a mock student
        Student.objects.create(name='Bob')
        
        # Send a mock GET request
        response = self.client.get(self.url)
        
        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['name'], 'Bob')