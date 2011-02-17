INFINITO = 9999   # apenas um numero suficientemente grande...

class Autor(object):
    def __init__(self, nome, numero):
        self.nome = nome
        self.numero_de_erdos = numero
        self.coautores = set()

    def __cmp__(self, other):
        if self.numero_de_erdos == other.numero_de_erdos: return 0
        elif self.numero_de_erdos > other.numero_de_erdos: return 1
        else: return -1
        
    def estabelecer_coautoria_com(self, autores):
        self.coautores.update(autores - set([self]))
        min(autores).perfilhar_cada_um_dos(autores)
        
    def perfilhar_cada_um_dos(self, autores):
        for autor in autores:
            if self < autor:
                autor.numero_de_erdos = self.numero_de_erdos + 1
                autor.perfilhar_cada_um_dos(autor.coautores)
                    
class NumeroDeErdos(dict):
    def __init__(self, livros):
        self['Erdos'] = Autor('Erdos', 0)
        self.incluir_autores_de(livros)

    def incluir_autores_de(self, livros):
        for livro in livros:
            autores = set(map(lambda nome: self.get(nome, Autor(nome, INFINITO)), livro))
            for autor in autores:
                self[autor.nome] = autor
                autor.estabelecer_coautoria_com(autores)
                
        