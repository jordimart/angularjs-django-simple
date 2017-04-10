## Práctica con una guía para utilizar angular como front-end y django como backend

En este repositorio he estado realizando pruebas para aprender a unir angularjs 1.x con un server de django.

La idea básica  a parte de aprender es buscar la forma más óptima de juntar un frontend realizado con angular al estilo de Jhon Papa y orientado a componentes( Angular 2) con un servidor django.

El fichero Readme me servirá como diario de descripciones y resultados, por eso se irá modificando y mejorando por el tiempo.

Los objetivos son:

- Obtener una estrutura básica reutilizable en la que tenga un frontend y un backend claramente separados.

- Buscar la forma más idónea de tener una aplicación con un deploy sencillo.

- Buscar la forma más idónea de poder desarrollar la aplicación sin tener en cuenta muchas configuraciones.

- Conectar Angular con django REST framework.

 ### Métodos y conclusiones: ###
 
 ### Método 1 ###

 Servir el index.html del cliente y su contenido estático desde el servidor al entrar en la ruta del dominio "/":

 En principio está idea me parece fenomenal, puedo tener el cliente y el servidor unidos solo por un index htmal.

 El deploy a priori puede resultar muy fácil en cualquier plataforma como mi vps o Heroku ya que solo instanciaría un servidor.

#### Resultado: ####

He conseguido servir el index html y parte del contenido estático de css y js, pero los ficheros json de traducción no los sirve,
los ficheros de imágenes que tienen las rutas en el html tampoco las ha servido.

He tenido que añadir a mano las etiquetas {% static %} para añadir los contenidos comprimidos en el index de la carpeta build. He buscado la forma de
servir el contenido en bloque pero no he encontrado nada que funcione, hay que añadir las tags por importación.

#### Conclusiones: ####

Sigo pensando que sería la forma ideal de trabajar para después tener un deploy único de django, con una instancia.

Veo que el desarrollo se complicaría ya que los cambios no serían refrescados como en el server de nodejs.

No sirvo por completo el contenido.

Por el momento probarélaopción de dos servidores para ver si es mas factible y poder comparar.

### Método 2 ###

Conectar mediante cross-domain Angular y django utilizandodos instancias.

Para trabajar con dos servidores es necesario utilizar cross domain y esto nos permitirá realizar conexiones ajax desde diferentes dominios
y de esta forma poder conectar los dos servidores.

El siguiente paso es instalar la API_REST FRAMEWORK de Djangoy realizar un get para recoger un listado.

#### Resultado: ####

He conseguido configurar el cros-domain, aunque la parte de angular no me quedo clara o no he sabido donde colocarla, la respuesta ha sido correcta.
Realizo la prueba de quitar el acceso en el Server y me responde como que no hay servidor.

La instalación sencilla mediante un tutorial de la API_REST también ha funcionado bien, de momento ya consigo listar el modelo de restaurantes en un console.log() con lo cual ya recibo los datos.
 
#### Conclusiones: ####

A pesar de tener dos instancias de servidor abiertas  de esta forma el cliente me trabaja bien sin tener que realizar grandes cambios.
Por lo menos para desarrollar es mas fácil y mas ágil.

Las pruebas de la API las realicé primero mediante shell de django, después mediante un mini server llamdo httpie y finalmente añadí la petición al código deAngular y pude ver el resultado.








 