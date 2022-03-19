import unittest
import datetime
import Agenda


class Testes(unittest.TestCase):
    def setUp(self):
        self.agenda = Agenda.Agenda("minhaAgenda")

    def testeAddCompromissoCenarioIdeal(self):
        print("\nTeste - Add Compromisso Caso Ideal")
        self.assertEqual(self.agenda.addCompromisso(datetime.datetime(2021, 8, 24, 20, 00, 00, 00), datetime.datetime(2021, 8, 24, 21, 00, 00, 00), "Agenda 1"), True)

    def testeAddCompromissoHorarioOcupado(self):
        print("\nTeste - Add Compromisso Horario Ocupado")
        self.agenda.addCompromisso(datetime.datetime(2021, 8, 24, 20, 00, 00, 00), datetime.datetime(2021, 8, 24, 21, 00, 00, 00), "Agenda 2")
        self.assertEqual(self.agenda.addCompromisso(datetime.datetime(2021, 8, 24, 20, 10, 00, 00), datetime.datetime(2021, 8, 24, 21, 00, 00, 00), "Agenda 1"), False)

    def testeApagaCompromissoCenarioIdeal(self):
        print("\nTeste - Apagar Compromisso Caso Ideal")
        self.agenda.addCompromisso(datetime.datetime(2021, 8, 24, 20, 00, 00, 00), datetime.datetime(2021, 8, 24, 21, 00, 00, 00), "Agenda 1")
        self.assertEqual(self.agenda.apagarCompromisso("Agenda 1"), True)

    def testeApagaCompromissoInexistente(self):
        print("\nTeste - Apaga Compromisso Inexistente")
        self.assertEqual(self.agenda.apagarCompromisso("aaa"), False) 

    def testeAlteraCompromissoInexistente(self):
        print("\nTeste - Altera Compromisso Inexistente")
        self.assertEqual(self.agenda.alterarCompromisso(datetime.datetime(2021, 8, 24, 20, 00, 00, 00), datetime.datetime(2021, 8, 24, 21, 00, 00, 00), "Agenda 1"), False) 

    def testeAlteraCompromissoCasoIdeal(self):
        print("\nTeste - Altera Compromisso Caso Ideal")
        self.agenda.addCompromisso(datetime.datetime(2021, 8, 24, 20, 00, 00, 00), datetime.datetime(2021, 8, 24, 21, 00, 00, 00), "Agenda 1")
        self.assertEqual(self.agenda.alterarCompromisso(datetime.datetime(2021, 8, 24, 20, 00, 00, 00), datetime.datetime(2021, 8, 24, 22, 00, 00, 00), "Agenda 1"), True) 

    def testeAlteraCompromissoDataOcupada(self):
        print("\nTeste - Altera Compromisso Data Ocupada")
        self.agenda.addCompromisso(datetime.datetime(2021, 8, 24, 20, 00, 00, 00), datetime.datetime(2021, 8, 24, 21, 00, 00, 00), "Agenda 1")
        self.agenda.addCompromisso(datetime.datetime(2021, 8, 24, 22, 00, 00, 00), datetime.datetime(2021, 8, 24, 22, 30, 00, 00), "Agenda 2")
        self.assertEqual(self.agenda.alterarCompromisso(datetime.datetime(2021, 8, 24, 22, 00, 00, 00), datetime.datetime(2021, 8, 24, 22, 10, 00, 00), "Agenda 1"), False) 

    def testeSalvaAgenda(self):
        print("\nTeste - Salva agenda")
        self.agenda.addCompromisso(datetime.datetime(2021, 8, 24, 20, 00, 00, 00), datetime.datetime(2021, 8, 24, 21, 00, 00, 00), "Compromisso_1")
        self.agenda.addCompromisso(datetime.datetime(2021, 8, 24, 22, 00, 00, 00), datetime.datetime(2021, 8, 24, 22, 30, 00, 00), "Compromisso_2")
        gerenciador = Agenda.Gerenciador(self.agenda)
        gerenciador.salvaArquivo()


if __name__ == "__main__":
    unittest.main()