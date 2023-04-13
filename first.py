
# CODIGO PARA APRENDIZAGEM DAS FUNCOES DO PYTHON

"""
    ESTE COMENTARIO POSSUI DIVERSAS LINHAS

    Programa:       first.py
    Programador:    Gerson Dias
    Objetivo:       Fonte para aprendizagem dos conceitos de Python
    Data:           13/04/2023
    
"""

# VARIAVEIS


"""
    TIPOS:
    
    1. int      - 28 - numeros inteiros
    2. float    - 1.70 - numeros decimais
    3. str      - 'Texto' - Entre aspas
    4. bool     - True / False - Case sensitive

"""
# VARIAVEIS DO PROGRAMA
txt_escolha     = 'Voce selecionou: '
tp_atendimento  = 'Atendimento'
tp_voltar       = 'Voltar'
tp_sair         = 'Sair'

# FUNCOES

def escolha_tipo():

    print('####################################################################')
    print('|')
    print('| 1 - ', tp_atendimento)
    print('| 2 - ', tp_sair)
    print('|')
    print('#####################################################################')


    #opcao = 2 # variavel fixa - 2 atribuido a variavel opcao

    opcao = input('Digite a opção desejada:') # variavel dinamica, digitada pelo usuario
    #print( type(opcao) ) # Eh possivel imprimir o tipo de uma variavel com esta funcao

    #print('Voce selecionou: ' + str(opcao) ) # so eh possivel concatenar variaveis do mesmo tipo. Convertendo inteiro para str para concatenar

    if opcao == '1':
        print(txt_escolha, tp_atendimento)
        atendimento()

    elif opcao == '2':
        print(txt_escolha, tp_sair)
    
    else:
        print('Opcão inválida! Digite novamente')
        escolha_tipo()

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
    
    if opcao == '1':
        print(txt_escolha, tp_sair)
        atendente()
    elif opcao == '2':
        print(txt_escolha, tp_voltar)
        escolha_tipo()
    elif opcao == '3':
        print(txt_escolha, tp_sair)

    else:
        print('Opcão inválida! Digite novamente')
        atendimento()

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

    if opcao == '1':
        print(txt_escolha, tp_voltar)
        atendimento()

    elif opcao == '2':
        print(txt_escolha, tp_sair)
    
    else:
        print('Opcão inválida! Digite novamente')
        atendente()



# IMPRIMINDO TEXTOS NA TELA
print('Hello World!')
escolha_tipo()


