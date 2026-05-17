# o que aprendi nesse mini projeto
# 1 melhorei minha logica boleana
# 2 pratiquei tudo que aprendi 
# 3 descobri novas formas de aplicar o uso de funções + modularização 
# --------------------------
# ferramentas que usei para meu aprendizado
# IA COPILOT 
# VS CODE
# PYTHON
# --------------------------
# erros que cometi 
# nomes confusos
# 📝 Mini anotação — erro e correção
# Erro cometido:  
# No código original você escreveu:
# python
# if self.produtos:
#    print(f'nao contem produtos no estoque {self.produtos}')
# else:
#   print(f'produtos no estoque e preços\n{self.produtos}')
# O problema é que a mensagem está invertida.

# if self.produtos significa que o dicionário não está vazio (há produtos), mas você imprimiu "não contém produtos".

# Correção:

#python
# if not self.produtos:
#    print("Não contém produtos no estoque")
# else:
#   print(f"Produtos no estoque e preços:\n{self.produtos}")
# not self.produtos → dicionário vazio → sem produtos.

# else → dicionário com itens → mostra os produtos.

# 👉 Resumindo:

# Estruturas vazias ({}, [], "") → False

# Estruturas com conteúdo → True

# fim autor/aluno: ruan felix
