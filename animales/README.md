# Proyecto Unidad 2

El zoológico de Morelia requiere un sistema para poder administrar todas sus operaciones, así como poder llevar la gestión de todo su personal / visitante / animales.

El director del zoológico require que el sistema pueda contar primeramente con una opción para poder registrar a todos sus empleados, considera que la información más importante de ellos es la siguiente.

| Nombre | Apellidos |
| --- | --- |
| Fecha de nacimiento | Fecha de ingreso como trabajador |
| RFC | CURP |
| Salario | Horario |
| Rol (existen los siguiente tipos: Veterinario, Guía, Mantenimiento, Administración) |  

De igual forma, le gustaría poder almacenar toda la información de sus visitantes, y de esta forma, contar con promociones para los visitantes más frecuentes. De los visitantes se require la siguiente información.

| Nombre | Apellidos |
| --- | --- |
| Fecha de nacimiento | CURP |
| Número de visitas (inicialmente comienza en 0) | Fecha de registro |

Al director del zoológico le gustaría contar con una opción para poder registrar cada vez que haya una visita en el zoológico (el precio del boleto por persona es de $100 MXN por adulto y $50 MXN por niño). Por lo tanto, cada que un visitante llegue al zoológico, desea que en el sistema pueda registrar esa visita y que en esa ella se guarde el guía que estará a cargo de ella, así como los visitantes que formarán parte de ella. Es decir, una visita es guiada por un guía y puede tener uno o muchos visitantes en ella. Es necesario recordar que al momento de que se registra una visita, el atributo de ***número de visitas*** del cliente debe de aumentar en 1, ya que cada 5 visitas, el visitante tendrá un descuento del 20% en su boleto. Resumiendo lo anterior, el director desea que al momento de registrar una visita se registre lo siguiente.

| Guía a cargo | Visitantes [] |
| --- | --- |
| Costo total de la visita (la suma de los boletos de los visitantes) | Fecha de la visita |
| Cantidad de niños (se puede calcular con las fechas de nacimiento) | Cantidad de adultos (se puede calcular con las fechas de nacimiento) |

En cuanto a los animales, el director desea que cada vez que llegue un nuevo animal, se registre lo siguiente.

| Tipo animal | Fecha nacimiento |
| --- | --- |
| Fecha llegada al zoológico | Peso |
| Enfermedades (Será un arreglo de cadenas en caso de que cuente con alguna/s) | Frecuencia de alimentación |
| Tipo de alimentación | Cuenta con vacunas (valor booleano) |

De igual forma, desea que al momento de darle de comer a los animales o realizar algún mantenimiento, el sistema lleve un control de todo eso y guarde la información siguiente.

| Empleado que encargada (debe ser un empleado con el rol de mantenimiento) | ID del animal |
| --- | --- |
| Proceso que se realizó (Mantenimiento, limpieza, alimentación, etc) | Fecha del proceso |
| Observaciones (opcional) |  |

Por último, el director desea que para los empleados, animales y visitantes pueda realizar las siguientes operaciones.

- Registro
- Modificación (Siempre y cuando no rompa alguna relación como las visitas, mantenimientos, etc)
- Eliminación (Siempre y cuando no rompa alguna relación como las visitas, mantenimientos, etc)
- Consulta

Para las visitas y los mantenimientos desea también que se cuente solo con la opción de registro y de consulta, no se podrán eliminar ni modificar una vez registradas.

De igual forma, desea que se cuente con una contraseña para que solo el tenga acceso al sistema y pueda realizar todo lo descrito con anterioridad.

***INTEGRANTES DEL EQUIPO***
- Manuel Alberto Tena García
- Miguel Angel Medina García
- Miguel Angel Contrera Ceballos
