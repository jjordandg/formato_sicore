import pandas as pd

# Cargar el archivo Excel en un DataFrame
excel_file = r"C:\pruebas\prueba2.xlsx"
df = pd.read_excel(excel_file)

# Formatear la fecha en el formato deseado (dd/mm/yyyy)
fecha_formateada = df['Fecha-fin-de-mes'].values[0].replace('"', '')

# Ruta del archivo de salida en formato de texto
output_file = r"C:\pruebas\datos1.txt"

# Abre el archivo de texto en modo escritura y recorre las filas para escribirlas en el archivo con saltos de línea
with open(output_file, "w") as file:
    for index, row in df.iterrows():
        
        #calcula la cantidad de espacios que deberá insertarse entre el primer y el segundo bloque
        espacios = ''       
        i = 0
        while(i < 28 - len(str(row['Honorarios-brutos']).replace('"', '') + str(row['Cod-2']).replace('"', ''))):
            espacios+= ' '
            i = i +1
        espacio_primer_bloque = espacios
        
        #calcula la cantidad de espacios que deberá insertarse entre el segundo y el tercer bloque
        espacios = ''
        i = 0
        while(i < 27 - len(str(row['Base-de-calculo']).replace('.', ',').replace('"', '') + fecha_formateada + '010')):
            espacios+= ' '
            i = i +1
        espacio_segundo_bloque = espacios
        
        #calcula la cantidad de espacios que deberá insertarse entre el tercer y el cuarto bloque
        espacios = ''
        i = 0
        while(i < 43 - len(str(row['Retencion']).replace('.', ',').replace('"', '') + '  ' + '0,00' + '          ' + str(row['Cod-5']).replace('"', '') + str(row['CUIL']).replace('"', ''))):
            espacios+= ' '
            i = i +1
        espacio_tercer_bloque = espacios
        
        #calcula la cantidad de espacios que deberá insertarse entre el cuarto y el quinto bloque
        espacios = ''
        i = 0
        while(i < 37 - len(str(row['Digito1']).replace('"', '') + '0000' + str(row['Anio']).replace('"', '') + str(row['Digito2']).split('.')[0].replace('"', '') + str(row['Digito3']).replace('"', ''))):
            espacios+= ' '
            i = i +1
        espacio_cuarto_bloque = espacios     
        
        #concatena los datos y agrega los espacios
        linea_formateada = (
            '01' + str(row['Fecha-Comprobante']).replace('"', '') + str(row['Cod-Comprobante']).replace('"', '') + espacio_primer_bloque + #primer bloque
            str(row['Honorarios-brutos']).replace('"', '') + str(row['Cod-2']).replace('"', '') + espacio_segundo_bloque+ #segundo bloque
            str(row['Base-de-calculo']).replace('.', ',').replace('"', '') + fecha_formateada + '010' + espacio_tercer_bloque +#tercer bloque
            str(row['Retencion']).replace('.', ',').replace('"', '') + '  ' + '0,00' + '          ' + str(row['Cod-5']).replace('"', '') + str(row['CUIL']).replace('"', '') + espacio_cuarto_bloque + #cuarto bloque
            str(row['Digito1']).replace('"', '') + '0000' + str(row['Anio']).replace('"', '') + str(row['Digito2']).split('.')[0].replace('"', '') + str(row['Digito3']).replace('"', '') #quinto bloque 
        )
        #escribe la linea con el formato necesario en el archivo de texto
        file.write(linea_formateada + "\n")

print(f"Los datos se han escrito en {output_file}")



     
    
