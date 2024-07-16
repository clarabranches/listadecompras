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


    def calcular_soma_coluna(valor,quantidade):
        global result
        result += (valor*quantidade) 
        print(result)
        valor_total.value = result
        pagina.update


    def add_produto(e):
        nonlocal rows
        id = str(len(rows) + 1)  # Gerando um ID automaticamente
        nome = campo_produto.value
        valor = campo_valor.value
        qtd = campo_qtd.value
        
        valor_float = float(valor)
        quantidade = int(qtd)

        rows.append(
            ft.DataRow(cells=[
                ft.DataCell(ft.Text(id)),
                ft.DataCell(ft.Text(nome)),
                ft.DataCell(ft.Text(valor)),
                ft.DataCell(ft.Text(quantidade)),
            ])
        )
        table.rows = rows
        calcular_soma_coluna(valor_float, quantidade)
        print(len(rows))
        campo_produto.value = ""
        campo_valor.value = ""
        campo_qtd.value = "1"
        pagina.update()

    # def excluir_produto(e):
    #     cell_value_to_delete = campo_produto_excluir.value
    #     for i, row in enumerate(table.rows):
    #         for id in row.id:
    #             if id.value == cell_value_to_delete:
    #                 del table.rows[i]
    #                 table.update()

    
    table = ft.DataTable(columns=columns, rows=rows)

    campo_produto = ft.TextField(label="Produto", width=160)
    campo_valor = ft.TextField(label="Valor", width=80)
    campo_qtd = ft.TextField(label="Qtd", width=60)
    campo_qtd.value = "1"
    btn_enviar = ft.ElevatedButton("Add", on_click=add_produto)

    label_total = ft.Text("Total")
    valor_total = ft.Text(0.0)

    label_excluir = ft.Text("Excluir Produto")
    campo_produto_excluir = ft.TextField(label="Id do Produto", width=180)
    # btn_excluir = ft.ElevatedButton("Excluir", on_click=excluir_produto)



    pagina.add(table)
    pagina.add(ft.Row([campo_produto, campo_valor, campo_qtd, btn_enviar]))
    pagina.add(ft.Row([label_total, valor_total]))
    pagina.add(ft.Row([label_excluir, campo_produto_excluir, btn_excluir]))


ft.app(target=main)
