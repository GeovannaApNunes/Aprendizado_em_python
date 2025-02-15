# Controle de decisão-IF

#if<condição>
temp=eval(input('Digite a temperatura: '))
if temp>= 40:
  print('Está muito calor')
elif temp >30:
    print('Está agradavél')
else:
  print('Está frio!')

#Exercicios
nota=eval(input('Qual a sua nota? '))
if nota>7:
  print('Parabens vc foi aprovado!')
elif nota<7:
  print('Você foi reprovado')
else:
  print('Muito bem!')

nota1 = eval(input('Digite a primeira nota: '))
nota2 = eval(input('Digite a segunda nota:' ))

media = (nota1 + nota2) / 2

if media >= 7:
  print('Você foi aprovado!')
elif nota<7:
  print('Você foi reprovado')

nota1 = eval(input('Digite a primeira nota: '))
nota2 = eval(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if media >= 7:
  print(f'Você foi aprovado!')
elif media >= 5 and media < 7:
  print('Você esta de recuperação')
else:
  print('Você foi reprovado')