from sistema import Sistema

produtos = Sistema()

# menu do vendedor
while True:
    print('opções\n1 - cadastro\n2 - registrar produtos\n3 - exibir produtos\n4 - remover produtos\n5 - sair ')
    try:
        opcoes = int(input('selecione uma opção:'))
        if opcoes == 1:
            produtos.cadastrar()
        elif opcoes == 2:
            produtos.registrar_produtos()
        elif opcoes == 3:
            produtos.exibir()

        elif opcoes == 4:
            produtos.remover_produtos()

        elif opcoes == 5:
            break
        else:
            print('opção invalida')
    except ValueError:
        print('erro ao selecionar uma opção digite apenas numeros')

