import unittest
import MOEDAS_LUIS

class Test_moedas(unittest.TestCase):
    def test_valor_moedas(self):
        self.assertEqual(MOEDAS_LUIS.valor_moedas('2.45'),"Moedas de 1 :2 Moedas de 0.5 :0 Moedas de 0.2 :2 Moedas de 0.1 :0 Moedas de 0.05 :1 Moedas de 0.01 :0 ")
    def test_valor_moedas_1(self):
        self.assertEqual(MOEDAS_LUIS.valor_moedas('3.235245'),"Moedas de 1 :3 Moedas de 0.5 :0 Moedas de 0.2 :1 Moedas de 0.1 :0 Moedas de 0.05 :0 Moedas de 0.01 :4 ")
    def test_valor_moedas_2(self):
        self.assertEqual(MOEDAS_LUIS.valor_moedas("2,7888"),"Moedas de 1 :2 Moedas de 0.5 :1 Moedas de 0.2 :1 Moedas de 0.1 :0 Moedas de 0.05 :1 Moedas de 0.01 :4 ")
if __name__ == '__main__':
    unittest.main()