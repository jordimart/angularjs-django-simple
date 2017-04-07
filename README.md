## Práctica con una guía para utilizar angular como front-end y django como backend

En este repositorio he estado realizando pruebas para aprender a unir angularjs 1.x con un server de django.

La idea básica  a parte de aprender es buscar la forma más óptima de juntar un frontend realizado con angular al estilo de Jhon Papa y orientado a componentes( Angular 2) con un servidor django.

El fichero Readme me servirá como diario de descripciones y resultados, por eso se irá modificando y mejorando por el tiempo.

Los objetivos son:

- Obtener una estrutura básica reutilizable en la que tenga un frontend y un backend claramente separados.

- Buscar la forma más idónea de tener una aplicación con un deploy sencillo.

- Buscar la forma más idónea de poder desarrollar la aplicación sin tener en cuenta muchas configuraciones.

- Conectar Angular con django REST framework.

 Ideas y conclusiones:

 1- 7/4/2017: Servir el index.html delcliente y su contenido estático desde el servidor al entrar en la ruta del dominio "/":

 En principio está idea me parece fenomenal, puedo tener el cliente y el servidor unidos solo por un index htmal.

 El deploy a priori puede resultar muy fácil en cualquier plataforma como mi vps o Heroku ya que solo instanciaría un servidor.

 