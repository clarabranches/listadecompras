# planilha para exibir os produtos, valores, quantidades e btn_excluir
# adicionar produto: label e caixa de texto 
# adicionar preço: label e caixa de texto
# adicionar quantidades: label e caixa de texto
#btn_enviar

import flet as ft
import numpy as np

result = 0.0

def main(pagina: ft.Page):
    pagina.title = "Exemplo de Tabela com Flet"
    columns = [
        ft.DataColumn(ft.Text("ID")),
        ft.DataColumn(ft.Text("Produto")),
        ft.DataColumn(ft.Text("Valor")),
        ft.DataColumn(ft.Text("Quantidade")),
    ]
    rows = [ ]


    def calcular_soma_coluna(valor):
        global result
        result += valor
        print(result)
        valor_total.value = result
        pagina.update


    def add_produto(e):
        nonlocal rows
        id = str(len(rows) + 1)  # Gerando um ID automaticamente
        nome = campo_produto.value
        valor = campo_valor.value
        valor_float = float(valor)
        qtd = campo_qtd.value

        rows.append(
            ft.DataRow(cells=[
                ft.DataCell(ft.Text(id)),
                ft.DataCell(ft.Text(nome)),
                ft.DataCell(ft.Text(valor)),
                ft.DataCell(ft.Text(qtd)),
            ])
        )
        table.rows = rows
        calcular_soma_coluna(valor_float)
        print(len(rows))
        pagina.update()

    
    table = ft.DataTable(columns=columns, rows=rows)

    campo_produto = ft.TextField(label="Produto")
    campo_valor = ft.TextField(label="Valor")
    campo_qtd = ft.TextField(label="Quantidade")
    btn_enviar = ft.ElevatedButton("Add", on_click=add_produto)

    label_total = ft.Text("Total")
    valor_total = ft.Text(0.0)


    pagina.add(table)
    pagina.add(ft.Row([campo_produto, campo_valor, campo_qtd, btn_enviar]))
    pagina.add(ft.Row([label_total, valor_total]))


ft.app(target=main)
