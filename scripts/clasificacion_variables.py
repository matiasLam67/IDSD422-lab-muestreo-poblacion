# Clasificacion_variables.py — Parte A: clasificación de las variables de clientes.csv.
#
# El archivo data/clientes.csv tiene 12 clientes y 7 variables (más el id).
# El objetivo: clasificar cada variable (numérica continua/discreta, categórica
# binaria/ordinal/nominal) y verificar la clasificación en código.
#
# Regla del capítulo 3: el dtype es una pista, no la clasificación — el criterio
# (¿tiene sentido la mitad del valor? ¿hay orden entre las categorías?) decide.
#
# Uso (desde la raíz del repositorio):  python scripts/clasificacion_variables.py

import pandas as pd

clientes = pd.read_csv("../data/clientes.csv")
a,b = clientes.shape

# ---------------------------------------------------------------------------
# 1. Estructura del archivo
# ---------------------------------------------------------------------------
print(f"Dimensiones: {a} filas × {b} columnas\n")
print("Primeras filas:")
print(clientes.to_string(index=False)+"\n")

# ---------------------------------------------------------------------------
# 2. Tipos inferidos (dtype) — la pista que da el lenguaje
# ---------------------------------------------------------------------------
print("Tipos inferidos (dtype):")
print(clientes.dtypes)
print()
# TODO 1: ¿qué columnas llegan como número y cuáles como texto? Anótalo para el
#         informe. Ojo con satisfaccion: llega como número y es ordinal
#         ("4 no es el doble de 2") — la justificación va en el informe.

# ---------------------------------------------------------------------------
# 3. Valores únicos — ¿cuántas categorías hay y cuáles son?
# ---------------------------------------------------------------------------
# TODO 2: completa el bucle para imprimir, por columna, cuántos valores únicos
#         hay y cuáles son. Pista: for columna in clientes.columns: ...  con
#         clientes[columna].unique() y len(). ¿Cuántas categorías tiene genero?

for columna in clientes.columns:
    unicos=clientes[columna].unique()
    cantidad=len(unicos)
    print(f"Columna {columna}: {cantidad} valores únicos -> {unicos}\n")

# ---------------------------------------------------------------------------
# 4. Declarar el orden de las variables ordinales

# ---------------------------------------------------------------------------
# Una ordinal se guarda como texto (o como número) y su orden natural se pierde:
# alfabéticamente "Posgrado" iría antes que "Primaria", que no tiene sentido.
#
# TODO 3: convierte nivel_educacion a categoría ordenada.
#         Pista: astype(pd.CategoricalDtype(categories=[...], ordered=True)).
#         Comprueba con .min(): debe devolver "Primaria".

educacion_orden=clientes["nivel_educacion"].astype(pd.CategoricalDtype(categories=["Primaria","Secundaria","Universidad","Posgrado"], ordered=True))
print("Primer nivel del orden: "+educacion_orden.max())
print("Ultimo nivel del orden: "+educacion_orden.min())

# TODO 4: haz lo mismo con satisfaccion (escala 1–5 como etiquetas ordenadas).
#         Prueba extra: ¿qué pasa si en la lista de categorías escribes
#         "Postgrado" (con t) para nivel_educacion? Cuenta los faltantes con
#         .isna().sum() — la trampa del typo es silenciosa.
print()
satisfaccion_orden=clientes["satisfaccion"].astype(pd.CategoricalDtype(categories=[1,2,3,4,5], ordered=True))
print("Ultimo valor del orden: "+ str(satisfaccion_orden.min()))
# ---------------------------------------------------------------------------
# 5. Resumen de la clasificación (para el informe)
# ---------------------------------------------------------------------------
# TODO 5: completa el resumen con el tipo de cada variable (el criterio que
#         justifica cada clasificación va en el informe).
clasificacion = {
    "cliente_id": "Cualitativa nominal",
    "edad": "Cuantitativa continua",
    "numero_hijos": "Cuantitativa discreta",
    "genero": "Cualitativa nominal",
    "nivel_educacion": "Cualitativa ordinal",
    "ciudad": "Cualitativa nominal",
    "ingresos_mensuales": "Cuantitativa continua",
    "satisfaccion": "Cualitativa ordinal",
}
print("Resumen de la clasificación (para el informe):")
for variable, tipo in clasificacion.items():
    print(f"  {variable:20s} {tipo}")
