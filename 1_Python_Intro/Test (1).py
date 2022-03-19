import unittest
from Sorveteria import Sorveteria
from Cliente import Cliente

class Testes(unittest.TestCase):
    def setUp(self):
        self.sorveteria = Sorveteria(10, 1.5, 0)
        self.cliente = Cliente("Pedro", 10)

    def testeRecebePedido(self):
        print("\nTeste de Sorveteria receber pedido")
        self.assertEqual(self.sorveteria.receberPedido(2), 3)

    def testeRecebePedidoSemEstoque(self):
        print("\nTeste de Sorveteia receber pedido acima do Estoque")
        self.assertEqual(self.sorveteria.receberPedido(11), 0)

    def testeRecebePedidoInvalido(self):
        print("\nTeste de Sorveteia receber pedido invalido")
        self.assertEqual(self.sorveteria.receberPedido(-3), 0)

    def testeRecebePedidoLetra(self):
        print("\nTeste de Sorveteia receber pedido com letra")
        self.assertEqual(self.sorveteria.receberPedido("a"), 0)

    def testeFazPedidoInvalido(self):
        print("\nTeste de Cliente fazer pedido qtde negativa")
        self.assertEqual(self.cliente.fazPedido(-10, self.sorveteria), -1)

    def testeClienteSorveteriaFeliz(self):
        print("\nTeste de cliente e sorveteria efetuarem o fluxo completo ideal")
        self.cliente.fazPedido(3, self.sorveteria)
        self.assertEqual(self.cliente.pagaConta(4.5, self.sorveteria), 5.5)

if __name__ == "__main__":
    unittest.main()