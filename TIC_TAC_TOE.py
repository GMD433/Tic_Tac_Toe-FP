#Numero-199233, NOME-Gustavo Manuel Cabral de Mascarenhas Diogo
tab =((0,0,0),(0,0,0),(0,0,0))
""" funcao que combina os tres tuplos num ficando ("","","","","","","","","")"""
def  altera_tab(tab):
    junta_tab = ((tab[0]) + (tab[1]) + (tab[2]))
    return (junta_tab)
"""a funcao junta os valores todo e combina-as num so tuplo"""
"""funcao que verifica se e um tabuleiro e da return True ou False(booleano)"""
def eh_tabuleiro(tab):
    tab = altera_tab(tab)
    tab_modelo = ("","","","","","","","","")
    if len(tab) == len(tab_modelo):
        for i in range (len (tab)):
            if tab[i] not in (-1,0,1):
                return False
    else:
        return False
    return True
"""a funcao verifica se e um tabuleiro"""

"""checka se a posicao esta entre 1 e 10"""
def eh_posicao(pos):
    if pos in range(1,10):
        return True
    return False
"""verifica se a posicao e uma das do tabuleiro"""

""" ve o tabuleiro e a posicao dada e da a coluna correspondente"""
def obter_coluna(tab,pos):
    if eh_tabuleiro(tab) == False:
        raise ValueError ("eh_posicao_livre: algum dos argumentos e invalido")
    tab = altera_tab(tab)
    for i in range(len(tab)):
        if tab[i] not in (-1,0,1):
            raise ValueError ("obter_coluna: algum dos argumentos e invalido")
    if pos == 1:
        return (tab[0],tab[3],tab[6])
    elif pos == 2:
        return (tab[1],tab[4],tab[7])
    elif pos == 3:
        return (tab[2],tab[5],tab[8])
    else:
        raise ValueError ("obter_coluna: algum dos argumentos e invalido")
    raise ValueError("obter_coluna: algum dos argumentos e invalido")

""" ve o tabuleiro e a posicao dada e da a linha correspondente"""
def obter_linha(tab,pos):
    if eh_tabuleiro(tab) == False:
        raise ValueError ("obter_linha: algum dos argumentos e invalido")
    tab = altera_tab(tab)
    for i in range(len(tab)):
        if tab[i] not in (-1,0,1):
            raise ValueError ("obter_linha: algum dos argumentos e invalido")
    if pos == 1:
        return (tab[0],tab[1],tab[2])
    elif pos == 2:
        return (tab[3],tab[4],tab[5])
    elif pos == 3:
        return (tab[6],tab[7],tab[8])
    else:
        raise ValueError ("obter_linha: algum dos argumentos e invalido")
    raise ValueError("obter_linha: algum dos argumentos e invalido")

""" ve o tabuleiro e a posicao dada e da a diagonal correspondente"""
def obter_diagonal(tab,pos):
    if eh_tabuleiro(tab) == False:
        raise ValueError ("obter_diagonal: algum dos argumentos e invalido")
    tab = altera_tab(tab)
    for i in range(len(tab)):
        if tab[i] not in (-1,0,1):
            raise ValueError ("obter_diagonal: algum dos argumentos e invalido")
    if pos == 1:
        return (tab[0],tab[4],tab[8])
    elif pos == 2:
        return (tab[6],tab[4],tab[2])
    else:
        raise ValueError ("obter_diagonal: algum dos argumentos e invalido")
    raise ValueError("obter_diagonal: algum dos argumentos e invalido")

"""recebe valores e da as pecas X,O ou espaco e retorna um novo tuplo"""
def cria_pecas(tab):
    tab = altera_tab(tab)
    X =" X "
    O = " O "
    _ = "   "
    novotab = ()
    for pos in range(len(tab)):
        if tab[pos] == 1:
            novotab += (X,)
        elif tab[pos] == 0:
            novotab += (_,)
        elif tab[pos] == -1:
            novotab += (O,)
    return (novotab[0],novotab[1],novotab[2],novotab[3],novotab[4],novotab[5],novotab[6],novotab[7],novotab[8])
"""pega no tabuleiro e coloca as pecas no lugar dos valores"""            

"""devolve o tabuleiro no terminal"""
def tabuleiro_str(tab):
    if eh_tabuleiro(tab) == True:
        tab = cria_pecas(tab)
        return (tab[0] + "|" + tab[1] + "|" + tab[2] + "\n-----------\n" + tab[3] + "|" + tab[4] + "|" + tab[5] + "\n-----------\n" + tab[6] + "|" + tab[7] + "|" + tab[8])
    else:
         raise ValueError ("tabuleiro_str: o argumento e invalido")
    raise ValueError ("tabuleiro_str: o argumento e invalido")
"""da-nos o tabulerio classico do jogo do galo"""

"""recebe o tabuleiro e uma posicao e retorna True ou False(booleano)"""
def eh_posicao_livre(tab,pos):
    if eh_tabuleiro(tab) == False:
        raise ValueError ("eh_posicao_livre: algum dos argumentos e invalido")
    tab = altera_tab(tab)
    if 1 <= pos <= 9:
        if tab[pos - 1] == -1 or tab[pos - 1] == 1:
            return False
        elif tab[pos - 1] == 0:
            return True
        else:
            raise ValueError ("eh_posicao_livre: algum dos argumentos e invalido")
    raise ValueError ("eh_posicao_livre: algum dos argumentos e invalido")
"""verifica se uma posicao esta livre ou nao"""

"""recebe o tabuleiro e retorna as posicoes livres"""
def obter_posicoes_livres(tab):
    if eh_tabuleiro(tab) == False:
        raise ValueError ("obter_posicoes_livres: o argumento e invalido")
    tup1 = ()
    i = 0
    tab = altera_tab(tab)
    while i in range(len(tab)):
        if tab[i] == 0:
            tup1 += (i+1,)
            i += 1
        elif tab[i]== -1 or tab[i]== 1:
            i += 1
        else:
            raise ValueError ("obter_posicoes_livres: o argumento e invalido")
    return (tup1)
"""procura e mostra as posicoes livres do tabuleiro"""

"""recebe o tabuleiro e retorna o valor do vencedor"""
def jogador_ganhador(tab):
    if eh_tabuleiro(tab) == False:
        raise ValueError ("jogador_ganhador: algum dos argumentos e invalido")
    if eh_tabuleiro(tab) == True:    
        for pos in range(1,4):
            x=obter_linha(tab,pos)
            if x[0] == x[1] == x[2] == -1:
                return (-1)
            elif x[0] == x[1] == x[2] == 1:
                return (1)
        for pos in range(1,4):
            x=obter_coluna(tab,pos)
            if x[0] == x[1] == x[2] == -1:
                return (-1)
            elif x[0] == x[1] == x[2] == 1:
                return (1)
        for pos in range(1,3):    
            x = obter_diagonal(tab,pos)
            if x[0] == x[1] == x[2] == -1:
                return (-1)
            elif x[0] == x[1] == x[2] == 1:
                return (1)
        return(0)
    else:
        raise ValueError("jogador_ganhador: o argumento e invalido")
    raise ValueError("jogador_ganhador: o argumento e invalido")
"""verifica quem ganhou e mostra o seu simbolo no terminal"""   
    
"""recebe o tabuleiro, o valor da peca e a posicao e retorna um novo tabuleiro com a peca no valor da posicao se a posicao for 0"""
def marcar_posicao(tab,peca,posicao):   
    if eh_tabuleiro(tab) == True:
        if peca in (-1,1):
            livre = obter_posicoes_livres(tab)
            if posicao in livre:
                tab1 = altera_tab(tab)
                tab2 = tab1[:posicao - 1] + (peca,) + tab1[posicao:]
                tab3 = ((tab2[0],tab2[1],tab2[2]),(tab2[3],tab2[4],tab2[5]),(tab2[6],tab2[7],tab2[8]))  
                return (tab3)
        else:
            raise ValueError("marcar_posicao: algum dos argumentos e invalido")
    raise ValueError("marcar_posicao: algum dos argumentos e invalido")
"""cria um novo tabuleiro com a posicao preenchida com a peca escolhida se a posicao estiver livre"""

"""recebe o tabuleiro e pede input da posicao e retorna a posicao se a posicao for 0 no tabuleiro)"""
def escolher_posicao_manual(tab):
    if eh_tabuleiro(tab) == False:
        raise ValueError("escolher_posicao_manual: o argumento e invalido")
    play = int(input("Turno do jogador. Escolha uma posicao livre: "))
    livre = obter_posicoes_livres(tab)
    if play in livre:
        return (play)
    else:
        raise ValueError("escolher_posicao_manual: a posicao introduzida e invalida")
    raise ValueError("escolher_posicao_manual: a posicao introduzida e invalida")
"""permite que o jogador humano jogue"""

"""recebe o tabuleiro, a peca e a dificuldade e devolve a primeira posicao que cumpre os criterios de selecao"""
def escolher_posicao_auto(tab, peca, dif):
    if eh_tabuleiro (tab) == False:
        raise ValueError("escolher_posicao_auto: algum dos argumentos e invalido")
    if peca == -1:
        if dif == "basico":
            livre = obter_posicoes_livres(tab)
            if 5 in livre:
                return (5)
            elif 1 in livre:
                return (1)
            elif 3 in livre:
                return (3)
            elif 7 in livre:
                return (7)
            elif 9 in livre:
                return (9)
            elif 2 in livre:
                return (2)
            elif 4 in livre:
                return (4)
            elif 6 in livre:
                return (6)
            elif 8 in livre:
                return (8)
        elif dif == "normal":
            livre = obter_posicoes_livres(tab)
            tab = altera_tab(tab)
            if (tab[0]==tab[1]== -1 or tab[0]==tab[1]== 1) and 3 in livre:
                return 3
            elif (tab[2]==tab[1]== -1 or tab[2]==tab[1]== 1) and 1 in livre:
                return 1 
            elif (tab[0]==tab[2]== -1 or tab[0]==tab[2]== 1) and 2 in livre:
                return 2 
            elif (tab[3]==tab[4]== -1 or tab[3]==tab[4]== 1) and 6 in livre:
                return 6 
            elif (tab[5]==tab[4]== -1 or tab[5]==tab[4]== 1) and 4 in livre:
                return 1
            elif (tab[3]==tab[5]== -1 or tab[3]==tab[5]== 1) and 5 in livre:
                return 5 
            elif (tab[6]==tab[7]== -1 or tab[6]==tab[7]== 1) and 9 in livre:
                return 9
            elif (tab[8]==tab[7]== -1 or tab[8]==tab[7]== 1) and 7 in livre:
                return 7 
            elif (tab[6]==tab[8]== -1 or tab[6]==tab[8]== 1) and 8 in livre:
                return 8 
            elif (tab[0]==tab[3]== -1 or tab[0]==tab[3]== 1) and 7 in livre:
                return 7 
            elif (tab[6]==tab[3]== -1 or tab[6]==tab[3]== 1) and 1 in livre:
                return 1 
            elif (tab[0]==tab[6]== -1 or tab[0]==tab[6]== 1) and 4 in livre:
                return 4 
            elif (tab[1]==tab[4]== -1 or tab[1]==tab[4]== 1) and 8 in livre:
                return 8
            elif (tab[7]==tab[4]== -1 or tab[7]==tab[4]== 1) and 2 in livre:
                return 2
            elif (tab[1]==tab[7]== -1 or tab[1]==tab[7]== 1) and 5 in livre:
                return 5 
            elif (tab[2]==tab[5]== -1 or tab[2]==tab[5]== 1) and 9 in livre:
                return 9
            elif (tab[8]==tab[5]== -1 or tab[8]==tab[5]== 1) and 3 in livre:
                return 3
            elif (tab[2]==tab[8]== -1 or tab[2]==tab[8]== 1) and 6 in livre:
                return 6 
            elif (tab[0]==tab[4]== -1 or tab[0]==tab[4]== 1) and 9 in livre:
                return 9
            elif (tab[8]==tab[4]== -1 or tab[8]==tab[4]== 1) and 1 in livre:
                return 1
            elif (tab[0]==tab[8]== -1 or tab[0]==tab[8]== 1) and 5 in livre:
                return 5 
            elif (tab[6]==tab[4]== -1 or tab[6]==tab[4]== 1) and 3 in livre:
                return 3
            elif (tab[2]==tab[4]== -1 or tab[2]==tab[4]== 1) and 7 in livre:
                return 7
            elif (tab[2]==tab[6]== -1 or tab[2]==tab[6]== 1) and 5 in livre:
                return 5 
            elif 5 in livre:
                return (5)
            elif tab[0]== 1 and 9 in livre:
                return 9
            elif tab[2]== 1 and 7 in livre:
                return 7
            elif tab[6]== 1 and 3 in livre:
                return 3
            elif tab[8]== 1 and 1 in livre:
                return 1
            elif 1 in livre:
                return (1)
            elif 3 in livre:
                return (3)
            elif 7 in livre:
                return (7)
            elif 9 in livre:
                return (9)
            elif 2 in livre:
                return (2)
            elif 4 in livre:
                return (4)
            elif 6 in livre:
                return (6)
            elif 8 in livre:
                return (8)
        elif dif == "perfeito":
            livre = obter_posicoes_livres(tab)
            tab = altera_tab(tab)
            if (tab[0]==tab[1]== -1 or tab[0]==tab[1]== 1) and 3 in livre:
                return 3
            elif (tab[2]==tab[1]== -1 or tab[2]==tab[1]== 1) and 1 in livre:
                return 1 
            elif (tab[0]==tab[2]== -1 or tab[0]==tab[2]== 1) and 2 in livre:
                return 2 
            elif (tab[3]==tab[4]== -1 or tab[3]==tab[4]== 1) and 6 in livre:
                return 6 
            elif (tab[5]==tab[4]== -1 or tab[5]==tab[4]== 1) and 4 in livre:
                return 1
            elif (tab[3]==tab[5]== -1 or tab[3]==tab[5]== 1) and 5 in livre:
                return 5 
            elif (tab[6]==tab[7]== -1 or tab[6]==tab[7]== 1) and 9 in livre:
                return 9
            elif (tab[8]==tab[7]== -1 or tab[8]==tab[7]== 1) and 7 in livre:
                return 7 
            elif (tab[6]==tab[8]== -1 or tab[6]==tab[8]== 1) and 8 in livre:
                return 8 
            elif (tab[0]==tab[3]== -1 or tab[0]==tab[3]== 1) and 7 in livre:
                return 7 
            elif (tab[6]==tab[3]== -1 or tab[6]==tab[3]== 1) and 1 in livre:
                return 1 
            elif (tab[0]==tab[6]== -1 or tab[0]==tab[6]== 1) and 4 in livre:
                return 4 
            elif (tab[1]==tab[4]== -1 or tab[1]==tab[4]== 1) and 8 in livre:
                return 8
            elif (tab[7]==tab[4]== -1 or tab[7]==tab[4]== 1) and 2 in livre:
                return 2
            elif (tab[1]==tab[7]== -1 or tab[1]==tab[7]== 1) and 5 in livre:
                return 5 
            elif (tab[2]==tab[5]== -1 or tab[2]==tab[5]== 1) and 9 in livre:
                return 9
            elif (tab[8]==tab[5]== -1 or tab[8]==tab[5]== 1) and 3 in livre:
                return 3
            elif (tab[2]==tab[8]== -1 or tab[2]==tab[8]== 1) and 6 in livre:
                return 6 
            elif (tab[0]==tab[4]== -1 or tab[0]==tab[4]== 1) and 9 in livre:
                return 9
            elif (tab[8]==tab[4]== -1 or tab[8]==tab[4]== 1) and 1 in livre:
                return 1
            elif (tab[0]==tab[8]== -1 or tab[0]==tab[8]== 1) and 5 in livre:
                return 5 
            elif (tab[6]==tab[4]== -1 or tab[6]==tab[4]== 1) and 3 in livre:
                return 3
            elif (tab[2]==tab[4]== -1 or tab[2]==tab[4]== 1) and 7 in livre:
                return 7
            elif (tab[2]==tab[6]== -1 or tab[2]==tab[6]== 1) and 5 in livre:
                return 5
            if (tab[0]==tab[8]== -1 or tab[0]==tab[8]== 1) and 3 in livre:
                return 3
            elif (tab[0]==tab[8]== -1 or tab[0]==tab[8]== 1) and 7 in livre:
                return 7
            elif (tab[0]==tab[4]== -1 or tab[0]==tab[4]== 1) and 2 in livre:
                return 2
            elif (tab[0]==tab[4]== -1 or tab[0]==tab[4]== 1) and 4 in livre:
                return 4
            elif (tab[2]==tab[6]== -1 or tab[2]==tab[6]== 1) and 9 in livre:
                return 9
            elif (tab[2]==tab[6]== -1 or tab[2]==tab[6]== 1) and 1 in livre:
                return 1
            elif (tab[2]==tab[4]== -1 or tab[2]==tab[4]== 1) and 6 in livre:
                return 6
            elif (tab[2]==tab[4]== -1 or tab[2]==tab[4]== 1) and 2 in livre:
                return 2
            elif (tab[4]==tab[6]== -1 or tab[4]==tab[6]== 1) and 4 in livre:
                return 4
            elif (tab[4]==tab[6]== -1 or tab[4]==tab[6]== 1) and 8 in livre:
                return 8
            elif (tab[4]==tab[8]== -1 or tab[4]==tab[8]== 1) and 6 in livre:
                return 6
            elif (tab[4]==tab[8]== -1 or tab[4]==tab[8]== 1) and 8 in livre:
                return 8
            elif 5 in livre:
                return (5)
            elif tab[0]== 1 and 9 in livre:
                return 9
            elif tab[2]== 1 and 7 in livre:
                return 7
            elif tab[6]== 1 and 3 in livre:
                return 3
            elif tab[8]== 1 and 1 in livre:
                return 1
            elif 1 in livre:
                return (1)
            elif 3 in livre:
                return (3)
            elif 7 in livre:
                return (7)
            elif 9 in livre:
                return (9)
            elif 2 in livre:
                return (2)
            elif 4 in livre:
                return (4)
            elif 6 in livre:
                return (6)
            elif 8 in livre:
                return (8)
    if peca == 1:
        if dif == "basico":
            livre = obter_posicoes_livres(tab)
            if 5 in livre:
                return (5)
            elif 1 in livre:
                return (1)
            elif 3 in livre:
                return (3)
            elif 7 in livre:
                return (7)
            elif 9 in livre:
                return (9)
            elif 2 in livre:
                return (2)
            elif 4 in livre:
                return (4)
            elif 6 in livre:
                return (6)
            elif 8 in livre:
                return (8)
        elif dif == "normal":
            livre = obter_posicoes_livres(tab)
            tab = altera_tab(tab)
            if (tab[0]==tab[1]== -1 or tab[0]==tab[1]== 1) and 3 in livre:
                return 3
            elif (tab[2]==tab[1]== -1 or tab[2]==tab[1]== 1) and 1 in livre:
                return 1 
            elif (tab[0]==tab[2]== -1 or tab[0]==tab[2]== 1) and 2 in livre:
                return 2 
            elif (tab[3]==tab[4]== -1 or tab[3]==tab[4]== 1) and 6 in livre:
                return 6 
            elif (tab[5]==tab[4]== -1 or tab[5]==tab[4]== 1) and 4 in livre:
                return 1
            elif (tab[3]==tab[5]== -1 or tab[3]==tab[5]== 1) and 5 in livre:
                return 5 
            elif (tab[6]==tab[7]== -1 or tab[6]==tab[7]== 1) and 9 in livre:
                return 9
            elif (tab[8]==tab[7]== -1 or tab[8]==tab[7]== 1) and 7 in livre:
                return 7 
            elif (tab[6]==tab[8]== -1 or tab[6]==tab[8]== 1) and 8 in livre:
                return 8 
            elif (tab[0]==tab[3]== -1 or tab[0]==tab[3]== 1) and 7 in livre:
                return 7 
            elif (tab[6]==tab[3]== -1 or tab[6]==tab[3]== 1) and 1 in livre:
                return 1 
            elif (tab[0]==tab[6]== -1 or tab[0]==tab[6]== 1) and 4 in livre:
                return 4 
            elif (tab[1]==tab[4]== -1 or tab[1]==tab[4]== 1) and 8 in livre:
                return 8
            elif (tab[7]==tab[4]== -1 or tab[7]==tab[4]== 1) and 2 in livre:
                return 2
            elif (tab[1]==tab[7]== -1 or tab[1]==tab[7]== 1) and 5 in livre:
                return 5 
            elif (tab[2]==tab[5]== -1 or tab[2]==tab[5]== 1) and 9 in livre:
                return 9
            elif (tab[8]==tab[5]== -1 or tab[8]==tab[5]== 1) and 3 in livre:
                return 3
            elif (tab[2]==tab[8]== -1 or tab[2]==tab[8]== 1) and 6 in livre:
                return 6 
            elif (tab[0]==tab[4]== -1 or tab[0]==tab[4]== 1) and 9 in livre:
                return 9
            elif (tab[8]==tab[4]== -1 or tab[8]==tab[4]== 1) and 1 in livre:
                return 1
            elif (tab[0]==tab[8]== -1 or tab[0]==tab[8]== 1) and 5 in livre:
                return 5 
            elif (tab[6]==tab[4]== -1 or tab[6]==tab[4]== 1) and 3 in livre:
                return 3
            elif (tab[2]==tab[4]== -1 or tab[2]==tab[4]== 1) and 7 in livre:
                return 7
            elif (tab[2]==tab[6]== -1 or tab[2]==tab[6]== 1) and 5 in livre:
                return 5 
            elif 5 in livre:
                return (5)
            elif tab[0]== -1 and 9 in livre:
                return 9
            elif tab[2]== -1 and 7 in livre:
                return 7
            elif tab[6]== -1 and 3 in livre:
                return 3
            elif tab[8]== -1 and 1 in livre:
                return 1
            elif 1 in livre:
                return (1)
            elif 3 in livre:
                return (3)
            elif 7 in livre:
                return (7)
            elif 9 in livre:
                return (9)
            elif 2 in livre:
                return (2)
            elif 4 in livre:
                return (4)
            elif 6 in livre:
                return (6)
            elif 8 in livre:
                return (8)
        elif dif == "perfeito":
            livre = obter_posicoes_livres(tab)
            tab = altera_tab(tab)
            if (tab[0]==tab[1]== -1 or tab[0]==tab[1]== 1) and 3 in livre:
                return 3
            elif (tab[2]==tab[1]== -1 or tab[2]==tab[1]== 1) and 1 in livre:
                return 1 
            elif (tab[0]==tab[2]== -1 or tab[0]==tab[2]== 1) and 2 in livre:
                return 2 
            elif (tab[3]==tab[4]== -1 or tab[3]==tab[4]== 1) and 6 in livre:
                return 6 
            elif (tab[5]==tab[4]== -1 or tab[5]==tab[4]== 1) and 4 in livre:
                return 1
            elif (tab[3]==tab[5]== -1 or tab[3]==tab[5]== 1) and 5 in livre:
                return 5 
            elif (tab[6]==tab[7]== -1 or tab[6]==tab[7]== 1) and 9 in livre:
                return 9
            elif (tab[8]==tab[7]== -1 or tab[8]==tab[7]== 1) and 7 in livre:
                return 7 
            elif (tab[6]==tab[8]== -1 or tab[6]==tab[8]== 1) and 8 in livre:
                return 8 
            elif (tab[0]==tab[3]== -1 or tab[0]==tab[3]== 1) and 7 in livre:
                return 7 
            elif (tab[6]==tab[3]== -1 or tab[6]==tab[3]== 1) and 1 in livre:
                return 1 
            elif (tab[0]==tab[6]== -1 or tab[0]==tab[6]== 1) and 4 in livre:
                return 4 
            elif (tab[1]==tab[4]== -1 or tab[1]==tab[4]== 1) and 8 in livre:
                return 8
            elif (tab[7]==tab[4]== -1 or tab[7]==tab[4]== 1) and 2 in livre:
                return 2
            elif (tab[1]==tab[7]== -1 or tab[1]==tab[7]== 1) and 5 in livre:
                return 5 
            elif (tab[2]==tab[5]== -1 or tab[2]==tab[5]== 1) and 9 in livre:
                return 9
            elif (tab[8]==tab[5]== -1 or tab[8]==tab[5]== 1) and 3 in livre:
                return 3
            elif (tab[2]==tab[8]== -1 or tab[2]==tab[8]== 1) and 6 in livre:
                return 6 
            elif (tab[0]==tab[4]== -1 or tab[0]==tab[4]== 1) and 9 in livre:
                return 9
            elif (tab[8]==tab[4]== -1 or tab[8]==tab[4]== 1) and 1 in livre:
                return 1
            elif (tab[0]==tab[8]== -1 or tab[0]==tab[8]== 1) and 5 in livre:
                return 5 
            elif (tab[6]==tab[4]== -1 or tab[6]==tab[4]== 1) and 3 in livre:
                return 3
            elif (tab[2]==tab[4]== -1 or tab[2]==tab[4]== 1) and 7 in livre:
                return 7
            elif (tab[2]==tab[6]== -1 or tab[2]==tab[6]== 1) and 5 in livre:
                return 5
            if (tab[0]==tab[8]== -1 or tab[0]==tab[8]== 1) and 3 in livre:
                return 3
            elif (tab[0]==tab[8]== -1 or tab[0]==tab[8]== 1) and 7 in livre:
                return 7
            elif (tab[0]==tab[4]== -1 or tab[0]==tab[4]== 1) and 2 in livre:
                return 2
            elif (tab[0]==tab[4]== -1 or tab[0]==tab[4]== 1) and 4 in livre:
                return 4
            elif (tab[2]==tab[6]== -1 or tab[2]==tab[6]== 1) and 9 in livre:
                return 9
            elif (tab[2]==tab[6]== -1 or tab[2]==tab[6]== 1) and 1 in livre:
                return 1
            elif (tab[2]==tab[4]== -1 or tab[2]==tab[4]== 1) and 6 in livre:
                return 6
            elif (tab[2]==tab[4]== -1 or tab[2]==tab[4]== 1) and 2 in livre:
                return 2
            elif (tab[4]==tab[6]== -1 or tab[4]==tab[6]== 1) and 4 in livre:
                return 4
            elif (tab[4]==tab[6]== -1 or tab[4]==tab[6]== 1) and 8 in livre:
                return 8
            elif (tab[4]==tab[8]== -1 or tab[4]==tab[8]== 1) and 6 in livre:
                return 6
            elif (tab[4]==tab[8]== -1 or tab[4]==tab[8]== 1) and 8 in livre:
                return 8
            elif 5 in livre:
                return (5)
            elif tab[0]== 1 and 9 in livre:
                return 9
            elif tab[2]== 1 and 7 in livre:
                return 7
            elif tab[6]== 1 and 3 in livre:
                return 3
            elif tab[8]== 1 and 1 in livre:
                return 1
            elif 1 in livre:
                return (1)
            elif 3 in livre:
                return (3)
            elif 7 in livre:
                return (7)
            elif 9 in livre:
                return (9)
            elif 2 in livre:
                return (2)
            elif 4 in livre:
                return (4)
            elif 6 in livre:
                return (6)
            elif 8 in livre:
                return (8)
    raise ValueError ("escolher_posicao_auto: algum dos argumentos e invalido")
"""inteligencia do computador"""

"""vai permitir que o jogador jogue contra o computador a medida que atualiza o tabuleiro e da um vencedor"""
def jogo_do_galo(peca,dif):
    print ("Bem-vindo ao JOGO DO GALO")
    if dif == "basico":
        if peca == "O":
            global tab 
            print("O jogador joga com 'O'")
            i = 0
            while i < 9:
                print ("Turno do computador (basico)")
                jogau =escolher_posicao_auto(tab,1,"basico")
                tab = marcar_posicao (tab,1,jogau)
                print (tabuleiro_str(tab))
                if jogador_ganhador(tab) == 1:
                    return ("X")
                i += 1
                if i == 9 and jogador_ganhador(tab) == 0:
                    return ("EMPATE")
                jogm = escolher_posicao_manual(tab)
                tab = marcar_posicao(tab,-1,jogm)
                print (tabuleiro_str(tab))
                if jogador_ganhador(tab) == -1:
                    return ("O")
                i += 1
        if peca == "X":
            print("O jogador joga com 'X'")
            i = 0
            while i < 9:
                jogm = escolher_posicao_manual(tab)
                tab = marcar_posicao(tab,1,jogm)
                print (tabuleiro_str(tab))
                if jogador_ganhador(tab) == 1:
                    return ("X")
                i += 1
                if i == 9 and jogador_ganhador(tab) == 0:
                    return ("EMPATE")
                print ("Turno do computador (basico)")
                jogau =escolher_posicao_auto(tab,-1,"basico")
                tab = marcar_posicao (tab,-1,jogau)
                print (tabuleiro_str(tab))
                if jogador_ganhador(tab) == -1:
                    return ("O")
                i += 1
    if dif == "normal":
        if peca == "O": 
            print("O jogador joga com 'O'")
            i = 0
            while i < 9:
                print ("Turno do computador (normal)")
                jogau =escolher_posicao_auto(tab,1,"normal")
                tab = marcar_posicao (tab,1,jogau)
                print (tabuleiro_str(tab))
                if jogador_ganhador(tab) == 1:
                    return ("X")
                i += 1
                if i == 9 and jogador_ganhador(tab) == 0:
                    return ("EMPATE")
                jogm = escolher_posicao_manual(tab)
                tab = marcar_posicao(tab,-1,jogm)
                print (tabuleiro_str(tab))
                if jogador_ganhador(tab) == -1:
                    return ("O")
                i += 1
        if peca == "X":
            print("O jogador joga com 'X'")
            i = 0
            while i < 9:
                jogm = escolher_posicao_manual(tab)
                tab = marcar_posicao(tab,1,jogm)
                print (tabuleiro_str(tab))
                if jogador_ganhador(tab) == 1:
                    return ("X")
                i += 1
                if i == 9 and jogador_ganhador(tab) == 0:
                    return ("EMPATE")
                print ("Turno do computador (normal)")
                jogau =escolher_posicao_auto(tab,-1,"normal")
                tab = marcar_posicao (tab,-1,jogau)
                print (tabuleiro_str(tab))
                if jogador_ganhador(tab) == -1:
                    return ("O")
                i += 1
    if dif == "perfeito":
        if peca == "O": 
            print("O jogador joga com 'O'")
            i = 0
            while i < 9:
                print ("Turno do computador (perfeito)")
                jogau =escolher_posicao_auto(tab,1,"perfeito")
                tab = marcar_posicao (tab,1,jogau)
                print (tabuleiro_str(tab))
                if jogador_ganhador(tab) == 1:
                    return ("O")
                i += 1
                if i == 9 and jogador_ganhador(tab) == 0:
                    return ("EMPATE")
                jogm = escolher_posicao_manual(tab)
                tab = marcar_posicao(tab,-1,jogm)
                print (tabuleiro_str(tab))
                if jogador_ganhador(tab) == -1:
                    return ("X")
                i += 1
        if peca == "X":
            print("O jogador joga com 'X'")
            i = 0
            while i < 9:
                jogm = escolher_posicao_manual(tab)
                tab = marcar_posicao(tab,1,jogm)
                print (tabuleiro_str(tab))
                if jogador_ganhador(tab) == 1:
                    return ("X")
                i += 1
                if i == 9 and jogador_ganhador(tab) == 0:
                    return ("EMPATE")
                print ("Turno do computador (perfeito)")
                jogau =escolher_posicao_auto(tab,-1,"perfeito")
                tab = marcar_posicao (tab,-1,jogau)
                print (tabuleiro_str(tab))
                if jogador_ganhador(tab) == -1:
                    return ("O")
                i += 1
    raise ValueError("jogo do galo:algum dos argumentos e invalido")
"""jogo do galo contra o computador"""

print (jogo_do_galo("X","perfeito"))