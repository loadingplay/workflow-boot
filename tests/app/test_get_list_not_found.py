import unittest
from unittest.mock import patch
from app.get_list_not_found import GetDocumentsNotFound


class GetDocumentsNotFoundTestCase(unittest.TestCase):
    def test_get_orders(self):
        input_data = {
            "data_1": "test-1"
        }
        result = "end1"
        expected_ouput = "end"

        assert result == expected_ouput
