# muestreo.py — Parte B: población vs. muestra (RetailAndina).
#
# La población es la base completa de fidelización: data/clientes_400.csv (N = 400).
# La pregunta de negocio: ¿cuál es el ingreso mensual promedio de los clientes?
# Se estima con tres diseños de muestreo y se compara cada estimación con el
# parámetro real, que aquí sí se conoce porque la población es pequeña y visible.
#
# Uso (desde la raíz del repositorio):  python scripts/muestreo.py

from pathlib import Path
import pandas as pd

pd.set_option("display.width", 100)


def reporte(nombre, muestra, parametro):
    """Imprime n, media estimada y composición por ciudad de una muestra.

    Composición por ciudad: es la pista que delata un sesgo de selección.
    """
    if muestra is None:
        print(f"[{nombre}] pendiente de completar (TODO)")
        return
    n = len(muestra)
    media = muestra["ingresos_mensuales"].mean()
    comp = muestra["ciudad"].value_counts().to_dict()
    print(f"{nombre} n={n}  media={media:.2f} USD "
          f"(parámetro {parametro:.2f}, diferencia {media - parametro:+.2f})")
    print(f"    composición por ciudad: {comp}")


# ---------------------------------------------------------------------------
# 1. La población y su parámetro (N = 400)
# ---------------------------------------------------------------------------
# Cargar la población desde la ruta dinámicamente respecto a la carpeta del script
BASE_DIR = Path(__file__).resolve().parent.parent
RUTA_CSV = BASE_DIR / "data" / "clientes_400.csv"

poblacion = pd.read_csv(RUTA_CSV)
parametro = poblacion["ingresos_mensuales"].mean()
print(f"Población: {poblacion.shape[0]} clientes × {poblacion.shape[1]} columnas")
print(f"Parámetro poblacional — ingreso medio: {parametro:.2f} USD")
print("Ciudades en la población:", poblacion["ciudad"].value_counts().to_dict())
print()

# ---------------------------------------------------------------------------
# 2. Muestra por conveniencia: "los primeros que llegaron"
# ---------------------------------------------------------------------------
# TODO 1: toma como muestra las primeras 20 filas de la población.
muestra_conv = poblacion.head(20)

# ---------------------------------------------------------------------------
# 3. Muestra aleatoria simple: el sorteo de 20
# ---------------------------------------------------------------------------
# TODO 2: sortea 20 clientes con la misma probabilidad para todos (20/400 = 5 %).
muestra_aas = poblacion.sample(20, random_state=1)

# TODO 3: repite el sorteo con las semillas 2 a 5 para evaluar la variabilidad.
print("--- TODO 3: Variabilidad de la muestra aleatoria simple (Semillas 1 a 5) ---")
for semilla in range(1, 6):
    m_temp = poblacion.sample(20, random_state=semilla)
    media_temp = m_temp["ingresos_mensuales"].mean()
    print(f"  Semilla {semilla}: Media estimada = {media_temp:.2f} USD (Dif: {media_temp - parametro:+.2f})")
print("-" * 75 + "\n")

# ---------------------------------------------------------------------------
# 4. Muestra estratificada: 5 % dentro de cada ciudad
# ---------------------------------------------------------------------------
# TODO 4: muestrea dentro de cada ciudad (el estrato) con afijación proporcional (5 %).
muestra_est = poblacion.groupby("ciudad", group_keys=False).apply(
    lambda x: x.sample(frac=0.05, random_state=1)
)

# ---------------------------------------------------------------------------
# 5. Comparación final
# ---------------------------------------------------------------------------
reporte("Conveniencia", muestra_conv, parametro)
reporte("Aleatorio simple", muestra_aas, parametro)
reporte("Estratificado", muestra_est, parametro)
print()

if muestra_conv is not None and muestra_aas is not None and muestra_est is not None:
    resumen = pd.DataFrame([
        {"diseño": "Conveniencia (head)", "n": len(muestra_conv),
         "media estimada": round(muestra_conv["ingresos_mensuales"].mean(), 2)},
        {"diseño": "Aleatorio simple (sample)", "n": len(muestra_aas),
         "media estimada": round(muestra_aas["ingresos_mensuales"].mean(), 2)},
        {"diseño": "Estratificado (groupby + frac)", "n": len(muestra_est),
         "media estimada": round(muestra_est["ingresos_mensuales"].mean(), 2)},
    ])
    print(f"Parámetro poblacional: {parametro:.2f} USD")
    print(resumen.to_string(index=False))
    print()
    print("Con estas salidas responde en informe.md las preguntas P2 a P5:")
    print("  P2: ¿cuál diseño quedó más cerca del parámetro y por qué un solo")
    print("      número no basta para declarar un ganador?")
    print("  P3: ¿qué defecto tiene la muestra por conveniencia y cómo lo delata")
    print("      su composición por ciudad? ¿Se corrige con más filas?")
    print("  P4: ¿qué implica la variabilidad entre semillas para una decisión")
    print("      tomada con un solo estudio?")
    print("  P5: ¿cuándo usarías cada diseño? (piloto · subgrupos · conclusión)")
else:
    print("Completa los TODO 1 a 4 para ver la tabla comparativa.")