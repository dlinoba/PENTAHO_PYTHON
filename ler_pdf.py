from tabula.io import read_pdf
from datetime import date, timedelta
from sqlalchemy import create_engine

def to_int(x):
    return int(x.replace('.',''))

def to_float(x):
    return float(x.replace('.','').replace(',','.'))

file1 = "C:/PDI_PROEJTOS/read_pdf_file/produtos.pdf"

tables = read_pdf(file1,pages=1)

table = tables[0]

table.columns = ['Produto', 'Val_Uni', 'QTD', 'Total']

# adiciona coluna 'horario' com o horario atual
table['Data_Ref'] = date.today() - timedelta(days = 1)

# converte números que eram strings para o tipo correto
table['Val_Uni'] = table['Val_Uni'].apply(to_float)
table['Total'] = table['Total'].apply(to_float)

engine = create_engine("mysql://@USER:@SENHA@SERVER:@PORTA/@DATABASE_NAME")

table.to_sql('PRODUTO', con=engine, if_exists='append', index=False)