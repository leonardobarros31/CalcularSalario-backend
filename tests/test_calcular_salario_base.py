import unittest

class TestCalcularSalarioBase(unittest.TestCase):
    
    def test_ct01(self):
        vendedor = Vendedor('Leonardo', 5, 0.0)
        self.assertEqual(vendedor.calcular_salario_base(), 1500.0)