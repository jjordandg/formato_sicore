import tkinter as tk

# Función para realizar cálculos
def calcular():
    num1 = float(entrada_num1.get())
    num2 = float(entrada_num2.get())
    resultado.set(num1 + num2)

# Crear una ventana
ventana = tk.Tk()
ventana.title("Calculadora")

# Variables de control
entrada_num1 = tk.Entry(ventana)
entrada_num2 = tk.Entry(ventana)
resultado = tk.StringVar()

# Etiquetas y botón
etiqueta_num1 = tk.Label(ventana, text="Número 1:")
etiqueta_num2 = tk.Label(ventana, text="Número 2:")
etiqueta_resultado = tk.Label(ventana, textvariable=resultado)
boton_calcular = tk.Button(ventana, text="Calcular", command=calcular)

# Colocar widgets en la ventana
etiqueta_num1.grid(row=0, column=0)
etiqueta_num2.grid(row=1, column=0)
etiqueta_resultado.grid(row=2, column=0, columnspan=2)
entrada_num1.grid(row=0, column=1)
entrada_num2.grid(row=1, column=1)
boton_calcular.grid(row=3, column=0, columnspan=2)

# Ejecutar el bucle principal
ventana.mainloop()
