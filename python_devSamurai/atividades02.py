#Atividades

numero = int(input("Digite um número:"))
fatorial = numero
while numero >= 2:
  fatorial = fatorial * (numero - 1)
  numero -= 1
print(fatorial)

numero = int(input("Digite um número inteiro: "))
fatorial = numero
while numero >= 2:
  fatorial = fatorial * (numero - 1)
  numero -= 1
print(fatorial)

senha = '0000'
tentativas = 3
while tentativas !=0:
  tentativa = input("Digite uma senha numerica de quatro digitos: ")

  if tentativa == senha:
    print("Senha correta. Acesso concedido")
    break

  else:
    print("Senha incorreta. Tente")
    tentativas -= 1

#for
tabuada = int(input("Qual a tabuada será gerada? "))
limite = int(input("Até qual valor iremos calcular? "))
for numero in range(0, limite+1):
  print(f'{tabuada} x {numero} = {tabuada * numero}')

n = int(input('Digite qual elemento de serie deve ser mostrado: '))
primeiro = 1
segundo = 1

if n==1 or n==2:
  print('1')

else:
  for _ in range(2, n):
    elemento = primeiro + segundo
    segundo = primeiro
    primeiro = elemento
print(elemento)