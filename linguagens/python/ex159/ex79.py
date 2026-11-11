
produtos = ['beb3453', 'tfa3142','beb2464']

def alcoolica(bebida, cod_categoria):
    bebida = bebida.upper()
    if 'BEB' in bebida: 
        return True
    else:
        return False

for produto in produtos:
    if alcoolica(produto,'BAS'): 
        print(f"{produto} -> Setor de bebidas alcóolicas")

