import tkinter as tk

# Inscribir bandas por categoría.
# Registrar puntajes por criterios. Registrar bandas con: nombre de la banda, institución y categoría.
# Listar bandas inscritas.
# Generar un ranking final.

class Banda_Participante:
  pass


class Banda_Escolar:
  def __init__(self, nombre, institucion, categoria):
    self.nombre = nombre
    self.institucion = institucion
    self.categoria = categoria

  # Listar bandas inscritas.
  def Listar_Bandas(self):
    return f"{self.nombre} - {self.institucion} - {self.categoria}"
  
  
# Inscribir banda : nombre de la banda, institución y categoría(Primaria, Basico, Diversificado).
class Inscribir_por_Categoria(Banda_Escolar) :
  pass


# Criterios de evaluación (0 a 10): ritmo, uniformidad, coreografía, alineación, puntualidad.
# Puntaje total = suma de criterios.
class Puntaje_por_Criterio(Banda_Escolar) :
  pass


# Retorna las bandas ordenadas por total y criterios de desempate.
class Generar_Ranking_Final(Banda_Escolar) :
  pass


class Consurso_Bandas:
  pass