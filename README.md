# Proyecto Dashboard CSV Django

Una aplicación web Django que crea dashboards interactivos a partir de archivos de datos CSV. El dashboard genera automáticamente varios tipos de gráficos incluyendo gráficos de líneas, gráficos de barras, gráficos de pastel y gráficos de dispersión basados en la estructura de los datos.

## Características

- **Carga de Archivos CSV**: Sube archivos CSV a través de una interfaz web
- **Generación Automática de Gráficos**: Crea múltiples tipos de gráficos basados en la estructura de datos:
  - Gráficos de líneas para datos de series temporales
  - Gráficos de barras para datos categóricos vs numéricos
  - Gráficos de pastel para distribuciones categóricas
  - Gráficos de dispersión para correlaciones numéricas
- **Resumen de Datos**: Muestra estadísticas sobre los datos cargados
- **Vista Previa de Datos**: Muestra las primeras 10 filas de datos en una tabla
- **Diseño Responsivo**: Funciona en dispositivos de escritorio y móviles

## Instalación

1. **Clona o descarga los archivos del proyecto**

2. **Instala las dependencias de Python**:
   ```bash
   pip3 install virtualenv
   virtualenv -p python3 dash_env
   .\dash_env\Scripts\activate
   python.exe -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

3. **Ejecuta las migraciones de la base de datos**:
   ```bash
   python manage.py makemigrations dashboard_app
   python manage.py migrate
   ```

4. **Crea un superusuario (opcional)**:
   ```bash
   python manage.py createsuperuser
   ```

5. **Ejecuta el servidor de desarrollo**:
   ```bash
   python manage.py runserver
   ```

6. **Accede a la aplicación**:
   - Dashboard principal: http://127.0.0.1:8000/
   - Panel de administración: http://127.0.0.1:8000/admin/

## Uso

1. **Sube un archivo CSV**:
   - Haz clic en "Upload New CSV" en el dashboard
   - Selecciona un archivo CSV de tu computadora
   - Haz clic en "Upload CSV"

2. **Ve el dashboard**:
   - El dashboard mostrará automáticamente gráficos basados en tus datos
   - Diferentes tipos de gráficos aparecerán dependiendo de la estructura de tus datos

3. **Datos de ejemplo**:
   - Usa el archivo `sample_data.csv` incluido para probar la aplicación

## Requisitos del Archivo CSV

- El archivo debe estar en formato CSV (.csv)
- La primera fila debe contener encabezados de columnas
- Incluye tanto datos numéricos como categóricos para la mejor visualización
- Tamaño máximo del archivo: 10MB

## Formato de Datos de Ejemplo

```csv
Name,Age,Department,Salary,Experience,Performance_Score
John Doe,30,Engineering,75000,5,85
Jane Smith,28,Marketing,65000,3,78
...
```

## Estructura del Proyecto

```
dashboard_project/
├── dashboard_project/          # Configuración del proyecto Django
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── dashboard_app/              # Aplicación principal
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── templates/                  # Plantillas HTML
│   ├── base.html
│   └── dashboard_app/
│       ├── dashboard.html
│       └── upload.html
├── manage.py
├── requirements.txt
├── sample_data.csv
└── README.md
```

## Tecnologías Utilizadas

- **Django 4.2.7**: Framework web
- **Pandas**: Procesamiento y análisis de datos
- **Chart.js**: Gráficos y diagramas interactivos
- **Bootstrap 5**: Framework de UI responsivo
- **SQLite**: Base de datos (por defecto)

## Personalización

Puedes personalizar el dashboard:

1. **Agregando nuevos tipos de gráficos** en `dashboard_app/views.py`
2. **Modificando la UI** en los archivos de plantilla
3. **Agregando lógica de procesamiento de datos** en la función `prepare_chart_data`
4. **Estilizando** modificando el CSS en `templates/base.html`

## Solución de Problemas

- **Problemas de carga de CSV**: Asegúrate de que el archivo esté en formato CSV correcto con encabezados
- **Gráficos no se muestran**: Revisa la consola del navegador para errores de JavaScript
- **Errores de base de datos**: Ejecuta las migraciones con `python manage.py migrate`

## Licencia

Este proyecto es de código abierto y está disponible bajo la Licencia MIT.
