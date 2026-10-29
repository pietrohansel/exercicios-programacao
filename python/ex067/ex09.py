# 9. Caixa eletrônico com saque mínimo de cédulas

valor = int(input("Digite seu valor: "))

qt100 = 0 
qt50 = 0
qt20 = 0
qt10 = 0
qt5 = 0 
qt2 = 0 
qt1 = 0

while valor >= 100:
    valor = valor - 100    
    qt100 = qt100 + 1

while valor >= 50:
    valor = valor - 50   
    qt50 = qt50 + 1


while valor >= 20:
    valor = valor - 20    
    qt20 = qt20 + 1


while valor >= 10:
    valor = valor - 10    
    qt10 = qt10 + 1


while valor >= 5:
    valor = valor - 5    
    qt5 = qt5 + 1

while valor >= 2:
    valor = valor - 2    
    qt2 = qt2 + 1

while valor >= 1:
    valor = valor - 1    
    qt1 = qt1 + 1

print(f'''\nNotas de R$100: {qt100}\nNotas de R$50: {qt50}\nNotas de R$20: {qt20}\nNotas de R$10: {qt10}\nNotas de R$5: {qt5}\nNotas de R$2: {qt2}\nMoedas de R$1: {qt1}\n
''')