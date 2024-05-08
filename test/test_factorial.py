import unittest
from factorial.factorial_module import factorial_iterative, factorial_recursion, clumsy

class TestFactorialFunctions(unittest.TestCase):
    def test_factorial_iterative_positive(self):
        self.assertEqual(factorial_iterative(5), 120)

    def test_factorial_iterative_zero(self):
        self.assertEqual(factorial_iterative(0), 1)

    def test_factorial_iterative_large(self):
        self.assertEqual(factorial_iterative(10), 3628800)

    def test_factorial_recursion_positive(self):
        self.assertEqual(factorial_recursion(5), 120)

    def test_factorial_recursion_zero(self):
        self.assertEqual(factorial_recursion(0), 1)

    def test_factorial_recursion_large(self):
        self.assertEqual(factorial_recursion(10), 3628800)

    def test_clumsy_positive(self):
        self.assertEqual(clumsy(5), 7)  # 5 * 4 / 3 + 2 - 1 = 7

    def test_clumsy_zero(self):
        self.assertEqual(clumsy(0), 0)

    def test_clumsy_large(self):
        self.assertEqual(clumsy(10), 12)  # 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1 = 12

    def test_clumsy_negative_input(self):
        with self.assertRaises(ValueError):
            clumsy(-1)

    def test_clumsy_float_input(self):
        with self.assertRaises(TypeError):
            clumsy(5.5)

if __name__ == '__main__':
    unittest.main()
