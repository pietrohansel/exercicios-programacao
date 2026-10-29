
#  Aula 9



frase = ('curso em video')
print(frase[9])  # mostra a 9° letra

frase = ('curso em video')
print(frase[9:13])  # lê a partir do 9 até a 13, mas não lê a 13

frase = ('Curso em vídeo')
print(frase[9:21:2])  # pula de dois em dois

frase = ('Curso em Vídeo')
print(frase[:5])  # começa do zero, sem excluir o mesmo

frase = ('Curso em vídeo')
print(frase[9::3])  # pula três

frase = ('Curso em vídeo')

print(len(frase))  # mostra quantos caracteres a string possui

print(frase.count('o'))  # conta apenas uma letra específica ('o')

print(frase.find('Cur'))  # fala quando começa a palavra pedida

print(frase.find('Android'))  # fala quando começa a palavra pedida, caso não tenha, ele retorna -1

print('Curso' in frase)  # retorna true ou falso caso exista a palavra procurado na string

print(frase.replace('vídeo', 'texto'))  # troca a palavra

print(frase.upper())  # deixa em maiusculo

print(frase.lower())  # deixe em minusculo

print(frase.capitalize()) # Deixa apenas a primeira letra da string maiúscula e o restante minúsculo

print(frase.title())  # Deixa No Formato de Título

print(frase.strip())  # remove espaços inuteis na string

print(frase.rstrip())  # remove espaços inuteis na string a partir da right (direita)

print(frase.lstrip())  # remove os espaços inuteis da string a partir da esquerda (left)

print(frase.split())  # transforma em lista  cria uma divisão de espaços e cada palavra agora começa do zero 0 - nova indexação

print('-'.join(frase))  # deixa-o-texto-assim




# EXERCICIOS ---------------------------------------------------------------------------------------




nome_de_uma_pessoa = str(input("Digite seu nome: ")).strip()


print(f"Nome Maiúsculo:{nome_de_uma_pessoa.upper()}")

print(f'Nome minúsculo:{nome_de_uma_pessoa.lower()}')

print(
    f'Contagem de letras: {len(nome_de_uma_pessoa)-nome_de_uma_pessoa.count(" ")}')

print(f'Letras do prmeiro nome: {nome_de_uma_pessoa.find(" ")}')



numero_aleatorio = int(input('Digite algum número: '))

u = numero_aleatorio//1 % 10  # exemplo 20/1= 20 tem resto 0 = unidade
d = numero_aleatorio//10 % 10
c = numero_aleatorio//100 % 10
m = numero_aleatorio//1000 % 10

print(f'Unidade: {u}, Dezena: {d}, Centena:{c}, Milhar: {m}')

'''
'''
nome_da_cidade = str(input('Digite o nome da cidade: ')).strip()

print(nome_da_cidade[:5].upper() == 'SANTO')
'''
'''
nome_da_pessoa = input('Escreva seu nome: ').strip()

print(f'Seu nome tem Silva? {"silva" in nome_da_pessoa.lower()}')
'''
'''
frase_aleatoria = str(input('Escreva sua frase: ')).strip().upper()

print(f'A letra A aparece:{frase_aleatoria.count('A')} vezes')

print(f'A letra A aparece pela primeira vez em {frase_aleatoria.find('A')+1}')

print(f'A letra A aparece pela última vez em {frase_aleatoria.rfind('A')+1}')

# print(
# f'A letra A aparece na primeira vez na posição: {frase_aleatoria.find("a")}')


nome_completo_de_uma_pessoa = str(
    input('Escreva seu nome completo: ')).strip().split()

print(nome_completo_de_uma_pessoa[0])
print(nome_completo_de_uma_pessoa[-1])
