## Prueba tecnica EdMachina con FASTAPI

1. Clonar Repositorio
2. Tener instalado docker y docker compose, correr comando: " docker-compose up --build "
3. Utilizar api para dar de alta registros atraves de swagger en la ruta, http://localhost:8000/docs

## Endpoints

## Degree

1. POST /degree, recibe un nombre para crear una carrera de grado.
2. GET /degree, recibe un id como parametro, y obtiene el nombre de la carrera, en caso de no existir devuelve un 404.

## Course

1. POST /courses, crea una materia o asignatura, recibe el nombre de la asignatura y el id del degree anteriormente creado.
   Debe existir por lo menos un Degree anteriormente para crear un Course.

## Lead

1. POST /leads, recibe los atributos de la persona, nombre, apellido telefono, email, y un arreglo de ID de materias.
   Los ID que se pasan en el arreglo deben existir en la tabla Course, tienen que existir o va a tirar error en la validacion.
2. GET /leads, se obtiene toda la informacion de leads paginada, con las materias que se anoto.
3. GET /leads/{lead_id} Atravez del ID se obtiene informacion de un lead en particular.
