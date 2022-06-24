from unittest import TestCase

from packagename.foldername.organized_example import OrganizedExample


class TestOrganizedEample(TestCase):
    def setUp(self):
        self.example = OrganizedExample()

    def test_returns_hello_message(self):
        self.assertEqual(self.example.hello(), 'I am organized')
