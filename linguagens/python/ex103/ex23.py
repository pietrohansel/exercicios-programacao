# 4) Interprete o código abaixo e escreva o fluxograma desse código: 

idade = 20 

if idade >= 18:
    print("A")
else:
    print("B")

print("C")

"""

+------------+
| idade = 20 |
+------------+


+-----------+             +------------+
|           |             |            |
| idade>=18 | -- Sim -->  | print("A") |
|           |             |            |
+-----------+             +------------+
      
      |               +------------+
      |               |            |
      |               | print("B") |
      --- Não -->     |            |
                      +------------+


 +-----------+                     
 |           |
 | print("C) |
 |           | 
 +-----------+                                   

"""
