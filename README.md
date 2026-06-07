# **PrestaFácil**

# *Integrantes*
## **Mariana Aguirre Vidales**
### Descripción
> Estudiante de Ingeniería Industrial en la Universidad de Antioquia, 18 años. Es organizada y trabaja en equipo. Se adapta facilmente y aporta ideas para desarrollar el proyecto de forma clara y eficiente. 
## **Fabio Alberto Bravo Charris**
### Descripción
> Estudiante de Ingeniería Industrial, 18 años. Vive en Medellín, pero nació en Montería, Córdoba. Es creativo, trabaja bien en equipo y se adapta facilmente a diferentes entornos. Se destaca por su comunicación asertiva, amabilidad y resiliencia.

# *Detalles proyecto*
> PrestaFácil es una plataforma de servicios financieros enfocada en la gestión de préstamos de forma rápida, segura y accesible. La herramienta permite el acceso únicamente a usuarios registrados, validando su identidad antes de realizar cualquier operación. Además, gestiona préstamos y devoluciones, genera recordatorios y notificaciones según el tiempo de uso, y emite certificados y facturas en caso de incumplimiento.

![Imagen](Img/3%20sin%20título_20260405140642.png)

# *Licencia*
<a href="https://github.com/marianaaguirrev11/Prestafacil">PrestaFacil</a> © 2026 by <a href="https://github.com/fabiobrav0, https://github.com/marianaaguirrev11">Mariana Aguirre - Fabio Bravo</a> is licensed under <a href="https://creativecommons.org/licenses/by-nc-nd/4.0/">CC BY-NC-ND 4.0</a><img src="https://mirrors.creativecommons.org/presskit/icons/cc.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;"><img src="https://mirrors.creativecommons.org/presskit/icons/by.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;"><img src="https://mirrors.creativecommons.org/presskit/icons/nc.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;"><img src="https://mirrors.creativecommons.org/presskit/icons/nd.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;">
# *Soporte de vision*
> PrestaFaćil es un sistema de gestión de préstamos desarrollado en Python que permite registrar usuarios, administrar ítems, controlar préstamos y devoluciones, y generar reportes como certificados y facturas.
El objetivo del sistema es facilitar la organización y control de objetos prestados, evitando pérdidas de información y mejorando el seguimiento de cada préstamo.
Como beneficios, el sistema permite automatizar procesos, reducir errores humanos, mejorar la trazabilidad de los préstamos y ofrecer una solución eficiente y fácil de usar mediante una interfaz en consola.

# *Requisitos de función*
## **Requisitos funcionales**
- Registrar usuarios con validaciones.
- Registrar ítems con categoría, precio, ID y estado.
- Realizar pŕestamos solo a usuarios registrados.
- Registrar devoluciones de préstamos activos.
- Generar certificados de devolución.
- Generar venta automática de ítems con más de 30 días.
- Calcular subtotal, impuesto (23%) y total.
- Consultar estado de préstamos.
- Acceder a módulo administrador con usuario y contraseña.
- Generar reportes (préstamos, devoluciones, ventas).

# *Plan de proyecto*
## **Actividades**
- Análisis del problema
- Diseño del sistema
- Desarrollo del código
- Pruebas del sistema
- Documentación (README y manual)
- Subida a GitHub

# *Cronograma “Diagrama de Gantt"*
![Imagen](Img/plan)

# **Presupuesto**
> El proyecto es desarrollado por dos estudiantes, con una dedicación total de 50 horas de trabajo. Estas horas se distribuyen equitativamente, correspondiendo a 25 horas por integrante.
> El valor del trabajo se estima como práctica profesional equivalente a 1, de acuerdo con los lineamientos del proyecto académico.
> Este presupuesto no presenta un pago real, sino una estimación del valor del tiempo invertido en el desarrollo del software.  

# *Plan de versionado*
## **Evolución del software**
- **Versión 0.1.0 (19 de mayo):** Creación del esqueleto general del programa en 'principal.py', diseño del menú interactivo con match-case y el título gigante en arte ASCII.
- **Versión 0.2.0 (24 de mayo):** Implementación del módulo de registro de usuarios con validaciones de longitud de cédula, control de formato de nombres y filtro para evitar datos duplicados.
- **Versión 0.3.0 (28 de mayo):** Creación del registro de ítems con asignación automática de ID por categoría, cálculo de estado físico y el filtro de seguridad con clave para el administrador.
- **Versión 0.4.0 (31 de mayo):** Conexión del sistema de préstamos en la opción 3, validando la existencia del usuario y cambiando la disponibilidad real del artículo a falso.
- **Versión 0.5.0 (3 de junio):** Módulo de devoluciones con cálculo de días utilizados y activación de alertas por infracción si el préstamo excede el tiempo límite de la plataforma.
- **Versión 1.0.0 (7 de junio):** Integración final de reportes corporativos en pdf con ReportLab usando líneas vectoriales, balance contable con impuesto del 23%, analítica del administrador y depuración del código. 
