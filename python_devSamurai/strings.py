#Strings

'sou uma string'

s="sou uma string"

type(s)

s='ola'
s == 'ola'

t='mundo'
s+t  #contenação de string

s + ' ' + t

'-' * 3

4 * 'A'

'm' in t

'M' in t

len(t) #mundo

## Indexação de strings

s = 'python'
s[0]

len(s)

nova_string=s[0:2]
print(nova_string)

nova_string=s[:4]
print(nova_string)

nova_string=s[-1]
print(nova_string)

s[-1]  #a primeira letra é 0, quando negativo ele vai pegar a ultima letra da palavra/frase

## Funções Built-in de Strings


s = 'ola mundo'

s.count('a')

s.lower()

s.upper()

s.split()

s.split('o')

