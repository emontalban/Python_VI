## 1. Clases en Python
Las clases son estructuras que permiten definir un tipo de objeto agrupando datos (atributos) y comportamientos(funciones) que un objeto especifico tendrá. Son como plantillas o moldes para crear objetos. La convencion en python es usar para el nombre de la clase CamelCase.

Las clases se utilizan para organizar codigo  en estructruras logicas, representas entidades del mundo real, reutilizan codigo y aplican programacion orientada a objetos.

Ademas, permite organizar el codigo de forma modular y clara, facilitando la creacion de programas complejos mediante conceptos como la herencia y el encapsulamiento.

La herencia permite que una clase herede atributos y métodos de otra y el encapsulamiento consiste en ocultar los datos de un objeto asi se controla su acceso y protejen evitando que se modifique indebidamente.

Ejemplo de una clase
```python
class ProgrammingLanguage:
    def __init__(self, name, year, type_):
        self.name = name
        self.year = year
        self.type_ = type_

```
Cuando usar las clases:

Se usan las clases cuando vas a construir un programa  que va a crecer y necesitas crear muchas reutilizar en codigo y tu programa representa cosas del mundo real. 

En cambio cuando tienes un programa pequeño que no va a crecer como una automatizacion o un calculo simple , con una funcion es mas que suficiente y mas rapido de escribir



## 2. Método que se ejecuta automáticamente cuando se crea una instancia de una clase

El metodo que se ejecuta automaticamente cuando se crea una instancia de una clase es llama constructor.
Un constructor es un metodo especial de la clase que se ejecuta automaticamente en el momento en que se crea(intancia) un objeto, permitiendo inicializar sus atributos. Si no añades el constructor el programa no se rompe, pero no se inicializaran los atributos y obtendras un objeto vacio.

Se define con el metodo `__init__`, el doble guion bajo significa que este reservado para un uso especial del lenguaje, en este caso sería para el constructor.

```python
class Person:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

    def sayHello(self):
        print(f' Hello my name is {self.name}{self.last_name}')

# Creamos una instancia
jhon = Person("Jhon"," Doe")


#Probamos el resultado
jhon.sayHello()
```

## 3. Los tres verbos de API
En esta pregunta creo que se refiere al CRUD y yo tengo 4.   
Lo verbos de una API(llamados tecnicamente Métodos HTTP) que son las acciones que indican al servidor lo que queremos hacer con un recurso especifico. Las cuatro principales son crear, leer, actualizar y borrar que en ingles  forman un acronimo de CRUD (**C**reate, **R**ead, **U**pdate, **D**elete).

1. POST (Crear)  
   Se usa para enviar nuevos datos al servidor para que cree un nuevo registro.
2. GET (Leer)  
   Se  usa para pedir informacion al servidor. Solo es para consulta.
3. PUT (Actulizar)  
   Se usa para modificar algo que ya existe, se reemplaza por los nuevos datos.
4. DEL (Borrar)  
   Se usa para borrar un registro. 


## 4.MongoDB

MongoDb es un sistema de bases de datos NoSQL. A diferencia de las bases de datos tradicionales SQL no utilizan tablas con filas y columnas, sino que almacena la informacion en documentos con formato JSON.  
Se utiliza cuando los datos cambian rapidamente y no tiene estructura fija, tambien cuando se necesita escalar rapidamente. Es emplea para aplicaciones web , APIs y  sistemas en tiempo real.  

Una colección en MongoDB es un conjunto de documentos relacionados que se almacenan dentro de una base de datos.  

- Colección:  agrupa datos (equivale a una tabla en SQL)  
- Documentos:  cada elemento dentro de la colección  
- Campos: los datos de cada documento  



| SQL (tradicional) | MongoDB          |
| ----------------- | ---------------- |
| Tablas            | Colecciones      |
| Filas             | Documentos       |
| Columnas          | Campos           |

Este es un ejemplo de un documento, puede tener distintos tipos de datos.
```javascript
{
    _id: ObjectId('69c571b4a6cd3228e511403c'),
    name: 'Dart',
    year: 2011,
    creator: 'Google',
    type: 'compilado',
    paradigm: 'multiparadigma',
    popular_use: 'apps multiplataforma',
    extension: '.dart',
    frameworks: [ 'Flutter' ],
    libraries: [ 'http', 'provider' ],
  
  }
```
## 5.API
Una API (Application Progamming interfaz) es un conjunto de reglas que permite que dos aplicaciones se comunique entre si. Si ellas los programas no podrian compartir datos. 
Actua de como un intermediario que permite que un programa solicite informacion  a otro programa sin necsidad de conoces como esta construido internamente.
Las ventajas de usar una Api:
- Reutilizar: Permite usar funcionalidades, datos o servicios ya desarrollados en otros sistemas sin tener que implementar desde cero.
- Modularidad : Divide el sistemas en partes independientes, facilitando su desarrollo y mantenimiento
- Escalable:  Permite que crezca y soporte mas usuarios sin necesidad de  rediseñarla  completamente.
- Integracion: Facilita la conexion y comounicacion entre diferentes aplicaciones.

Vamos a explicarlo con una analogia sobre el tiempo paso a paso:
Tenemos una app del tiempo y queremos saber que tiempo va a hacer el fin de semana.
1. Tu *"usuario"* abres la app y pones la ciudad.
2. La App *"Cliente"* es lo que vemos los botones, el cuadro de texto donde introducimos la ciudad, las imagenes, etc... solo diseño, no sabe que tiempo hace.
3. El Servidor Meteorologico *"Servidor"*  es donde se almacenan y se guardan los datos del tiempo.
4. La API *"mensajero"* es el puente que conecta la app con el servidor meterologico, enviado la peticion y devolviendo la respuesta.



## 6.Postman

Es una herramienta que permite probar, crear y trabajar con APIs de forma sencilla, sin tener necesidad de programar una aplicacion completa. Se utiliza principalmente para enviar petiiones HTTP como GET, PUT, POST y DELETE a un servidor y ver las respuestas que devuelve.

Un ejemplo practico imagina que queremos hacer una app de Pokemon.

Queremos que la app muestre los datos del pokemon, ej: habilidades, nombre, tipo, etc..., antes de que programar nada en tu proyecto puedes probar si la api funciona y para ello se hace una prueba con postman a ver si te devuelve los datos.
Si en el postman le haces una peticion GET https://pokeapi.co/api/v2/pokemon/charizard postman de devuelve por un lado un 200 OK significa que funciona que te ha devuelto los datos y por otro te devuelve un Json con los datos.

En este caso solo puedes hacer GET, pero se podria crear nuestra propia API y enviar las peticiones que fuesen necesarias.



## 7.Polimorfismo

El poliforfismo es un principio de programacion orientada a objetos que permiten que diferentes clases respondan al mismo metodo pero de manera distinta.  
Se basa en la idea de un mismo mensaje (llamada a un metodo )puede producir diferentes resultados dependiendo del objeto que lo recibe.
En resumen la palabra viene de (poli=muchos, morfismo=formas) lo que significa: una misma accion que toma muchas formas.
Para que funcione las diferentes clases han de compartir un metodo identico, por ello suele ir acompañado de la herencia de clases

Ejemplo:
```Python
cclass Restaurant:
    def __init__(self,name):
        self.name = name
    
    def menu(self):
        return 'Menu of the restaurant'

class Vegan(Restaurant):
    def menu(self):
        return f'{self.name}: 100% vegan and healthy menu'

class Burger(Restaurant):
    def menu(self):
        return f'{self.name}: Menu with hamburgers and french fries'


restaurant_vegan = Vegan("The Green Spoon")
restaurant_burger = Burger("The Stackhouse")

# Llamamos al mismo método, pero cada clase responde diferente
print(restaurant_vegan.menu()) # The Green Spoon: 100% vegan and healthy menu
print(restaurant_burger.menu())  # The Stackhouse: Menu with hamburgers and french fries

```

En este ejemplo tenemos una clase Padre llamada Restaurant y dos clases hijas (Vegan y Burger) todas tienen el mismo metodo `menu()` pero cada una responde distingo segun su implementacion.

## 8.Método dunder

Son metodos que comienzan y acaban con dos guiones bajos, por ejemplo `__init__`, `__str__`.  
La palabra `dunder` viene de **d**ouble **under**score. Se utilizan para definir comportamientos especiales de objetos y permiten que las clases interactúen con operadores o funciones integradas en python.
Los metodos dunder permiten que los objetos se comportes como tipos nativos de python, por ejemplo:
```python

a+b # Llama a a.___add__(b)
len(objeto)   # llama a objeto.__len__()
print(objeto) # llama a objeto.__str__()

```

Python tiene la filosofía de “todo es objeto”. Para que todas las operaciones estándar funcionen con cualquier tipo de objeto, necesitaba un mecanismo uniforme para que los objetos respondieran a operadores y funciones integradas.

Ejemplo:

- Cuando haces print(obj), Python internamente necesita una forma consistente de convertir cualquier objeto en texto.  
- Para eso, llama al método especial` __str__ `del objeto.  
- Si no existiera `__str__`, Python no tendría forma de saber cómo representar tu objeto como cadena.  

Los métodos dunder son la interfaz estándar que Python usa para operar con todos los objetos, sin importar si son objetos propios o creados por el usuario.
Ejemplo:

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


p = Persona("Keira", 30)
print(p) # <__main__.Persona object at 0x000001B458C98C20>

```
Lo que sucede aqui es que te esta mostrando que es un objeto y en que posicion de memoria esta guardado. Para que te muestre el nombre y la edad habe que usar un metodo dunder como por ejemplo `__str__`
```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"


p = Persona("Keira", 30)
print(p) # Nombre: Keira, Edad: 30
```
Aqui si  imprime el nombre y edad
## 9.Decorador 

Los decoradores son una herramienta que permite modificar el comportamiento de una funcion sin cambiar su codigo original es como envolver una funcion dentro de otra.  
Una Analogia:  
Una llave es una funcion que abre una puerta, si añadimos un decorador en este caso un llavero con nombre, no cambia la forma de la llave, pero sabes que puerta abre.   
La sintaxis es la `@` seguido del nombre del decorador.     
`@mi_decorador`  
El python los decoradores `@property`y `@<propiedad>setter`  se usan para controlar como se acceden y modifican los atributos de una clase. De esta manera se encapsulan los datos protegiendolo, tambien se valida la informacion antes de modificarla.  

Ejemplo
```python
class Language:
    def __init__(self, name, kind):
        self._name = name         
        self.kind = kind      


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, valor):
        self._name = valor     


    @property
    def kind(self):
        return self._kind

    @kind.setter
    def kind(self, valor):
        if valor.lower() in ['interpretado', 'compilado']:
            self._kind = valor
        else:
            self._kind =  "Error: el tipo  debe ser 'interpretado' o 'compilado'"

    
    def info(self):
        return f"{self._name} - {self._kind}"


python = Language("Python", "interpretado")
java = Language("Java", "compilado")
rust = Language("Rust","dinamico")

print(python.info())
print(java.info())
print(rust.info())
```

Vamos a desglosarlo:
- el guion bajo delante del nombre de los atributos `_name`sirve guarda el nombre como atributo privado. 
- Para poder acceder a los atributos fuera de la clase se crean los getter y setters.
- En el caso de el segundo atributo el setter valida que solo se puede asignar 'interpretado' o 'compilado'.

