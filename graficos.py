import tkinter as tk

ventana = tk.Tk()
ventana.title("Concurso de Bandas Escolares")
ancho = ventana.winfo_screenwidth()
alto = ventana.winfo_screenheight()
ventana.geometry(f"{ancho}x{alto}")


def inscribir():
  global entrada_banda, entrada_institucion, entrada_categoria
  nombre_de_banda = tk.Label(ventana, text="Nombre de la Banda:", font=("Arial", 12))
  nombre_de_banda.pack(pady=5)
  entrada_banda = tk.Entry(ventana)
  entrada_banda.pack(pady=5)
  nombre_de_institucion = tk.Label(ventana, text="Nombre de la Institución:", font=("Arial", 12))
  nombre_de_institucion.pack(pady=5)
  entrada_institucion = tk.Entry(ventana)
  entrada_institucion.pack(pady=5)
  nombre_de_categoria = tk.Label(ventana, text="Nombre de la Categoría:", font=("Arial", 12))
  nombre_de_categoria.pack(pady=5)
  entrada_categoria = tk.Entry(ventana)
  entrada_categoria.pack(pady=5)
  
  
def registrar_evaluacion():
  global entrada_banda, entrada_alineacion, entrada_ritmo, entrada_uniformidad, entrada_puntualidad
  nombre_de_banda = tk.Label(ventana, text="Nombre de la Banda:", font=("Arial", 12))
  nombre_de_banda.pack(pady=5)
  entrada_banda = tk.Entry(ventana)
  entrada_banda.pack(pady=5)
  puntaje_alineacion = tk.Label(ventana, text="Puntaje de Alineación (0-10):", font=("Arial", 12))
  puntaje_alineacion.pack(pady=5)
  entrada_alineacion = tk.Entry(ventana)
  entrada_alineacion.pack(pady=5)
  puntaje_ritmo = tk.Label(ventana, text="Puntaje de Ritmo (0-10):", font=("Arial", 12))
  puntaje_ritmo.pack(pady=5)
  entrada_ritmo = tk.Entry(ventana)
  entrada_ritmo.pack(pady=5)
  puntaje_uniformidad = tk.Label(ventana, text="Puntaje de Uniformidad (0-10):", font=("Arial", 12))
  puntaje_uniformidad.pack(pady=5)
  entrada_uniformidad = tk.Entry(ventana)
  entrada_uniformidad.pack(pady=5)
  puntaje_puntualidad = tk.Label(ventana, text="Puntaje de Puntualidad (0-10):", font=("Arial", 12))
  puntaje_puntualidad.pack(pady=5)
  entrada_puntualidad = tk.Entry(ventana)
  entrada_puntualidad.pack(pady=5)


def cancelar():
  # Buscar y destruir todos los widgets hijos de la ventana excepto los botones principales
  for widget in ventana.winfo_children():
    if isinstance(widget, tk.Entry) or isinstance(widget, tk.Label):
      widget.destroy()


def salir():
  ventana.quit()

inscribir_banda = tk.Button(ventana, text="Inscribir Banda", font=("Arial", 14), command=inscribir) # Inscribir Banda
inscribir_banda.pack(pady=5)
registrar_evaluacion = tk.Button(ventana, text="Registrar Evaluación", font=("Arial", 14), command=Concurso.registrar_evaluacion) # Registrar Evaluación
registrar_evaluacion.pack(pady=5)
listar_bandas = tk.Button(ventana, text="Listar Bandas", font=("Arial", 14), command=Concurso.listar_bandas) # Listar Bandas
listar_bandas.pack(pady=5)
generar_ranking = tk.Button(ventana, text="Generar Ranking Final", font=("Arial", 14), command=Concurso.ranking) # Generar Ranking Final
generar_ranking.pack(pady=5)
cancelar = tk.Button(ventana, text="Cancelar", font=("Arial", 14), command=cancelar) # Cancelar
cancelar.pack(pady=5)
salir = tk.Button(ventana, text="Salir", font=("Arial", 14), command=ventana.quit) # Salir
salir.pack(pady=5)


ventana.mainloop()