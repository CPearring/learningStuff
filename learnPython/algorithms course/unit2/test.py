import unittest
from merge import msort
from heap import hsort
from avl import avlsort
from counting import csort
from radix import rsort
class TestSorts(unittest.TestCase):

    got = [33, 213, 1, 6, 73, 22, 351, 2, 5, 55, 5]
    want = [1, 2, 5, 5, 6, 22, 33, 55, 73, 213, 351]

    def testmergesort(self):
        sorter = msort()
        self.assertTrue(sorter.mergeSort(got) == want)

    def testheapsort(self):
        sorter = hsort()
        self.assertTrue(sorter.heapSort(got) == want)

    def testavlsort(self):
        sorter = avlsort()
        self.assertTrue(sorter.avlSort(got) == want)

    def testcsort(self):
        sorter = csort()
        self.assertTrue(sorter.countingSort(got) == want)

    def testrsort(self):
        sorter = rsort()
        self.assertTrue(sorter.radixSort(got) == want)



if __name__ == "__main__":
  unittest.main()