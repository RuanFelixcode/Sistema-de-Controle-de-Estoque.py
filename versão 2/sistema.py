class Sistema:
    def __init__(self):
        self.usuario = ''
        self.senha = ''
        self.produtos = {}
    
    def cadastrar(self):
        # cadastrar nome
        while True:
            nome = input('digite seu nome de usuario:')
            if not nome.replace(' ','').isalpha():
                print('nao e permitido numeros')
                continue
            self.usuario = nome
            break
        # fim do registro do nome
        #-------------------------
        # registrar senha
        while True:
            senha = input('digite a senha:')
            if len(senha) < 6:
                print('senha fraca digite ao menos 6 caracteres')
                continue
            if ' ' in senha :
                print('nao e permitido espaço')
                continue
            if senha.isalnum():
                self.senha = senha
                print('senha criada com sucesso')
                break
            else:
                print('na senha digite letras e numeros')
        # fim 
        #-------------------------
        # adicionar produtos
    def registrar_produtos(self):
        if self.usuario == '' or self.senha == '':
            print('crie um perfil de usuario primeiro')
            self.cadastrar()

        while True:
            nome_produto = input('digite o nome do produto:')
            if not nome_produto.replace(' ','').isalpha():
                print('no nome do produto nao deve conter numeros')
                continue
            try:
                preco_produto = float(input('digite o preço do produto:'))
                if preco_produto <= 0 :
                    print('nao e permitido valores 0 ou abaixo de 0')
                    continue
            except ValueError:
                print('nao digite letras ou espaços no preço')
            self.produtos.update({nome_produto:preco_produto})
            from modulos import continuar_ou_nao
            if not continuar_ou_nao():
                break
            
        # fim
        #------------------------- 
        # exibir produtos ao vendedor
    def exibir (self):
        # um dicionario vazio em python tem valor boleano de false
        if not self.produtos:
            print(f'nao contem produtos no estoque {self.produtos}')
        else:
            print(f'produtos no estoque e preços\n{self.produtos}')
        # fim
        #-------------------------
        # remover produtos 
    def remover_produtos(self):
        if self.usuario == '' or self.senha == '':
            print('crie um perfil de usuario primeiro')
            self.cadastrar()
            
        while True:
            self.exibir()
            remover = input('digite o nome do produto a ser removido:')
            if remover in self.produtos:
                self.produtos.pop(remover)
            else:
                print('nao existe esse produto no estoque')
            from modulos import continuar_ou_nao
            if not continuar_ou_nao():
                break   
        # fim
        #-------------------------

    
                


    
        
            


