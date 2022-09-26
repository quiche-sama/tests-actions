import unittest

from app.main import pouet


class MyTestCase(unittest.TestCase):
    def test_pouet(self):
        x = pouet()
        self.assertEqual(x, 2)  # add assertion here


if __name__ == '__main__':
    unittest.main()
