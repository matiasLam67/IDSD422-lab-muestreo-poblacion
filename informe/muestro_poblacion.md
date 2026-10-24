
<!-- CARÁTULA UNIFORMADA EPN (PÁGINA ÚNICA) -->
<div style="font-family: 'Segoe UI', Arial, sans-serif; text-align: center; max-width: 750px; margin: 0 auto; padding: 40px 20px; color: #555555; page-break-after: always; break-after: page;">
  <!-- ENCABEZADO INSTITUCIONAL -->
<h2 style="color: #1b2a47; font-size: 1.4em; font-weight: 800; letter-spacing: 2px; margin-bottom: 6px; text-transform: uppercase;">
    ESCUELA POLITÉCNICA NACIONAL
  </h2>
  <p style="color: #555555; font-size: 0.95em; margin-top: 0; margin-bottom: 25px;">
    Facultad de Ingeniería de Sistemas &middot; Carrera de Ciencia de Datos e Inteligencia Artificial
  </p>
  <!-- LÍNEA DECORATIVA DORADA -->
<div style="width: 60px; height: 3px; background-color: #b5984d; margin: 0 auto 30px auto; border-radius: 2px;"></div>
  <!-- TÍTULO DE LA PRÁCTICA -->
<p style="color: #b5984d; font-weight: 700; font-size: 0.9em; letter-spacing: 1.5px; text-transform: uppercase; margin-bottom: 10px;">
    INFORME DE LABORATORIO N.&deg; 3
  </p>
  <h1 style="color: #1b2a47; font-size: 2.1em; font-weight: 800; margin-top: 0; margin-bottom: 12px;">
    Clasificación de variables y población vs. muestra
  </h1>
  <p style="color: #555555; font-size: 0.92em; margin-top: 0; margin-bottom: 45px;">
    Tópico del PEA &middot; Asignatura IDSD422 &mdash; Estadística y Programación para Ciencia de Datos I
  </p>
  <!-- TABLA DE DATOS -->
<table style="width: 100%; border-collapse: collapse; margin: 0 auto; text-align: left; font-size: 0.9em; border: 1px solid #dcdfe6;">
    <tbody>
      <tr style="border-bottom: 1px solid #dcdfe6;">
        <th style="background-color: #f4f6f8; color: #1b2a47; width: 32%; padding: 12px 16px; font-weight: 700;">Estudiante(s)</th>
        <td style="padding: 12px 16px; color: #333333;">Lamiña Flores, Matías Andres &mdash; usuario de GitHub: <a href="https://github.com/matiasLam67" target="_blank" style="color: #0366d6; text-decoration: none;">https://github.com/matiasLam67</a></td>
      </tr>
      <tr style="border-bottom: 1px solid #dcdfe6;">
        <th style="background-color: #f4f6f8; color: #1b2a47; padding: 12px 16px; font-weight: 700;">Docente</th>
        <td style="padding: 12px 16px; color: #333333;">SUAREZ COBOS CHRISTIAN GONZALO</td>
      </tr>
      <tr style="border-bottom: 1px solid #dcdfe6;">
        <th style="background-color: #f4f6f8; color: #1b2a47; padding: 12px 16px; font-weight: 700;">Período académico</th>
        <td style="padding: 12px 16px; color: #333333;">2026-B</td>
      </tr>
      <tr style="border-bottom: 1px solid #dcdfe6;">
        <th style="background-color: #f4f6f8; color: #1b2a47; padding: 12px 16px; font-weight: 700;">Fecha de entrega</th>
        <td style="padding: 12px 16px; color: #333333;">23/10/2026</td>
      </tr>
      <tr>
        <th style="background-color: #f4f6f8; color: #1b2a47; padding: 12px 16px; font-weight: 700;">Repositorio (fork)</th>
        <td style="padding: 12px 16px; color: #333333;"><a href="https://github.com/matiasLam67/IDSD422-lab-muestreo-poblacion.git" target="_blank" style="color: #0366d6; text-decoration: none;">https://github.com/matiasLam67/IDSD422-lab-muestreo-poblacion.git</a></td>
      </tr>
    </tbody>
  </table>
</div>
<!-- FIN DE CARÁTULA -->

---


### 1. Introducción

RetailAndina S.A. necesita comprender la estructura de su base de clientes 
fidelizados para futuros análisis y requiere estimar el ingreso mensual 
promedio utilizando una muestra reducida de 20 personas, asegurando que 
esta fracción sea realmente representativa. Además, es crucial evidenciar empíricamente que un diseño
de muestreo sesgado no se soluciona simplemente recolectando más datos, 
sino aplicando la técnica adecuada. Como analista de Business 
Intelligence, clasifiqué y verifiqué los tipos de datos mediante 
código en Python, y comparé la precisión de tres diseños de muestreo 
distintos frente al parámetro poblacional real.

---

### 2. Objetivos

**Objetivo general**
Clasificar la estructura de variables de la base de fidelización de RetailAndina S.A. y evaluar la precisión de tres diseños de muestreo estadístico frente al parámetro real poblacional.

**Objetivos específicos**
1. **Clasificar** las siete variables del conjunto de datos según su naturaleza estadística (nominal, ordinal, discreta o continua) y **verificar** empíricamente sus tipos inferidos (`dtypes`) en código.
2. **Implementar** el orden jerárquico explícito de las variables cualitativas ordinales utilizando las estructuras categóricas de Pandas.
3. **Comparar** las estimaciones de la media de ingresos obtenidas mediante un muestreo por conveniencia, uno aleatorio simple y uno estratificado.
4. **Interpretar** el sesgo de selección y la variabilidad originada por el azar (semillas) para reportar a la gerencia los límites y cuidados al decidir con base en muestras.

---

### 3. Desarrollo de la práctica
Organízalo en dos partes, con subtítulos. Para cada paso: qué hiciste, con qué (Python o R; Colab, Posit Cloud o local) y el resultado obtenido. Incluye el código clave comentado y las capturas crudas numeradas y descritas. Si algo falló (una ruta, un tipo inesperado, un nivel mal escrito), cuéntalo y explica cómo lo resolviste.

#### 3.1 Parte A — Clasificación de las variables
* Completa la tabla con el **criterio** (¿tiene sentido la mitad del valor? ¿Hay orden entre las categorías?), no con el ejemplo. En «verificación» anota qué mostró el código: dtype, número de valores únicos y, si declaraste el orden, cómo lo comprobaste.
* La base de trabajo es `data/clientes.csv`: 12 clientes, 7 variables + el identificador.

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


**P1. ¿Qué te dijo el dtype de satisfacción y por qué no basta para clasificarla? ¿Qué pasa si una ordinal queda como texto sin declarar el orden? (Responde con la evidencia de tu ejecución.)**

#### 3.2 Parte B — Población vs. muestra
* La población es `data/clientes_400.csv`: 400 clientes (Quito 200 / Guayaquil 120 / Cuenca 80). La variable de interés es `ingresos_mensuales`.
* Primero calcula el parámetro poblacional y completa la tabla. Luego corre los tres diseños y registra sus salidas tal como salieron. La composición por ciudad es la pista que delata el sesgo.

| Concepto                      |       Valor        |
|-------------------------------|:------------------:|
| Población (N)                 |        200         |
| Variable de interés           | ingresos mensuales |
| Parámetro poblacional (media) |    1330.72 USD     |

¿Por qué se muestrea si aquí el parámetro existe y se calculó? 

| Diseño                          | n  | Media estimada |             Composición por ciudad             | Diferencia vs. parámetro |
|---------------------------------|----|----------------|:----------------------------------------------:|:------------------------:|
| Conveniencia  (`head`)          | 20 | 1348.50        |                   `Quito:20`                   |          +17.78          |
| Aleatorio simple (`sample`)     | 20 | 1336.00        | `Cuenca: 8`<br/>`Quito: 8`<br/>`Guayaquil: 4`  |          +5.28           |
| Estratificado (`groupby` + 5 %) | 20 | 1212.50        | `Cuenca: 10`<br/>`Quito: 6`<br/>`Guayaquil: 4` |         -118.22          |


Anota también las medias de 5 sorteos distintos del aleatorio simple (semillas 1 a 5):

| Semilla     | 1       | 2       | 3       | 4       | 5       |
|-------------|---------|---------|---------|---------|---------|
| Media (USD) | 1336.00 | 1405.00 | 1235.00 | 1491.00 | 1288.00 |

**P2. ¿Cuánto vale el parámetro poblacional y cuánto estimó cada diseño? ¿Cuál quedó más cerca y por qué eso no alcanza para declarar un ganador?**

El parámetro poblacional es **1330.72 USD**. Las estimaciones fueron:
* **Conveniencia:** 1348.50 USD (Dif: +17.78)
* **Aleatorio Simple (Semilla 1):** 1336.00 USD (Dif: +5.28)
* **Estratificado:** 1212.50 USD (Dif: -118.22)

En este intento puntual, el **Aleatorio Simple** quedó más cerca del valor real (+5.28 USD). Sin embargo, esto **no alcanza para declararlo un ganador** porque una sola muestra está sujeta al azar (variabilidad muestral). Como se observa al cambiar la semilla en el muestreo aleatorio simple, el resultado oscila fuertemente entre 1235.00 USD y 1491.50 USD. Aunque el diseño estratificado dio un valor más alejado en esta ejecución concreta debido al tamaño pequeño de muestra ($n=20 $), teóricamente es el diseño con menor varianza estructural a largo plazo.

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

### 4. ¿Qué aprendí con esta práctica?

En esta práctica comprendí que la forma en que un lenguaje de programación almacena un dato no define su naturaleza estadística. Ahora entiendo por qué `dtype` no alcanza para clasificar una variable: la columna `satisfaccion` se cargaba como `int64`, pero conceptualmente es cualitativa ordinal. Aprendí a forzar esta jerarquía usando `pd.CategoricalDtype` y a comprobar que funcionaba usando `.min()`, lo cual devolvió la categoría más baja según la lógica estadística ('Primaria') y no la primera en orden alfabético.

Lo más difícil del laboratorio fue lidiar con las rutas de los 
archivos y los entornos de ejecución. Al intentar cargar 
`clientes.csv` ejecutando el script desde la carpeta `scripts/`, 
me topé con un `FileNotFoundError` porque el *Working Directory* no 
coincidía con la raíz del proyecto. Lo resolví abandonando las rutas 
estáticas temporalmente para hacer que el código 
construya la ruta dinámicamente y sea 100 % portable en GitHub. 

La próxima vez que me enfrente a la transformación de datos, revisaré 
primero los valores únicos reales de la base (usando `.unique()`) 
antes de declarar las categorías ordenadas. En un inicio intenté 
clasificar el nivel educativo usando la palabra "Bachillerato", 
pero al comparar con los datos noté que la base original decía 
"Secundaria" y "Universidad", lo que me habría generado valores nulos 
(`NaN`) de no haberlo corregido a tiempo. También aprendí a leer y 
silenciar advertencias de actualización de librerías, como
`FutureWarning` al usar `.groupby().apply()`, añadiendo el 
argumento `include_groups=False`.

---

### 5. Conclusiones

1. **El tipo de dato informático no sustituye el criterio analítico:** La inferencia automática de Pandas no es suficiente para preparar los datos. Se demostró que variables como `satisfaccion` (`int64`) requerían una reclasificación explícita a tipo categórico ordinal. Sin esta intervención, cualquier gráfico o modelo posterior habría tratado esta jerarquía como un número continuo o alfabético, invalidando el análisis.
2. **El muestreo por conveniencia genera sesgos sistemáticos:** Tomar las primeras 20 filas (`head`) resultó en una estimación de ingresos de 1348.50 USD, pero la composición de la muestra delató un sesgo extremo: el 100 % de los clientes seleccionados (`{'Quito': 20}`) pertenecía a una sola ciudad, excluyendo por completo a los 200 clientes que la población real tiene en Guayaquil y Cuenca. 
3. **La aleatoriedad simple presenta alta variabilidad muestral:** La estimación de un parámetro es incierta si se toma un solo muestreo. Al evaluar el diseño aleatorio simple ($n= 20 $) con 5 semillas distintas, la media de ingresos fluctuó drásticamente entre 1235.00 USD (semilla 3) y 1491.50 USD (semilla 4) respecto al parámetro real de 1330.72 USD, lo que evidencia el peligro de tomar decisiones con un único número sin medir su margen de error.

**Mensaje final a la gerencia:**
Con esta base de fidelización y los diseños evaluados, la conclusión aplica para las estimaciones financieras basadas en subconjuntos de clientes de RetailAndina S.A. Recomendamos a la gerencia exigir siempre una auditoría del método de selección antes de aprobar decisiones basadas en encuestas o estudios pilotos. Añadir más filas a una muestra mal tomada no corrige sus defectos de origen; en estadística comercial, **el diseño de la muestra es lo que decide su validez y representatividad, no el tamaño de la misma**.

---

## 6. Bibliografía

Escuela Politécnica Nacional. (2026). *Base de datos de fidelización clientes.csv y clientes_400.csv (Caso RetailAndina S.A.)* [Conjunto de datos]. Recuperado de https://github.com/christian-suarez1979/IDSD422-lab-muestreo-poblacion.git

Pandas development team. (2026). *pandas.CategoricalDtype*. Documentación oficial de pandas. Recuperado de https://pandas.pydata.org/docs/reference/api/pandas.CategoricalDtype.html

Pandas development team. (2026). *pandas.DataFrame.groupby*. Documentación oficial de pandas. Recuperado de https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html

**Declaración de uso de herramientas de IA:**
Se utilizó un modelo de lenguaje (IA) como asistente de programación y redacción durante esta práctica. Su uso específico consistió en depurar errores de rutas de ejecución (`FileNotFoundError`), comprender la sintaxis de categorización ordinal en Pandas y estructurar la sintaxis Markdown del presente documento.

### 7. Anexos (opcional)

>![Captura de pantalla 2026-10-23 232026.png](Captura%20de%20pantalla%202026-10-23%20232026.png)
> _Imagen 1. Data set immpreso junto con su número de filas y columnas._

>![Captura de pantalla 2026-10-23 232100.png](Captura%20de%20pantalla%202026-10-23%20232100.png)  
> _Iamgen 2. Tipos de datos de cada columna. obtenidos por dataypes._
 
>![Captura de pantalla 2026-10-23 232146.png](Captura%20de%20pantalla%202026-10-23%20232146.png)
>_Imagen 3. Los valores únicos de cada columna._

>![Captura de pantalla 2026-10-23 232211.png](Captura%20de%20pantalla%202026-10-23%20232211.png)
>_Imagen 4. Clasificacíon de variables_

---

