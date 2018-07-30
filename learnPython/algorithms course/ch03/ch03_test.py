import unittest
from ch03 import alg
class TestSorts(unittest.TestCase):

    def testFibonacci(self):
        got = 1
        want = 0
        self.assertTrue(alg.fib(got) == want)

    def testFibonacci2(self):
        got = 6
        want = 5
        self.assertTrue(alg.fib(got) == want)


if __name__ == "__main__":
  unittest.main()