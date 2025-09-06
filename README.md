# Proyecto Dashboard CSV Django

Una aplicación web Django que crea dashboards interactivos a partir de archivos de datos CSV. El dashboard genera automáticamente varios tipos de gráficos incluyendo gráficos de líneas, gráficos de barras, gráficos de pastel y gráficos de dispersión basados en la estructura de los datos.

Creada utilizando Cursor AI por Esp. Ing. Carlos Rodríguez, parte de el Curso en vivo de IA en la Industria 4.0 de http://ingelearn.com/

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

## Prerrequisitos

### 1. **Instalar Python**

#### **Windows:**
1. Ve a [python.org](https://www.python.org/downloads/)
2. Descarga la versión más reciente de Python (3.8 o superior)
3. **IMPORTANTE**: Durante la instalación, marca la casilla "Add Python to PATH"
4. Verifica la instalación abriendo Command Prompt y ejecutando:
   ```cmd
   python --version
   pip --version
   ```

#### **macOS:**
1. Instala Homebrew (si no lo tienes):
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
2. Instala Python:
   ```bash
   brew install python
   ```

#### **Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

### 2. **Instalar GitHub Desktop**

#### **Windows:**
1. Ve a [desktop.github.com](https://desktop.github.com/)
2. Descarga GitHub Desktop para Windows
3. Ejecuta el instalador y sigue las instrucciones
4. Inicia sesión con tu cuenta de GitHub o crea una nueva

#### **macOS:**
1. Ve a [desktop.github.com](https://desktop.github.com/)
2. Descarga GitHub Desktop para macOS
3. Arrastra la aplicación a la carpeta Applications
4. Inicia sesión con tu cuenta de GitHub

#### **Linux:**
GitHub Desktop no está disponible oficialmente para Linux. Alternativas:
- **GitKraken**: [gitkraken.com](https://www.gitkraken.com/)
- **Git GUI**: Instalado con Git
- **VS Code**: Con extensión de Git integrada

### 3. **Instalar Cursor Desktop (Asistente de Código con IA)**

#### **Windows:**
1. Ve a [cursor.com/downloads](https://cursor.com/downloads)
2. Descarga la versión de Windows:
   - **Windows (x64) (User)** - Para instalación de usuario (recomendado)
   - **Windows (ARM64) (User)** - Para procesadores ARM
   - **Windows (x64) (System)** - Para instalación del sistema
   - **Windows (ARM64) (System)** - Para procesadores ARM del sistema
3. Ejecuta el instalador y sigue las instrucciones
4. Abre Cursor y configura tu cuenta (opcional pero recomendado)
5. Cursor incluye Git integrado, por lo que no necesitas GitHub Desktop si prefieres usar Cursor

#### **macOS:**
1. Ve a [cursor.com/downloads](https://cursor.com/downloads)
2. Descarga la versión de macOS:
   - **Mac Universal** - Compatible con Intel y Apple Silicon (recomendado)
   - **Mac (ARM64)** - Solo para Apple Silicon (M1/M2/M3)
   - **Mac (x64)** - Solo para procesadores Intel
3. Arrastra la aplicación a la carpeta Applications
4. Abre Cursor desde Applications
5. Configura tu cuenta para acceso a funciones avanzadas de IA

#### **Linux:**
1. Ve a [cursor.com/downloads](https://cursor.com/downloads)
2. Descarga la versión de Linux según tu arquitectura:
   - **Linux AppImage (x64/ARM64)** - Ejecutable portable (recomendado)
   - **Linux .deb (x64/ARM64)** - Para Debian/Ubuntu
   - **Linux RPM (x64/ARM64)** - Para Red Hat/Fedora/OpenSUSE
3. Instala según el formato descargado:
   ```bash
   # Para AppImage (hacer ejecutable)
   chmod +x cursor-*.AppImage
   ./cursor-*.AppImage
   
   # Para Debian/Ubuntu (.deb)
   sudo dpkg -i cursor-*.deb
   
   # Para Red Hat/Fedora (.rpm)
   sudo rpm -i cursor-*.rpm
   ```
4. Abre Cursor desde el menú de aplicaciones

#### **Características de Cursor:**
- **Asistente de código con IA**: Genera código automáticamente
- **Chat con IA**: Pregunta sobre tu código y recibe respuestas contextuales
- **Git integrado**: Control de versiones sin necesidad de herramientas adicionales
- **Soporte para múltiples lenguajes**: Python, JavaScript, HTML, CSS, etc.
- **Compatible con extensiones de VS Code**: Reutiliza tu configuración existente

## Instalación y ejecución del Dashboard

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

## Uso del Dashboard

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
