#-*- encoding: utf-8 -*-

import unittest
from pprint import pprint
from erdos import CoautoresDeErdos, INFINITO

class TesteNumeroDeErdos(unittest.TestCase):
    def test_erdos_tem_zero_coautor(self):
        livros = [['Erdos']]
        coautoresDeErdos = CoautoresDeErdos(livros)
        self.assertEqual(0, len(coautoresDeErdos['Erdos'].coautores))

    def test_erdos_tem_um_coautor(self):
        livros = [['Erdos', 'Silva']]
        coautoresDeErdos = CoautoresDeErdos(livros)
        self.assertEqual('Silva', coautoresDeErdos['Silva'].nome)
        self.assertEqual(1, len(coautoresDeErdos['Erdos'].coautores))
        
    def test_erdos_tem_dois_coautores(self):
        livros = [['Erdos', 'Silva', 'Santos']]
        coautoresDeErdos = CoautoresDeErdos(livros)
        self.assertEqual(2, len(coautoresDeErdos['Erdos'].coautores))
        
    def test_erdos_e_silva_tem_cada_um_um_coautor(self):
        livros = [['Erdos', 'Souza'],
                  ['Silva', 'Santos']]
        coautoresDeErdos = CoautoresDeErdos(livros)
        self.assertEqual(1, len(coautoresDeErdos['Erdos'].coautores))
        self.assertEqual(1, len(coautoresDeErdos['Silva'].coautores), coautoresDeErdos['Silva'].coautores)
        
class TesteErdos(unittest.TestCase):
    def test_numero_de_erdos_no_para_erdos_eh_zero(self):
        livros = [['Erdos']]
        coautoresDeErdos = CoautoresDeErdos(livros)
        self.assertEqual(0, coautoresDeErdos['Erdos'].numero_de_erdos)
        
    def test_numero_de_erdos_de_autores_sem_relacao_com_erdos_eh_INFINITO(self):
        livros = [
                  ['Silva', 'Santos'],
                  ['Erdos'],
                 ]
        coautoresDeErdos = CoautoresDeErdos(livros)
        self.assertEqual(0, coautoresDeErdos['Erdos'].numero_de_erdos)
        self.assertEqual(INFINITO, coautoresDeErdos['Silva'].numero_de_erdos)
        self.assertEqual(INFINITO, coautoresDeErdos['Santos'].numero_de_erdos)
        
    def test_numero_de_erdos_de_co_autores_de_erdos_eh_um(self):
        livros = [['Erdos', 'Silva', 'Santos']]
        nerdos = [[0, 1, 1]]
        coautoresDeErdos = CoautoresDeErdos(livros)
        self.assertEqual(0, coautoresDeErdos['Erdos'].numero_de_erdos)
        self.assertEqual(1, coautoresDeErdos['Silva'].numero_de_erdos, coautoresDeErdos)
        self.assertEqual(1, coautoresDeErdos['Santos'].numero_de_erdos)
        
    def test_numero_de_erdos_de_tres_autores_em_cascata(self):
        livros = [
                  ['Silva', 'Santos'],
                  ['Erdos', 'Silva'],
                 ]
        coautoresDeErdos = CoautoresDeErdos(livros)
        self.assertEqual(0, coautoresDeErdos['Erdos'].numero_de_erdos)
        self.assertEqual(1, coautoresDeErdos['Silva'].numero_de_erdos)
        self.assertEqual(2, coautoresDeErdos['Santos'].numero_de_erdos)
        
    def test_numero_de_erdos_de_quatro_autores_em_cascata(self):
        livros = [
                  ['Silva', 'Santos'],
                  ['Erdos', 'Silva'],
                  ['Santos', 'Souza'],
                 ]
        coautoresDeErdos = CoautoresDeErdos(livros)
        self.assertEqual(0, coautoresDeErdos['Erdos'].numero_de_erdos)
        self.assertEqual(1, coautoresDeErdos['Silva'].numero_de_erdos)
        self.assertEqual(2, coautoresDeErdos['Santos'].numero_de_erdos)
        self.assertEqual(3, coautoresDeErdos['Souza'].numero_de_erdos)
        
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
        coautoresDeErdos = CoautoresDeErdos(livros)
        self.assertEqual(0, coautoresDeErdos['Erdos'].numero_de_erdos)
        self.assertEqual(1, coautoresDeErdos['Silva'].numero_de_erdos)
        self.assertEqual(2, coautoresDeErdos['Santos'].numero_de_erdos)
        self.assertEqual(3, coautoresDeErdos['Souza'].numero_de_erdos)
        self.assertEqual(4, coautoresDeErdos['Souto'].numero_de_erdos)
        
    def test_numero_de_erdos_de_dois_autores_que_escreveram_dois_livros_c_erdos_eh_um(self):
        livros = [
                  ['Erdos', 'Silva'],
                  ['Erdos', 'Santos'],
                 ]
        coautoresDeErdos = CoautoresDeErdos(livros)
        self.assertEqual(0, coautoresDeErdos['Erdos'].numero_de_erdos)
        self.assertEqual(1, coautoresDeErdos['Silva'].numero_de_erdos)
        self.assertEqual(1, coautoresDeErdos['Santos'].numero_de_erdos)
        
    def test_numero_de_erdos_de_dois_autores_que_escreveram_com_coautores_de_erdos_eh_dois(self):
        livros = [
                  ['Silva', 'Souza'],
                  ['Santos', 'Souto'],
                  ['Erdos', 'Santos'],
                  ['Erdos', 'Silva'],
                 ]
        coautoresDeErdos = CoautoresDeErdos(livros)
        self.assertEqual(0, coautoresDeErdos['Erdos'].numero_de_erdos)
        self.assertEqual(1, coautoresDeErdos['Silva'].numero_de_erdos)
        self.assertEqual(1, coautoresDeErdos['Santos'].numero_de_erdos)
        self.assertEqual(2, coautoresDeErdos['Souto'].numero_de_erdos)
        self.assertEqual(2, coautoresDeErdos['Souza'].numero_de_erdos)
    
    def test_dos_segundos_coautores(self):
        livros = [
                  ['Santos', 'Pereira'],
                  ['Erdos', 'Santos'],
                  ['Silva', 'Souza'],
                  ['Santos', 'Souto'],
                  ['Silva', 'Vaz'],
                  ['Erdos', 'Silva'],
                 ]
        coautoresDeErdos = CoautoresDeErdos(livros)
        self.assertEqual(0, coautoresDeErdos['Erdos'].numero_de_erdos)
        self.assertEqual(1, coautoresDeErdos['Silva'].numero_de_erdos)
        self.assertEqual(1, coautoresDeErdos['Santos'].numero_de_erdos)
        self.assertEqual(2, coautoresDeErdos['Souto'].numero_de_erdos)
        self.assertEqual(2, coautoresDeErdos['Souza'].numero_de_erdos)
        self.assertEqual(2, coautoresDeErdos['Vaz'].numero_de_erdos)
        self.assertEqual(2, coautoresDeErdos['Pereira'].numero_de_erdos)
        
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
        coautoresDeErdos = CoautoresDeErdos(livros)
        self.assertEqual(0, coautoresDeErdos['Erdos'].numero_de_erdos)
        self.assertEqual(1, coautoresDeErdos['Silva'].numero_de_erdos)
        self.assertEqual(1, coautoresDeErdos['Santos'].numero_de_erdos)
        self.assertEqual(2, coautoresDeErdos['Souto'].numero_de_erdos)
        self.assertEqual(2, coautoresDeErdos['Caminha'].numero_de_erdos)

        self.assertEqual(2, coautoresDeErdos['Souza'].numero_de_erdos)
        self.assertEqual(2, coautoresDeErdos['Vaz'].numero_de_erdos)
        self.assertEqual(2, coautoresDeErdos['Pereira'].numero_de_erdos)
        self.assertEqual(INFINITO, coautoresDeErdos['Coutinho'].numero_de_erdos)
        self.assertEqual(INFINITO, coautoresDeErdos['Malta'].numero_de_erdos)
        self.assertEqual(INFINITO, coautoresDeErdos['Guedes'].numero_de_erdos)
        self.assertEqual(INFINITO, coautoresDeErdos['Salviano'].numero_de_erdos)
        
        coautoresDeErdos.incluir_autores_de([['Souto', 'Guedes']])
        self.assertEqual(2, coautoresDeErdos['Souto'].numero_de_erdos)
        self.assertEqual(3, coautoresDeErdos['Guedes'].numero_de_erdos)

class TestesComFlavio(unittest.TestCase):
    def test_varios_autores_infinitos(self):
        livros = [['Zé', 'Mané'],
                  ['Erdos']]
        coautoresDeErdos = CoautoresDeErdos(livros)
        self.assertEqual(coautoresDeErdos['Mané'].numero_de_erdos, INFINITO)

    def test_coautor_de_erdos_eh_1(self):
        livros = [['Erdos', 'Berrondo']]
        coautoresDeErdos = CoautoresDeErdos(livros)
        self.assertEqual(coautoresDeErdos['Erdos'].numero_de_erdos, 0)
        self.assertEqual(coautoresDeErdos['Berrondo'].numero_de_erdos, 1)

    def test_coautor_de_Berrondo_eh_2(self):
        livros = [
            ['Erdos', 'Berrondo'],
            ['Berrondo', 'Flávio'],
        ]
        coautoresDeErdos = CoautoresDeErdos(livros)
        self.assertEqual(coautoresDeErdos['Erdos'].numero_de_erdos, 0)
        self.assertEqual(coautoresDeErdos['Berrondo'].numero_de_erdos, 1)
        self.assertEqual(coautoresDeErdos['Flávio'].numero_de_erdos, 2)

    def test_coautor_de_Berrondo_eh_2_independente_da_ordem(self):
        livros = [
            ['Berrondo', 'Flávio'],
            ['Erdos', 'Berrondo'],
        ]
        coautoresDeErdos = CoautoresDeErdos(livros)
        self.assertEqual(coautoresDeErdos['Erdos'].numero_de_erdos, 0)
        self.assertEqual(coautoresDeErdos['Berrondo'].numero_de_erdos, 1)
        self.assertEqual(coautoresDeErdos['Flávio'].numero_de_erdos, 2)

    def teste_alguem_de_fora_escreve_com_alguem_de_dentro(self):
        livros = [
            ['A', 'B'],
            ['B', 'C'],
            ['C', 'D'],
            ['Berrondo', 'Flávio'],
            ['Erdos', 'Berrondo'],
        ]
        coautoresDeErdos = CoautoresDeErdos(livros)
        self.assertEqual(coautoresDeErdos['Erdos'].numero_de_erdos, 0)
        self.assertEqual(coautoresDeErdos['Berrondo'].numero_de_erdos, 1)
        self.assertEqual(coautoresDeErdos['Flávio'].numero_de_erdos, 2)
        self.assertEqual(coautoresDeErdos['A'].numero_de_erdos, INFINITO)
        self.assertEqual(coautoresDeErdos['B'].numero_de_erdos, INFINITO)
        self.assertEqual(coautoresDeErdos['C'].numero_de_erdos, INFINITO)
        self.assertEqual(coautoresDeErdos['D'].numero_de_erdos, INFINITO)

        novos_livros = [['B', 'Flávio']]
        coautoresDeErdos.incluir_autores_de(novos_livros)
        self.assertEqual(coautoresDeErdos['Erdos'].numero_de_erdos, 0)
        self.assertEqual(coautoresDeErdos['Berrondo'].numero_de_erdos, 1)
        self.assertEqual(coautoresDeErdos['Flávio'].numero_de_erdos, 2)
        self.assertEqual(coautoresDeErdos['A'].numero_de_erdos, 4)
        self.assertEqual(coautoresDeErdos['B'].numero_de_erdos, 3)
        self.assertEqual(coautoresDeErdos['C'].numero_de_erdos, 4)
        self.assertEqual(coautoresDeErdos['D'].numero_de_erdos, 5)

    def teste_promocao_intermediaria(self):
        livros = [
            ['Erdos', 'Berrondo'],
            ['Berrondo', 'Flávio'],
            ['Flávio', 'Magdalena'],
            ['Magdalena', 'Luiza'],
        ]
        coautoresDeErdos = CoautoresDeErdos(livros)
        self.assertEqual(coautoresDeErdos['Erdos'].numero_de_erdos, 0)
        self.assertEqual(coautoresDeErdos['Berrondo'].numero_de_erdos, 1)
        self.assertEqual(coautoresDeErdos['Flávio'].numero_de_erdos, 2)
        self.assertEqual(coautoresDeErdos['Magdalena'].numero_de_erdos, 3)
        self.assertEqual(coautoresDeErdos['Luiza'].numero_de_erdos, 4)

        novos_livros = [['Erdos', 'Luiza']]
        coautoresDeErdos.incluir_autores_de(novos_livros)
        self.assertEqual(coautoresDeErdos['Erdos'].numero_de_erdos, 0)
        self.assertEqual(coautoresDeErdos['Berrondo'].numero_de_erdos, 1)
        self.assertEqual(coautoresDeErdos['Flávio'].numero_de_erdos, 2)
        self.assertEqual(coautoresDeErdos['Magdalena'].numero_de_erdos, 2)
        self.assertEqual(coautoresDeErdos['Luiza'].numero_de_erdos, 1)

    def teste_boladao(self):
        livros = [
            ['Erdos', '1'],
            ['1', '2'],
            ['2', '3'],
            ['3', '4'],
            ['4', '5'],
            ['5', '6'],
            ['6', '7'],
            ['7', '8'],
        ]
        coautoresDeErdos = CoautoresDeErdos(livros)
        self.assertEqual(coautoresDeErdos['Erdos'].numero_de_erdos, 0)
        self.assertEqual(coautoresDeErdos['1'].numero_de_erdos, 1)
        self.assertEqual(coautoresDeErdos['2'].numero_de_erdos, 2)
        self.assertEqual(coautoresDeErdos['3'].numero_de_erdos, 3)
        self.assertEqual(coautoresDeErdos['4'].numero_de_erdos, 4)
        self.assertEqual(coautoresDeErdos['5'].numero_de_erdos, 5)
        self.assertEqual(coautoresDeErdos['6'].numero_de_erdos, 6)
        self.assertEqual(coautoresDeErdos['7'].numero_de_erdos, 7)
        self.assertEqual(coautoresDeErdos['8'].numero_de_erdos, 8)

        novos_livros = [['2', '5']]
        coautoresDeErdos.incluir_autores_de(novos_livros)
        self.assertEqual(coautoresDeErdos['Erdos'].numero_de_erdos, 0)
        self.assertEqual(coautoresDeErdos['1'].numero_de_erdos, 1)
        self.assertEqual(coautoresDeErdos['2'].numero_de_erdos, 2)
        self.assertEqual(coautoresDeErdos['3'].numero_de_erdos, 3)
        self.assertEqual(coautoresDeErdos['4'].numero_de_erdos, 4)
        self.assertEqual(coautoresDeErdos['5'].numero_de_erdos, 3)
        self.assertEqual(coautoresDeErdos['6'].numero_de_erdos, 4)
        self.assertEqual(coautoresDeErdos['7'].numero_de_erdos, 5)
        self.assertEqual(coautoresDeErdos['8'].numero_de_erdos, 6)

        novissimos_livros = [['Erdos', '4']]
        coautoresDeErdos.incluir_autores_de(novissimos_livros)
        self.assertEqual(coautoresDeErdos['Erdos'].numero_de_erdos, 0)
        self.assertEqual(coautoresDeErdos['1'].numero_de_erdos, 1)
        self.assertEqual(coautoresDeErdos['2'].numero_de_erdos, 2)
        self.assertEqual(coautoresDeErdos['3'].numero_de_erdos, 2)
        self.assertEqual(coautoresDeErdos['4'].numero_de_erdos, 1)
        self.assertEqual(coautoresDeErdos['5'].numero_de_erdos, 2)
        self.assertEqual(coautoresDeErdos['6'].numero_de_erdos, 3)
        self.assertEqual(coautoresDeErdos['7'].numero_de_erdos, 4)
        self.assertEqual(coautoresDeErdos['8'].numero_de_erdos, 5)

        livros_mais_novos_ainda = [['3', '5', '8']]
        coautoresDeErdos.incluir_autores_de(livros_mais_novos_ainda)
        self.assertEqual(coautoresDeErdos['Erdos'].numero_de_erdos, 0)
        self.assertEqual(coautoresDeErdos['1'].numero_de_erdos, 1)
        self.assertEqual(coautoresDeErdos['2'].numero_de_erdos, 2)
        self.assertEqual(coautoresDeErdos['3'].numero_de_erdos, 2)
        self.assertEqual(coautoresDeErdos['4'].numero_de_erdos, 1)
        self.assertEqual(coautoresDeErdos['5'].numero_de_erdos, 2)
        self.assertEqual(coautoresDeErdos['6'].numero_de_erdos, 3)
        self.assertEqual(coautoresDeErdos['7'].numero_de_erdos, 4)
        self.assertEqual(coautoresDeErdos['8'].numero_de_erdos, 3)


        
unittest.main()