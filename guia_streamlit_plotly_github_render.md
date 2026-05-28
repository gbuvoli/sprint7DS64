# 🚀 Clase: Despliegue de una aplicación de visualización con Streamlit, Plotly, GitHub y Render

## Duración estimada

**1 hora y 30 minutos**

## Objetivo de la clase

En esta clase vamos a construir y desplegar una aplicación web sencilla de visualización de datos usando:

```text
GitHub → VS Code → Conda → Streamlit → Plotly → Render
```

La idea es entender el flujo completo:

1. Crear un repositorio en GitHub.
2. Clonarlo en VS Code.
3. Crear un ambiente virtual con Conda.
4. Instalar librerías.
5. Construir una app interactiva con Streamlit y Plotly.
6. Probar la app localmente.
7. Crear el archivo `requirements.txt`.
8. Subir cambios a GitHub.
9. Desplegar la aplicación en Render.

---

## 1. Requisitos antes de empezar

Cada estudiante debe tener:

- **VS Code** instalado.
- **Anaconda** o **Miniconda** instalado.
- **Git** instalado.
- Una cuenta de **GitHub**.
- Una cuenta de **Render**.
- Extensiones de VS Code:
  - Python.
  - Jupyter, opcional para exploración.

---

## 2. Agenda de la sesión

| Tiempo estimado | Actividad |
|---|---|
| 10 min | Introducción a Streamlit y Plotly |
| 10 min | Crear repositorio en GitHub y clonarlo |
| 15 min | Crear ambiente Conda e instalar librerías |
| 30 min | Construir la aplicación en Streamlit |
| 10 min | Probar localmente y crear `requirements.txt` |
| 15 min | Subir a GitHub y desplegar en Render |

---

# Parte 1: Introducción breve

## 3. ¿Qué es Streamlit?

**Streamlit** es una librería de Python que permite crear aplicaciones web interactivas de datos sin tener que escribir HTML, CSS o JavaScript.

Con Streamlit podemos convertir un script de Python en una aplicación web usando componentes como:

- títulos;
- texto;
- tablas;
- métricas;
- gráficos;
- barras laterales;
- selectores;
- botones;
- checkboxes;
- sliders.

Ejemplo mínimo:

```python
import streamlit as st

st.title("Mi primera app")
st.write("Hola desde Streamlit")
```

Para ejecutar una app de Streamlit usamos:

```bash
streamlit run app.py
```

La idea central es:

> Si sabes escribir Python, puedes empezar a construir aplicaciones de datos.

---

## 4. ¿Qué es Plotly?

**Plotly** es una librería de visualización interactiva.

Con Plotly podemos crear gráficos como:

- barras;
- líneas;
- dispersión;
- mapas;
- histogramas;
- gráficos interactivos con tooltips, zoom y filtros visuales.

En esta clase usaremos **Plotly Express**, que es una interfaz simple para crear gráficos rápidamente.

Ejemplo:

```python
import plotly.express as px

fig = px.scatter(
    data_frame=df,
    x="gdpPercap",
    y="lifeExp",
    color="continent"
)
```

Luego, en Streamlit podemos mostrar ese gráfico con:

```python
st.plotly_chart(fig)
```

---

# Parte 2: Crear el proyecto desde GitHub

## 5. Crear repositorio en GitHub

En GitHub:

1. Ir a **New repository**.
2. Nombre sugerido:

```text
streamlit-gapminder-app
```

3. Agregar descripción:

```text
Aplicación de visualización interactiva con Streamlit y Plotly.
```

4. Marcar la opción:

```text
Add a README file
```

5. Crear el repositorio.

---

## 6. Clonar el repositorio en VS Code

Desde GitHub, copia la URL del repositorio.

Luego, en la terminal:

```bash
git clone URL_DEL_REPOSITORIO
```

Ejemplo:

```bash
git clone https://github.com/tu_usuario/streamlit-gapminder-app.git
```

Entramos a la carpeta:

```bash
cd streamlit-gapminder-app
```

Abrimos VS Code:

```bash
code .
```

---

# Parte 3: Crear el ambiente virtual

## 7. Crear ambiente con Conda

Dentro del proyecto, abrimos la terminal de VS Code y creamos un ambiente:

```bash
conda create -n streamlit_env python=3.11
```

Activamos el ambiente:

```bash
conda activate streamlit_env
```

Instalamos las librerías:

```bash
pip install streamlit pandas plotly
```

También podemos verificar que quedaron instaladas:

```bash
pip list
```

---

## 8. Seleccionar el intérprete en VS Code

En VS Code:

```text
Ctrl + Shift + P
Python: Select Interpreter
```

Seleccionamos el ambiente:

```text
streamlit_env
```

Esto es importante porque VS Code puede tener acceso a varios Python diferentes.

---

# Parte 4: Crear la aplicación

## 9. Estructura del proyecto

El proyecto tendrá esta estructura:

```text
streamlit-gapminder-app/
│
├── app.py
├── requirements.txt
└── README.md
```

Creamos el archivo principal:

```text
app.py
```

---

## 10. Dataset que usaremos

Usaremos el dataset `gapminder`, disponible desde Plotly Express.

Este dataset contiene información por país y año sobre:

- continente;
- país;
- año;
- expectativa de vida;
- población;
- PIB per cápita.

Es práctico para clase porque no necesitamos descargar archivos externos.

---

## 11. Primera versión de la app

En `app.py`, escribimos:

```python
import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(
    page_title="Gapminder Dashboard",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 Gapminder Dashboard")
st.write(
    "Aplicación interactiva para explorar expectativa de vida, población "
    "y PIB per cápita por país y continente."
)

df = px.data.gapminder()

st.write("Vista previa de los datos:")
st.dataframe(df.head())
```

Ejecutamos la app:

```bash
streamlit run app.py
```

Streamlit abrirá la aplicación en el navegador.

Si no se abre automáticamente, normalmente podrás verla en:

```text
http://localhost:8501
```

---

## 12. Agregar barra lateral

Ahora vamos a crear filtros en la barra lateral.

Reemplazamos el contenido de `app.py` por esta versión:

```python
import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(
    page_title="Gapminder Dashboard",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 Gapminder Dashboard")
st.write(
    "Explora cómo han cambiado la expectativa de vida, la población "
    "y el PIB per cápita en diferentes países."
)

df = px.data.gapminder()

st.sidebar.header("Filtros")

continentes = sorted(df["continent"].unique())

continente_seleccionado = st.sidebar.selectbox(
    "Selecciona un continente",
    continentes
)

df_continente = df[df["continent"] == continente_seleccionado]

paises_disponibles = sorted(df_continente["country"].unique())

paises_seleccionados = st.sidebar.multiselect(
    "Selecciona países",
    paises_disponibles,
    default=paises_disponibles[:5]
)

anio_seleccionado = st.sidebar.slider(
    "Selecciona un año",
    int(df["year"].min()),
    int(df["year"].max()),
    int(df["year"].max()),
    step=5
)

usar_escala_log = st.sidebar.checkbox(
    "Usar escala logarítmica para PIB per cápita",
    value=True
)

df_filtrado = df_continente[
    (df_continente["country"].isin(paises_seleccionados))
]

df_anio = df_filtrado[df_filtrado["year"] == anio_seleccionado]

st.subheader("Datos filtrados")
st.dataframe(df_anio)
```

Probamos nuevamente:

```bash
streamlit run app.py
```

---

## 13. Agregar métricas principales

Debajo del dataframe, agregamos:

```python
col1, col2, col3 = st.columns(3)

promedio_vida = df_anio["lifeExp"].mean()
poblacion_total = df_anio["pop"].sum()
pib_promedio = df_anio["gdpPercap"].mean()

col1.metric("Expectativa de vida promedio", f"{promedio_vida:,.1f} años")
col2.metric("Población total", f"{poblacion_total:,.0f}")
col3.metric("PIB per cápita promedio", f"${pib_promedio:,.0f}")
```

Las métricas ayudan a resumir la información filtrada antes de ver los gráficos.

---

## 14. Agregar visualizaciones con Plotly

Ahora agregamos tres gráficos:

1. Dispersión: PIB per cápita vs expectativa de vida.
2. Barras: población por país.
3. Línea: evolución de expectativa de vida.

Agregamos este bloque:

```python
st.subheader("Visualizaciones")

fig_scatter = px.scatter(
    df_anio,
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="country",
    hover_name="country",
    log_x=usar_escala_log,
    title=f"PIB per cápita vs expectativa de vida - {anio_seleccionado}"
)

st.plotly_chart(fig_scatter, use_container_width=True)


fig_bar = px.bar(
    df_anio.sort_values("pop", ascending=False),
    x="country",
    y="pop",
    color="country",
    title=f"Población por país - {anio_seleccionado}"
)

st.plotly_chart(fig_bar, use_container_width=True)


fig_line = px.line(
    df_filtrado,
    x="year",
    y="lifeExp",
    color="country",
    markers=True,
    title="Evolución de la expectativa de vida"
)

st.plotly_chart(fig_line, use_container_width=True)
```

---

## 15. Código completo de `app.py`

Al final, `app.py` debe quedar así:

```python
import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(
    page_title="Gapminder Dashboard",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 Gapminder Dashboard")
st.write(
    "Explora cómo han cambiado la expectativa de vida, la población "
    "y el PIB per cápita en diferentes países."
)

df = px.data.gapminder()

st.sidebar.header("Filtros")

continentes = sorted(df["continent"].unique())

continente_seleccionado = st.sidebar.selectbox(
    "Selecciona un continente",
    continentes
)

df_continente = df[df["continent"] == continente_seleccionado]

paises_disponibles = sorted(df_continente["country"].unique())

paises_seleccionados = st.sidebar.multiselect(
    "Selecciona países",
    paises_disponibles,
    default=paises_disponibles[:5]
)

anio_seleccionado = st.sidebar.slider(
    "Selecciona un año",
    int(df["year"].min()),
    int(df["year"].max()),
    int(df["year"].max()),
    step=5
)

usar_escala_log = st.sidebar.checkbox(
    "Usar escala logarítmica para PIB per cápita",
    value=True
)

df_filtrado = df_continente[
    df_continente["country"].isin(paises_seleccionados)
]

df_anio = df_filtrado[df_filtrado["year"] == anio_seleccionado]

st.subheader("Datos filtrados")
st.dataframe(df_anio)

col1, col2, col3 = st.columns(3)

promedio_vida = df_anio["lifeExp"].mean()
poblacion_total = df_anio["pop"].sum()
pib_promedio = df_anio["gdpPercap"].mean()

col1.metric("Expectativa de vida promedio", f"{promedio_vida:,.1f} años")
col2.metric("Población total", f"{poblacion_total:,.0f}")
col3.metric("PIB per cápita promedio", f"${pib_promedio:,.0f}")

st.subheader("Visualizaciones")

fig_scatter = px.scatter(
    df_anio,
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="country",
    hover_name="country",
    log_x=usar_escala_log,
    title=f"PIB per cápita vs expectativa de vida - {anio_seleccionado}"
)

st.plotly_chart(fig_scatter, use_container_width=True)

fig_bar = px.bar(
    df_anio.sort_values("pop", ascending=False),
    x="country",
    y="pop",
    color="country",
    title=f"Población por país - {anio_seleccionado}"
)

st.plotly_chart(fig_bar, use_container_width=True)

fig_line = px.line(
    df_filtrado,
    x="year",
    y="lifeExp",
    color="country",
    markers=True,
    title="Evolución de la expectativa de vida"
)

st.plotly_chart(fig_line, use_container_width=True)
```

---

# Parte 5: Validar la app localmente

## 16. Ejecutar la aplicación

En la terminal:

```bash
streamlit run app.py
```

Validamos que:

- la app abre en el navegador;
- la barra lateral funciona;
- el selector de continente cambia los países;
- el multiselect cambia los gráficos;
- el slider de año actualiza los datos;
- el checkbox cambia la escala del gráfico de dispersión;
- los gráficos se renderizan correctamente.

---

## 17. Crear `requirements.txt`

Para que Render sepa qué librerías instalar, necesitamos un archivo llamado:

```text
requirements.txt
```

En la raíz del proyecto, creamos ese archivo con este contenido:

```text
streamlit
pandas
plotly
```

Para esta práctica lo crearemos manualmente, escribiendo únicamente las librerías principales que usa la aplicación.

No usaremos `pip freeze`, porque ese comando puede incluir muchas dependencias adicionales que no necesitamos explicar en esta clase.

---

# Parte 6: Guardar cambios con Git

## 18. Revisar estado

```bash
git status
```

## 19. Agregar archivos

```bash
git add .
```

## 20. Crear commit

```bash
git commit -m "Crea dashboard interactivo con Streamlit y Plotly"
```

## 21. Subir a GitHub

```bash
git push
```

Si es el primer push y Git lo solicita:

```bash
git push -u origin main
```

---

# Parte 7: Desplegar en Render

## 22. Crear cuenta en Render

1. Ir a Render.
2. Crear una cuenta o iniciar sesión.
3. Conectar Render con GitHub.
4. Autorizar el acceso al repositorio del proyecto.

---

## 23. Crear un nuevo Web Service

En Render:

1. Clic en **New**.
2. Seleccionar **Web Service**.
3. Buscar el repositorio:

```text
streamlit-gapminder-app
```

4. Clic en **Connect**.

No debemos seleccionar **Static Site**, porque una app de Streamlit ejecuta código Python del lado del servidor.

---

## 24. Configurar el servicio

Usar esta configuración:

| Campo | Valor |
|---|---|
| Name | `streamlit-gapminder-app` |
| Runtime / Language | Python |
| Branch | `main` |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `streamlit run app.py --server.port $PORT --server.address 0.0.0.0` |
| Instance Type | Free, si está disponible |

---

## 25. Variable de entorno opcional

Render permite definir variables de entorno.

Para evitar diferencias de versión, podemos agregar:

| Key | Value |
|---|---|
| `PYTHON_VERSION` | `3.11.0` |

Esto ayuda a que Render use una versión de Python similar a la del ambiente local.

---

## 26. Desplegar

Después de configurar:

1. Clic en **Deploy Web Service**.
2. Esperar a que Render instale dependencias.
3. Revisar los logs.
4. Cuando aparezca como **Live**, abrir la URL generada por Render.

La URL normalmente termina en:

```text
.onrender.com
```

---

# Parte 8: Errores frecuentes

## 27. Error: `ModuleNotFoundError`

Ejemplo:

```text
ModuleNotFoundError: No module named 'plotly'
```

Causa probable:

- La librería no está en `requirements.txt`.

Solución:

```text
Agregar plotly a requirements.txt
Hacer commit
Hacer push
Render redeploy
```

---

## 28. Error: la app funciona localmente pero falla en Render

Posibles causas:

- Falta una librería en `requirements.txt`.
- El comando de inicio está mal escrito.
- Render no está encontrando `app.py`.
- El archivo no está en la raíz del repositorio.
- La app no está escuchando en `$PORT`.

Comando recomendado para Render:

```bash
streamlit run app.py --server.port $PORT --server.address 0.0.0.0
```

---

## 29. Error: Render despliega pero la app no abre rápido

En el plan gratuito, algunos servicios pueden tardar en despertar después de estar inactivos.

Esto no significa necesariamente que la app esté dañada.

---

## 30. Error: GitHub no tiene los últimos cambios

Revisar:

```bash
git status
```

Luego:

```bash
git add .
git commit -m "Actualiza app"
git push
```

Si los cambios no están en GitHub, Render no podrá desplegarlos.

---

# Parte 9: Reto de cierre

## 31. Mejorar la app

Agrega al menos una de estas mejoras:

1. Un `st.radio` para elegir la variable del eje Y:
   - `lifeExp`
   - `pop`
   - `gdpPercap`

2. Un `st.checkbox` para mostrar u ocultar la tabla.

3. Un `st.button` que muestre un mensaje:

```python
if st.button("Mostrar conclusión"):
    st.write("La visualización permite comparar indicadores entre países y años.")
```

4. Un segundo `selectbox` para elegir el tipo de gráfico:
   - barras;
   - dispersión;
   - líneas.

---

## 32. Solución sugerida para mostrar u ocultar tabla

```python
mostrar_tabla = st.sidebar.checkbox("Mostrar tabla de datos", value=True)

if mostrar_tabla:
    st.subheader("Datos filtrados")
    st.dataframe(df_anio)
```

---

## 33. Solución sugerida para botón

```python
if st.button("Mostrar conclusión"):
    st.write(
        "Los filtros permiten explorar cómo cambian los indicadores "
        "según continente, país y año."
    )
```

---

# Cierre

Hoy construimos una aplicación de visualización de datos de principio a fin:

```text
GitHub → VS Code → Conda → Streamlit → Plotly → Render
```

Aprendimos que:

- Streamlit permite convertir scripts de Python en aplicaciones web.
- Plotly permite crear gráficos interactivos.
- GitHub guarda el código del proyecto.
- `requirements.txt` le dice al servidor qué instalar.
- Render toma el repositorio, instala dependencias y ejecuta la app.
- El despliegue necesita un comando de inicio correcto.

La idea más importante:

> Una app de datos no es solo un gráfico bonito.  
> Es un flujo completo: código, ambiente, dependencias, repositorio y despliegue.
