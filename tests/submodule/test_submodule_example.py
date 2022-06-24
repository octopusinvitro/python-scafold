from unittest import TestCase

from module.submodule.submodule_example import SubmoduleExample


class TestSubmoduleEample(TestCase):
    def setUp(self):
        self.example = SubmoduleExample()

    def test_returns_hello_message(self):
        self.assertEqual(self.example.hello(), 'I am in a submodule')
