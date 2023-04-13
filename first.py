
"""########################################################################
#
#    FONTE PARA APRENDIZAGEM DAS FUNCOES DO PYTHON
#
#    Programa:       first.py
#    Programador:    Gerson Dias
#    Objetivo:       Fonte para aprendizagem dos conceitos de Python
#    Data:           13/04/2023
#    
#########################################################################"""

"""-------------------------------------------------------------------------
    TIPOS DE VARIAVEIS:
    
    1. int      - 28 - numeros inteiros
    2. float    - 1.70 - numeros decimais
    3. str      - 'Texto' - Entre aspas
    4. bool     - True / False - Case sensitive

-------------------------------------------------------------------------"""
# VARIAVEIS DO PROGRAMA
txt_escolha     = 'Voce selecionou: '
tp_atendimento  = 'Atendimento'
tp_atendente    = 'Falar com atendente'
tp_voltar       = 'Voltar'
tp_sair         = 'Sair'
#-------------------------------------------------------------------------

# FUNCOES DO PROGRAMA
def escolha_tipo():

    print('####################################################################')
    print('|')
    print('| Olá, Usuário')
    print('| 1 - ', tp_atendimento)
    print('| 2 - ', tp_sair)
    print('|')
    print('#####################################################################')


    #opcao = 1 # variavel fixa - 2 atribuido a variavel opcao

    opcao = input('Digite a opção desejada:') # variavel dinamica, digitada pelo usuario
    
    #print( type(opcao) ) # Eh possivel imprimir o tipo de uma variavel com esta funcao

    #print('Voce selecionou: ' + str(opcao) ) # so eh possivel concatenar variaveis do mesmo tipo. Convertendo inteiro para str para concatenar

    if opcao == '1':        # SE SELECIONADO 1 ENCAMINHAR PARA ATENDIMENTO
        print(txt_escolha, tp_atendimento)
        atendimento()

    elif opcao == '2':      # SE SELECIONADO 2 SAIR
        print(txt_escolha, tp_sair)
    
    else:                   # SELECAO INVALIDA REPETIR
        print('Opcão inválida! Digite novamente')
        escolha_tipo()
#-------------------------------------------------------------------------

def atendimento():
    print('#################################################################')
    print('|')
    print('| Bem vindo ao Atendimento')
    print('| 1 - Falar com atendente')
    print('| 2 - Voltar')
    print('| 3 - Sair')
    print('|')
    print('#################################################################')

    opcao = input('Digite a opção desejada:')
    
    if opcao == '1':        # SE SELECIONADO 1 ENCAMINHAR PARA ATENDENTE
        print(txt_escolha, tp_atendente)
        atendente()
    elif opcao == '2':      # SE SELECIONADO 2 VOLTAR
        print(txt_escolha, tp_voltar)
        escolha_tipo()
    elif opcao == '3':      # SE SELECIONADO 3 SAIR
        print(txt_escolha, tp_sair)

    else:                   # SELECAO INVALIDA REPETIR
        print('Opcão inválida! Digite novamente')
        atendimento()
#-------------------------------------------------------------------------

def atendente():
    print('#################################################################')
    print('|')
    print('| Bem vindo ao Atendimento')
    print('| No momento estamos sem atendentes disponíveis')
    print('| 1 - Voltar')
    print('| 2 - Sair')
    print('|')
    print('#################################################################')

    opcao = input('Digite a opção desejada:')

    if opcao == '1':        # SE SELECIONADO 1 VOLTAR
        print(txt_escolha, tp_voltar)
        atendimento()

    elif opcao == '2':      # SE SELECIONADO 2 SAIR
        print(txt_escolha, tp_sair)
    
    else:                   # SELECAO INVALIDA REPETIR
        print('Opcão inválida! Digite novamente')
        atendente()
#-------------------------------------------------------------------------

# IMPRIMINDO TEXTOS NA TELA
print('Hello World!')

# CAMHANDO FUNCAO PRINCIPAL
escolha_tipo()


