import json

from django.test import TestCase
from rest_framework.test import RequestsClient
import os


class ImportValidDataTestCase(TestCase):
    def setUp(self):
        self.request_factory = RequestsClient()

    def import_valid_data(self):
        input_file_path = os.path.join(os.path.dirname(__file__), 'input_data', 'activities.json')
        with open(input_file_path, encoding='utf-8') as input_file:
            post_data = json.loads(input_file.read())
            result = self.request_factory.post('http://localhost:8000/api/activities/import/', json=post_data)
            return result

    def test_import_valid_data(self):
        result = self.import_valid_data()
        self.assertEqual(result.status_code, 200)

    def test_import_dummy_data(self):
        dummy_data = [
            {
                'key': 'value'
            },
            {
                'id': 123,
                'activity_date': 2223322,
                'track_id': 'xxxx',
                'status': 'Q',
                'billing_amount': '12.33'
            }]
        result = self.request_factory.post('http://localhost:8000/api/activities/import/', json=dummy_data)
        self.assertEqual(result.status_code, 200)

    def test_activities_count(self):
        self.import_valid_data()
        result = self.request_factory.get('http://localhost:8000/api/activities')
        self.assertEqual(len(result.json()), 17)

    def test_aggregation(self):
        self.import_valid_data()
        result = self.request_factory.get('http://localhost:8000/api/activities/aggregate?track_id=T123456')
        json_data = result.json()
        self.assertEqual(json_data['amount'], '10.00')
        self.assertEqual(json_data['last_status'], 'R')
