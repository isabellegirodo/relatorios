import csv
import pandas as pd
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os

pessoas = []
while True:
    nome = str(input('Nome completo: ')).title().strip()
    departamento = str(input('Departamento: ')).upper().strip()
    horas_extras = int(input('Quantidade de horas extras: '))
    mes = str(input('Mês: ')).capitalize().strip()
    
    pessoas.append([nome, departamento, horas_extras, mes])
    
    adicionar_mais_pessoa = ' '
    while adicionar_mais_pessoa not in 'SsNn' or adicionar_mais_pessoa == '':
        adicionar_mais_pessoa = str(input('Deseja adicionar mais alguém? [S/N]: ')).strip()
    if adicionar_mais_pessoa in 'Nn':
        break

arquivo_existente = os.path.isfile('pessoas.csv')

with open('pessoas.csv', 'a', newline='', encoding='utf-8') as arquivo:
    escritor_csv = csv.writer(arquivo)
    
    if not arquivo_existente:
        escritor_csv.writerow(['Nome', 'Departamento', 'Horas Extras', 'Mês de Referência'])

    escritor_csv.writerows(pessoas)


tabela = pd.read_csv('pessoas.csv')

for linha in tabela.index:
    nome_pessoa = tabela.loc[linha, "Nome"]
    departamento_pessoa = tabela.loc[linha, "Departamento"]
    horas_extras_pessoa = tabela.loc[linha, "Horas Extras"]
    mes_pessoa = tabela.loc[linha, "Mês de Referência"]
    
    pdf = canvas.Canvas(f'Relatório de {nome_pessoa}.pdf', A4)
    pdf.setFont('Times-Bold', 18)
    pdf.drawString(105, 750, f'Relatório de Horas Extras de {nome_pessoa}')
    
    pdf.setFont('Courier', 14)
    pdf.drawString(105, 720, f'Nome: {nome_pessoa}')
    pdf.drawString(105, 690, f'Departamento: {departamento_pessoa}')
    pdf.drawString(105, 660, f'Horas Extras: {horas_extras_pessoa}')
    pdf.drawString(105, 630, f'Mês de Referência: {mes_pessoa}')
    pdf.save()

print('Relatórios criados com sucesso')
