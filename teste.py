import unittest

class Test(unittest.TestCase):
    def test_api(self):
        self.assertEqual(fatorial(0), 1)
        self.assertEqual(fatorial(1), 1)
        self.assertEqual(fatorial(2), 2)

if __name__ == '__main__':
    unittest.main()