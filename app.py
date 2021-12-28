# playlist estrutura de dados do canal "Programação dinâmica"

# 1. Recursos computacionais
# - Memória = armazenar dados (ler e gravar) (ex: a = 5; b = 7)
# *** todo valor é armazenado na memória, mesmo que não esteja associado a uma variável, ou seja, a variável serve apenas para identificar onde está aquele valor, mas todo valor é gravado.
# - Processamento = realizar operações aritméticas

# 2. Noção intuitiva de complexidade
# - Complexidade de espaço: o quanto de memória está sendo utilizado (não é a complexidade default, pois na maioria dos casos o processamento que será mais escasso.)
# - Complexidade de tempo: quantas operações estão sendo feitas e quanto isso irá demorar
# *Para calcular complexidade, não necessitamos do número exato, e sim entender o quanto ela varia dependendo do tamanho do input

# 3. Noção matemática de complexidade
# - Ao se referir a "o grande" de um algoritmo, estamos nos referindo em qual a complexidade dele, ou seja, buscando entender o termo dominante que rege esse algoritmo. Dessa forma, todas as constantes fazendo operações aritméticas com o termo dominante não importam, pois ao pensar em entradas muitos grandes (utilizando conceitos de Limites), importa-se somente o quanto ele cresce. Com isso, é importante saber que estaremos interessados no pior caso desse algoritmo, ou seja, o máximo de recursos que ele irá utilizar.

# 4. Lista linear em alocação sequencial - como funciona seu armazenamento
# - Ao se tratar de listas, podemos acessar seus valores por meio dos índices, e assim, sendo um índice após o outro. Com isso, entende-se que a lista é armazenada em um lugar aleatório de forma sequêncial, ou seja, um elemento após o outro na memória. Em uma lista com iguais tipos de dados, podemos prever em qual espaço da memória estará o próximo elemento, mas como no Python podemos armazenar diferentes tipos de dados em uma lista, ele utiliza ponteiros para armazenar esses dados e dessa forma podemos saber onde cada dado acaba e começa o próximo (sabendo em qual byte começou e quantos bytes um ponteiro ocupa).
# - E para acessar um elemento da lista, basta ir neste espaço da memória e pegar esse valor, sendo então uma operação O(1)

# 5. Buscar linear em listas
# - Caso seja uma lista em que não temos nenhuma informação sobre ela, teremos que no mínimo percorre-la por completo pelo menos uma vez para saber se uma valor está contido nela (1), havendo então uma complexidade de O(n). Caso tenhamos a informação de que é uma lista composta por inteiros e está ordenada, podemos reduzir a complexidade da lista utilizando o algoritmo de busca binária (2) (dividir para conquistar).

# (1).
lista = [1, 5, 2, 'abc', True]
elemento_escolhido = 2

def busca_lista (lista, elemento):
  """Busca por elemento na lista e retorna o seu índice caso esteja contido na lista ou retorna None caso contrário"""
  for i in range(len(lista)):
    if lista[i] == elemento:
      return i
  return None

# (2).
lista = [1, 2, 5, 8, 10, 24]
elemento_escolhido = 10

def busca_binaria_lista(lista, elemento):
  """Busca binária na lista e retorna o seu índice caso esteja contido na lista ou retorna None caso contrário"""
  pass


# 6. Inserção e remoção em listas
# - Para inserir um elemento na lista, o melhor caso em termos de complexidade é inserir um elemento no final da lista, assim, basta saber se é um espaço livre na memória, e se sim, basta colocar o valor lá. Com isso, contém uma complexidade de O(1).
# - Já para inserir o elemento em qualquer lugar da lista, quanto mais perto do início maior será a complexidade, pois há a necessidade de ir movendo os elementos para para o final da lista. Com isso, caso queira inserir um elemento no início da lista, há a necessidade de mover todos os elementos da lista para liberar esse espaço no início. Com isso, é um algoritmo de complexidade O(n), sendo n o tamanho da lista.
# *Por baixo dos panos, quando adicionarmos um elemento na lista, a linguagem procura por outro espaço na memória com maior tamanho para colocar a nova lista lá e libera o espaço anterior.

# - A remoção de um elemento da lista segue a mesma ideia, remover um elemento na última posição tem complexidade O(1) e remover qualquer outro elemento na lista tem complexidade variável sendo então O(n) (isso pois não pode haver buracos na lista, então move os elementos para preencher).
# *Uma desvantagem das listas de alocação sequêncial é que ao remover um elemento, o espaço de memória para lista se mantém do criado inicialmente. Então, assim como para adicionar um novo elemento há a alocação de um novo espaço de forma automática, deve-se fazer isso para uma lista que foi diminuida.

# 7. Nó e alocação encadeada (objetos/dicionário)
# - Diferente das listas de alocação sequenciais, são armazenados em espaços quaisquer e só há a alocação de memória a mais quando necessário. Para fazer o encadeamento desses dados que não são contíguos, há o uso do "nó". Sendo um envelope que está na memória e dentro desse envelope contém o dado em si e a informação do próximo nó, para formar o encadeamento. *não é possível encontrar o elemento anterior com o nó.
# - Python não há um built-in para criar as linked lists, assim, se cria manualmente utilizando os conceitos de nó's. As linked lists são utilizadas para armazenar valores como as listas de alocação sequêncial, porém, com uma maior facilidade para gerenciamento de memória, pois esse alocamento é feito de forma dinâmica, ou seja, se precisar adicionar mais um valor, a alteração ocorre apenas adicionando esse valor, não há alteração na lista inteira como na lista de alocação sequêncial (add um valor => cria uma lista nova inteira com o novo valor).

# * Análise de complexidade entre listas sequênciais e linked lists
# - Acessar um elemento: sequencial = O(1) / linked = O(n)
# - Modificar elemento: sequencial = O(1) / linked = O(n)
# - Adicionar um novo elemento: sequencial = O(1) / linked = O(n)
# - Remover um elemento: sequencial = O(1) / linked = O(n)


# 8. Pilhas
# - Utilizado para situações específicas em que os dados terão a política de acesso LIFO (last in -> first out), ou seja, último a entrar será o primeiro a sair.
# - As pilhas também utilizam o conceito de nó, contendo nele o dado e a informação do próximo elemento (sempre começando do topo para baixo).
# - O acesso nos elementos da pilha ocorre do topo para baixo, ou seja, caso queira visualizar o último elemento da pilha (topo), bastaria uma complexidade de O(1). Com essa informação, é possível constatar que as operações de adicionar um elemento na pilha ou remover um elemento (ambos ocorrem no topo), basta apenas saber qual o último elemento, tendo então uma complexidade O(1). E para visualizar os elementos da pilha, bastaria percorre-la por inteira, com complexidade O(n).

# 9. Filas
# - Seguem a política de acesso FIFO (first in -> first out), assim, o primeiro a chegar será o primeiro a sair.
# - As filas mantém o conceito de nó e usualmente são importantes estruturas de dados para gerenciar processos e requisições, em que aplicações podem aguentar grande sobrecarga e realizar as tarefas sem a queda do sistema, sendo uma ótima opção para gerenciar um sistema em gargalo ao organiza-los em filas e realizando as ações em sequência sem perder dados.
# - Com o objetivo de aumentar a performance, as filas adicionam elementos no final dela e retiram no início, e isso só é possível pois a pilha armazena o primeiro e último nó na sua criação. Mas a estrutura do nó se mantém.
# - Em termos de complexidade, adicionar ou remover um elemento na fila tem complexidade O(1), pois só podemos adicionar um elemento no final dela (temos a informação do nó final) e também só podemos retirar um elemento se estiver no início dela (tb temos essa informação). E para saber o primeiro elemento da fila tb há a complexidade O(1).
