# *MANUAL DE USO DEL SISTEMA PRESTAFACIL*

## **1. Introducción**
> PrestaFacil es un sistema desarrollado en Python para la gestión de préstamos de artículos entre usuarios. Permite registrar usuarios, registrar artículos, realizar préstamos, gestionar devoluciones, generar certificados y facturas en formato PDF, consultar artículos prestados y administrar la información general del sistema.
> Este manual está dirigido a personas que no poseen conocimientos de programación y explica paso a paso cómo utilizar el sistema correctamente.

## **2. Requisitos para ejecutar el sistema**
- Antes de utilizar PrestaFacil es necesario contar con:
- Python instalado.
- Biblioteca ReportLab instalada.
- Archivos del proyecto dentro de la carpeta obligatoria `src`:
  - `principal.py`
  - `funciones.py`

> Para iniciar el sistema se debe ejecutar el archivo central: `principal.py`

## **3. Menú Principal**
- Al iniciar el programa aparecerá el siguiente menú interactivo en consola:
  1. Registrar Usuario
  2. Registrar Item
  3. Registrar Préstamo
  4. Registrar Devolución
  5. Consultar Items con más de 30 días
  6. Consultar Artículos Prestados
  7. Administrador
  8. Salir
- Cada opción cumple una función específica detallada a continuación.

## **4. Registrar Usuario**
- Permite registrar una nueva persona dentro del sistema a través de la opción 1.
- **Datos solicitados:**
  - Número de cédula.
  - Nombre.
  - Apellido.
  - Correo electrónico.
  - Tiempo límite de préstamo.
- **Restricciones del sistema:**
  - La cédula debe contener únicamente números.
  - El nombre y apellido no pueden contener números.
  - El correo debe tener un formato válido.
  - Los tiempos permitidos son estrictamente: 5 días, 10 días, 15 días o 30 días.
- Si el registro es correcto, el sistema mostrará un mensaje de confirmación en la consola.

## **5. Registrar Ítem**
- Permite registrar un artículo que podrá ser prestado posteriormente a través de la opción 2. Pero solo con el usuario y la contraseña del administrador.
- **Datos solicitados:**
  - Nombre del ítem.
  - Categoría.
  - Precio de compra.
  - Estado del artículo.
- **Categorías disponibles:**
  1. Videojuegos
  2. Libros
  3. Música y video
  4. Herramientas
  5. Dinero
  6. Misceláneo y varios
- El sistema genera automáticamente un identificador único para cada artículo (ejemplos: `VID1`, `LIB2`, `HER3`).
- **Estados del artículo según escala numérica:**
  - Excelente (80 a 100)
  - Bueno (50 a 79)
  - Regular (1 a 49)

## **6. Registrar Préstamo**
- Permite prestar un artículo a un usuario registrado a través de la opción 3.
- **Procedimiento:**
  1. Ingresar la cédula del usuario.
  2. Seleccionar uno de los artículos disponibles en el inventario.
  3. Confirmar la transacción del préstamo.
- **Una vez prestado:**
  - El artículo deja de aparecer como disponible en el sistema.
  - El sistema registra internamente la transacción.

## **7. Registrar Devolución**
- Permite devolver un artículo prestado a través de la opción 4.
- **Procedimiento:**
  1. Ingresar la cédula del usuario.
  2. Indicar cuántos días tuvo el artículo en su posesión.
- **Posibles resultados:**
  - **Devolución a tiempo:** Si el usuario devuelve el artículo dentro del plazo permitido, el artículo vuelve al inventario disponible y se genera automáticamente un certificado de devolución en formato PDF.
  - **Devolución fuera de tiempo:** Si el usuario supera el tiempo permitido originalmente, el préstamo queda marcado bajo el estado de mora y el sistema informará el incumplimiento.

## **8. Consultar Ítems con Más de 30 Días**
- Esta opción (número 5) revisa todos los préstamos que fueron marcados previamente en mora.
- **Si existen préstamos incumplidos:**
  - Se genera una factura de venta automatizada en PDF.
  - El artículo se considera vendido de forma definitiva.
  - El préstamo se cierra automáticamente dentro de las estructuras de datos.
- Si no existen usuarios en estado de mora, el sistema lo informará textualmente.

## **9. Consultar Artículos Prestados**
- Muestra de forma organizada todos los artículos que actualmente se encuentran bajo préstamo a través de la opción 6.
- **La información presentada incluye:**
  - ID del artículo.
  - Nombre del artículo.
  - Nombre del usuario correspondiente.
  - Cédula.
  - Días de préstamo pactados.
- Los registros se muestran ordenados algorítmicamente por la cantidad de días de préstamo.

## **10. Módulo Administrador**
- Permite consultar estadísticas generales y contables del sistema mediante la opción 7.
- **Credenciales de acceso requeridas:**
  - **Usuario:** `admin`
  - **Contraseña:** `yo12345`
- **Información analítica disponible:**
  - Total de préstamos registrados.
  - Total de devoluciones realizadas.
  - Total de ventas realizadas.
  - Total de dinero recaudado por concepto de ventas.
  - Listado de artículos vendidos.
  - Listado de usuarios registrados en el sistema.
  - Identificación del usuario con mayor cantidad de préstamos.
  - Identificación del usuario con menor cantidad de préstamos.

## **11. Archivos PDF Generados**
- El sistema compila y genera automáticamente dos tipos de reportes de forma vectorial:
- **Certificado de Devolución:** Se genera cuando el usuario devuelve un artículo dentro del plazo establecido. Contiene el nombre del usuario, ID del artículo y la fecha exacta de devolución.
- **Factura de Venta:** Se genera cuando un artículo entra en proceso de venta automática por incumplimiento mayor a 30 días. Contiene el nombre del usuario, ID y nombre del artículo, valor base del artículo, impuesto del 23% aplicado por mora y el total neto a pagar.

## **12. Salir del Sistema**
- La opción 8 permite finalizar la ejecución del programa de manera segura.
- Al seleccionarla, se limpiará el flujo, se mostrará un mensaje de despedida y el programa terminará su ejecución en la consola de Spyder.

## **13. Recomendaciones**
- Registrar primero los usuarios antes de intentar realizar un préstamo.
- Registrar detalladamente los artículos en el inventario antes de prestarlos.
- Verificar cuidadosamente el número de cédula ingresado para evitar colisiones.
- Mantener los archivos PDF generados de forma local como evidencia de devoluciones y ventas.
- Utilizar únicamente las credenciales autorizadas para acceder a las métricas del módulo administrador.

> Fin del Manual de Usuario.
