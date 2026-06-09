vendas = [
   [1200, 850, 900, 1500],
   [900, 1100, 1000, 1300],
   [1500, 1600, 1400, 1800],
   [700, 600, 800, 900]
]

vendas_vendedores = [ sum(vendedor) for vendedor in vendas]

vendas_dia = [ sum(dia) for dia in zip(*vendas)]

for i, valor in enumerate(vendas_vendedores, 1):
    print(f"0 vendedor {i} vendeu R$ {valor}")

for i, valor in enumerate(vendas_dia, 1):
    print(f"o vendedor {i} vendeu R$ {valor}")
