km = int(input("km: "))

dias = int(input("Dias: "))

valor_dia = 60 
valor_km = 0.15

conversao = valor_dia * dias + valor_km * km

print(f"Valor final: RS{conversao:.2f}")

