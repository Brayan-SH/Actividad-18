Parámetros de estilo en Tkinter
1. Colores y fondo
  • bg o background: color de fondo.
  • fg o foreground: color del texto.
  • activebackground: color de fondo cuando el mouse está encima (solo algunos widgets).
  • activeforeground: color del texto cuando el mouse está encima.
  • disabledforeground: color del texto si está deshabilitado.
  • highlightbackground: color del borde cuando el widget no tiene foco.
  • highlightcolor: color del borde cuando el widget sí tiene foco.
  • highlightthickness: grosor del borde de enfoque.


2. Texto y fuentes
  • text: texto mostrado en el widget.
  • font: fuente, tamaño y estilo. Ejemplo: ("Arial", 14, "bold italic").
  • justify: alineación del texto (LEFT, CENTER, RIGHT).
  • anchor: posición del texto dentro del widget (n, s, e, w, center).
  • wraplength: ancho máximo en píxeles antes de saltar línea.


3. Bordes y relieve
  • bd o borderwidth: grosor del borde.
  • relief: estilo del borde (flat, raised, sunken, groove, ridge).


4. Dimensiones
  • width: ancho (caracteres o píxeles, depende del widget).
  • height: alto.
  • padx, pady: espacio interno en X e Y.
5. Cursor y mouse


  • cursor: forma del cursor (arrow, hand2, xterm, etc.).
  • takefocus: si acepta foco al tabular (True / False).


6. Estado
state: estado del widget. Opciones: "normal", "active", "disabled".