import random
import unittest
from time import perf_counter as current_time
from prog985a import Calc


# normal 1,2 edge 0,0 error 1,-1


class TestCalc(unittest.TestCase):
  def setUp(self):
    self.startTime = current_time()
  def tearDown(self):
    t = current_time() - self.startTime
    print(f"{self.id()}: {t:.6f}")
  
  def test_add_edge_case(self):
    self.assertEqual(Calc.add(0,0),0)
  def test_add_normal_case(self):
    self.assertEqual(Calc.add(1, 2), 3)
  def test_add_error_case(self):
    self.assertEqual(Calc.add(1, -1), 0)

  def test_div_normal_case(self):
    self.assertEqual(Calc.div(1,2), 0.5)
  def test_div_error_case(self):
    self.assertEqual(Calc.div(1, -1), -1)
  def test_div_edge_case(self):
    with self.assertRaises(ZeroDivisionError):
      Calc.div(0,0)

  def test_mult_edge_case(self):
    self.assertEqual(Calc.mult(0,0),0)
  def test_mult_normal_case(self):
    self.assertEqual(Calc.mult(1, 2), 2)
  def test_mult_error_case(self):
    self.assertEqual(Calc.mult(1, -1), -1)

  def test_sub_edge_case(self):
    self.assertEqual(Calc.sub(0,0),0)
  def test_sub_normal_case(self):
    self.assertEqual(Calc.sub(1, 2), -1)
  def test_sub_error_case(self):
    self.assertEqual(Calc.sub(1, -1), 2)

  def test_mod_edge_case(self):
    with self.assertRaises(ZeroDivisionError):
      Calc.mod(0,0)
  def test_mod_normal_case(self):
    self.assertEqual(Calc.mod(1, 2), 1)
  def test_mod_error_case(self):
    self.assertEqual(Calc.mod(1, -1), 0)
    # def test_one(self):
    #     self.assertEqual(methodcall, expectedvalue)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCalc)
    unittest.TextTestRunner(verbosity=0).run(suite)
