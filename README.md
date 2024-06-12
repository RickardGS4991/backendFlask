# Proyecto backend con CLEAN architecture

##Indice
*[Introducción](#Introducción)
*[Proceso](#Proceso)
*[Tecnologías](#Tecnologías)

## 💻Introduction
Se desarrolló una API REST con Flask el cuál consume información desde una base de datos SQL y una colección de datos JSON. Además de esto, se aplicó una arquitectura CLEAN en el proyecto, por lo que es flexible y escalable para su expansión. Finalmente, la aplicación fue puesta en un docker para su correcto funcionamiento en diferentes máquinas.

## 🛠️Proceso
Para probar esta aplicación, es necesario que usted tenga docker instalado en su máquina. Solo tiene que clonar el repositorio. Después, en la terminal, accede a la carpeta donde se encuentra clonado este repositorio. Aquí usted va a escribir la siguiente línea de comando en su terminal 

### docker-compose up --build

IMPORTANTE: Recuerde iniciar sesión en su aplicación Docker, de lo contrario, no va a funcionar la linea de comando.

Una vez que escribió la linea de comando anterior, podrá visualizar su contenedor en la aplicación docker. Si al ejecutar la linea de comandos anterior, aparece esto en su terminal:


Quiere decir que la ejecución fue un éxito. Si aparece un error relacionado a los puertos, simplememte cierre el proceso que se desarrolla en los puertos 3308:3306 o en el 4000:4000 (O cambielos en el archivo docker-compose.yml).

Para acceder a la API, utilice la siguiente liga http://127.0.0.1:4000/nombreDeLaRuta/. En esta aplicación solo hay dos modulos:

1. questions
2. flights

Por lo que si quiere acceder a la ruta del primer módulo, simplemente escriba http://127.0.0.1:4000/questions/, y podrá visualizar todos los datos. Si quiere acceder al endpoint de flights, simplemente escriba http://127.0.0.1:4000/flights/, y podrá visualizar la información almacenada en la base de datos SQL en el contenedor. Además, cada módulo tiene más rutas para una acción diferente. Solo cheque en el directorio application.route, y podrá visualizar los endpoints de cada módulo.

## 🎥Descripción
Cada módulo de este proyecto tiene la siguiente estructura

- Application
- Domain
- Data

En Application, podremos visualizar la lógica de la experiencia del usuario o la visualización de datos. Es decir, cómo le vas a mostrar la información de tu base de datos al usuario. En Domain, se encarga de la lógica de negocios de la aplicación. Es decir, de las reglas de negocio fundamentales, y como se van a desarrollar. Finalmente, Data se encarga de la lógico para el acceso de datos a la base. La regla fundamental en la CLEAN architecture es la separación de responsabilidades (SoC) para mantener un código limpio y fácil de mantener. 

Por esa razón, decidí crear una API REST en Flask con esta arquitectura. No hay mucha información al respecto para desarrollar el principio de inversión de dependencias. No obstante, no es algo ajeno a mis conocimientos, dado que ya lo he aplicado en aplicaciones con ExpressJS o React. Además, el uso de esta arquitectura te permite realizar de una manera más sencilla pruebas unitarias (se agregarán en el próximo commit). 

## 📺Tecnologías
- Flask (Python):
  - Librerías:
    1. flask-injector
    2. SQLAlchemy
    3. injector
- MySQL
- Docker
- Angular (Próximamente)
