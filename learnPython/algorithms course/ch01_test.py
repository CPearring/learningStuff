import unittest
from ch01 import sorts
class TestSorts(unittest.TestCase):

    def testInsertionSortDuplicates(self):
        got = [33, 213, 1, 6, 73, 22, 351, 2, 5, 55, 5]
        want = [1, 2, 5, 5, 6, 22, 33, 55, 73, 213, 351]
        sorter = sorts()
        results =  sorter.insertionSort(got)
        self.assertTrue(results == want)

    def testtwoitem(self):
        got = [99, 45]
        want = [45, 99]
        sorter = sorts()
        results = sorter.insertionSort(got)
        self.assertTrue(results == want)



if __name__ == "__main__":
  unittest.main()