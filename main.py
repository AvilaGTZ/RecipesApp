from GEN_Recetario import *
from ModeloRecetas import *
from PeticionRecetas import *
from tkinter import *
from tkinter import messagebox





def Empieza(Nombre_recetario, Numero_recetas):
    
    try:
        Numero_verificar = int(Numero_recetas.get())
        
        if Numero_verificar <= 0:
            messagebox.showerror("Error de informacion", "El numero de recetas debe ser mayor a cero")
            return
    except:
        messagebox.showerror("Error de informacion", "El valor ingresado para numero de recetas no es numerico")
        return
    
    Nombre_recetario_extraido  = Nombre_recetario.get().strip()
    if Nombre_recetario_extraido == "":
        messagebox.showerror("Error de informacion", "Debe ingresar un nombre para el recetario")
        return
    
    print("El nombre ingresado para el recetario es: " + Nombre_recetario.get())
    print("El numero de recetas deseadas es: " + Numero_recetas.get())
    
    Recetas           = Obtener_recetas(int(Numero_recetas.get()))

    Mensaje_estado, Recetas_modeladas = Genera_Modelo_Recetas(Recetas)
    if Mensaje_estado != "OK":
        print(Mensaje_estado)
        
    Mensaje_estado = Generar_recetario_excel(Recetas_modeladas, Nombre_recetario.get())
    if Mensaje_estado != "OK":
        print(Mensaje_estado)

Ventana_principal = Tk()
Ventana_principal.geometry("400x120")
Ventana_principal.title("Mi generador de recetas")

Etiqueta_Nombre_Recetario = Label(Ventana_principal, text =  "Nombre recetario")
Etiqueta_Nombre_Recetario.place(x = 10, y = 10)

NombreRecetario = StringVar()
Entrada_Nombre_Recetario = Entry(Ventana_principal, width = 40, textvariable = NombreRecetario)
Entrada_Nombre_Recetario.place(x = 130, y = 10)

Etiqueta_Numero_recetas   = Label(Ventana_principal, text = "Numero de recetas")
Etiqueta_Numero_recetas.place(x = 10, y = 40)

NumeroRecetas = StringVar()
Entrada_Numero_recetas = Entry(Ventana_principal, width = 40, textvariable = NumeroRecetas)
Entrada_Numero_recetas.place(x = 130, y = 40)

Boton_generar = Button(Ventana_principal, text = "GEN Recetario!", height = 2, width = 15, command = lambda: Empieza(NombreRecetario, NumeroRecetas))
Boton_generar.place(x = 260, y = 70)



Ventana_principal.mainloop()
