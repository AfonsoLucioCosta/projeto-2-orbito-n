# POSICAO (2.1.1)
# Construtor
def cria_posicao(col, lin):
    
    """
    Cria uma posicao, que e  um par ordenado de dois valores: uma letra entre 'a' e 'j' e um numero inteiro entre 1 e 10.
    
    Argumentos:
        col (str): Letra entre 'a' e 'j'.
        lin (int): Numero inteiro entre 1 e 10.
    
    Retorna:
        tuple: Uma posicao, que e  um par ordenado (col, lin).
    
    Erros:
        ValueError: Se os argumentos nao forem validos.
    """
    if type(col) != str or type(lin) != int: #verifica se os argumentos sao validos, coluna string e linha inteiro
        raise ValueError('cria_posicao: argumentos invalidos') 
        
    if col not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'] or lin not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]: #verifica se a coluna e a linha estao dentro dos limites
        raise ValueError('cria_posicao: argumentos invalidos')
    
    return (col, lin) 

# Seletores
def obtem_pos_col(p) -> str:
    """
    Devolve a coluna de uma posicao p.
    
    Argumentos:
        p (tuple): Uma posicao.
    
    Retorna:
        str: A coluna de p.
    """
    return p[0] #retorna a coluna

def obtem_pos_lin(p) -> int:    
    """
    Devolve a linha de uma posicao p.
    
    Argumentos:
        p (tuple): Uma posicao.
    
    Retorna:
        int: A linha de p.
    """
    return p[1] #retorna a linha

# Reconhecedor
def eh_posicao(arg) -> bool:
    """
    Verifica se um argumento eh uma posicao.
    
    Argumentos:
        arg (object): O argumento a ser verificado.
    
    Retorna:
        bool: True se o argumento for uma posicao, False caso contrario.
    """
    if not isinstance(arg, tuple) or len(arg) != 2: #verifica se o argumento e uma tuplo de 2 elementos
        return False
    if not isinstance(arg[0], str) or type(arg[1]) != int: #verifica se o primeiro elemento do tuplo e uma string e o segundo e um inteiro
        return False
    if arg[0] not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'] or arg[1] not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]: #verifica se a coluna e a linha estao dentro dos limites
        return False
    return True

# Teste
def posicoes_iguais(p1, p2) -> bool:
    """
    Verifica se duas posicoes sao iguais.
    
    Argumentos:
        p1 (tuple): Primeira posicao.
        p2 (tuple): Segunda posicao.
    
    Retorna:
        bool: True se as posicoes forem iguais, False caso contrario.
    """
    if not (eh_posicao(p1) and eh_posicao(p2)): #verifica se as posicoes sao validas
        return False
    return p1 == p2 #verifica se as posicoes sao iguais
    
def posicao_para_str(p) -> str:
    """
    Converte uma posicao para uma string.
    
    Argumentos:
        p (tuple): A posicao a ser convertida.
    
    Retorna:
        str: A string que representa a posicao.
    """
    if type(p) == tuple: #verifica se a posicao e uma tuplo
        return f"{obtem_pos_col(p)}{obtem_pos_lin(p)}" #converte a posicao para uma string

def str_para_posicao(s) -> tuple:
    """
    Converte uma string para uma posicao.
    
    Argumentos:
        s (str): A string a ser convertida.
    
    Retorna:
        tuple: A posicao que representa a string.
    """
    if type(s) == str: #verifica se a string e uma string
        return cria_posicao(s[0], int(s[1])) #converte a string para uma posicao

# Funcoes de alto nivel
def eh_posicao_valida(p, n) -> bool:

    """
    Verifica se uma posicao e valida para um tabuleiro de tamanho n.
    
    Argumentos:
        p (tuple): A posicao a ser verificada.
        n (int): O tamanho do tabuleiro.
    
    Retorna:
        bool: True se a posicao for valida, False caso contrario.
    """
    if not (2 <= n <= 5): #verifica se o tabuleiro tem um tamanho entre 2 e 5 orbitas
        return False
    min_lin = 1  # minima linha
    max_lin = 2 * n  # maxima linha
    min_col = 'a'  # minima coluna
    max_col = chr(96 + 2 * n)  # maxima coluna
    if eh_posicao(p) and min_lin <= obtem_pos_lin(p) <= max_lin and min_col <= obtem_pos_col(p) <= max_col: #verifica se a posicao e valida e se esta dentro do tabuleiro
        return True
    return False

def obtem_posicoes_adjacentes(p, n, d) -> list:

    """
    Devolve uma lista com as posicoes adjacentes a uma dada posicao p, considerando um tabuleiro de tamanho n.
    
    Argumentos:
        p (tuple): A posicao a ser considerada.
        n (int): O tamanho do tabuleiro.
        d (bool): Booleano que indica se a funcao deve considerar 4 ou 8 posicoes adjacentes.
    
    Retorna:
        list: Uma lista com as posicoes adjacentes a p, considerando o valor de d.
    """
    column, row = p 
    final=[]
    resultado = []
    if d == False: #se d for False retorna as posicoes ortogonais
        resultado = [(column, row - 1), (chr(ord(column) + 1), row), (column, row + 1), (chr(ord(column) - 1), row)] #retorna as posicoes adjacentes
        for i in resultado: 
            if eh_posicao_valida(i, n): #verifica se as posicoes ortogonais sao validas
                final.append(i) #adiciona as posicoes ortogonais
        return final

    else: #se d for True retorna as posicoes adjacentes
        resultado = [(column, row - 1), (chr(ord(column) + 1), row - 1 ), (chr(ord(column) + 1), row), (chr(ord(column) + 1), row + 1), (column, row + 1), (chr(ord(column) - 1), row + 1), (chr(ord(column) - 1), row), (chr(ord(column) - 1), row - 1)] #retorna as posicoes adjacentes
        for i in resultado: 
            if eh_posicao_valida(i, n): #verifica se as posicoes adjacentes sao validas
                final.append(i) #adiciona as posicoes adjacentes
        return final

def aux_ordena_posicoes(p, n) -> int:
    """
    Calcula a distância de uma posição ao centro de um tabuleiro.

    Argumentos:
        p (tuple): A posição a ser avaliada.
        n (int): O tamanho do tabuleiro.

    Retorna:
        int: A distância máxima da posição ao centro do tabuleiro.
    """
    centro = n + 0.5 #posicao do centro
    dist = max(abs(centro - (ord(obtem_pos_col(p))-96)), abs(centro - obtem_pos_lin(p))) #calcula a distancia
    return dist

def ordena_posicoes(t, n) -> tuple:
    """
    Ordena um tuplo de posições de acordo com a distância ao centro do tabuleiro.

    Argumentos:
        t (list): A lista de posições a ser ordenada.
        n (int): O tamanho do tabuleiro.

    Retorna:
        tuple: A lista de posições ordenada.
    """
    
    x = sorted(t, key=lambda p: (aux_ordena_posicoes(p, n), obtem_pos_lin(p), obtem_pos_col(p))) #ordena as posicoes de acordo com a distancia
    return tuple(x)

# PEDRA (2.1.2)
# Construtor
def cria_pedra_branca() -> str:
    """
    Cria uma pedra branca.
    
    Retorna:
        str: Uma pedra branca.
    """
    return 'O' #retorna a pedra branca 'O'

def cria_pedra_preta() -> str:
    """
    Cria uma pedra preta.
    
    Retorna:
        str: Uma pedra preta.
    """
    return 'X' #retorna a pedra preta 'X'

def cria_pedra_neutra() -> str:
    """
    Cria uma pedra neutra.
    
    Retorna:
        str: Uma pedra neutra.
    """
    return ' ' #retorna a pedra neutra ' '

# Reconhecedor
def eh_pedra(arg) -> bool:
    """
    Verifica se um argumento eh uma pedra.
    
    Argumentos:
        arg (object): O argumento a ser verificado.
    
    Retorna:
        bool: True se o argumento for uma pedra, False caso contrario.
    """
    return arg == 'O' or arg == 'X' or arg == ' ' #verifica se o argumento e uma pedra, caso contrario retorna False

def eh_pedra_branca(p) -> bool:
    """
    Verifica se uma pedra eh branca.
    
    Argumentos:
        p (str): A pedra a ser verificada.
    
    Retorna:
        bool: True se a pedra for branca, False caso contrario.
    """
    return p == 'O' #verifica se a pedra e branca

def eh_pedra_preta(p) -> bool:
    """
    Verifica se uma pedra eh preta.
    
    Argumentos:
        p (str): A pedra a ser verificada.
    
    Retorna:
        bool: True se a pedra for preta, False caso contrario.
    """
    return p == 'X' #verifica se a pedra e preta

# Teste
def pedras_iguais(p1, p2) -> bool:
    """
    Verifica se duas pedras sao iguais.
    
    Argumentos:
        p1 (str): A primeira pedra a ser comparada.
        p2 (str): A segunda pedra a ser comparada.
    
    Retorna:
        bool: True se as pedras forem iguais, False caso contrario.
    """
    return eh_pedra(p1) and eh_pedra(p2) and p1 == p2 #verifica se as pedras sao iguais

def pedra_para_str(p) -> str:
    """
    Converte uma pedra em sua representação em string.

    Argumentos:
        p (str): A pedra a ser convertida.

    Retorna:
        str: 'O' se a pedra for branca, 'X' se for preta, ou ' ' se for neutra.
    """
    if eh_pedra_branca(p): #verifica se a pedra e branca
        return 'O'
    if eh_pedra_preta(p): #verifica se a pedra e preta
        return 'X'
    return ' '  #se nao for branca nem preta retorna ' '

#Funções de alto nivel
def eh_pedra_jogador(p) -> bool:
    """
    Verifica se uma pedra pertence a um jogador (branca ou preta).
    
    Argumentos:
        p (str): A pedra a ser verificada.
    
    Retorna:
        bool: True se a pedra for de um jogador (branca ou preta), False caso contrario.
    """
    if eh_pedra_branca(p) or eh_pedra_preta(p): #verifica se a pedra e branca ou preta
        return True #se sim, é uma pedra de um jogador
    return False    

def pedra_para_int(p) -> int:
    """
    Converte uma pedra em sua representação inteira.

    Argumentos:
        p (str): A pedra a ser convertida.

    Retorna:
        int: -1 se a pedra for branca, 1 se for preta, ou 0 se for neutra.
    """
    if eh_pedra_branca(p): #verifica se a pedra e branca
        return -1 
    if eh_pedra_preta(p): #verifica se a pedra e preta
        return 1
    return 0

# Tabuleiro (2.1.3)
# Construtor
def cria_tabuleiro_vazio(n) -> list:
    # Validação do argumento n
    """
    Cria um tabuleiro vazio para o jogo do Orbito-n com n orbitas.
    
    Argumentos:
        n (int): O tamanho do tabuleiro.
    
    Retorna:
        list: Um tabuleiro vazio com n*2 linhas e n*2 colunas.
    """
    if type(n) != int or n < 2 or n > 5: #verifica se o argumento n, numero de orbitas é valido
        raise ValueError('cria_tabuleiro_vazio: argumento invalido')
    tabuleiro = []
    for i in range(n*2): #percorre as linhas
        linha = [' '] * n * 2  #cria uma linha vazia
        tabuleiro.append(linha) #insere a linha vazia no tabuleiro
    return tabuleiro

def cria_tabuleiro(n, tp, tb):
    """
    Cria um tabuleiro para o jogo do Orbito-n com n orbitas e posicoes de pedras pretas e brancas.

    Argumentos:
        n (int): O tamanho do tabuleiro.
        tp (tuple): Posicoes de pedras pretas.
        tb (tuple): Posicoes de pedras brancas.

    Retorna:
        list: Um tabuleiro com n*2 linhas e n*2 colunas.
    """
    
    if type(n) != int or n < 2 or n > 5 or type(tp) != tuple or type(tb) != tuple: #verifica se o argumento n, numero de orbitas, tuplo de posicoes de pedras pretas e tuplo de posicoes de pedras brancas são validos
        raise ValueError('cria_tabuleiro: argumentos invalidos')
    for i in tp: #percorre o tuplo de posicoes de pedras pretas
        if not eh_posicao_valida(i, n):   #verifica se as posicoes se as pedras pretas são validas
            raise ValueError('cria_tabuleiro: argumentos invalidos')
    for i in tb: #percorre o tuplo de posicoes de pedras brancas
        if not eh_posicao_valida(i, n):   #verifica se as posicoes se as pedras brancas são validas
            raise ValueError('cria_tabuleiro: argumentos invalidos')

    novo_tabuleiro = cria_tabuleiro_vazio(n) #cria um tabuleiro vazio
    for p in tp: #percorre o tuplo de posicoes de pedras pretas
        lin, col = obtem_pos_lin(p), obtem_pos_col(p) #obtem a linha e a coluna da posicao
        coluna_index = ord(col) - 97 #obtem o indice da coluna
        novo_tabuleiro[coluna_index][lin-1] = cria_pedra_preta() #insere a pedra preta no tabuleiro
    for p in tb: #percorre o tuplo de posicoes de pedras brancas
        lin, col = obtem_pos_lin(p), obtem_pos_col(p) #obtem a linha e a coluna da posicao
        coluna_index = ord(col) - 97 #obtem o indice da coluna
        novo_tabuleiro[coluna_index][lin-1] = cria_pedra_branca() #insere a pedra branca no tabuleiro
    return novo_tabuleiro #retorna o tabuleiro

def cria_copia_tabuleiro(t) -> list:
    """
    Cria uma copia do tabuleiro.

    Argumentos:
        t (list): O tabuleiro a ser copiado.

    Retorna:
        list: Uma copia do tabuleiro.
    """
    
    return list(map(list, t)) #cria uma copia do tabuleiro

# Seletores
def obtem_numero_orbitas(t) -> int:
    """
    Devolve o numero de orbitas do tabuleiro.

    Argumentos:
        t (list): O tabuleiro.

    Retorna:
        int: O numero de orbitas do tabuleiro.
    """
    return len(t) // 2 #devolve o numero de orbitas

def obtem_pedra(t, p) -> str:

    """
    Devolve a pedra na posicao p do tabuleiro t.

    Argumentos:
        t (list): O tabuleiro.
        p (tuple): A posicao.

    Retorna:
        str: A pedra na posicao p do tabuleiro t. Se a posicao estiver vazia, devolve uma pedra neutra.
    """
    lin = obtem_pos_lin(p) - 1 #obtem a linha da posicao
    col = ord(obtem_pos_col(p)) - 97 # obtem a coluna da posicao

    if 0 <= lin < len(t) and 0 <= col < len(t[0]): #verifica se a linha e a coluna da posicao estão dentro do tabuleiro
        return t[col][lin] if t[col][lin] else cria_pedra_neutra() #devolve a pedra da posicao
    return cria_pedra_neutra() #caso contrario, devolve uma pedra neutra

def obtem_linha_horizontal(t, p) -> tuple:    
    """
    Devolve as posicoes e pedras na linha horizontal de uma posicao dada em um tabuleiro.

    Argumentos:
        t (list): O tabuleiro.
        p (tuple): A posicao de referencia.

    Retorna:
        tuple: Um tuplo contendo as posicoes e as pedras na linha horizontal da posicao p.
    """
    col, lin = obtem_pos_col(p), obtem_pos_lin(p) #obtem a coluna e a linha da posicao
    linha_horizontal = ()
    for i in range(len(t[0])):  # Percorre as colunas do tabuleiro
        linha_horizontal += ((cria_posicao(chr(ord("a") + i), lin), obtem_pedra(t, cria_posicao(chr(ord("a") + i), lin))),) #devolve as posicoes e as pedras na linha horizontal
    return linha_horizontal

def obtem_linha_vertical(t, p) -> tuple:
    """
    Devolve as posicoes e pedras na coluna vertical de uma posicao dada em um tabuleiro.

    Argumentos:
        t (list): O tabuleiro.
        p (tuple): A posicao de referencia.

    Retorna:
        tuple: Um tuplo contendo as posicoes e as pedras na coluna vertical da posicao p.
    """
    col, lin = obtem_pos_col(p), obtem_pos_lin(p) #obtem a coluna e a linha da posicao
    coluna_vertical = ()
    for i in range(len(t)):  # Percorre as linhas do tabuleiro
        coluna_vertical += ((cria_posicao(col, i + 1), obtem_pedra(t, cria_posicao(col, i + 1))),) #devolve as posicoes e as pedras na coluna vertical
    return coluna_vertical

def obtem_linhas_diagonais(t, p) -> tuple:
    """
    Devolve as posicoes e pedras nas linhas diagonais de uma posicao dada em um tabuleiro.

    Argumentos:
        t (list): O tabuleiro.
        p (tuple): A posicao de referencia.

    Retorna:
        tuple: Um tuplo contendo as posicoes e as pedras nas linhas diagonais da posicao p.
    """
    col_aux, lin_aux = obtem_pos_col(p), obtem_pos_lin(p) #obtem a coluna e a linha da posicao
    diagonal = () 
    antidiagonal = () 

    col_aux = ord(col_aux) - 96 #passa a coluna para o formato numerico


    linha = lin_aux
    coluna = col_aux
    while linha >= 0 and coluna >= 0: #percorre a diagonal da esquerda para a direita
        if linha >= len(t) or coluna >= len(t[0]): #verifica se a posicao ultrapassa os limites do tabuleiro
            linha -= 1 #se sim, diminui a linha
            coluna -= 1 #diminui a coluna
            continue #continua a percorrer a diagonal
        diagonal = ((cria_posicao(chr(ord('a') + coluna), linha + 1), obtem_pedra(t, cria_posicao(chr(ord('a') + coluna), linha + 1))),) + diagonal #devolve as posicoes e as pedras na diagonal
        linha -= 1 
        coluna -= 1

    linha = lin_aux + 1 
    coluna = col_aux + 1 
    while linha < len(t) and coluna < len(t):  
        diagonal += ((cria_posicao(chr(ord('a') + coluna), linha + 1), obtem_pedra(t, cria_posicao(chr(ord('a') + coluna), linha + 1))),)
        linha += 1
        coluna += 1


    linha = lin_aux -1 
    coluna = col_aux -1
    while linha >= 0 and coluna < len(t):  
        antidiagonal = antidiagonal + ((cria_posicao(chr(ord('a') + coluna), linha + 1), obtem_pedra(t, cria_posicao(chr(ord('a') + coluna), linha + 1))),) 
        linha -= 1
        coluna += 1

    linha = lin_aux 
    coluna = col_aux - 2 
    while linha < len(t) and coluna >= 0:  
        antidiagonal = ((cria_posicao(chr(ord('a') + coluna), linha + 1), obtem_pedra(t, cria_posicao(chr(ord('a') + coluna), linha + 1))),) + antidiagonal
        linha += 1
        coluna -= 1

    return diagonal, antidiagonal

def obtem_posicoes_pedra(t, j) -> tuple:
    
    """
    Devolve as posicoes de pedras de um dado tipo em um tabuleiro.

    Argumentos:
        t (list): O tabuleiro.
        j (str): O tipo de pedra ('b' para branca ou 'p' para preta).

    Retorna:
        tuple: Um tuplo com as posicoes das pedras do tipo 'j' no tabuleiro.
    """
    posicoes = []
    for lin in range(len(t)):  # Percorre as linhas do tabuleiro
        for col in range(len(t[0])):  # Percorre as colunas do tabuleiro
            if t[col][lin] == j:  # Se a posição tem uma pedra do tipo 'j'
                posicao = cria_posicao(chr(ord('a') + col), lin + 1) #devolve a posicao
                posicoes.append(posicao) #adiciona a posicao na lista de posicoes
    posicoes_ordenadas = ordena_posicoes(posicoes, obtem_numero_orbitas(t)) #ordena as posicoes
    return posicoes_ordenadas 

# Modificadores
def coloca_pedra(t, p, j) -> list:
    """
    Modifica o tabuleiro para ter uma pedra do tipo 'j' na posicao 'p'.

    Argumentos:
        t (list): O tabuleiro.
        p (str): A posicao para onde se deseja colocar a pedra.
        j (str): O tipo de pedra ('b' para branca ou 'p' para preta).

    Retorna:
        list: O tabuleiro com a pedra do tipo 'j' na posicao 'p'.
    """
    col, lin = obtem_pos_col(p), obtem_pos_lin(p) #obtem a coluna e a linha
    t[ord(col)-97][lin - 1] = j #troca a pedra no tabuleiro
    return t

def remove_pedra(t, p) -> list:
    """
    Remove a pedra na posicao 'p' do tabuleiro.

    Argumentos:
        t (list): O tabuleiro.
        p (str): A posicao da pedra a ser removida.

    Retorna:
        list: O tabuleiro com a pedra na posicao 'p' removida.
    """
    col, lin = obtem_pos_col(p), obtem_pos_lin(p) #obtem a coluna e a linha
    t[lin - 1][ord(col)-97] = cria_pedra_neutra() #remove a pedra no tabuleiro
    return t

# Reconhecedor
def eh_tabuleiro(tab) -> bool:

    """
    Verifica se o argumento dado representa um tabuleiro válido para o jogo do Orbito-n.

    Argumentos:
        tab (list): O tabuleiro a ser verificado.

    Retorna:
        bool: True se o tabuleiro for válido, False caso contrário. Um tabuleiro válido deve ser uma lista de listas (representando colunas), cada uma com o mesmo comprimento, entre 4 e 10, contendo apenas pedras brancas, pretas ou neutras.
    """
    if type(tab) != list: #verifica se o argumento eh uma lista
        return False
    for i in tab: #percorre o tabuleiro
        if type(i) != list:  #verifica se cada elemenot do tabuleiro é uma lista
            return False
    for i in tab: #percorre o tabuleiro
        if len(i) != len(tab): #verifica se todas as listas do tabuleiro tem o mesmo comprimento
            return False
    if not 4 <= len(tab) <= 10: #verifica se o tabuleiro tem entre 4 e 10 linhas
        return False
    for col in tab: #percorre o tabuleiro
        for lin in col: #percorre as linhas
            if not lin in [cria_pedra_branca(), cria_pedra_preta(), cria_pedra_neutra()]: #verifica se cada elemento do tabuleiro é uma pedra
                return False
    return True

def tabuleiros_iguais(t1, t2) -> bool:
    """
    Verifica se dois tabuleiros são iguais.

    Argumentos:
        t1 (list): O primeiro tabuleiro.
        t2 (list): O segundo tabuleiro.

    Retorna:
        bool: True se os tabuleiros forem iguais, False caso contrário.
    """

    if not eh_tabuleiro(t1) or not eh_tabuleiro(t2): #verifica se os argumentos forem tabuleiros
        return False
    return t1 == t2 #verifica se os tabuleiros sao iguais

def tabuleiro_para_str(t) -> str:
    
    """
    Converte um tabuleiro em forma de string.

    A função tabuleiro_para_str converte um tabuleiro em forma de string, representando
    cada linha do tabuleiro com uma linha na string. Entre cada linha do tabuleiro, é
    adicionado um caractere de linha nova ("\n") e uma linha de separação que tem o mesmo
    comprimento da linha do tabuleiro. Entre cada coluna do tabuleiro, é adicionado um
    separador ("-").

    Args:
        t (list): O tabuleiro representado como um tuplo de tuplos.

    Returns:
        str: A string representando o tabuleiro.
    """
    
    tabuleiro = "   "
    for letra in range(len(t)): # Percorre as colunas
        if letra == len(t) - 1: # Se chegarmos à último
            tabuleiro += f" {chr(ord('a') + letra)}\n" # Adiciona a letra e uma quebra de linha para finalizar a linha
            break
        tabuleiro += f" {chr(ord('a') + letra)}  " # Adiciona a letra e um separador para a coluna seguinte

    for col in range(len(t)): # Percorre as colunas
        line = f"{col + 1:02} " # Adiciona a linha e o separador 
        for lin in range(len(t[col])): # Percorre as linhas
            if lin == len(t[col])-1: # Se chegarmos à última coluna
                line += f"[{t[lin][col]}]" # Acaba com X/O/' ', por ser a última coluna
                if not col == len(t)-1: # Enquanto não chegarmos à última linha (a percorrer todas as linhas)
                    line += "\n"
                    line_break = line.replace("[O]", " | ").replace("[X]", " | ").replace("[ ]", " | ").replace("-", " ").replace(f"{col + 1:02}", "  ")
                    line += line_break[:-2] + "\n" # Adiciona o separador, removendo o último separador extra
                tabuleiro += line # Concatena a linha ao tabuleiro
                break
            line += f"[{t[lin][col]}]-" # Enquanto estiver a percorrer as colunas
    return tabuleiro

# Funções de alto nivel
def move_pedra(t, p1, p2) -> list:
    """
    Move uma pedra de uma posição para outra no tabuleiro.

    A função move_pedra move uma pedra de uma posição para outra no tabuleiro. A
    pedra é removida da sua posição original e adicionada à sua posição destino.

    Argumentos:
        t (list): O tabuleiro.
        p1 (tuple): A posição original da pedra.
        p2 (tuple): A posição destino da pedra.

    Retorna:
        list: O tabuleiro com a pedra movida.
    """

    col1, lin1 = obtem_pos_col(p1), obtem_pos_lin(p1) # Obtem a coluna e linha da pedra
    x = t[ord(col1)-97][lin1 - 1] # Obtem a pedra
    if x == cria_pedra_neutra(): # Se a pedra for neutra
        return t # Retorna o tabuleiro
    col2, lin2 = obtem_pos_col(p2), obtem_pos_lin(p2)  # Obtem a coluna e linha da pedra
    t[ord(col2)-97][lin2 - 1] = x # Adiciona a pedra na nova posição
    t[ord(col1)-97][lin1 - 1] = cria_pedra_neutra() # Remove a pedra da antiga posição
    return t # Retorna o tabuleiro

def obtem_posicao_seguinte(t, p, s) -> tuple:
    """
    Devolve a posição seguinte à 'p' no tabuleiro 't', no sentido horário se 's' for
    True, ou no sentido anti-horário se 's' for False.

    Argumentos:
        t (list): O tabuleiro.
        p (str): A posição atual.
        s (bool): O sentido de movimento (True para horário, False para anti-horário).

    Retorna:
        tuple: A próxima posição no sentido especificado, ou None se não houver
        nenhuma posição adjacente na mesma órbita.
    """

    orbita = round(aux_ordena_posicoes(p, obtem_numero_orbitas(t)) + 0.1) # Obtem a orbita
    pos_adjacentes = obtem_posicoes_adjacentes(p, obtem_numero_orbitas(t), False) # Obtem as posicoes adjacentes
    same_orbit_positions = [pos for pos in pos_adjacentes if round(aux_ordena_posicoes(pos, obtem_numero_orbitas(t)) + 0.1) == orbita]     # Filtrar as posicoes adjacentes que pertencem à mesma orbita


    if not same_orbit_positions: 
        return None  # Retorna None se nao houver posicoes na mesma orbita

    return same_orbit_positions[0] if s else same_orbit_positions[-1] # Retorna a posição seguinte

def roda_tabuleiro(t) -> list:

    """
    Roda o tabuleiro 't' no sentido anti-horário.
    
    Retorna:
        list: O tabuleiro rodado.
    """
    num_colunas = len(t)
    num_linhas = len(t[0]) if num_colunas > 0 else 0

    for o in range(obtem_numero_orbitas(t)):  # Percorre as orbitas

        orbita = []

        for i in range(o, num_linhas - o):  # percorre as linhas
            orbita.append(t[i][o])  # Adiciona a linha superior da órbita
        
        for j in range(o + 1, num_colunas - o):  # percorre as colunas
            orbita.append(t[num_linhas - o - 1][j])  # Adiciona a linha inferior da órbita

        for i in range(num_linhas - o - 2, o - 1, -1):  # percorre as linhas
            orbita.append(t[i][num_colunas - o - 1])  # Adiciona a linha inferior da órbita
        
        for j in range(num_colunas - o - 1, o, -1):  # percorre as colunas
            orbita.append(t[o][j])  # Adiciona a linha superior da órbita

        # Rotaciona a órbita anti-horário
        orbita_rotacionada = orbita[1:] + orbita[:1]

        # Reinsere a órbita no tabuleiro
        index = 0
        
        for i in range(o, num_linhas - o): # percorre as linhas
            t[i][o] = orbita_rotacionada[index]  # Reinsere a linha superior da órbita
            index += 1
        
        for j in range(o + 1, num_colunas - o): # percorre as colunas
            t[num_linhas - o - 1][j] = orbita_rotacionada[index]  # Reinsere a linha inferior da órbita
            index += 1
        
        for i in range(num_linhas - o - 2, o - 1, -1): # percorre as linhas
            t[i][num_colunas - o - 1] = orbita_rotacionada[index]  # Reinsere a linha inferior da órbita
            index += 1
        
        for j in range(num_colunas - o - 1, o, -1): # percorre as colunas
            t[o][j] = orbita_rotacionada[index]  # Reinsere a linha superior da órbita
            index += 1

    return t # Retorna o tabuleiro rodado

def verifica_consecutivas(t, posicoes, p, j, k) -> bool:
    """
    Verifica se existe k pedras consecutivas em uma lista de posições.

    A função verifica_consecutivas verifica se existe k pedras consecutivas em
    uma lista de posições. A lista de posições pode ser horizontal, vertical ou
    diagonal.

    Argumentos:
        t (list): O tabuleiro.
        posicoes (list): A lista de posições a verificar.
        p (str): A posição a verificar.
        j (str): A pedra do jogador (X ou O).
        k (int): O número de pedras consecutivas a verificar.

    Retorna:
        bool: True se existir k pedras consecutivas, False caso contrário.
    """
    count = 0
    found_p = False

    # Itera pelas posições
    if obtem_pedra(t, p) != j:  # Verifica se é a pedra do jogador
        return False

    for pos in posicoes: #percorre as posicoes
        if pos[0] == p: # Verifica se a posicao é igual a p
            found_p = True  # Encontrou a posição p
        if pos[1] == j: # Verifica se a posicao tem a pedra do jogador
            count += 1  # Incrementa o contador
        else:
            count = 0  # Reseta o contador se não for a pedra do jogador
        
        # Se encontramos p e temos k pedras consecutivas, retorna True
        if found_p and count >= k:
            return True
    
    return False

def verifica_linha_pedras(t, p, j, k) -> bool:
    """
    Verifica se há uma linha de pedras consecutivas de um jogador no tabuleiro.

    A função verifica_linha_pedras verifica se há k pedras consecutivas pertencentes ao
    jogador especificado em qualquer direção (horizontal, vertical ou diagonal) a partir
    da posição dada no tabuleiro.

    Argumentos:
        t (list): O tabuleiro do jogo.
        p (str): A posição de referência no tabuleiro.
        j (str): A representação da pedra do jogador (X ou O).
        k (int): O número de pedras consecutivas a serem verificadas.

    Retorna:
        bool: True se houver ao menos uma linha de k pedras consecutivas, False caso contrário.
    """
    diagonal, antidiagonal = obtem_linhas_diagonais(t, p) # a partir da funcão obtem_linhas_diagonais, obtem as linhas diagonais e antidiagonais
    horizontal = obtem_linha_horizontal(t, p) # a partir da funcão obtem_linha_horizontal, obtem a linha horizontal
    vertical = obtem_linha_vertical(t, p) # a partir da funcão obtem_linha_vertical, obtem a linha vertical

    # Verifica se existe k pedras consecutivas em cada direção
    if verifica_consecutivas(t, horizontal, p, j, k) or \
       verifica_consecutivas(t, vertical, p, j, k) or \
       verifica_consecutivas(t, diagonal, p, j, k) or \
       verifica_consecutivas(t, antidiagonal, p, j, k):
        return True

    return False

def eh_vencedor(t, j) -> bool:
    """
    Verifica se o jogador especificado é o vencedor no tabuleiro.

    A função eh_vencedor percorre o tabuleiro e verifica se o jogador especificado
    possui uma linha de pedras consecutivas que satisfaça as condições de vitória.
    A verificação é feita para cada posição do tabuleiro chamando a função
    verifica_linha_pedras.

    Argumentos:
        t (list): O tabuleiro do jogo.
        j (str): A representação da pedra do jogador (X ou O).

    Retorna:
        bool: True se o jogador for o vencedor, False caso contrário.
    """
    for col in range(len(t)): # Percorre as colunas
        for lin in range(len(t[0])): # Percorre as linhas
            pos = cria_posicao(chr(ord('a') + col), lin + 1) # Cria a posicao
            if verifica_linha_pedras(t, pos, j, len(t)): # Verifica se existe uma linha de pedras consecutivas
                return True # Retorna True
            break # Encerra o loop se for encontrada uma linha de pedras consecutivas
    return False # Retorna False




