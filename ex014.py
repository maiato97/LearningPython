print('---------- ALUGUEL DE CARROS -----------')
d = int(input("Quantos dias será alugado: "))
km = float(input("Quantos KM rodados durante o aluguel: "))
preco = d * 60 + (km * 0.15)
print('O total a pagar é: R$',preco)



