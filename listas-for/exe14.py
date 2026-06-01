vendas = [1200.50, 3400.00, 980.00, 5600.20, 2100.00, 850.00]

media = sum(vendas) / len(vendas)

acima_media = []

for venda in vendas:
    if venda > media:
        acima_media.append(venda)

print("Média das vendas:" , media)
print("Acima da média:" , vendas)