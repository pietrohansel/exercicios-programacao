
produtos = ['beb3453', 'tfa3142','beb2464']

def categoria(bebida, cod_categoria):
    bebida = bebida.upper()
    if cod_categoria in bebida: 
        return True
    else:
        return False

for produto in produtos:
    if categoria(produto,'BEB'): print(f"{produto} -> Setor de bebidas alcóolicas")
    else:
        if categoria(produto,'TFA'): 
            print(f"{produto} -> Setor de bebidas comuns")

s = 0 

print("Hello")