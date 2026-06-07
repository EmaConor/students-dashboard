# Dashboard Estudiantil - Grupo 051

Un panel de visualizacion interactiva de datos construido con Streamlit para explorar la informacion de los estudiantes del Grupo 051. Proporciona filtros en tiempo real, resumenes estadisticos y graficos dinamicos para analizar la demografia, atributos fisicos y mas.

Read in [English](README.md)

---

## Tecnologias

- **Python** 3.9+
- **Streamlit** - Interfaz web interactiva
- **Pandas** - Procesamiento y analisis de datos
- **Plotly** - Graficos interactivos
- **Openpyxl** - Lectura de archivos Excel

---

## Funcionalidades

- **Filtros en barra lateral**: Filtrar por tipo de sangre, color de cabello, barrio, rango de edad y rango de estatura
- **Metricas clave**: Total de estudiantes, edad promedio, estatura promedio, peso promedio e IMC promedio
- **Graficos de distribucion**: Distribucion por edad y por tipo de sangre (grafico circular)
- **Graficos de relacion**: Dispersion estatura vs peso, distribucion por color de cabello
- **Talla de zapato y barrios**: Grafico de lineas para tallas de zapato, top 10 barrios
- **Top 5 rankings**: Estudiantes con mayor estatura y mayor peso
- **Resumen estadistico**: Valores minimos, maximos y promedio de estatura, peso e IMC

---

## Como empezar

### Requisitos previos

- Python 3.9 o superior instalado en su sistema
- Git (opcional, para clonar el repositorio)

### Instalacion

**1. Clonar el repositorio**

```bash
git clone https://github.com/tu-usuario/student-dashboard.git
cd student-dashboard
```

O descargue y extraiga el archivo ZIP.

**2. Crear un entorno virtual**

Se recomienda usar un entorno virtual para aislar las dependencias.

En Windows (Command Prompt o PowerShell):
```bash
python -m venv venv
venv\Scripts\activate
```

En macOS / Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

**3. Instalar dependencias**

```bash
pip install -r requirements.txt
```

**4. Configurar variables de entorno**

Copie el archivo de ejemplo de entorno y ajustelo si es necesario:

```bash
cp .env.example .env
```

Los valores por defecto en `.env` son:

```env
EXCEL_FILE_PATH=ListadoDeEstudiantesGrupo_051.xlsx
SHEET_NAME=Hoja2
```

- `EXCEL_FILE_PATH`: Ruta al archivo Excel con los datos
- `SHEET_NAME`: Nombre de la hoja que contiene los datos

**5. Archivo de datos**

El repositorio incluye un archivo Excel de ejemplo (`ListadoDeEstudiantesGrupo_051.xlsx`) con datos anonimizados para que pueda probar el dashboard inmediatamente. Reemplacelo con su propio archivo cuando lo desee.

Si usa su propio archivo, actualice `EXCEL_FILE_PATH` en `.env` segun corresponda. Las columnas esperadas en la hoja de Excel son:

| Columna              | Descripcion                    |
|----------------------|--------------------------------|
| Codigo               | Codigo del estudiante          |
| Nombre_Estudiante    | Nombre del estudiante          |
| Apellido_Estudiante  | Apellido del estudiante        |
| Fecha_Nacimiento     | Fecha de nacimiento            |
| RH                   | Tipo de sangre                 |
| Estatura             | Estatura (cm o m)              |
| Peso                 | Peso (kg)                      |
| Talla_Zapato         | Talla de zapato                |
| Color_Cabello        | Color de cabello               |
| Barrio_Residencia    | Barrio de residencia           |

**6. Ejecutar la aplicacion**

```bash
streamlit run app.py
```

Si el comando `streamlit` no es reconocido, use:

```bash
python -m streamlit run app.py
```

El panel se abrira en su navegador web predeterminado en `http://localhost:8501`.

---

## Estructura del proyecto

```
student-dashboard/
├── app.py                          # Aplicacion principal de Streamlit
├── requirements.txt                # Dependencias de Python
├── .env.example                    # Plantilla de variables de entorno
├── .env                            # Configuracion de entorno (no se sube)
├── .gitignore                      # Reglas de ignorados de Git
├── ListadoDeEstudiantesGrupo_051.xlsx  # Datos de ejemplo (anonimizados)
├── README.md                       # Documentacion en ingles
├── README.es.md                    # Documentacion en espanol
└── venv/                           # Entorno virtual (no se sube)
```

---

## Uso

1. Use los filtros en la barra lateral para acotar los datos por tipo de sangre, color de cabello, barrio o rangos numericos
2. Visualice las metricas y graficos actualizados en tiempo real segun su seleccion
3. Pase el cursor sobre los graficos para ver detalles de cada punto de datos
4. Desplace hacia abajo para explorar los resumenes estadisticos y los rankings principales
