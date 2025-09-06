# ================================
# Actividad 18 - Concurso de Bandas
# Municipalidad de Quetzaltenango
# Con manejo de archivos de texto
# ================================

import os, tkinter as tk

# -----------------
# Clase base
# -----------------
class Participante:
    def __init__(self, nombre, institucion):
        self.nombre = nombre
        self.institucion = institucion

    def mostrar_info(self):
        return f"{self.nombre} - {self.institucion}"


# -----------------
# Clase hija
# -----------------
class BandaEscolar(Participante):
    CATEGORIAS_VALIDAS = ["Primaria", "Básico", "Diversificado"]
    CRITERIOS_VALIDOS = ["ritmo", "uniformidad", "coreografía", "alineación", "puntualidad"]

    def __init__(self, nombre, institucion, categoria):
        super().__init__(nombre, institucion)
        self._categoria = None
        self._puntajes = {}
        self.set_categoria(categoria)

    # Validación de categoría
    def set_categoria(self, categoria):
        if categoria not in BandaEscolar.CATEGORIAS_VALIDAS:
            raise ValueError(f"Categoría inválida: {categoria}. Válidas: {BandaEscolar.CATEGORIAS_VALIDAS}")
        self._categoria = categoria

    # Registro de puntajes
    def registrar_puntajes(self, puntajes: dict):
        if set(puntajes.keys()) != set(BandaEscolar.CRITERIOS_VALIDOS):
            raise ValueError(f"Los criterios deben ser exactamente: {BandaEscolar.CRITERIOS_VALIDOS}")
        for criterio, valor in puntajes.items():
            if not (0 <= valor <= 10):
                raise ValueError(f"Puntaje inválido en {criterio}: {valor}. Debe estar entre 0 y 10.")
        self._puntajes = puntajes

    # Propiedades
    @property
    def total(self):
        return sum(self._puntajes.values()) if self._puntajes else 0

    @property
    def promedio(self):
        return self.total / len(self._puntajes) if self._puntajes else 0

    # Sobrescribe mostrar_info
    def mostrar_info(self):
        base = super().mostrar_info()
        if self._puntajes:
            return f"{base} , Categoría: {self._categoria} , Total: {self.total}"
        else:
            return f"{base} , Categoría: {self._categoria} , (sin evaluar)"

    # Serializar para archivo
    def to_line(self):
        # nombre,institucion,categoria,ritmo,uniformidad,coreografía,alineación,puntualidad
        puntajes_str = ",".join(str(self._puntajes.get(c, -1)) for c in BandaEscolar.CRITERIOS_VALIDOS)
        return f"{self.nombre},{self.institucion},{self._categoria},{puntajes_str}"

    @staticmethod
    def from_line(linea):
        partes = linea.strip().split(",")
        if len(partes) != 8:
            return None
        nombre, institucion, categoria = partes[:3]
        puntajes = partes[3:]
        banda = BandaEscolar(nombre, institucion, categoria)
        if puntajes[0] != "-1":  # ya tiene puntajes
            puntajes_dict = {c: int(p) for c, p in zip(BandaEscolar.CRITERIOS_VALIDOS, puntajes)}
            banda.registrar_puntajes(puntajes_dict)
        return banda


# -----------------
# Clase Concurso
# -----------------
class Concurso:
    def __init__(self, nombre='', fecha="", archivo="bandas.txt"):
        self.nombre = nombre
        self.fecha = fecha
        self._bandas = {}
        self.archivo = archivo
        self.cargar_desde_archivo()

    def inscribir_banda(self, banda: BandaEscolar):
        if banda.nombre in self._bandas:
            raise ValueError(f"Ya existe una banda inscrita con el nombre '{banda.nombre}'")
        self._bandas[banda.nombre] = banda
        self.guardar_en_archivo()

    def registrar_evaluacion(self, nombre_banda, puntajes):
        if nombre_banda not in self._bandas:
            raise ValueError(f"No existe la banda '{nombre_banda}' en el concurso.")
        self._bandas[nombre_banda].registrar_puntajes(puntajes)
        self.guardar_en_archivo()

    def listar_bandas(self):
        bienvenida = tk.Label(ventana, text=f"\n=== Bandas Inscritas ===", font=("consolas", 14, "bold"))
        bienvenida.pack(pady=5)
        for banda in self._bandas.values():
            info = tk.Label(ventana, text=banda.mostrar_info(), font=("consolas", 12))
            info.config(fg="#4b2292" if banda.total > 0 else "white")
            info.pack(pady=5)

    def ranking(self):
        bandas_evaluadas = [b for b in self._bandas.values() if b.total > 0]
        ordenadas = sorted(bandas_evaluadas, key=lambda b: (b.total, b.promedio), reverse=True)

        print(f"\n=== Ranking Final {self.nombre} ===")
        for i, banda in enumerate(ordenadas, start=1):
            print(f"{i}. {banda.nombre} - {banda.institucion} "
                  f"({banda._categoria}) | Total: {banda.total}")

    # --- Manejo de archivos ---
    def guardar_en_archivo(self):
        with open(self.archivo, "w", encoding="utf-8") as f:
            for banda in self._bandas.values():
                f.write(banda.to_line() + "\n")

    def cargar_desde_archivo(self):
        if not os.path.exists(self.archivo):
            return
        with open(self.archivo, "r", encoding="utf-8") as f:
            for linea in f:
                banda = BandaEscolar.from_line(linea)
                if banda:
                    self._bandas[banda.nombre] = banda


# -----------------
# FLUJO MÍNIMO
# -----------------
# if __name__ == "__main__":
#     concurso = Concurso("Concurso de Bandas - 15 de Septiembre", "2025-09-15")

#     # Si el archivo está vacío, registrar bandas iniciales
#     if not concurso._bandas:
#         banda1 = BandaEscolar("Estrella Infantil", "Colegio Luz", "Primaria")
#         banda2 = BandaEscolar("Liceo Xela", "Instituto Xela", "Básico")
#         banda3 = BandaEscolar("Águilas del Occidente", "Colegio Occidente", "Diversificado")

#         concurso.inscribir_banda(banda1)
#         concurso.inscribir_banda(banda2)
#         concurso.inscribir_banda(banda3)

#         puntajes1 = {"ritmo": 8, "uniformidad": 9, "coreografía": 7, "alineación": 8, "puntualidad": 10}
#         puntajes2 = {"ritmo": 9, "uniformidad": 8, "coreografía": 8, "alineación": 9, "puntualidad": 9}
#         puntajes3 = {"ritmo": 10, "uniformidad": 9, "coreografía": 9, "alineación": 9, "puntualidad": 8}

#         concurso.registrar_evaluacion("Estrella Infantil", puntajes1)
#         concurso.registrar_evaluacion("Liceo Xela", puntajes2)
#         concurso.registrar_evaluacion("Águilas del Occidente", puntajes3)

#     # Mostrar resultados (desde archivo o memoria)
#     concurso.listar_bandas()
#     concurso.ranking()


import tkinter as tk

ventana = tk.Tk()
ventana.title("Concurso de Bandas - Quetzaltenango")
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

concurso = Concurso()
inscribir_banda = tk.Button(ventana, text="Inscribir Banda", font=("Arial", 14), command=inscribir) # Inscribir Banda
inscribir_banda.pack(pady=5)
registrar_evaluacion = tk.Button(ventana, text="Registrar Evaluación", font=("Arial", 14), ) # Registrar Evaluación
registrar_evaluacion.pack(pady=5)
listar_bandas = tk.Button(ventana, text="Listar Bandas", font=("Arial", 14), command=concurso.listar_bandas) # Listar Bandas
listar_bandas.pack(pady=5)
generar_ranking = tk.Button(ventana, text="Generar Ranking Final", font=("Arial", 14)) # Generar Ranking Final
generar_ranking.pack(pady=5)
cancelar = tk.Button(ventana, text="Cancelar", font=("Arial", 14), command=cancelar) # Cancelar
cancelar.pack(pady=5)
salir = tk.Button(ventana, text="Salir", font=("Arial", 14), command=ventana.quit) # Salir
salir.pack(pady=5)


ventana.mainloop()