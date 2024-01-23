import random
import unittest
from time import perf_counter as current_time
from prog985u import Quicksort

class TestQuicksort(unittest.TestCase):
    def setUp(self):
        self.startTime = current_time()

    def tearDown(self):
        t = current_time() - self.startTime
        print(f"{self.id()}: {t:.6f}")

    # def test_one(self):
    #     self.assertEqual(methodcall, expectedvalue)
    def test_normal_case(self):
      input = [4,2,5,1,3]
      expected = [1,2,3,4,5]
      self.assertEqual(Quicksort.sort(input),expected)
    def test_performance_large_dataset(self):
      input = generate_large_list()
      start_time = current_time()
      Quicksort.sort(input)
      end_time = current_time()
      self.assertLess(end_time - start_time, 10)



def generate_large_list():
  return [random.randint(0, 10_000_000) for i in range(1_000_000)]
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestQuicksort)
    unittest.TextTestRunner(verbosity=0).run(suite)