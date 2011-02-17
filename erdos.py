INFINITO = 9999   # um numero bem grande...

class No(object):
    def __init__(self, nome, nos_pais, numero):
        self.nome = nome
        self.nos_pais = nos_pais
        self._numero_de_erdos = numero
        self.coautores = set()
        self.deve_perfilhar_coautores = False
        
    def __call__(self): return self.numero_de_erdos
    
    def __cmp__(self, other):
        if self.numero_de_erdos == other.numero_de_erdos: return 0
        elif self.numero_de_erdos > other.numero_de_erdos: return 1
        else: return -1
        
    def coautoria(self, nos):
        # coautoria...
        for no in nos:
            if no.nome != self.nome:
                self.coautores.add(no)
        
        # e paternidade, apenas para relacionados com Erdos:
        no_menor = min(nos)
        if no_menor.numero_de_erdos != INFINITO:
            no_menor.perfilhar_nos_em(nos)
             
    def perfilhar_nos_em(self, nos):
        for no in nos:
            if no.nome != self.nome and self.numero_de_erdos != INFINITO:
                try:
                    no.nos_pais.add(self)
                    # ao ser perfilhado, noh ganha numero do perfilhador, se menor...
                    no._numero_de_erdos = min(no._numero_de_erdos, self.numero_de_erdos + 1)
                    # e tem que perfilhar seus coautores:
                    no.deve_perfilhar_coautores = True
                except AttributeError:
                    pass
                    
    @property
    def numero_de_erdos(self):
        if self._numero_de_erdos is None:
            self._numero_de_erdos = min(list(self.nos_pais)).numero_de_erdos + 1
        return self._numero_de_erdos
        
class NumeroDeErdos(dict):
    def __init__(self, livros):
        self['Erdos'] = self.no_central = No('Erdos', None, 0)
        self.incluir_livros(livros)
        
    def __call__(self, nome): return self[nome]
        
    def incluir_livros(self, livros):
        for livro in livros:
            # autores de cada livro viram nos e chaves no dict...
            nos = []
            for nome_do_autor in livro:
                no = self[nome_do_autor] = self.get(nome_do_autor, 
                                                    No(nome_do_autor, set(), INFINITO))
                nos.append(no)
                
            # depois sao relacionados atraves da coautoria:
            for no in nos:
                no.coautoria(nos)
                
        # e eh preciso reequilibrar a arvore:
        for n_vezes in range(len(livros) - 1):  ## soh isto aqui nao estah legal...
            self.reequilibrar_se()
            
    def reequilibrar_se(self):
        for no in self.values():
            if no.deve_perfilhar_coautores:
                no.perfilhar_nos_em(no.coautores)
                no.deve_perfilhar_coautores = False
