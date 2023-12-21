import tkinter as tk
from tkinter import filedialog
import pandas as pd

def seleccionar_archivo_entrada():
    archivo = filedialog.askopenfilename(filetypes=[("Archivos Excel", "*.xlsx")])
    entrada_excel.set(archivo)

def seleccionar_archivo_salida():
    archivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt")])
    salida_txt.set(archivo)

def generar_archivo_txt():
    archivo_entrada = entrada_excel.get()
    if archivo_entrada:
        archivo_salida = salida_txt.get()

        df = pd.read_excel(archivo_entrada)

        # El código de formateo y escritura del archivo que proporcionaste
        # ... (tu código original) ...

        with open(archivo_salida, "w") as file:
            for index, row in df.iterrows():
                espacios = ''
                i = 0
                while(i < 28 - len(str(row['Honorarios-brutos']).replace('"', '') + str(row['Cod-2']).replace('"', '')):
                    espacios+= ' '
                    i = i +1
                espacio_primer_bloque = espacios

                # Resto del código de formato y escritura
                # ...

        print(f"Los datos se han escrito en {archivo_salida}")
    else:
        print("Selecciona un archivo Excel antes de generar el archivo de texto.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Convertir Excel a Texto")

# Variables para almacenar las rutas de entrada y salida
entrada_excel = tk.StringVar()
salida_txt = tk.StringVar()

# Etiquetas y botones para seleccionar archivos
etiqueta_entrada = tk.Label(ventana, text="Seleccionar archivo Excel:")
etiqueta_salida = tk.Label(ventana, text="Guardar archivo de texto:")

boton_seleccionar_entrada = tk.Button(ventana, text="Seleccionar", command=seleccionar_archivo_entrada)
boton_seleccionar_salida = tk.Button(ventana, text="Seleccionar", command=seleccionar_archivo_salida)

boton_generar_txt = tk.Button(ventana, text="Generar archivo de texto", command=generar_archivo_txt)

# Campos de entrada para mostrar las rutas seleccionadas
entrada_ruta_entrada = tk.Entry(ventana, textvariable=entrada_excel, state="disabled")
entrada_ruta_salida = tk.Entry(ventana, textvariable=salida_txt, state="disabled")

# Colocar widgets en la ventana
etiqueta_entrada.grid(row=0, column=0)
etiqueta_salida.grid(row=1, column=0)

boton_seleccionar_entrada.grid(row=0, column=2)
boton_seleccionar_salida.grid(row=1, column=2)

entrada_ruta_entrada.grid(row=0, column=1)
entrada_ruta_salida.grid(row=1, column=1)

boton_generar_txt.grid(row=2, column=0, columnspan=3)

# Ejecutar la ventana
ventana.mainloop()
