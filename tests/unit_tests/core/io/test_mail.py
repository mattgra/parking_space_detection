import unittest
# Unittests to be added


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # Should not return error

    def test_something_else(self):
        self.assertEqual(True, False)  # Should return error


if __name__ == '__main__':
    unittest.main()
