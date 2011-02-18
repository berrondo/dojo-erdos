'bout Erdos:

ent�o, quando um desses problemas de dojo te pega?

verdade � que �s vezes achamos alguns problemas interessantes, �s vezes n�o e, quando achamos, frequentemente n�o encontramos o tempo ou a oportunidade para darmos os nossos tratos � bola...

mas, problem-solving-addicts que somos, pode haver um dia em que a cabe�a deixada vaga dos problemas do dia-a-dia seja tomada por um daqueles que a gente v� no dojo.

e foi o que aconteceu comigo e com o N�mero de Erdos, sei l� porque...

tanto que propus tr�s se��es de dojo seguidas com o problema e ainda o levei para casa!

e ainda fizemos uma sess�o extra, eu e o Fl�vio Amieiro, para atacar o problema (sei que tem gente a� que queria ter participado dessa sess�o...)

tudo come�a com a gente discutindo afinal o que s�o baby-steps, o que � o design orientado pelos testes, como roubar legalmente (!) e onde e quando quebrar as regras.

frequentemente vemos em nossos encontros semanais regras sendo levadas a s�rio demais e os baby-steps e o salutar h�bito de roubar (!) serem v�timas de misconceptions...

disclaimer aqui que um dos motivos da sa�de, vitalidade, longevidade e fertilidade do nosso grupo � exatamente seu amor pelas regras! o fato de a turma nunca ter deixado o dojo degenerar. seguir as regras garante um dojo inclusivo para qualquer um que chega, em qualquer momento. e � quem est� chegando que vai levar o dojo adiante.

e seguir regras � o que fazemos quando n�o sabemos: quando a repeti��o fizer da regra nosso h�bito, saberemos quando quebr�-la!

em nossa primeira sess�o de dojo com o n�mero de Erdos, terminamos com a impress�o de que precis�vamos uma �rvore. por isso, em uma sess�o seguinte, tentei propor aos presentes que, em vez de fugir, como sempre fazemos, do core do problema (porque focamos o processo e n�o a solu��o), que em vez disso, atac�ssemos o problema de constriur uma �rvore, baby-steps, orientados por testes e tendo como pano de fundo o problema concreto do Erdos.

n�o, a sugest�o n�o foi adiante e naquele dia come�amos de novo. o Juan Lopes ent�o sugeriu que se tratava de um grafo e de um algoritmo de menor caminho...

e � mesmo. algo como:

import grafo

grafo.menor_caminho('erdos', 'fulano')

e l� se foi o baby-step, o test driven e a ideia de menor solu��o que possa funcionar! claro que um grafo e o menor caminho s�o a solu��o gen�rica para este problema e para milhares de outros, mas e qual � a menor solu��o poss�vel que nos permita calcular o n�mero de Erdos? ser� que ela nos levaria a implementar um grafo e calcular menores caminhos?

al�m disso, uma �rvore � um caso particular do grafo e se os livros dados de nossos autores jamais fossem mudar, solu��o suficiente se constru�da corretamente.

a ideia da �rvore foi uma hip�tese que exploramos. algo para nos levar adiante na compreens�o do problema, sem que fic�ssemos paralizados pensando em resolver o problema inteiro e todos os seus corner cases.

bom, isto *�* um baby-step! e *tamb�m �* um roubo!

�s vezes no dojo, roubar parece ser a busca da solu��o mais porca poss�vel... mas roubar pra valer � apenas aplicar a melhor solu��o que abstra�mos para o momento, com a compreens�o do problema que adquirimos at� aquele momento, nos valendo do fato que o dom�nio do problema est� sob o nosso controle atrav�s dos testes: testamos o menor mundo que pudermos imaginar ou o menor que nos caiba na cabe�a com a compreens�o que temos at� ent�o.

com a nossa �rvore n�o foi diferente. orientamos nossos testes a levar nosso c�digo a ser capaz de lidar com uma �rvore de um ramo s�! o que seria facilmente implementado em uma lista. e ficamos capazes de mostrar que cada n� da �rvore podia perguntar o n�mero de erdos de seu pai e somar um para nos mostrar o seu!

dar este simples passo - em vez de ficar paralizado pensando na solu��o do problema inteiro ou roubando de maneira porca - nos coloca um pouco mais para dentro do espa�o do problema e passamos a compreender melhor as rela��es que estes "n�s-autores" ter�o que manter para que possamos calcular seus n�meros (que � apenas a dist�ncia deles at� o "n�-erdos") e mais, entendermos que com qualquer nova rela��o entre "n�s-autores" dadas por novas coautorias entre eles, temos que ser capazes de atualizar essas rela��es e recalcular os n�meros dos n�s envolvidos.

enfim, um problema cheio de manhas! (e por isso mesmo interessante!)

na nossa primeira implementa��o da �rvore, t�nhamos pais, t�nhamos filhos e chegamos a escrever um algoritmo de busca na �rvore! que quebrou com o primeiro aprofundamento ou alargamento da �rvore...

porque uma das coisas que descobrimos era de que precis�vamos recuperar cada n�-autor na �rvore para estabelecer, ou seguir, ou atualizar suas rela��es, o que nos levou a outra "solu��o mais simples que podia funcionar": para acharmos cada n�, bastava um �ndice, logo, porque n�o um dicion�rio?!

de novo, o objetivo da solu��o n�o � implementar uma busca em largura, profundidade, backtrack, whatever e nos fazer procurar nos cadernos do tempo da disciplina de estrutura de dados. n�o! apenas temos que ser capazes de dizer qual o n�mero de erdos de um autor espec�fico!!

assim, o dicion�rio cuja chave � o nome do autor e o valor o n�-autor � um baby-step! um roubo, uma menor solu��o que pode funcionar!! e, de novo, elimina um problema de nossa cabe�a e nos leva mais para perto do problema a solucionar de fato!



