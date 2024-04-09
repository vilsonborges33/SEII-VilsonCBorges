texto = "Oi pessoal"
print(texto)
print(len(texto))
print(texto[6])
print(texto[0:2])
print(texto[:2])
print(texto[3:])
print(texto.lower())
print(texto.upper())
print(texto.count('s'))
print(texto.find('a'))
print(texto.find('b'))

novotexto = texto.replace('pessoal','gente')
print(novotexto)

texto = texto.replace('pessoal','gente')
print(texto)

t1 = 'Ola'
t2 = 'Vilson'
mensagem = t1 + ', ' + t2 + '. Bem-vindo!'
print(mensagem)

mensagem = '{}, {}. Bem-vindo!'.format(t1, t2)
print(mensagem)

#mensagem = f'{t1}, {t2}. Bem-vindo!'
#print(mensagem)

#mensagem = f'{t1}, {t2.upper()}. Bem-vindo!'
#print(mensagem)

print(dir(t2))
print(help(str))
print(help(str.lower))