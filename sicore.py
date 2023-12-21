import pandas as pd
import os

# Cargar el archivo Excel en un DataFrame
excel_file = r"C:\Users\fernando.tome\OneDrive - CASA HOSPITAL SAN JUAN DE DIOS\Escritorio\pRUEBA\prueba.xlsx"
df = pd.read_excel(excel_file)

# Función para formatear una fila en el formato deseado
def formatear_fila(row):
    # Obtener los valores de las columnas y formatearlos según las longitudes requeridas
    campo1 = str(row['Campo1']).ljust(18)  # Asegura que tenga una longitud de 18 caracteres
    campo2 = '{:.2f}'.format(float(row['Campo2'])).replace('.', ',').rjust(16)  # Formato con dos decimales, ',' como separador y longitud de 16 caracteres
    campo3 = '{:.2f}'.format(float(row['Campo3'])).replace('.', ',').rjust(16)
    campo4 = '{:.2f}'.format(float(row['Campo4'])).replace('.', ',').rjust(16)
    campo5 = str(row['Campo5']).rjust(8)
    campo6 = str(row['Campo6']).ljust(14)
    campo7 = str(row['Campo7']).ljust(24)

    # Combinar los campos en una sola línea
    linea_formateada = campo1 + campo2 + campo3 + campo4 + campo5 + campo6 + campo7

    return linea_formateada

# Aplicar la función de formateo a cada fila del DataFrame
formatted_data = df.apply(formatear_fila, axis=1)

# Ruta del archivo de salida (usando os.path.join para manejar rutas de manera segura)
output_file = os.path.join(r"C:\Users\fernando.tome\OneDrive - CASA HOSPITAL SAN JUAN DE DIOS\Escritorio\pRUEBA", "datos.txt")

# Escribir los datos formateados en un archivo de texto
with open(output_file, "w") as file:
    for row in formatted_data:
        file.write(row + "\n")

print(f"Los datos se han escrito en {output_file}")
