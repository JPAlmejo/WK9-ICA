import unittest
import fibonacci

class TestCaseFibonacci(unittest.TestCase):


#testing some random number
      def test1(self):
        self.assertEqual(fibonacci.Fibonacci(9), 21)

if __name__== '__main__':
    unittest.main(verbosity=2)