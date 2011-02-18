'bout Erdos:

então, quando um desses problemas de dojo te pega?

verdade é que às vezes achamos alguns problemas interessantes, às vezes não e, quando achamos, frequentemente não encontramos o tempo ou a oportunidade para darmos os nossos tratos à bola...

mas, problem-solving-addicts que somos, pode haver um dia em que a cabeça deixada vaga dos problemas do dia-a-dia seja tomada por um daqueles que a gente vê no dojo.

e foi o que aconteceu comigo e com o Número de Erdos, sei lá porque...

tanto que propus três seções de dojo seguidas com o problema e ainda o levei para casa!

e ainda fizemos uma sessão extra, eu e o Flávio Amieiro, para atacar o problema (sei que tem gente aí que queria ter participado dessa sessão...)

tudo começa com a gente discutindo afinal o que são baby-steps, o que é o design orientado pelos testes, como roubar legalmente (!) e onde e quando quebrar as regras.

frequentemente vemos em nossos encontros semanais regras sendo levadas a sério demais e os baby-steps e o salutar hábito de roubar (!) serem vítimas de misconceptions...

disclaimer aqui que um dos motivos da saúde, vitalidade, longevidade e fertilidade do nosso grupo é exatamente seu amor pelas regras! o fato de a turma nunca ter deixado o dojo degenerar. seguir as regras garante um dojo inclusivo para qualquer um que chega, em qualquer momento. e é quem está chegando que vai levar o dojo adiante.

e seguir regras é o que fazemos quando não sabemos: quando a repetição fizer da regra nosso hábito, saberemos quando quebrá-la!

em nossa primeira sessão de dojo com o número de Erdos, terminamos com a impressão de que precisávamos uma árvore. por isso, em uma sessão seguinte, tentei propor aos presentes que, em vez de fugir, como sempre fazemos, do core do problema (porque focamos o processo e não a solução), que em vez disso, atacássemos o problema de constriur uma árvore, baby-steps, orientados por testes e tendo como pano de fundo o problema concreto do Erdos.

não, a sugestão não foi adiante e naquele dia começamos de novo. o Juan Lopes então sugeriu que se tratava de um grafo e de um algoritmo de menor caminho...

e é mesmo. algo como:

import grafo

grafo.menor_caminho('erdos', 'fulano')

e lá se foi o baby-step, o test driven e a ideia de menor solução que possa funcionar! claro que um grafo e o menor caminho são a solução genérica para este problema e para milhares de outros, mas e qual é a menor solução possível que nos permita calcular o número de Erdos? será que ela nos levaria a implementar um grafo e calcular menores caminhos?

além disso, uma árvore é um caso particular do grafo e se os livros dados de nossos autores jamais fossem mudar, solução suficiente se construída corretamente.

a ideia da árvore foi uma hipótese que exploramos. algo para nos levar adiante na compreensão do problema, sem que ficássemos paralizados pensando em resolver o problema inteiro e todos os seus corner cases.

bom, isto *é* um baby-step! e *também é* um roubo!

às vezes no dojo, roubar parece ser a busca da solução mais porca possível... mas roubar pra valer é apenas aplicar a melhor solução que abstraímos para o momento, com a compreensão do problema que adquirimos até aquele momento, nos valendo do fato que o domínio do problema está sob o nosso controle através dos testes: testamos o menor mundo que pudermos imaginar ou o menor que nos caiba na cabeça com a compreensão que temos até então.

com a nossa árvore não foi diferente. orientamos nossos testes a levar nosso código a ser capaz de lidar com uma árvore de um ramo só! o que seria facilmente implementado em uma lista. e ficamos capazes de mostrar que cada nó da árvore podia perguntar o número de erdos de seu pai e somar um para nos mostrar o seu!

dar este simples passo - em vez de ficar paralizado pensando na solução do problema inteiro ou roubando de maneira porca - nos coloca um pouco mais para dentro do espaço do problema e passamos a compreender melhor as relações que estes "nós-autores" terão que manter para que possamos calcular seus números (que é apenas a distância deles até o "nó-erdos") e mais, entendermos que com qualquer nova relação entre "nós-autores" dadas por novas coautorias entre eles, temos que ser capazes de atualizar essas relações e recalcular os números dos nós envolvidos.

enfim, um problema cheio de manhas! (e por isso mesmo interessante!)

na nossa primeira implementação da árvore, tínhamos pais, tínhamos filhos e chegamos a escrever um algoritmo de busca na árvore! que quebrou com o primeiro aprofundamento ou alargamento da árvore...

porque uma das coisas que descobrimos era de que precisávamos recuperar cada nó-autor na árvore para estabelecer, ou seguir, ou atualizar suas relações, o que nos levou a outra "solução mais simples que podia funcionar": para acharmos cada nó, bastava um índice, logo, porque não um dicionário?!

de novo, o objetivo da solução não é implementar uma busca em largura, profundidade, backtrack, whatever e nos fazer procurar nos cadernos do tempo da disciplina de estrutura de dados. não! apenas temos que ser capazes de dizer qual o número de erdos de um autor específico!!

assim, o dicionário cuja chave é o nome do autor e o valor o nó-autor é um baby-step! um roubo, uma menor solução que pode funcionar!! e, de novo, elimina um problema de nossa cabeça e nos leva mais para perto do problema a solucionar de fato!



