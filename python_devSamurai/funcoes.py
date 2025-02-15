#Funções

#função sem retorno e sem passagem de parâmetros
def ola_mundo():
  'Função que mostra uma msg padrão na tela.'
  print('Olá Mundo!')

help(ola_mundo)
ola_mundo()

#função sem retorno e com passagem de parâmetros
def ola_mundo(name='User'):
    'Função que mostra um texto customizado na tela.'
    print(f'Olá mundo, meu nome é {name}')

name = input('Qual o seu nome? ')
ola_mundo()

#função com retorno e passagem de parâmetros
def soma(a, b):
  'Função que recebe dois num e realiza a soma entre eles'
  return a+b

resultado = soma(3,4)
print(resultado)

#Atividades
def quadrado(numero=5):
  return numero * numero

quadrado(2)

def temperatura(temp):
  celius = (5/9) * (temp - 32)
  return celius

print(temperatura(32))
print(temperatura(10))
print(temperatura(30))


def calculo(comando, numero):
  if comando == 'quadrado':
    return numero * numero
  else:
    return numero * numero * numero

print(calculo('cubo', 2))
print(calculo('quadrado', 6))