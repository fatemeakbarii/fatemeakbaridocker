import unittest
from app import index

class TestApp(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(index(), "Hello, World!")

if __name__ == '__main__':
    unittest.main()
