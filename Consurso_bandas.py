import os
import tkinter as tk

# Inscribir bandas por categoría.
# Registrar puntajes por criterios. Registrar bandas con: nombre de la banda, institución y categoría.
# Listar bandas inscritas.
# Generar un ranking final.

# Nombre de la banda, institución(Primaria, Básico, Diversificado).
class Banda_Participante:
  @property
  def nombre(self):
    return self.__nombre

  @property
  def institucion(self):
    return self.__institucion
  def __init__(self, nombre, institucion):
    self.__nombre = nombre
    self.__institucion = institucion

  def mostrar_info(self):
    return (
      f'>Banda Participante : '
      f'Nombre: {self.nombre}'
      f'Institución: {self.institucion}'
    )


class Banda_Escolar(Banda_Participante):
  def __init__(self, nombre, institucion, categoria):
    super().__init__(nombre, institucion)
    self.__categoria = None # Primaria, Básico, Diversificado
    self.__puntajes = {}
    self.set_categoria(categoria)

  
  # Validar categoría : Primaria, Básico, Diversificado
  def Set_Categoria(self, categoria):
    categoria_aux = True if categoria in ['Primaria', 'Basico', 'Diversificado'] else False
    if categoria_aux :
      self.__categoria = categoria
      return self.__categoria
    else :
      print('Categoría inválida. Debe ser Primaria, Básico o Diversificado.')
      return None
  
  
  # Criterios de evaluación (0 a 10): 
  # • ritmo,
  # • uniformidad, 
  # • coreografía, 
  # • alineación, 
  # • puntualidad.
  # Puntaje total = suma de criterios.
  def Registrar_Puntaje(self, puntaje):
    if 0 <= puntaje <= 10:
      self.__puntajes.append(puntaje)
    else:
      return None
      # return None
  
  
  # Propiedades total y promedio.
  def Total_Puntaje(self):
    return sum(self.__puntajes)


  # Promedio de puntajes.
  def Promedio_Puntaje(self):
    if len(self.__puntajes) == 0:
      return 0
    return sum(self.__puntajes) / len(self.__puntajes)


  def Mostrar_Info(self):
    info = super().Mostrar_Info()
    info += f'Categoría: {self.__categoria}\n'
    info += f'Total Puntaje: {self.Total_Puntaje()}\n' if self.__puntajes else 'No evaluada aún.\n'
    return info


class Consurso_Bandas(Banda_Escolar):
  def __init__(self):
    self.bandas = {}
    
  def Inscribir_Banda(self, banda: Banda_Escolar):
    if banda.nombre not in self.bandas:
      self.bandas[banda.nombre] = banda
      print(f'Banda {banda.nombre} inscrita exitosamente.')
  
  
   # Criterios de evaluación (0 a 10): 
  # • ritmo,
  # • uniformidad, 
  # • coreografía, 
  # • alineación, 
  # • puntualidad.
  # Puntaje total = suma de criterios.
  def Registrar_Evaluacion(self, nombre_banda, puntajes):
    while True:
      Banda_Escolar.Limpiar()
      print('Criterios de evaluación (0 a 10) : ')
      ritmo = int(input('• Ritmo : '))
      if 0 <= ritmo <= 10:
        Banda_Escolar.Registrar_Puntaje(ritmo)
        break

    while True:
      Banda_Escolar.Limpiar()
      print('Criterios de evaluación (0 a 10) : ')
      uniformidad = int(input('• Uniformidad : '))
      if 0 <= uniformidad <= 10:
        Banda_Escolar.Registrar_Puntaje(uniformidad)
        break
    while True:
      Banda_Escolar.Limpiar()
      print('Criterios de evaluación (0 a 10) : ')
      coreografia = int(input('• Coreografía : '))
      if 0 <= coreografia <= 10:
        Banda_Escolar.Registrar_Puntaje(coreografia)
        break
    while True:
      Banda_Escolar.Limpiar()
      print('Criterios de evaluación (0 a 10) : ')
      alineacion = int(input('• Alineación : '))
      if 0 <= alineacion <= 10:
        Banda_Escolar.Registrar_Puntaje(alineacion)
        break
    while True:
      Banda_Escolar.Limpiar()
      print('Criterios de evaluación (0 a 10) : ')
      puntualidad = int(input('• Puntualidad : '))
      if 0 <= puntualidad <= 10:
        Banda_Escolar.Registrar_Puntaje(puntualidad)
        break


  # Listar bandas inscritas.
  def Listar_Bandas(self):
    with open('bandas_inscritas.txt', 'r') as file:
      for line in file:
        campos = line.strip().split(',')
        print(f'Nombre : {campos[0]}')
        print(f'Institución : {campos[1]}')
        print(f'Categoría : {campos[2]}')


  def Generar_Ranking_Final():
    pass

# Inscribir banda por categoria : nombre de la banda, institución.
  def Inscribir_por_Categoria(self, categoria) :
    self.__categoria = Banda_Escolar.set_categoria(categoria)
    bandera = False
    with open('bandas_inscritas.txt', 'r') as file:
      for line in file:
        campos = line.strip().split(',')
        if self.nombre == campos[0] :
          bandera = True
          print('La banda ya está inscrita.')
          break
        
      if not bandera :
        with open('bandas_inscritas.txt', 'a') as file:
          file.write(f'{self.nombre},{self.institucion},{self.__categoria}\n')
          print('Banda inscrita exitosamente.')

  def Limpiar() :
    os.system('cls' if os.name == 'nt' else 'clear')