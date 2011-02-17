import unittest
from pprint import pprint
from erdos import *

class TesteNumeroDeErdos(unittest.TestCase):
    def test_erdos_tem_zero_coautor(self):
        livros = [['Erdos']]
        numeroDeErdos = NumeroDeErdos(livros)
        self.assertEqual(0, len(numeroDeErdos['Erdos'].coautores))

    def test_erdos_tem_um_coautor(self):
        livros = [['Erdos', 'Silva']]
        numeroDeErdos = NumeroDeErdos(livros)
        self.assertEqual('Silva', numeroDeErdos['Silva'].nome)
        self.assertEqual(1, len(numeroDeErdos['Erdos'].coautores))
        
    def test_erdos_tem_dois_coautores(self):
        livros = [['Erdos', 'Silva', 'Santos']]
        numeroDeErdos = NumeroDeErdos(livros)
        self.assertEqual(2, len(numeroDeErdos['Erdos'].coautores))
        
    def test_erdos_e_silva_tem_cada_um_um_coautor(self):
        livros = [['Erdos', 'Souza'],
                  ['Silva', 'Santos']]
        numeroDeErdos = NumeroDeErdos(livros)
        self.assertEqual(1, len(numeroDeErdos['Erdos'].coautores))
        self.assertEqual(1, len(numeroDeErdos['Silva'].coautores), numeroDeErdos['Silva'].coautores)
        
class TesteErdos(unittest.TestCase):
    def test_numero_de_erdos_no_para_erdos_eh_zero(self):
        livros = [['Erdos']]
        numeroDeErdos = NumeroDeErdos(livros)
        self.assertEqual(0, numeroDeErdos('Erdos')())
        
    def test_numero_de_erdos_de_autores_sem_relacao_com_erdos_eh_INFINITO(self):
        livros = [
                  ['Silva', 'Santos'],
                  ['Erdos'],
                 ]
        numeroDeErdos = NumeroDeErdos(livros)
        self.assertEqual(0, numeroDeErdos('Erdos')())
        self.assertEqual(INFINITO, numeroDeErdos('Silva')())
        self.assertEqual(INFINITO, numeroDeErdos('Santos')())
        
    def test_numero_de_erdos_de_co_autores_de_erdos_eh_um(self):
        livros = [['Erdos', 'Silva', 'Santos']]
        nerdos = [[0, 1, 1]]
        numeroDeErdos = NumeroDeErdos(livros)
        self.assertEqual(0, numeroDeErdos('Erdos')())
        self.assertEqual(1, numeroDeErdos('Silva')(), numeroDeErdos)
        self.assertEqual(1, numeroDeErdos('Santos')())
        
    def test_numero_de_erdos_de_tres_autores_em_cascata(self):
        livros = [
                  ['Silva', 'Santos'],
                  ['Erdos', 'Silva'],
                 ]
        numeroDeErdos = NumeroDeErdos(livros)
        self.assertEqual(0, numeroDeErdos('Erdos')())
        self.assertEqual(1, numeroDeErdos('Silva')())
        self.assertEqual(2, numeroDeErdos('Santos')())
        
    def test_numero_de_erdos_de_quatro_autores_em_cascata(self):
        livros = [
                  ['Silva', 'Santos'],
                  ['Erdos', 'Silva'],
                  ['Santos', 'Souza'],
                 ]
        numeroDeErdos = NumeroDeErdos(livros)
        self.assertEqual(0, numeroDeErdos('Erdos')())
        self.assertEqual(1, numeroDeErdos('Silva')())
        self.assertEqual(2, numeroDeErdos('Santos')())
        self.assertEqual(3, numeroDeErdos('Souza')())
        
    def test_numero_de_erdos_de_cinco_autores_em_cascata(self):
        livros = [
                  ['Silva', 'Santos'],
                  ['Souza', 'Souto'],
                  ['Erdos', 'Silva'],
                  ['Santos', 'Souza'],
                 ]
        nerdos = [[0, 1],
                  [1, 2],
                  [2, 3],
                  [3, 4]]
        numeroDeErdos = NumeroDeErdos(livros)
        self.assertEqual(0, numeroDeErdos('Erdos')())
        self.assertEqual(1, numeroDeErdos('Silva')())
        self.assertEqual(2, numeroDeErdos('Santos')())
        self.assertEqual(3, numeroDeErdos('Souza')())
        self.assertEqual(4, numeroDeErdos('Souto')())
        
    def test_numero_de_erdos_de_dois_autores_que_escreveram_dois_livros_c_erdos_eh_um(self):
        livros = [
                  ['Erdos', 'Silva'],
                  ['Erdos', 'Santos'],
                 ]
        numeroDeErdos = NumeroDeErdos(livros)
        self.assertEqual(0, numeroDeErdos('Erdos')())
        self.assertEqual(1, numeroDeErdos('Silva')())
        self.assertEqual(1, numeroDeErdos('Santos')())
        
    def test_numero_de_erdos_de_dois_autores_que_escreveram_com_coautores_de_erdos_eh_dois(self):
        livros = [
                  ['Silva', 'Souza'],
                  ['Santos', 'Souto'],
                  ['Erdos', 'Santos'],
                  ['Erdos', 'Silva'],
                 ]
        numeroDeErdos = NumeroDeErdos(livros)
        self.assertEqual(0, numeroDeErdos('Erdos')())
        self.assertEqual(1, numeroDeErdos('Silva')())
        self.assertEqual(1, numeroDeErdos('Santos')())
        self.assertEqual(2, numeroDeErdos('Souto')())
        self.assertEqual(2, numeroDeErdos('Souza')())
    
    def test_dos_segundos_coautores(self):
        livros = [
                  ['Santos', 'Pereira'],
                  ['Erdos', 'Santos'],
                  ['Silva', 'Souza'],
                  ['Santos', 'Souto'],
                  ['Silva', 'Vaz'],
                  ['Erdos', 'Silva'],
                 ]
        numeroDeErdos = NumeroDeErdos(livros)
        self.assertEqual(0, numeroDeErdos('Erdos')())
        self.assertEqual(1, numeroDeErdos('Silva')())
        self.assertEqual(1, numeroDeErdos('Santos')())
        self.assertEqual(2, numeroDeErdos('Souto')())
        self.assertEqual(2, numeroDeErdos('Souza')())
        self.assertEqual(2, numeroDeErdos('Vaz')())
        self.assertEqual(2, numeroDeErdos('Pereira')())
        
class TesteErdosComMaisDeUmPai(unittest.TestCase):
    def test(self):
        livros = [
                  ['Erdos', 'Silva'],
                  ['Erdos', 'Santos'],
                  ['Silva', 'Souza'],
                  ['Caminha'],
                  ['Santos', 'Souto'],
                  ['Silva', 'Vaz'],
                  ['Santos', 'Pereira'],
                  ['Vaz', 'Caminha'],
                  ['Silva', 'Caminha'],
                  ['Coutinho', 'Malta', 'Guedes', 'Salviano'],
                 ]
        numeroDeErdos = NumeroDeErdos(livros)
        self.assertEqual(0, numeroDeErdos('Erdos')())
        self.assertEqual(1, numeroDeErdos('Silva')())
        self.assertEqual(1, numeroDeErdos('Santos')())
        self.assertEqual(2, numeroDeErdos('Souto')())
        self.assertEqual(2, numeroDeErdos('Caminha')())
        # # self.assertEqual(2, len(numeroDeErdos('Caminha').nos_pais))
        self.assertEqual(2, numeroDeErdos('Souza')())
        self.assertEqual(2, numeroDeErdos('Vaz')())
        self.assertEqual(2, numeroDeErdos('Pereira')())
        self.assertEqual(INFINITO, numeroDeErdos('Coutinho')())
        self.assertEqual(INFINITO, numeroDeErdos('Malta')())
        self.assertEqual(INFINITO, numeroDeErdos('Guedes')())
        self.assertEqual(INFINITO, numeroDeErdos('Salviano')())
        
        numeroDeErdos.incluir_autores_de([['Souto', 'Guedes']])
        self.assertEqual(2, numeroDeErdos('Souto')())
        self.assertEqual(3, numeroDeErdos('Guedes')())


        
unittest.main()