import pandas as pd

#ruta del archivo de salida
output_file = r"E:\Sicore\salida.txt"

#cargamos el Excel en un DataFrame
excel_file = r"E:\Sicore\excel_de_datos.xlsx"
df = pd.read_excel(excel_file)

#establecemos el largo de cada bloque
long_bloq1 = 28
long_bloq2 = 27
long_bloq3 = 43
long_bloq4 = 37

#nombre de columnas
columnas_excel_file = {
    "Cod.1",
    "Fecha Comprobante",
    "Cod. Comprobante",
    "Honorarios brutos",
    "Cod.2",
    "Base de calculo",
    "Fecha fin de mes",
    "Cod.3", "Retencion",
    "Cod.4",
    "Cod.5",
    "CUIL",
    "Digito1",
    "Cod.6",
    "Año",
    "Digito2",
    "Digito3"
}

#creamos un diccionario que mapea cada columna a "str" en el parámetro dtype
dtype_cadena_de_texto = {columna: str for columna in columnas_excel_file}

#leemos el excel y le especificamos el tipo de dato 
df = pd.read_excel(excel_file, dtype=dtype_cadena_de_texto)

#abrimos el archivo de texto en modo escritura para cargar los datos 
with open(output_file, "w") as file:
    for index, row in df.iterrows():

        bloq1 = str(row['Cod.1']) + str(row['Fecha Comprobante']) + str(row['Cod. Comprobante'])
        bloq2 = str(row['Honorarios brutos']) + str(row['Cod.2'])
        bloq3 = str(row['Base de calculo']) + str(row['Fecha fin de mes']) + str(row['Cod.3'])
        bloq4 = str(row['Retencion']) + '  ' + str(row['Cod.4']) + '          ' + str(row['Cod.5']) + str(row['CUIL'])
        bloq5 = str(row['Digito1']) + str(row['Cod.6']) + str(row['Año']) + str(row['Digito2']) + str(row['Digito3'])
        
        espacio_bloq1 = ' ' * (long_bloq1 - len(bloq2))
        espacio_bloq2 = ' ' * (long_bloq2 - len(bloq3))
        espacio_bloq3 = ' ' * (long_bloq3 - len(bloq4))
        espacio_bloq4 = ' ' * (long_bloq4 - len(bloq5))

        #concatena los datos y agrega los espacios
        linea_formateada = (
            bloq1 + espacio_bloq1 + 
            bloq2 + espacio_bloq2 + 
            bloq3 + espacio_bloq3 + 
            bloq4 + espacio_bloq4 + 
            bloq5
        )

        #escribe la linea con el formato necesario en el archivo de texto
        file.write(linea_formateada + "\n")

print(f"Los datos se han escrito en {output_file}")