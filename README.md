# Gerador automático de relatórios em python &#x1F4DD;

## Bibliotecas necessárias e instalação &#x1F4CC;
- pandas
    * pip install pandas
- reportlab
    * pip install reportlab
- csv (já vem instalado no python)

## Modo de Usar &#x1FAA7;
Quando rodar o código `python3 relatorios.py` será necessário informar 4 dados (nome, departamento, horas extras e mês de referência).  
---

Em seguida, será perguntado se quer adicionar mais uma pessoa, caso a resposta seja afirmativa, digite S ou s.   
---

Se a resposta for negativa, digite n ou N.   
Em ambos os casos será criado o arquivo `pessoas.csv` junto com os pdfs, referentes a cada pessoa que foi adicionada.   
---
Exemplo: se adicionar 3 pessoas, serão criados 3 pdfs
---

### Observação &#x26A0;&#xFE0F;
As fontes padrões do reportlab são:
* Helvetica
* Times-Homan
* Courier
* Symbol
* ZapfDingbats