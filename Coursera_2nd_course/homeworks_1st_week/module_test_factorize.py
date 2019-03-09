import unittest

def factorize(x):
    """ Factorize positive integer and return its factors.
        :type x: int,>=0
        :rtype: tuple[N],N>0
    """
    pass

class TestFactorize(unittest.TestCase):

    def test_wrong_types_raise_exception(self):
        cases = ("string", 1.5)
        for case in cases:
            with self.subTest(x=case):
                self.assertRaises(TypeError, factorize, case)

    def test_negative(self):
        cases = (-1, -10, -100)
        for case in cases:
            with self.subTest(x=case):
                self.assertRaises(ValueError, factorize, case)

    def test_zero_and_one_cases(self):
        cases = [0, 1]
        result = [(0,), (1,)]
        for val,res in zip(cases,result):
            with self.subTest(x=val):
                self.assertTupleEqual(factorize(val), res)

    def test_simple_numbers(self):
        cases = [3, 13, 29]
        result = [(3,), (13,), (29,)]
        for val,res in zip(cases,result):
            with self.subTest(x=val):
                self.assertTupleEqual(factorize(val), res)

    def test_two_simple_multipliers(self):
         cases = [6, 26, 121]
         result = [(2,3), (2,13), (11,11)]
         for val,res in zip(cases,result):
            with self.subTest(x=val):
                self.assertTupleEqual(factorize(val), res)

    def test_many_multipliers(self):
        '''Что для чисел 1001 и 9699690 возвращаются соответственно кортежи (7, 11, 13) и (2, 3, 5, 7, 11, 13, 17, 19).'''
        cases = [1001, 9699690]
        result = [(7, 11, 13), (2, 3, 5, 7, 11, 13, 17, 19)]
        for val, res in zip(cases, result):
            with self.subTest(x=val):
                self.assertTupleEqual(factorize(val), res)

if True:
    unittest.main()
