Parámetros de estilo en Tkinter
1. Colores y fondo
  > • bg o background: color de fondo.
  • fg o foreground: color del texto.
  > • activebackground: color de fondo cuando el mouse está encima (solo algunos widgets).
  > • activeforeground: color del texto cuando el mouse está encima.
  > • disabledforeground: color del texto si está deshabilitado.
  > • highlightbackground: color del borde cuando el widget no tiene foco.
  > • highlightcolor: color del borde cuando el widget sí tiene foco.
  > • highlightthickness: grosor del borde de enfoque.


2. Texto y fuentes
  > • text: texto mostrado en el widget.
  > • font: fuente, tamaño y estilo. Ejemplo: ("Arial", 14, "bold italic").
  > • justify: alineación del texto (LEFT, CENTER, RIGHT).
  > • anchor: posición del texto dentro del widget (n, s, e, w, center).
  > • wraplength: ancho máximo en píxeles antes de saltar línea.


3. Bordes y relieve
  > • bd o borderwidth: grosor del borde.
  > • relief: estilo del borde (flat, raised, sunken, groove, ridge).


4. Dimensiones
  > • width: ancho (caracteres o píxeles, depende del widget).
  > • height: alto.
  > • padx, pady: espacio interno en X e Y.

5. Cursor y mouse
  > • cursor: forma del cursor (arrow, hand2, xterm, etc.).
  > • takefocus: si acepta foco al tabular (True / False).


6. Estado
  > • state: estado del widget. Opciones: "normal", "active", "disabled".


Actividad 18
La Municipalidad de Quetzaltenango organizará el concurso de bandas del desfile del 14 de septiembre. Se necesita un programa en Python, usando POO, que permita gestionar la inscripción y evaluación de bandas escolares.

■ OBJETIVO
• Implementar clases, herencia, encapsulación y polimorfismo para:

• Inscribir bandas por categoría.
• Registrar puntajes por criterios.
• Listar bandas inscritas.
• Generar un ranking final. retorna las bandas ordenadas por total y criterios de desempate.

■ REQUISITOS FUNCIONALES
• Registrar bandas con: nombre de la banda, institución y categoría.
• Categorías válidas: Primaria, Básico, Diversificado.
• Criterios de evaluación (0 a 10): ritmo, uniformidad, coreografía, alineación, puntualidad.
• Puntaje total = suma de criterios.

■ REQUISITOS TECNICOS DE POO
1. Clase base Participante con:
    • nombre 
    • institucion
    • método mostrar_info().

2. Clase BandaEscolar(Participante) con:
    • Atributos protegidos: _categoria y _puntajes.
    • Método set_categoria(categoria) que valide la categoría.
    • Método registrar_puntajes(diccionario) que valide criterios y rangos (0–10).
    • Propiedades total 
    • promedio.
    • Sobrescribe mostrar_info() para incluir la categoría y el total si ya fue evaluada.

3. Clase Concurso con:
    • inscribir_banda(banda) (no permitir dos bandas con el mismo nombre).
    • registrar_evaluacion(nombre_banda, puntajes).
    • listar_bandas() imprime todas las bandas y sus puntajes si ya fueron evaluadas.
    • ranking() retorna las bandas ordenadas por total y criterios de desempate.

■ FLUJO MINIMO EXIGIDO
• Crear tres bandas (una por cada categoría).
• Inscribirlas en el concurso.
• Registrar puntajes válidos para cada una.
• Mostrar listado general.
• Mostrar ranking final.

■ REGLAS DE VALIDACION
• Rechazar categoría inválida.
• Rechazar puntajes fuera de 0–10 o con criterios incompletos.
• No permitir bandas con el mismo nombre.

■ EJEMPLO DE INTERACCION (REFERENCIAL)
• Crear banda “Liceo Xela” (Básico), “Estrella Infantil” (Primaria), “Águilas del Occidente” (Diversificado).
• Inscribir en Concurso("Concurso de Bandas - 15 de Septiembre", "2025-09-15").
• Registrar puntajes para cada banda.
• Imprimir listar_bandas() y luego el ranking() mostrando: posición, nombre, institución, categoría y total.

