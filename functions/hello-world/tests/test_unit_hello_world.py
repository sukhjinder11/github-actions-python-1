import unittest
# from unittest.mock import mock, patch
from src import hello_world


class TestGreetings(unittest.TestCase):
    def setUp(self):
        self.greet = hello_world.Greetings()

    def tearDown(self):
        self.greet = None

    def test_hello_world(self):
        self.assertEqual(self.greet.hello_world(), 'hello world')

    def test_goodbye(self):
        self.assertEqual(self.greet.goodbye(), 'goodbye!')
