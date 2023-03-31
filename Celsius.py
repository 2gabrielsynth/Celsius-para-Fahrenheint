print("Programa para converter Celsius em Fahrenheits.")
C = float(input("Digite a temperatura: "))
F = C*(1.8) + 32
print("A temperatura é:",F,"F" )

if F  == 77:
  print('Clima ameno')

if F < 77:
  print ('Friaca')

if F > 77:
  print('Calor do Cão')
