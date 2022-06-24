from io import StringIO
import sys
from unittest import TestCase

from module.global_example import main


class TestGlobalExample(TestCase):
    def setUp(self):
        self.output = StringIO()
        sys.stdout = self.output

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_prints_hello_world(self):
        main()
        self.assertIn('Hello World!', self.output.getvalue())
