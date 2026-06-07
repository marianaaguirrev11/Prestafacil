# *Manual de usuario - PrestaFacil*
## **Introducción**
> Este manual proporciona las intrucciones detalladas para operar el sistema de gestión de préstamos PrestaFacil. El programa funciona mediante una interfaz de consola interactiva y requiere ingresar las opciones númericas correspondientes.

## **Instrucciones de uso por módulos**

### **1. Registro de usuarios**
- Selecciones la opción 1 en el menú principal.
- Ingrese el número de cédula del cliente (debe tener entre 3 y 15 dígitos numéricos).
- Digite el nombre y el apellido por separado (el sistema rechazará textos que contengan números).
- Ingrese el correo electrónico institucional o personal del usuario.
- Defina el tiempo estimado de préstamo que solicita el usuario. (5,10,15 o 30 días).

### **2. Registro de ítems (Inventario)**
- Seleccione la opción 2 en el menú principal.
- Ingrese las credenciales de administrador obligatorias para desbloquear el acceso.
- Digite el nombre del artículo (mínimo 3 caracteres).
- Seleccione una categoría del menú numérico (1. Videojuegos, 2. Libros, 3. Música/Video, 4. Herramientas, etc.).
- Ingrese el precio de compra del artículo en valores numéricos mayores a cero.
- Califique el estado físico del ítem en una escala de 1 a 100 (el programa asignará automáticamente Excelente, Bueno o Regular).

### **3. Control de préstamos**
- Seleccione la opción 3 en el menú principal.
- Digite la cédula del usuario que solicita el préstamo. El sistema verificará que exista.
- Digite el ID del artículo solicitado (ej. V1, L2). El sistema comprobará que esté disponible.
- Al confirmarse, el artículo cambiará su estado automáticamente a no disponible.

### **4. Registro de devoluciones**
- Seleccione la opción 4 en el menú principal.
- Ingrese la cédula del usuario que va a realizar la entrega.
- Digite la cantidad de días reales que el usuario tuvo el artículo en su poder.
- Si la entrega es a tiempo, el sistema generará un **Certificado de Devolución** en PDF.
- Si el tiempo excede los 30 días, el sistema generará una **Factura de Venta por Incumplimiento** en PDF con un recargo del 23%.

### **5. Consultas e informes**
- **Opción 5 (Estado de préstamos):** Muestra de forma detallada la lista de artículos que se encuentran actualmente prestados.
- **Opción 6 (Consultar inventario):** Despliega el listado completo de los artículos registrados con sus respectivos códigos ID y estados de disponibilidad.

### **6. Módulo Administrador**
- Seleccione la opción 7 en el menú principal.
- Ingrese el usuario y la contraseña establecida.
- El sistema mostrará el balance contable con el total de ingresos por multas, la cantidad de préstamos activos y los usuarios con mayor y menor actividad en la plataforma.

## **Consideraciones del sistema**
> Las estructuras de datos operan en la memoria volátil del programa. Al cerrar la aplicación con la opción 8, los registros se reiniciarán.
> Todos los reportes en formato PDF se guardarán automáticamente en la carpeta raíz del proyecto con la nomenclatura correspondiente al usuario y artículo.
