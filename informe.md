# Informe — Clasificación de variables y población vs. muestra

<div style="display: flex; justify-content: space-between; gap: 20px;">
  <div>
    <p><strong>Para:</strong> Gerencia de RetailAndina S.A.</p>
    <p><strong>Fecha:</strong> 23/10/2026</p>
  </div>
  <div>
    <p><strong>De:</strong> Equipo de Business Intelligence</p>
    <p><strong>Asunto:</strong> Base de fidelización: tipos de variables y estimación por muestreo</p>
  </div>
</div>

---

## Resumen ejecutivo

**Para:** Gerencia de RetailAndina S.A.  
**De:** Equipo de Business Intelligence  
**Fecha:** 23/10/2026  
**Asunto:** Resumen ejecutivo — Clasificación de datos y estimación de ingresos por muestreo  

Estimada Gerencia,

Evaluamos la base de fidelización clasificando sus variables 
(demográficas, ordinales y monetarias) e inferimos el ingreso 
mensual promedio de los clientes mediante muestras de $n=20$ bajo 
tres diseños: conveniencia, aleatorio simple y estratificado por 
ciudad. Demostramos que la conveniencia sesga los resultados 
(excluyendo ciudades completas) y que la selección aleatoria 
presenta variabilidad entre intentos, por lo que la gerencia no debe 
tomar decisiones estratégicas basadas en un único valor puntual sin 
auditoría de representatividad e intervalos de confianza.

*-Equipo de Business Intelligence-*

## Parte A — Clasificación de las variables

*Completa la tabla usando el **criterio** (¿tiene sentido la mitad del valor? ¿hay orden entre las categorías?), no el ejemplo. En «verificación» anota qué mostró el código: dtype, número de valores únicos y, si declaraste el orden, cómo lo comprobaste.*

| Variable             | Tipo                  | Justificación (criterio)                                                                                                           | Verificación en código      |
|----------------------|-----------------------|------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|
| `cliente_id`         | Cualitativa nominal   | Identificador único alfanumérico; no representa una cantidad ni tiene un orden implícito, tampoco sirve para realizar operaciones. | `object`, 12 valores únicos |
| `edad`               | Cuantitativa continua | Representa tiempo; aunque en el dataset aparezca registrada en números enteros, el tiempo es continuo.                             | `int64`, 12 valores únicos  |
| `numero_hijos`       | Cuantitativa discreta | Conteo; toma valores enteros finitos y no admite valores decimales.                                                                | `int64`, 5 valores únicos   |
| `genero`             | Cualitativa nominal   | Categorías sin relación de orden jerárquico entre sí.                                                                              | `object`, 3 valores únicos  |
| `nivel_educacion`    | Cualitativa ordinal   | Grados académicos con una jerarquía clara e implícita.                                                                             | `object`, 4 valores únicos  |
| `ciudad`             | Cualitativa nominal   | Ubicación geográfica; sin orden implícito.                                                                                         | `object`, 3 valores únicos  |
| `ingresos_mensuales` | Cuantitativa continua | Variable monetaria; aunque figure en valores enteros, el dinero representa una escala continua.                                    | `int64`, 12 valores únicos  |
| `satisfaccion`       | Cualitativa ordinal   | Escala de nivel de satisfacción; tiene jerarquía implícita, pese a estar codificada  numéricamente.                                | `int64`, 4 valores únicos   |

**P1.** ¿Qué te dijo el dtype de `satisfaccion` y por qué no basta para clasificarla? ¿Qué pasa si una ordinal queda como texto sin declarar el orden?

>  El valor `int64` indica que Python procesa dicha columna como 
> números enteros (2, 3, 4, 5). Sin embargo, este formato es 
> insuficiente para clasificarla, ya que los tipos de datos 
> computacionales (`int64`, `float64`, `object`) describen cómo se 
> almacena la información técnicamente y no la esencia real de la 
> variable. Puesto que estos números reflejan una ***escala Likert*** de 
> percepción o satisfacción, se trata, desde una perspectiva 
> conceptual, de una variable cualitativa ordinal.

## Parte B — Población vs. muestra

### La población y su parámetro

| Concepto                      |       Valor        |
|-------------------------------|:------------------:|
| Población (N)                 |        200         |
| Variable de interés           | ingresos mensuales |
| Parámetro poblacional (media) |    1330.72 USD     |

**¿Por qué se muestrea si aquí el parámetro existe y se calculó?**


### Los tres diseños

*Corre tu script y registra las salidas. La composición por ciudad es la que delata el sesgo: anótala tal como salió.*

| Diseño                          | n  | Media estimada |             Composición por ciudad             | Diferencia vs. parámetro |
|---------------------------------|----|----------------|:----------------------------------------------:|:------------------------:|
| Conveniencia  (`head`)          | 20 | 1348.50        |                   `Quito:20`                   |          +17.78          |
| Aleatorio simple (`sample`)     | 20 | 1336.00        | `Cuenca: 8`<br/>`Quito: 8`<br/>`Guayaquil: 4`  |          +5.28           |
| Estratificado (`groupby` + 5 %) | 20 | 1212.50        | `Cuenca: 10`<br/>`Quito: 6`<br/>`Guayaquil: 4` |         -118.22          |

*Anota también las medias de 5 sorteos distintos del aleatorio simple (semillas 1 a 5):*

| Semilla     | 1       | 2       | 3       | 4       | 5       |
|-------------|---------|---------|---------|---------|---------|
| Media (USD) | 1336.00 | 1405.00 | 1235.00 | 1491.00 | 1288.00 |

**P2. ¿Cuánto vale el parámetro poblacional y cuánto estimó cada diseño? ¿Cuál quedó más cerca y por qué eso no alcanza para declarar un ganador?**  
El parámetro poblacional es **1330.72 USD**. Las estimaciones fueron:
* **Conveniencia:** 1348.50 USD (Dif: +17.78)
* **Aleatorio Simple (Semilla 1):** 1336.00 USD (Dif: +5.28)
* **Estratificado:** 1212.50 USD (Dif: -118.22)

En este intento puntual, el **Aleatorio Simple** quedó más cerca del valor real (+5.28 USD). Sin embargo, esto **no alcanza para declararlo un ganador** porque una sola muestra está sujeta al azar (variabilidad muestral). Como se observa al cambiar la semilla en el muestreo aleatorio simple, el resultado oscila fuertemente entre 1235.00 USD y 1491.50 USD. Aunque el diseño estratificado dio un valor más alejado en esta ejecución concreta debido al tamaño pequeño de muestra ($n=20$), teóricamente es el diseño con menor varianza estructural a largo plazo.

**P3. La muestra por conveniencia también tiene 20 filas. ¿Qué defecto tiene y cómo lo delatas en la composición por ciudad? ¿Se corrige tomando más filas?**   

El defecto principal es el **sesgo de selección** (falta de representatividad). Se delata claramente en la composición por ciudad: la muestra contiene **100 % clientes de Quito (`{'Quito': 20}`)**, excluyendo por completo a Guayaquil y Cuenca.  
**No se corrige tomando más filas** si se mantiene el mismo método de selección (tomar los primeros de la lista); aumentar el tamaño muestral bajo este criterio solo recolectará más datos con el mismo sesgo de origen.

**P4. El sorteo aleatorio dio un número distinto en cada semilla. ¿Qué implica esa variabilidad para una empresa que va a decidir con un solo estudio?**  

Implica que una estimación puntual derivada de una sola muestra conlleva un nivel de incertidumbre (error muestral) que depende del azar. Si la empresa toma una decisión financiera basándose únicamente en el resultado de un estudio (por ejemplo, proyectando ingresos con la Semilla 4 a $1491.50$ USD vs. la Semilla 3 a $1235.00$ USD), corre el riesgo de sobreestimar o subestimar la realidad. Por lo tanto, las decisiones de negocio no deben tomarse con una media única sin antes calcular **intervalos de confianza** o medir la variabilidad de la estimación.

**P5. ¿Cuándo usarías cada diseño en la práctica?**

* **Muestreo por Conveniencia:** Útil para exploraciones preliminares, pruebas técnicas rápidas o **estudios piloto** donde la prioridad es la velocidad y el bajo costo, sin pretender extrapolar los resultados a toda la población.
* **Muestreo Estratificado:** Recomendado cuando la población tiene **subgrupos (estratos) heterogéneos bien definidos que deben aparecer representados** en su justa proporción (ej. regiones, nivel socioeconómico, tipo de cliente), garantizando comparaciones justas entre segmentos.
* **Muestreo Aleatorio Simple:** Ideal para obtener una **conclusión general sobre toda la población** cuando esta es homogénea o cuando no se dispone de información previa para dividirla en subgrupos.

---

## Conclusiones

1. **La técnica de muestreo condiciona la validez de los datos:** Un tamaño de muestra grande no garantiza calidad si el método de recolección está sesgado (como en el muestreo por conveniencia). La aleatoriedad y la estratificación son fundamentales para garantizar la representatividad.
2. **Una estimación puntual requiere intervalos de confianza:** Dado que el muestreo aleatorio genera variabilidad entre distintas ejecuciones (semillas), nunca se debe presentar una cifra como una verdad absoluta ante la gerencia sin acompañarla de su correspondiente margen de error o intervalo de confianza.
3. **Recomendación gerencial:** Antes de tomar decisiones estratégicas basadas en muestras, la gerencia debe exigir la auditoría del método de selección de los datos y asegurar que la muestra represente la estructura real del mercado objetivo.