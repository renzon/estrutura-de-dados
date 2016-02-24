import unittest


def soma(param, param1):
    return param + param1


class SomaTestes(unittest.TestCase):
    def test_inteiro(self):
        resultado = soma(1, 2)
        self.assertEqual(3, resultado)

    def test_float(self):
        resultado = soma(1.0, 2.0)
        self.assertEqual(3.0, resultado)

if __name__=='__main__':
    unittest.main()
