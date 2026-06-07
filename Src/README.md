# *9. Algoritmo*

## **Estructura del código fuente**
> El código fuente del proyecto está completamente organizado y contenido dentro de la carpeta obligatoria `src`. El software se diseñó bajo una arquitectura modular para separar la interfaz de usuario de las reglas lógicas del negocio.

- **`principal.py`:** Es el archivo central y el punto de entrada del programa. Contiene el ciclo infinito `while True`, la impresión del menú principal estructurado con `match-case`, el manejo visual del arte ASCII y las llamadas directas a las funciones de control.
- **`funciones.py`:** Archivo que actúa como la librería interna del sistema. Aquí se encuentran alojadas todas las funciones de validación de cadenas de texto, verificación de rangos de cédulas, generadores de identificadores únicos indexados y los algoritmos para compilar reportes vectoriales en PDF usando la librería ReportLab.

## **Instrucciones para la ejecución**
1. Asegúrese de tener instalada la librería ReportLab en su entorno de Python (`pip install reportlab`).
2. Abra la carpeta `src` en su entorno de desarrollo (Spyder).
3. Ejecute el archivo `principal.py` para inicializar la consola interactiva de **PrestaFacil**.
