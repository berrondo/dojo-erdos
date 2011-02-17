#-*- encoding: utf-8 -*-

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
        self.assertEqual(0, numeroDeErdos['Erdos']())
        
    def test_numero_de_erdos_de_autores_sem_relacao_com_erdos_eh_INFINITO(self):
        livros = [
                  ['Silva', 'Santos'],
                  ['Erdos'],
                 ]
        numeroDeErdos = NumeroDeErdos(livros)
        self.assertEqual(0, numeroDeErdos['Erdos']())
        self.assertEqual(INFINITO, numeroDeErdos['Silva']())
        self.assertEqual(INFINITO, numeroDeErdos['Santos']())
        
    def test_numero_de_erdos_de_co_autores_de_erdos_eh_um(self):
        livros = [['Erdos', 'Silva', 'Santos']]
        nerdos = [[0, 1, 1]]
        numeroDeErdos = NumeroDeErdos(livros)
        self.assertEqual(0, numeroDeErdos['Erdos']())
        self.assertEqual(1, numeroDeErdos['Silva'](), numeroDeErdos)
        self.assertEqual(1, numeroDeErdos['Santos']())
        
    def test_numero_de_erdos_de_tres_autores_em_cascata(self):
        livros = [
                  ['Silva', 'Santos'],
                  ['Erdos', 'Silva'],
                 ]
        numeroDeErdos = NumeroDeErdos(livros)
        self.assertEqual(0, numeroDeErdos['Erdos']())
        self.assertEqual(1, numeroDeErdos['Silva']())
        self.assertEqual(2, numeroDeErdos['Santos']())
        
    def test_numero_de_erdos_de_quatro_autores_em_cascata(self):
        livros = [
                  ['Silva', 'Santos'],
                  ['Erdos', 'Silva'],
                  ['Santos', 'Souza'],
                 ]
        numeroDeErdos = NumeroDeErdos(livros)
        self.assertEqual(0, numeroDeErdos['Erdos']())
        self.assertEqual(1, numeroDeErdos['Silva']())
        self.assertEqual(2, numeroDeErdos['Santos']())
        self.assertEqual(3, numeroDeErdos['Souza']())
        
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
        self.assertEqual(0, numeroDeErdos['Erdos']())
        self.assertEqual(1, numeroDeErdos['Silva']())
        self.assertEqual(2, numeroDeErdos['Santos']())
        self.assertEqual(3, numeroDeErdos['Souza']())
        self.assertEqual(4, numeroDeErdos['Souto']())
        
    def test_numero_de_erdos_de_dois_autores_que_escreveram_dois_livros_c_erdos_eh_um(self):
        livros = [
                  ['Erdos', 'Silva'],
                  ['Erdos', 'Santos'],
                 ]
        numeroDeErdos = NumeroDeErdos(livros)
        self.assertEqual(0, numeroDeErdos['Erdos']())
        self.assertEqual(1, numeroDeErdos['Silva']())
        self.assertEqual(1, numeroDeErdos['Santos']())
        
    def test_numero_de_erdos_de_dois_autores_que_escreveram_com_coautores_de_erdos_eh_dois(self):
        livros = [
                  ['Silva', 'Souza'],
                  ['Santos', 'Souto'],
                  ['Erdos', 'Santos'],
                  ['Erdos', 'Silva'],
                 ]
        numeroDeErdos = NumeroDeErdos(livros)
        self.assertEqual(0, numeroDeErdos['Erdos']())
        self.assertEqual(1, numeroDeErdos['Silva']())
        self.assertEqual(1, numeroDeErdos['Santos']())
        self.assertEqual(2, numeroDeErdos['Souto']())
        self.assertEqual(2, numeroDeErdos['Souza']())
    
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
        self.assertEqual(0, numeroDeErdos['Erdos']())
        self.assertEqual(1, numeroDeErdos['Silva']())
        self.assertEqual(1, numeroDeErdos['Santos']())
        self.assertEqual(2, numeroDeErdos['Souto']())
        self.assertEqual(2, numeroDeErdos['Souza']())
        self.assertEqual(2, numeroDeErdos['Vaz']())
        self.assertEqual(2, numeroDeErdos['Pereira']())
        
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
        self.assertEqual(0, numeroDeErdos['Erdos']())
        self.assertEqual(1, numeroDeErdos['Silva']())
        self.assertEqual(1, numeroDeErdos['Santos']())
        self.assertEqual(2, numeroDeErdos['Souto']())
        self.assertEqual(2, numeroDeErdos['Caminha']())

        self.assertEqual(2, numeroDeErdos['Souza']())
        self.assertEqual(2, numeroDeErdos['Vaz']())
        self.assertEqual(2, numeroDeErdos['Pereira']())
        self.assertEqual(INFINITO, numeroDeErdos['Coutinho']())
        self.assertEqual(INFINITO, numeroDeErdos['Malta']())
        self.assertEqual(INFINITO, numeroDeErdos['Guedes']())
        self.assertEqual(INFINITO, numeroDeErdos['Salviano']())
        
        numeroDeErdos.incluir_autores_de([['Souto', 'Guedes']])
        self.assertEqual(2, numeroDeErdos['Souto']())
        self.assertEqual(3, numeroDeErdos['Guedes']())

class TestesComFlavio(unittest.TestCase):
    def test_varios_autores_infinitos(self):
        livros = [['Zé', 'Mané'],
                  ['Erdos']]
        erdos = NumeroDeErdos(livros)
        self.assertEqual(erdos.numero_do('Mané'), INFINITO)

    def test_coautor_de_erdos_eh_1(self):
        livros = [['Erdos', 'Berrondo']]
        erdos = NumeroDeErdos(livros)
        self.assertEqual(erdos.numero_do('Erdos'), 0)
        self.assertEqual(erdos.numero_do('Berrondo'), 1)

    def test_coautor_de_Berrondo_eh_2(self):
        livros = [
            ['Erdos', 'Berrondo'],
            ['Berrondo', 'Flávio'],
        ]
        erdos = NumeroDeErdos(livros)
        self.assertEqual(erdos.numero_do('Erdos'), 0)
        self.assertEqual(erdos.numero_do('Berrondo'), 1)
        self.assertEqual(erdos.numero_do('Flávio'), 2)

    def test_coautor_de_Berrondo_eh_2_independente_da_ordem(self):
        livros = [
            ['Berrondo', 'Flávio'],
            ['Erdos', 'Berrondo'],
        ]
        erdos = NumeroDeErdos(livros)
        self.assertEqual(erdos.numero_do('Erdos'), 0)
        self.assertEqual(erdos.numero_do('Berrondo'), 1)
        self.assertEqual(erdos.numero_do('Flávio'), 2)

    def teste_alguem_de_fora_escreve_com_alguem_de_dentro(self):
        livros = [
            ['A', 'B'],
            ['B', 'C'],
            ['C', 'D'],
            ['Berrondo', 'Flávio'],
            ['Erdos', 'Berrondo'],
        ]
        erdos = NumeroDeErdos(livros)
        self.assertEqual(erdos.numero_do('Erdos'), 0)
        self.assertEqual(erdos.numero_do('Berrondo'), 1)
        self.assertEqual(erdos.numero_do('Flávio'), 2)
        self.assertEqual(erdos.numero_do('A'), INFINITO)
        self.assertEqual(erdos.numero_do('B'), INFINITO)
        self.assertEqual(erdos.numero_do('C'), INFINITO)
        self.assertEqual(erdos.numero_do('D'), INFINITO)

        novos_livros = [['B', 'Flávio']]
        erdos.incluir_autores_de(novos_livros)
        self.assertEqual(erdos.numero_do('Erdos'), 0)
        self.assertEqual(erdos.numero_do('Berrondo'), 1)
        self.assertEqual(erdos.numero_do('Flávio'), 2)
        self.assertEqual(erdos.numero_do('A'), 4)
        self.assertEqual(erdos.numero_do('B'), 3)
        self.assertEqual(erdos.numero_do('C'), 4)
        self.assertEqual(erdos.numero_do('D'), 5)

    def teste_promocao_intermediaria(self):
        livros = [
            ['Erdos', 'Berrondo'],
            ['Berrondo', 'Flávio'],
            ['Flávio', 'Magdalena'],
            ['Magdalena', 'Luiza'],
        ]
        erdos = NumeroDeErdos(livros)
        self.assertEqual(erdos.numero_do('Erdos'), 0)
        self.assertEqual(erdos.numero_do('Berrondo'), 1)
        self.assertEqual(erdos.numero_do('Flávio'), 2)
        self.assertEqual(erdos.numero_do('Magdalena'), 3)
        self.assertEqual(erdos.numero_do('Luiza'), 4)

        novos_livros = [['Erdos', 'Luiza']]
        erdos.incluir_autores_de(novos_livros)
        self.assertEqual(erdos.numero_do('Erdos'), 0)
        self.assertEqual(erdos.numero_do('Berrondo'), 1)
        self.assertEqual(erdos.numero_do('Flávio'), 2)
        self.assertEqual(erdos.numero_do('Magdalena'), 2)
        self.assertEqual(erdos.numero_do('Luiza'), 1)

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
        erdos = NumeroDeErdos(livros)
        self.assertEqual(erdos.numero_do('Erdos'), 0)
        self.assertEqual(erdos.numero_do('1'), 1)
        self.assertEqual(erdos.numero_do('2'), 2)
        self.assertEqual(erdos.numero_do('3'), 3)
        self.assertEqual(erdos.numero_do('4'), 4)
        self.assertEqual(erdos.numero_do('5'), 5)
        self.assertEqual(erdos.numero_do('6'), 6)
        self.assertEqual(erdos.numero_do('7'), 7)
        self.assertEqual(erdos.numero_do('8'), 8)

        novos_livros = [['2', '5']]
        erdos.incluir_autores_de(novos_livros)
        self.assertEqual(erdos.numero_do('Erdos'), 0)
        self.assertEqual(erdos.numero_do('1'), 1)
        self.assertEqual(erdos.numero_do('2'), 2)
        self.assertEqual(erdos.numero_do('3'), 3)
        self.assertEqual(erdos.numero_do('4'), 4)
        self.assertEqual(erdos.numero_do('5'), 3)
        self.assertEqual(erdos.numero_do('6'), 4)
        self.assertEqual(erdos.numero_do('7'), 5)
        self.assertEqual(erdos.numero_do('8'), 6)

        novissimos_livros = [['Erdos', '4']]
        erdos.incluir_autores_de(novissimos_livros)
        self.assertEqual(erdos.numero_do('Erdos'), 0)
        self.assertEqual(erdos.numero_do('1'), 1)
        self.assertEqual(erdos.numero_do('2'), 2)
        self.assertEqual(erdos.numero_do('3'), 2)
        self.assertEqual(erdos.numero_do('4'), 1)
        self.assertEqual(erdos.numero_do('5'), 2)
        self.assertEqual(erdos.numero_do('6'), 3)
        self.assertEqual(erdos.numero_do('7'), 4)
        self.assertEqual(erdos.numero_do('8'), 5)

        livros_mais_novos_ainda = [['3', '5', '8']]
        erdos.incluir_autores_de(livros_mais_novos_ainda)
        self.assertEqual(erdos.numero_do('Erdos'), 0)
        self.assertEqual(erdos.numero_do('1'), 1)
        self.assertEqual(erdos.numero_do('2'), 2)
        self.assertEqual(erdos.numero_do('3'), 2)
        self.assertEqual(erdos.numero_do('4'), 1)
        self.assertEqual(erdos.numero_do('5'), 2)
        self.assertEqual(erdos.numero_do('6'), 3)
        self.assertEqual(erdos.numero_do('7'), 4)
        self.assertEqual(erdos.numero_do('8'), 3)


        
unittest.main()