import unittest
import sys
sys.path.append('../')

from main import hello_world

class TestHelloWorld(unittest.TestCase):

    def test_hello_world(self):
        self.assertEqual(hello_world(), 'Hello, World!', "Shoudl Return 'Hello, World!'")

if __name__ == '__main__':
    unittest.main()
