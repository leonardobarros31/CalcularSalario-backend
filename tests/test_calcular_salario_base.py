import unittest

from vendedor import Vendedor

class TestCalcularSalarioBase(unittest.TestCase):

    def test_ct01(self):
        vendedor = Vendedor('Leonardo', 0, 0.0)
        self.assertEqual(vendedor.calcular_salario_base(), 0.0)

    def test_ct02(self):
        vendedor = Vendedor('Leonardo', 1, 0.0)
        self.assertEqual(vendedor.calcular_salario_base(), 1500.0)

    def test_ct03(self):
        vendedor = Vendedor('Leonardo', 2, 0.0)
        self.assertEqual(vendedor.calcular_salario_base(), 1500.0)
    
    def test_ct04(self):
        vendedor = Vendedor('Leonardo', 11, 0.0)
        self.assertEqual(vendedor.calcular_salario_base(), 1500.0)
        
    def test_ct05(self):
        vendedor = Vendedor('Leonardo', 12, 0.0)
        self.assertEqual(vendedor.calcular_salario_base(), 1500.0)
        
    def test_ct06(self):
        vendedor = Vendedor('Leonardo', 13, 0.0)
        self.assertEqual(vendedor.calcular_salario_base(), 2000.0)
        
    def test_ct07(self):
        vendedor = Vendedor('Leonardo', 23, 0.0)
        self.assertEqual(vendedor.calcular_salario_base(), 2000.0)
    
    def test_ct08(self):
        vendedor = Vendedor('Leonardo', 24, 0.0)
        self.assertEqual(vendedor.calcular_salario_base(), 2000.0)
        
    def test_ct09(self):
        vendedor = Vendedor('Leonardo', 25, 0.0)
        self.assertEqual(vendedor.calcular_salario_base(), 2500.0)
        
    def test_ct10(self):
        vendedor = Vendedor('Leonardo', 35, 0.0)
        self.assertEqual(vendedor.calcular_salario_base(), 2500.0)
        
    def test_ct11(self):
        vendedor = Vendedor('Leonardo', 36, 0.0)
        self.assertEqual(vendedor.calcular_salario_base(), 2500.0)
        
    def test_ct12(self):
        vendedor = Vendedor('Leonardo', 37, 0.0)
        self.assertEqual(vendedor.calcular_salario_base(), 3000.0)