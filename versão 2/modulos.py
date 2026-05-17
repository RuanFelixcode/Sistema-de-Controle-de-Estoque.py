def continuar_ou_nao():
    while True:
        opc = input('deseja continuar? (s pra sim n pra nao)')
        if opc == 'n':
            return False
        elif opc == 's':
            return True
        else:
            print('opção invalida')
