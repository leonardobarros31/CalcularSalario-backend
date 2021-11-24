import unittest

from vendedor import Vendedor

class TestCalcularSalarioBase(unittest.TestCase):

    def test_ct01(self):
        vendedor = Vendedor('Victor', 5, 0.0)
        self.assertEqual(vendedor.calcular_salario_base(), 1500.0)

    def test_ct02(self):
        vendedor = Vendedor('Victor', 15, 0.0)
        self.assertEqual(vendedor.calcular_salario_base(), 2000.0)

    def test_ct03(self):
        vendedor = Vendedor('Victor', 100, 0.0)
        self.assertEqual(vendedor.calcular_salario_base(), 3000.0)