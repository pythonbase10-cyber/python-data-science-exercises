import pandas as pd

dados = {
    'Produto': ['Leite', 'Pao', 'Café',' Arroz' ],
    'Preço': [5.00, 3.50, 15.00, 20.00],
    'Quantidade': [2, 5, 1, 2]
}
tabela = pd.DataFrame(dados)

print('Minha tabela de compras')
print(tabela)

tabela ['Total'] = tabela['Preço'] * tabela['Quantidade']
print("\n--- Tabela com o total calculado___")

filtro_caro = tabela['Preço'] > 10

itens_caros = tabela[filtro_caro]
print('\n___Filtros que custam mais de R$ 10,00 reais___')
print(itens_caros)

# itens baratos
filtro_barato= tabela['Preço'] < 10

itens_baratos = tabela[filtro_barato]
print('\n___Filtros que custam menos de R$ 10,00 reais___')
print(itens_baratos)

gasto_barato = itens_baratos['Total'].sum()
print(f'Total gasto economicos R$: {gasto_barato:.2f}')

preco_max = itens_caros['Total'].max()
print(f'Total de itens caros R$: {preco_max:.2f}')

posi_mais_caro = tabela['Preço'].idxmax()
prod_mais_caro = tabela.loc[posi_mais_caro, 'Produto']
print(f' O item mais caro da lista é: {prod_mais_caro}')