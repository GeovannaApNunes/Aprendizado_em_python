# Listas

animais = ['cavalo', 'cachorro', 'calopsita', 'gato']
type(animais)

animais[0]

len(animais)

mais_animais = ['canarinho', 'cobra', 'macaco', 'rinoceronte']
nova_lista = animais + mais_animais
print(nova_lista)

'cobra' in nova_lista

diversas = ['string', 3, 4, 5]

diversas[0]

diversas[3]

valores = [10, 20, 30, 40, 50]
print(min(valores))
print(max(valores))

sum(valores)



## Listas built-in

mercado = ['arroz', 'feijão', 'cenoura', 'maçã', 'carne de frango']

#acrescentar um item ao final da lista
mercado.append('molho')
mercado

#conta quantas vezes o item repete na lista
mercado.count('molho')

#retorna a posição do elemento
mercado.index('maçã')

mercado.insert(1, 'refrigerante')
mercado

mercado.sort()
mercado

mercado.reverse()
mercado

#strings são imutáveis
s = 'ola pythan'
s[8]='o'

#listas são mutáveis
lista = [ 'cachorro', 'gato']
lista[0]='galinha'
lista

