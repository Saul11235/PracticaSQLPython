# Practica SQL en Python
 practica de scripts de python usando lenguaje sql,

# conceptos comunes 
 los sistemas de gestión de Bases de Datos Relacionales,
 o comunmente llamadas *RDBMS* relational database
 management system.
 existen dos tipos de estos sistemas.

- ***SQL***    almacena los datos en tablas
- ***No SQL*** en diferentes formatos json, bson, etc

 las operaciones mas comunes son:
- ***C*** create 
- ***R*** read
- ***U*** update
- ***D*** delete
para hacer estas operaciones hacemos *querys* o consultas

# nociones al momento de trabajar con tablas
 al momento de crear y registrar valores, estos se 
 relacionan a un ID(primary key), un numero automaticamente creado
 para relacionarse a esta fila. por ejemplo:

***Usuarios.bd***
|id |nombre    |edad  |pais |
|---|----------|------|-----|
|1  |Mario     |18    |PE   |
|2  |Mark      |38    |US   |
|3  |Juana     |40    |VE   |

cada *fila* equivale a un *registro*, y cada valor en la
tabla, incluyendo el id es llamado *dato*, la agrupación de
todos estos datos constituyen ***información*** por ejemplo si 
tuvieramos estos datos podriamos relacionarlos con esta otra
tabla.

***Productos.bd***
|id |producto  |cantidad|creado-por|
|---|----------|--------|----------|
|1  |Manzanas  |100     |1         |
|2  |Peras     |10      |3         |
|3  |Naranjas  |31      |1         |
|4  |Papayas   |32      |2         |

en este caso un usuario puede ser relacionado a varios productos
pero un producto se relaciona a un único usuario, esto se llama *1->n*
en caso de que queramos hacer una relación de *n->n* tendremos que 
hacer una tabla intermedia.

recordemos que el id de cada tabla se llama *primary key*, entonces los
datos de estos en nuevas columnas se llamara *foreign key* por ejemplo.

***Compras.bd***
|id |usuario_id|producto_id|cantidad|
|---|----------|-----------|--------|
|1  |1         |3          |100     |
|2  |2         |3          |40      |
|3  |1         |4          |20      |

esta relacion se llama *n->n*, puesto que relaciona varios datos con 
varios datos.

# notas adicionales
en este repositorio, usarmemos scripts de python usando el modulo
sqlite3, para probar las insturcciones de SQL, por lo que los modulos
de la carpeta */ejemplos*, usando la libreria estadar de python.

