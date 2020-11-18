import pandas as pd
import sqlite3
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt

# conecta con sqlite

conn = sqlite3.connect('pybodb.sqlite')

# buscar la dirección del csv para cargar

df = pd.read_csv(r'C:\Users\20360392008\Documents\Bases de datos\Agip\datos_agip.csv')

# para recordar las columnas del df

df.columns

# cuento las parcelas por antiguedad y por piso

group_1= df.groupby(["ANTIGUED","PISOS_ALTO"])["PISOS_ALTO"].count()

# transforma el df en sql para usar querys, elegir nombre ej ""agip""

df.to_sql('agip', con = conn)

# QUERY SQL: SELECT selecciono columna FROM la database

db = pd.read_sql("SELECT ANTIGUED FROM df", conn)

#salida a excel
#df.to_excel(r'Path to store the exported excel file\File Name.xlsx', index = False)


df.to_excel("C:\Users\20360392008\Documents\Bases de datos\Agip\edificios_piso_año.xlsx"