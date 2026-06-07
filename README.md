# Student Dashboard - Group 051

An interactive data visualization dashboard built with Streamlit for exploring student data from Group 051. It provides real-time filtering, statistical summaries, and dynamic charts to analyze student demographics, physical attributes, and more.

> Leer en [Espanol](README.es.md)

---

## Tech Stack

- **Python** 3.9+
- **Streamlit** - Interactive web UI
- **Pandas** - Data processing and analysis
- **Plotly** - Interactive charts and graphs
- **Openpyxl** - Excel file reading

---

## Features

- **Sidebar Filters**: Filter by blood type, hair color, neighborhood, age range, and height range
- **Key Metrics**: Total students, average age, height, weight, and BMI
- **Distribution Charts**: Age distribution, blood type distribution (pie chart)
- **Relationship Charts**: Height vs weight scatter plot, hair color distribution
- **Shoe Size & Neighborhood**: Line chart for shoe sizes, top 10 neighborhoods bar chart
- **Top 5 Rankings**: Students with the highest height and weight
- **Statistical Summary**: Min, max, and average values for height, weight, and BMI

---

## Getting Started

### Prerequisites

- Python 3.9 or higher installed on your system
- Git (optional, for cloning the repository)

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/your-username/student-dashboard.git
cd student-dashboard
```

Or download and extract the ZIP file.

**2. Create a virtual environment**

It is recommended to use a virtual environment to isolate dependencies.

On Windows (Command Prompt or PowerShell):
```bash
python -m venv venv
venv\Scripts\activate
```

On macOS / Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Configure environment variables**

Copy the example environment file and adjust if needed:

```bash
cp .env.example .env
```

The default values in `.env` are:

```env
EXCEL_FILE_PATH=ListadoDeEstudiantesGrupo_051.xlsx
SHEET_NAME=Hoja2
```

- `EXCEL_FILE_PATH`: Path to the Excel data file
- `SHEET_NAME`: Name of the sheet containing the data

**5. Data file**

The repository includes a sample Excel file (`ListadoDeEstudiantesGrupo_051.xlsx`) with anonymized data so you can test the dashboard immediately. Replace it with your own file when ready.

If you use your own file, update `EXCEL_FILE_PATH` in `.env` accordingly. The expected columns in the Excel sheet are:

| Column               | Description               |
|----------------------|---------------------------|
| Codigo               | Student ID code           |
| Nombre_Estudiante    | Student first name        |
| Apellido_Estudiante  | Student last name         |
| Fecha_Nacimiento     | Date of birth             |
| RH                   | Blood type                |
| Estatura             | Height (cm or m)          |
| Peso                 | Weight (kg)               |
| Talla_Zapato         | Shoe size                 |
| Color_Cabello        | Hair color                |
| Barrio_Residencia    | Neighborhood of residence |

**6. Run the application**

```bash
streamlit run app.py
```

If the `streamlit` command is not recognized, use:

```bash
python -m streamlit run app.py
```

The dashboard will open in your default web browser at `http://localhost:8501`.

---

## Project Structure

```
student-dashboard/
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── .env.example                    # Environment variable template
├── .env                            # Environment configuration (not committed)
├── .gitignore                      # Git ignore rules
├── ListadoDeEstudiantesGrupo_051.xlsx  # Sample student data (anonymized)
├── README.md                       # English documentation
├── README.es.md                    # Spanish documentation
└── venv/                           # Virtual environment (not committed)
```

---

## Usage

1. Use the sidebar filters to narrow down the student data by blood type, hair color, neighborhood, or numeric ranges
2. View real-time updated metrics and charts based on your selection
3. Hover over charts for detailed data points
4. Scroll down to explore statistical summaries and top rankings
