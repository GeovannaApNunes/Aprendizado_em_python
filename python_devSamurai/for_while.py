#Laço while e Laço For

numero = 0
while numero <= 20:
  print(numero)
  numero += 2 #numero + 1
print('Acabou o loop while')

numero_max = eval(input('Digite um numero:'))
numero = 0
while numero <= numero_max:
  print(numero)
  numero += 1
print('Sequencia gerada')

#Laço FOR

for dia in ['Segunda', 'Terça','Quarta','Quinta', 'Sexta']:
  print(dia)

for numero in ['1','2','3','4','5']:
  print(numero, end=" ")

for numero in range(6):
  print(numero, end=" ")

for numero in range(0,21): #sequencia iniciando no 0 e indo ate o vinte
  print(numero, end=" ")

for numero in range(5,50,5): #de 5 em 5
  print(numero, end=" ")