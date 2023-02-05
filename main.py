from math import floor
from os import system

def divide_num( num ):
    # Verifica se o decimal é negativo
    negativo = ( False if num.find( "-" ) == -1 else True )

    # Divisão entre inteiro e decimal
    if "." in num:
        num = num.split( "." )
        inteiro_b, decimal_b, point_char = int( num[ 0 ] ), float( "".join( ( "0.", num[ 1 ]  ) ) ), "."
    else:
        inteiro_b, decimal_b, point_char = int( num ), False, False

    # Retorna se o número é negativo, tem parte decimal e sua separação entre inteiro e decimal
    return negativo, point_char, inteiro_b, decimal_b

def gera_binario( inteiro_b, decimal_b ):
    inteiro_b *= ( -1 if inteiro_b < 0 else 1 )
    binario = ""
    
    # Parte inteira
    while( inteiro_b / 2 != 0 ):
        binario = "".join( ( binario, str( inteiro_b % 2 ) ) )
        inteiro_b = floor( inteiro_b / 2 )
    binario = binario [::-1 ] # Inverte a string

    # Parte decimal
    if decimal_b:
        binario = "".join( ( binario, point_char ) )    # Adição do ponto

        while( decimal_b != 0 ):
            decimal_b *= 2
            binario =  "".join( ( binario, str( floor( decimal_b ) ) ) )
            if( decimal_b >= 1 ):
                decimal_b -= 1
        
    return binario

def gera_negativo( binario, decimal_b ):
    binario = list( binario )                                       # Transforma a string de binario em lista de chars
    negativo_list = [ "", "", "" ]

    # 0 = Sinal e Amplitude
    negativo_list[ 0 ] = "".join( ( "1", "".join( binario ) ) )

    # 1 = Complemento de 1
    for i in range( len( binario ) ):                               # Para todo char diferente de "." ele inverte a casa binária
        if binario[ i ] != point_char:
            binario[ i ] = ( "1" if binario[ i ] == "0" else "0" )

    negativo_list[1] = "".join( ( "1", "".join( binario ) ) )       # Adiciona o bit de sinal + string gerado da junção da lista

    # 2 = Complemento de 2
    for i in range( binario.index( "." ) - 1, 0, -1 ):
        binario[ i ] = ( "0" if binario[i] == "1" else "1" )            # Faz adição de um bit
        if binario[ i ] == "1":                                         # até o bit na posição virar 1
            break

    negativo_list[ 2 ] = "".join( ( "1", "".join( binario ) ) )
    
    return negativo_list                                            # Retorna os binários negativos
    
def normaliza_binario( binario, decimal_b, n ):
    binario = list( binario )                               # Transforma a string em uma lista de chars  
    binario_norm = ""   
    i = 0                                                   # Quantidade de casas até achar o primeiro 1
    casas = 0                                               # Expoente da normalização
 
    if binario[ 0 ] != "0" and binario[ 0 ] != ".":         # Cobre o caso primeiro número do binário já for 1 e o binário ter parte inteira
        if decimal_b:                                               # Se o número tiver parte decimal o expoente vai ser o index do "." na string
            casas = binario.index( "." )                            
            binario.pop( binario.index( "." ) )
        else:                                                       # Senão o expoente vai ser o tamanho da string
            casas = len( binario )

        binario_norm = "".join( ( ".", "".join( binario ) ) )       # Gera a string do binário normalizado
    else:                                                   # Para os casos restantes
        for char in binario:                                    # Camimha na string contando quantas posições andou até achar o primeiro 1
            if char != '0' and char != ".":
                binario.pop( binario.index( "." ) )
                binario_norm = "".join( ( ".", "".join( binario[i:] ) ) )    # Gera uma string com "." + os chars do binario do index i pra frente

                break

            if not char == ".":                                 # Só adiciona +1 no i se o char for números
                i += 1

    return binario_norm[ :n + 1 ], casas-i    # Retorna o binario normalizado cortado na posição n + 1 e o expoente

def faz_decimal( binario, expoente, negativo ):
    if expoente < 0:                                            # Binário não tem parte inteira
        excesso = "0" * ( expoente * -1 )                           
        decimal_b = list("".join( ( excesso, binario[1:] ) ) )
        inteiro_b = list( )
    else:                                                       # Tem parte inteira
        inteiro_b = list( binario[ 1:expoente + 1 ] )               # Pega parte inteira sem o "."
        decimal_b = list( binario[ expoente + 1: ] )                # Pega parte decimal sem o "."

    decimal = 0
    i = 0       # Casa decimal (expoente)

    for char in inteiro_b[ ::-1 ]:                              # Percorre a string invertida
        decimal += ( 2 ** i if char == "1" else 0 )                 # Inverte usando 2 ^ a casa decimal 
        i += 1

    i = -1
    for char in decimal_b:                                      # Percorre a string normalmente
        decimal += ( 2 ** i if char == "1" else 0 )                 # Inverte usando 2 ^ a casa decimal negativa
        i -= 1

    return ( decimal * -1 if negativo else decimal )            # Retorna o número com sinal

while( 1 ):
    n, l, u, op = -1, 0, -1, 1

    while( 1 ):
        try:
            system( "cls" )
            print( "SIMULADOR FELIZ DE MAQUINA FINITA" )
            n = int( input( "n: " ) )
            if( n <= 0 ):
                raise

            break
        except:
            pass

    while( 1 ):
        try:
            system( "cls" )
            print( "SIMULADOR FELIZ DE MAQUINA FINITA" )
            print( f"n: { n }" )
            l = int( input( "l: " ) )

            break
        except:
            pass

    while( 1 ):
        try:
            system( "cls" )
            print( "SIMULADOR FELIZ DE MAQUINA FINITA" )
            print( f"n: { n }" )
            print( f"l: { l }" )
            u = int( input( "u: " ) )
            if( u < l ):
                raise
            
            break
        except:
            pass

    while( op == 1 ):
        system( "cls" )
        while( 1 ):
            print( f"F( 2, {n}, {l}, {u} )" )
            nums_str = input( "Numero decimal: " )
            try:
                teste = float( nums_str )
                break
            except:
                system( "cls" )
                print( "Número inválido:" )

        
        negativo_bool, point_char, inteiro_b, decimal_b = divide_num( num= nums_str )
        binario = gera_binario( inteiro_b= inteiro_b, decimal_b= decimal_b )
        if negativo_bool:
            binario_neg = gera_negativo( binario= binario, decimal_b= decimal_b)
        binario_norm, expoente = normaliza_binario( binario= binario, decimal_b=decimal_b, n= n )
        sinal = ( "1" if negativo_bool else "0" )
        decimal_res = faz_decimal( binario= binario_norm, expoente= expoente, negativo= negativo_bool )
        
        if len( binario_norm ) < len( binario ):
            print( "[!] Erro de aproximação" )
        if expoente < l:
            print( "[!] Underflow" )
        elif expoente > u:
            print( "[!] Overflow" )

        print( f"\nBinário: { binario }" )
        if negativo_bool:
            print( f"S/A: { binario_neg[ 0 ] }" )
            print( f"C1: { binario_neg[ 1 ] }" )
            print( f"C2: { binario_neg[2] }" )
        print( f"Numero normalizado armazenado em binário: { sinal } { binario_norm } x 2^{ expoente }" )
        print( f"Decimal: { format( decimal_res, '.40f' ) }" ) # Apresenta 40 casas de precisão
        op = int( input("\n[1] Escrever outro número\n[2] Mudar configurações\n[3] Sair\n> ") )
        
        if( op == 3 ):
            exit( )
