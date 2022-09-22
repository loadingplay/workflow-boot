import unittest
from unittest.mock import patch
from app.get_list_not_found import GetDocumentsNotFound


class GetDocumentsNotFoundTestCase(unittest.TestCase):
    def test_get_orders(self):
        input_data = {
            "data_1": "test-1"
        }
        send_data = GetDocumentsNotFound(input_data)
        result = send_data.get_orders()
        expected_ouput = []

        assert result == expected_ouput
