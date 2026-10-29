try:
    n = int(input(" "))
    m = int(input(" "))
    d = n/m

except (ValueError, TypeError):
    print("Tivemos um problema com os tipos de dados que você digitou.")
except ZeroDivisionError:
    print("Não é possível dividir com zero")
except KeyboardInterrupt:
    print("O usuário preferiu não informar os dados!")

# except Exception as erro:
#     print(f"Não é possível dividir com zero.\nProblema encontrado foi {erro.__class__}")
else:
    print(f"{d}")
finally:
    print("Volte sempre")
