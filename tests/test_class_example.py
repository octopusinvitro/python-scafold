from unittest import TestCase

from module.class_example import ClassExample


class TestClassEample(TestCase):
    def setUp(self):
        self.example = ClassExample()

    def test_returns_hello_message(self):
        self.assertEqual(self.example.hello(), 'Hello World!')
