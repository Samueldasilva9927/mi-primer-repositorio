"""Genera un documento Word con los datos personales del usuario."""

from pathlib import Path

from docx import Document

CARPETA = Path(r"C:\IAGenerativa\Clase06_Ejercicio28")
SALIDA = CARPETA / "mis_datos.docx"

DATOS = [
    ("Nombre", "Samuel da silva"),
    ("DNI", "43331509"),
    ("Correo electrónico", "esamueldasilva9@gmail.com"),
    ("Usuario", "samueldasilva9927"),
]

doc = Document()
doc.add_heading("Mis datos", level=1)

tabla = doc.add_table(rows=len(DATOS), cols=2)
tabla.style = "Table Grid"
for fila, (campo, valor) in zip(tabla.rows, DATOS):
    fila.cells[0].text = campo
    fila.cells[1].text = valor
    for parrafo in fila.cells[0].paragraphs:
        for run in parrafo.runs:
            run.bold = True

doc.save(SALIDA)

# Verificación: se relee el archivo y se imprimen las celdas.
leido = Document(SALIDA)
print(f"Archivo generado: {SALIDA}")
print(f"Párrafos: {len(leido.paragraphs)}; tablas: {len(leido.tables)}")
for fila in leido.tables[0].rows:
    print(" | ".join(celda.text for celda in fila.cells))
