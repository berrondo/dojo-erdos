INFINITO = 9999   # um numero bem grande...

class Autor(object):
    def __init__(self, nome, numero):
        self.nome = nome
        self.numero_de_erdos = numero
        self.coautores = set()
        self.deve_perfilhar_coautores = False
        
    def __call__(self): return self.numero_de_erdos
    
    def __cmp__(self, other):
        if self.numero_de_erdos == other.numero_de_erdos: return 0
        elif self.numero_de_erdos > other.numero_de_erdos: return 1
        else: return -1
        
    def estabelecer_coautoria_com(self, autores):
        self.coautores.update(autores - set([self]))
        
    def perfilhar_nos_em(self, autores):
        for autor in autores:
            if self < autor:
                # ao ser perfilhado, noh ganha numero do perfilhador, se menor...
                autor.numero_de_erdos = min(autor.numero_de_erdos, self.numero_de_erdos + 1)
                # e tem que perfilhar seus coautores:
                autor.perfilhar_nos_em(autor.coautores)
                    
class NumeroDeErdos(dict):
    def __init__(self, livros):
        self['Erdos'] = Autor('Erdos', 0)
        self.incluir_livros(livros)
        
    def __call__(self, nome): return self[nome]
        
    def incluir_livros(self, livros):
        for livro in livros:
            # autores de cada livro viram nos e chaves no dict...
            autores = set(map(lambda nome: self.get(nome, Autor(nome, INFINITO)), livro))
                
            # depois sao relacionados atraves da coautoria:
            for autor in autores:
                self[autor.nome] = autor
                autor.estabelecer_coautoria_com(autores)
                
            # e paternidade, apenas para relacionados com Erdos:
            min(autores).perfilhar_nos_em(autores)
        