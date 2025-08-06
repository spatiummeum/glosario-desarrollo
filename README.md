# 📖 Glosario de Programación

[![GitHub Stars](https://img.shields.io/github/stars/spatiummeum/glosario-desarrollo?style=social)](https://github.com/spatiummeum/glosario-desarrollo/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/spatiummeum/glosario-desarrollo?style=social)](https://github.com/spatiummeum/glosario-desarrollo/network/members)
[![Contributors](https://img.shields.io/github/contributors/spatiummeum/glosario-desarrollo)](https://github.com/spatiummeum/glosario-desarrollo/graphs/contributors)
[![License](https://img.shields.io/github/license/spatiummeum/glosario-desarrollo)](LICENSE)

> **Un glosario completo y comprensible de términos de programación, orientado especialmente a Desarrollo Web, JavaScript y Python.**

## 🎯 Acerca del Proyecto

Este glosario está diseñado para estudiantes, desarrolladores principiantes y cualquier persona que quiera comprender los conceptos fundamentales de la programación de manera clara y práctica. Cada término incluye:

- ✅ **Definición clara y sencilla**
- ✅ **Ejemplos prácticos**
- ✅ **Código de ejemplo** (cuando aplica)
- ✅ **Relación con JavaScript y Python**

## 🚀 Cómo Usar Este Glosario

1. **Busca por categoría** usando el índice de abajo
2. **Usa Ctrl+F** para buscar términos específicos
3. **Contribuye** agregando nuevos términos o mejorando los existentes

## 📚 Índice de Categorías

| Categoría | Descripción | Términos |
|-----------|-------------|----------|
| [🏛️ Conceptos Fundamentales](#🏛️-conceptos-fundamentales-de-programación) | Bases de la programación | 25+ términos |
| [📦 Programación Orientada a Objetos](#📦-programación-orientada-a-objetos-poo) | POO y conceptos relacionados | 20+ términos |
| [🌐 Desarrollo Web y Redes](#🌐-desarrollo-web-y-redes) | Tecnologías web e Internet | 15+ términos |
| [🖥️ Hardware y Sistemas](#🖥️-hardware-sistemas-y-arquitectura) | Arquitectura de computadoras | 20+ términos |
| [🧮 Tipos de Datos](#🧮-tipos-de-datos-y-operadores) | Datos y operadores | 15+ términos |
| [✍️ Sintaxis de Código](#✍️-estructura-y-sintaxis-de-código) | Estructura del código | 15+ términos |
| [🐛 Seguridad y Errores](#🐛-seguridad-y-errores) | Debugging y seguridad | 10+ términos |

## 🤝 Contribuir

¿Quieres ayudar a mejorar este glosario? ¡Genial! Aquí te explico cómo:

1. **Fork** este repositorio
2. **Crea** una nueva rama (`git checkout -b feature/nuevo-termino`)
3. **Agrega** tu término siguiendo el formato establecido
4. **Commit** tus cambios (`git commit -m 'Agrega término: NuevoTermino'`)
5. **Push** a la rama (`git push origin feature/nuevo-termino`)
6. **Abre** un Pull Request

### 📝 Formato para Nuevos Términos

```markdown
### Nombre del Término (English Name)

**Definición:** Explicación clara y sencilla del concepto.

**Ejemplo:** Ejemplo práctico o analogía para entender mejor.

**Ejemplo en Código (Lenguaje):**

```lenguaje
// Código de ejemplo bien comentado
```

## 🌟 Características Especiales

- 📱 **Responsive**: Se ve bien en cualquier dispositivo
- 🔍 **Navegación fácil**: Índice clickeable y búsqueda rápida
- 💡 **Ejemplos prácticos**: Código real que puedes probar
- 🎨 **Visualmente atractivo**: Emojis y formato limpio
- 🔄 **Constantemente actualizado**: La comunidad mantiene el contenido fresco

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

## 🙏 Agradecimientos

- A todos los [contribuidores](https://github.com/spatiummeum/glosario-desarrollo/graphs/contributors)
- A la comunidad de desarrolladores que comparte conocimiento
- A los recursos educativos que inspiraron este proyecto

---

---

## 🏛️ Conceptos Fundamentales de Programación

### Abstracción (Abstraction)

**Definición:** Es la técnica de enfocarse en "qué" hace algo, sin preocuparse por el "cómo" lo hace. Te permite usar una herramienta compleja a través de una interfaz simple, ocultando todos los detalles internos.

**Ejemplo:** Cuando conduces un auto, solo necesitas saber usar el volante, los pedales y la palanca de cambios (la abstracción). No necesitas conocer en detalle cómo funciona el motor de combustión interna o la transmisión para poder conducir (la implementación oculta).

**Ejemplo en Código (JavaScript):** Usas `fetch('https://api.example.com/data')` para obtener datos de un servidor. Sabes que te devolverá información, pero no necesitas saber todos los detalles complejos de los protocolos de red (HTTP, TCP/IP) que fetch maneja por debajo.

### Algoritmo (Algorithm)

**Definición:** Es una receta o una lista de pasos finitos y ordenados para resolver un problema o realizar una tarea. Es la lógica que le dice a la computadora exactamente qué hacer, paso a paso.

**Ejemplo:** Un algoritmo para iniciar sesión en un sitio web sería:

1. Pedir al usuario su email y contraseña.
2. Verificar que el email exista en la base de datos.
3. Si existe, comparar la contraseña ingresada con la guardada.
4. Si coinciden, dar acceso. Si no, mostrar un mensaje de error.

### Análisis (Analysis)

**Definición:** Es el proceso de estudiar un problema a fondo para entender qué se necesita construir. Antes de escribir código, analizas los requisitos para identificar qué debe hacer el sistema y cómo deben interactuar sus partes.

### Aplicación (Application)

**Definición:** Es un programa completo y funcional diseñado para ser utilizado por un usuario final. A diferencia de una simple pieza de código, una aplicación resuelve una necesidad específica.

**Ejemplo:** Una aplicación web de e-commerce, una app móvil de mensajería, o un programa de escritorio como VS Code. Tu proyecto de tercer semestre, aunque pequeño, es una aplicación.

### Biblioteca de clases (Class library)

**Definición:** Es una colección de código pre-escrito y reutilizable (en forma de clases) que puedes importar a tu proyecto para no tener que programar todo desde cero.

**Ejemplo:** En Python, la biblioteca requests es muy popular para hacer peticiones HTTP. En lugar de escribir todo el código de red tú mismo, simplemente la importas y usas sus clases y funciones para comunicarte con APIs.

### Bucle (Loop)

**Definición:** Es una estructura de control que permite repetir un bloque de código varias veces, ya sea un número fijo de veces o hasta que se cumpla una condición.

**Ejemplo en Código (Python):** Para mostrar una lista de productos en una página web, usarías un bucle:

```python
productos = ["Laptop", "Mouse", "Teclado"]
for producto in productos:
    print(f"Mostrando {producto} en la página...")
```

### Compilador (Compiler)

**Definición:** Es un programa traductor que lee todo tu código fuente (escrito en un lenguaje como C++ o Java) de una sola vez y lo convierte en un archivo ejecutable en lenguaje de máquina que la computadora puede entender directamente. Si encuentra un error, no genera el archivo.

**Relación con JS/Python:** JavaScript y Python son lenguajes interpretados, no compilados en el sentido clásico. No se genera un .exe. Sin embargo, detrás de escena, el motor de JavaScript (V8) y el intérprete de Python compilan el código a un formato intermedio (bytecode) para que se ejecute más rápido.

### Constante (Constant)

**Definición:** Es como una variable cuyo valor no puede ser cambiado una vez que ha sido asignado. Se usa para guardar datos que deben permanecer fijos a lo largo del programa.

**Ejemplo en Código (JavaScript):** Para definir la URL base de una API que no cambiará:

```javascript
const API_URL = "https://api.mi-ecommerce.com/v1";
```

### Datos (Data)

**Definición:** Es cualquier información que un programa manipula. Puede ser texto, números, imágenes, etc. Los programas reciben datos de entrada, los procesan y generan datos de salida.

### Depuración (Debugging)

**Definición:** Es el proceso de encontrar y corregir errores (bugs) en tu código. Es una tarea fundamental en la programación.

**Ejemplo:** Usas las "Herramientas de Desarrollador" del navegador (presionando F12) para ir línea por línea en tu código JavaScript y ver dónde los valores de las variables no son los que esperas.

### Depurador (Debugger)

**Definición:** Es una herramienta que te ayuda a depurar tu código. Te permite pausar la ejecución del programa en puntos específicos (breakpoints), inspeccionar el valor de las variables en ese momento y ejecutar el código paso a paso.

**Ejemplo:** El depurador integrado en Visual Studio Code, que puedes usar para tus proyectos de Python y JavaScript.

### Diagrama de flujo (Flowchart)

**Definición:** Es una representación gráfica de un algoritmo. Usa símbolos estandarizados (rectángulos para procesos, rombos para decisiones, óvalos para inicio/fin) conectados por flechas para mostrar el flujo de ejecución de un programa.

### Diagrama de N/S (Nassi-Schneiderman diagram)

**Definición:** Es una alternativa al diagrama de flujo para diseñar algoritmos de forma estructurada. En lugar de flechas, usa cajas anidadas para representar la secuencia, las decisiones y los bucles, lo que obliga a un diseño más ordenado.

### Diseño (Design)

**Definición:** Es la fase donde planificas cómo se va a construir el software. Defines la arquitectura, los componentes, los módulos, las interfaces y cómo interactuarán entre sí para cumplir con los requisitos del análisis.

### Función (Function)

**Definición:** Es un bloque de código reutilizable que realiza una tarea específica. Se le da un nombre y se le puede "llamar" desde otras partes del programa para ejecutar su tarea, opcionalmente pasándole datos (parámetros) para que trabaje con ellos.

**Ejemplo en Código (Python):**

```python
def saludar(nombre):
    return f"Hola, {nombre}!"

mensaje = saludar("Carlos") # Llamamos a la función
print(mensaje) # Imprime "Hola, Carlos!"
```

### Implementación (Implementation)

**Definición:** Es el acto de escribir el código real del programa, basándose en el diseño previamente definido. Es la fase donde las ideas se convierten en un software funcional.

### Informática (Computing/Informatics)

**Definición:** Es la ciencia que estudia el tratamiento automático de la información mediante computadoras. Abarca desde la teoría y el diseño de algoritmos hasta la creación de software y hardware.

### Intérprete (Interpreter)

**Definición:** Es un programa que lee y ejecuta tu código fuente línea por línea, traduciéndolo a lenguaje de máquina sobre la marcha. Si encuentra un error, se detiene en esa línea.

**Ejemplo:** Python y JavaScript son lenguajes interpretados. Cuando ejecutas un script de Python (`python mi_script.py`), el intérprete de Python lee la primera línea, la ejecuta, lee la segunda, la ejecuta, y así sucesivamente.

### Lenguaje de programación (Programming language)

**Definición:** Es un lenguaje formal con un conjunto de reglas (sintaxis y semántica) que los programadores utilizan para escribir instrucciones que una computadora puede ejecutar.

**Ejemplo:** Python, JavaScript, Java, C++, SQL.

### Lenguaje de Alto Nivel (High-Level Language)

**Definición:** Un lenguaje de programación diseñado para ser fácil de leer y escribir por los humanos. Usa palabras y sintaxis similares al lenguaje natural (en inglés). Python y JavaScript son ejemplos perfectos.

### Lenguaje de Bajo Nivel (Low-Level Language)

**Definición:** Un lenguaje de programación que está muy cerca del lenguaje que la máquina entiende. Es mucho más difícil de leer y escribir para los humanos, pero ofrece un control muy detallado sobre el hardware. El lenguaje ensamblador es un ejemplo.

### Lenguaje natural (Natural Language)

**Definición:** El lenguaje que hablamos y escribimos los humanos en nuestro día a día, como el español o el inglés. Uno de los grandes objetivos de la inteligencia artificial es lograr que podamos dar instrucciones a las computadoras usando nuestro lenguaje natural.

### Procedimiento (Procedure)

**Definición:** Es un término a menudo usado como sinónimo de "función". Se refiere a un subprograma o bloque de código que realiza una tarea específica.

### Programa (Program)

**Definición:** Es un conjunto de instrucciones escritas en un lenguaje de programación que le dicen a una computadora cómo realizar una tarea específica.

### Programación controlada por sucesos (Event-driven programming)

**Definición:** Es un paradigma de programación donde el flujo del programa está determinado por eventos (o "sucesos"), como acciones del usuario (clics, pulsaciones de teclas) o mensajes del sistema. El programa está en un estado de "escucha" constante, esperando que ocurra un evento para reaccionar.

**Ejemplo:** El desarrollo front-end con JavaScript es puramente controlado por eventos. Escribes código que dice: "Cuando el usuario haga clic en este botón, ejecuta esta función".

```javascript
const miBoton = document.getElementById('comprarBtn');
miBoton.addEventListener('click', function() {
    alert('¡Producto añadido al carrito!');
});
```

### Programación imperativa (Imperative programming)

**Definición:** Es un estilo de programación donde le dices a la computadora "cómo" hacer las cosas, describiendo paso a paso la secuencia de comandos que deben cambiar el estado del programa. La mayoría de los lenguajes populares, como Python y JavaScript, son fundamentalmente imperativos.

### Programador (Programmer)

**Definición:** La persona que diseña, escribe, prueba y depura programas de computadora. ¡Ese eres tú!

### Prueba (Testing)

**Definición:** Es el proceso de verificar sistemáticamente que un programa funciona como se espera, encontrando defectos o comprobando que cumple con los requisitos.

### Pseudocódigo (Pseudocode)

**Definición:** Es una forma de describir un algoritmo usando una mezcla de lenguaje natural y convenciones de lenguaje de programación, sin seguir la sintaxis estricta de ninguno. Sirve para planificar la lógica antes de escribir el código real.

**Ejemplo:**

```
INICIO
  pedir número1
  pedir número2
  resultado = número1 + número2
  mostrar resultado
FIN
```

### Variable

**Definición:** Es como una caja con una etiqueta. Usas la etiqueta (el nombre de la variable) para guardar, recuperar y modificar un dato (el valor) mientras el programa se está ejecutando.

**Ejemplo en Código (JavaScript):**

```javascript
let nombreUsuario = "Ana"; // Creas la caja "nombreUsuario" con "Ana" adentro
console.log(nombreUsuario); // Muestras "Ana"
nombreUsuario = "Juan"; // Cambias el contenido de la caja por "Juan"
console.log(nombreUsuario); // Ahora muestras "Juan"
```

### Variable Local (Local variable)

**Definición:** Una variable que solo existe y es accesible dentro de un bloque de código específico, como una función. Una vez que la función termina, la variable desaparece.

**Ejemplo en Código (Python):**

```python
def calcular_total():
    precio_local = 100 # Variable local, solo existe aquí
    impuesto = precio_local * 0.19
    return precio_local + impuesto

# print(precio_local) # Esto daría un error, porque no existe fuera de la función
```

---

## 📦 Programación Orientada a Objetos (POO)

### Acoplamiento (Coupling)

**Definición:** Mide qué tan dependiente es una parte de tu código (como una clase o un módulo) de otra. Un bajo acoplamiento es bueno, porque significa que puedes cambiar una parte sin tener que romper o cambiar muchas otras.

### Agregación (Aggregation)

**Definición:** Es una relación "tiene un" donde un objeto (el todo) está compuesto por otros objetos (las partes), pero las partes pueden existir independientemente del todo.

**Ejemplo:** Una Playlist (el todo) "tiene" Canciones (las partes). Si borras la playlist, las canciones pueden seguir existiendo en la biblioteca de música.

### Asociación (Association)

**Definición:** Es la relación más general entre dos clases. Simplemente indica que los objetos de una clase están conectados o se relacionan de alguna manera con los objetos de otra.

### Atributo (Attribute)

**Definición:** Es una característica o propiedad que describe un objeto. Los atributos representan el estado o los datos que pertenecen a una instancia de una clase. También se les conoce como "variables de instancia" o "propiedades".

**Ejemplo:** En una clase `Usuario`, los atributos podrían ser `email`, `nombre`, `edad` y `activo`. Cada objeto `Usuario` tendría sus propios valores para estos atributos.

**Ejemplo en Código (Python):**

```python
class Usuario:
    def __init__(self, email, nombre):
        self.email = email     # Atributo
        self.nombre = nombre   # Atributo
        self.activo = False    # Atributo con valor por defecto

# Creando un objeto con atributos específicos
usuario1 = Usuario("ana@correo.com", "Ana García")
print(usuario1.nombre)  # Accediendo al atributo nombre
```

### Clase (Class)

**Definición:** Es un plano o un molde para crear objetos. Define un conjunto de atributos (características o datos) y métodos (acciones o comportamientos) que tendrán los objetos creados a partir de ella.

**Ejemplo en Código (Python):**

```python
# El plano para todos los usuarios del sitio web
class Usuario:
    # El método "constructor" que se ejecuta al crear un nuevo objeto
    def __init__(self, email, password):
        self.email = email       # Un atributo
        self.activo = False      # Otro atributo

    # Un método (una acción)
    def activar_cuenta(self):
        self.activo = True
        print(f"La cuenta de {self.email} ha sido activada.")
```

### Clase abstracta (Abstract class)

**Definición:** Es una clase "incompleta" que no se puede usar para crear objetos directamente. Funciona como una plantilla base para otras clases (subclases), obligándolas a implementar ciertos métodos.

### Clase concreta (Concrete class)

**Definición:** Es una clase "completa" y normal, a partir de la cual se pueden crear objetos. Es lo contrario a una clase abstracta.

### Cohesivo (Cohesive)

**Definición:** Una clase es cohesiva cuando todas sus partes (atributos y métodos) están fuertemente relacionadas y contribuyen a un único y bien definido propósito. Es una señal de buen diseño.

### Constructor (Constructor)

**Definición:** Es un método especial dentro de una clase que se ejecuta automáticamente cuando se crea un nuevo objeto de esa clase. Su principal trabajo es inicializar los atributos del objeto.

**Ejemplo:** En Python, el constructor se llama `__init__`. En JavaScript, se llama `constructor`.

### Encapsulamiento (Encapsulation)

**Definición:** Es la idea de empaquetar los datos (atributos) y los métodos (comportamientos) que operan sobre esos datos dentro de una sola unidad (una clase). También implica ocultar el estado interno del objeto y solo permitir el acceso a través de métodos públicos, protegiendo los datos de manipulaciones indebidas.

### Herencia (Inheritance)

**Definición:** Es un mecanismo que permite a una clase (llamada subclase o clase hija) heredar atributos y métodos de otra clase (llamada superclase o clase padre). Esto promueve la reutilización de código.

**Ejemplo:** Podrías tener una clase base Vehiculo con atributos como marca y velocidad. Luego, las clases Coche y Moto pueden heredar de Vehiculo y añadir sus propios atributos específicos, como numero_puertas o tipo_manillar.

### Instancia (Instance) / Objeto (Object)

**Definición:** Una instancia es un objeto concreto creado a partir de una clase. Si la clase es el plano, la instancia es la casa construida a partir de ese plano. Puedes crear muchas instancias (objetos) a partir de una misma clase.

**Ejemplo en Código (Python):**

```python
# Usando la clase Usuario de antes
usuario1 = Usuario("ana@correo.com", "pass123") # usuario1 es una instancia u objeto
usuario2 = Usuario("juan@correo.com", "abc456") # usuario2 es otra instancia

usuario1.activar_cuenta() # Llamas al método del objeto usuario1
```

### Instanciación (Instantiation)

**Definición:** Es el proceso de crear una instancia (un objeto) a partir de una clase.

### Interfaz (Interface)

**Definición:** Es como un contrato que una clase se compromete a cumplir. Define un conjunto de métodos que la clase debe implementar, pero no dice cómo. Asegura que diferentes clases tengan un conjunto común de funcionalidades, lo que permite intercambiarlas.

### Jerarquía de clases (Class hierarchy)

**Definición:** Es la estructura organizativa de las clases en términos de herencia, mostrando las relaciones entre superclases y subclases, a menudo visualizada como un árbol.

### Mensaje (Message)

**Definición:** En POO, es el acto de invocar un método de un objeto. Cuando "llamas" a un método, le estás "enviando un mensaje" al objeto para que realice una operación.

### Método (Method)

**Definición:** Es una función que pertenece a una clase. Define un comportamiento o una acción que los objetos de esa clase pueden realizar.

**Ejemplo:** En la clase Usuario, `activar_cuenta()` es un método.

### Ocultación de la información (Information hiding)

**Definición:** Es un principio clave del encapsulamiento. Consiste en proteger los detalles internos de un objeto del mundo exterior. En la práctica, se logra declarando los atributos como privados y proporcionando métodos públicos (getters y setters) para acceder o modificarlos de forma controlada.

### Programación orientada a objetos (OOP)

**Definición:** Es un paradigma o estilo de programación basado en el concepto de "objetos". Organiza el código en torno a datos (atributos) y comportamientos (métodos) empaquetados en unidades llamadas objetos, lo que facilita la creación de programas complejos y reutilizables.

### Sobrecarga (Overload)

**Definición:** Es la capacidad de tener múltiples funciones o métodos con el mismo nombre dentro de la misma clase, pero con diferentes parámetros (ya sea en número o tipo). El sistema sabe cuál llamar basándose en los argumentos que le pasas.

**Nota:** Python no soporta la sobrecarga de métodos de la misma forma que lenguajes como Java o C++. JavaScript tampoco lo hace de forma nativa.

### Anular / Sustituir (Override)

**Definición:** Ocurre cuando una subclase proporciona su propia implementación de un método que ya está definido en su superclase. Esto permite a la subclase especializar o cambiar el comportamiento heredado.

### Variable de instancia (Instance variable)

**Definición:** Un atributo o dato que pertenece a una instancia específica de una clase. Cada objeto tiene su propia copia de las variables de instancia.

**Ejemplo:** email y activo en nuestra clase Usuario son variables de instancia. usuario1 y usuario2 tienen sus propios valores para email y activo.

---

## 🌐 Desarrollo Web y Redes

### Applet

**Definición:** Era un pequeño programa Java diseñado para ser ejecutado dentro de un navegador web. Esta tecnología está obsoleta y ha sido reemplazada por tecnologías modernas como JavaScript y WebAssembly.

### AWT (Abstract Window Toolkit)

**Definición:** Una de las primeras bibliotecas de Java para crear interfaces gráficas de usuario (ventanas, botones, etc.). Al igual que los Applets, es una tecnología mayormente superada por otras más modernas como Swing y JavaFX, y no se usa en desarrollo web.

### Buscador (Search Engine)

**Definición:** Un sistema de software (como Google, Bing) que indexa el contenido de la World Wide Web y permite a los usuarios buscar información mediante palabras clave.

### Chat

**Definición:** Comunicación en tiempo real entre dos o más personas a través de texto en una red, como Internet.

### Correo electrónico (E-mail)

**Definición:** Un sistema para enviar y recibir mensajes digitales a través de una red de computadoras.

### HTML (HyperText Markup Language)

**Definición:** No es un lenguaje de programación, sino un lenguaje de marcado. Se usa para estructurar el contenido de una página web (títulos, párrafos, imágenes, enlaces, etc.). Es el esqueleto de cualquier sitio web.

**Ejemplo en Código:**

```html
<h1>Este es un título principal</h1>
<p>Este es un párrafo de texto.</p>
<a href="https://www.google.com">Ir a Google</a>
```

### Internet

**Definición:** Una gigantesca red mundial de computadoras interconectadas que permite compartir información y servicios. La World Wide Web (WWW) es uno de los servicios que se ejecutan sobre Internet.

### Java

**Definición:** Un lenguaje de programación orientado a objetos, de propósito general y muy popular. Aunque se puede usar para el backend de sitios web (con frameworks como Spring), no debe confundirse con JavaScript. Java y JavaScript son dos lenguajes completamente diferentes.

### JPEG

**Definición:** Un formato de archivo muy común para imágenes con compresión, ideal para fotografías y gráficos con muchos colores. Es ampliamente utilizado en la web junto con otros formatos como PNG, GIF y WebP.

### Multihilo (Multithreading)

**Definición:** La capacidad de un programa para ejecutar múltiples tareas o hilos de ejecución de forma concurrente. En un servidor web, esto permite atender a múltiples usuarios al mismo tiempo.

**Relación con JS:** JavaScript en el navegador es, por naturaleza, de un solo hilo (single-threaded). Para tareas pesadas, utiliza mecanismos asíncronos y Web Workers para no bloquear la interfaz de usuario.

### Red (Network)

**Definición:** Una infraestructura que conecta dos o más computadoras para que puedan comunicarse y compartir recursos.

### Etiqueta (Tag)

**Definición:** En HTML, una etiqueta es una instrucción encerrada en `< >` que le dice al navegador cómo debe mostrar o estructurar un elemento. `<h1>`, `<p>`, `<img>` son ejemplos de etiquetas.

### UML (Unified Modeling Language)

**Definición:** Un lenguaje visual estandarizado para modelar y documentar sistemas de software. Se utiliza para crear diagramas (como diagramas de clases, de secuencia, etc.) que ayudan a visualizar la arquitectura y el diseño de una aplicación.

### Unicode

**Definición:** Un estándar de codificación de caracteres universal que asigna un número único a cada carácter de prácticamente todos los sistemas de escritura del mundo. Es fundamental para que las webs y las aplicaciones puedan mostrar texto en cualquier idioma correctamente (incluyendo emojis 😉). UTF-8, la codificación más común en la web, se basa en Unicode.

---

## 🖥️ Hardware, Sistemas y Arquitectura

### Almacenamiento (Storage)

**Definición:** Cualquier medio físico (disco duro, SSD, CD-ROM) donde se guardan datos de forma permanente o semi-permanente.

### ANSI (American National Standards Institute)

**Definición:** Una organización de EE. UU. que supervisa el desarrollo de estándares para productos, servicios y sistemas. En informática, definieron estándares históricos como el juego de caracteres ANSI.

### ASCII (American Standard Code for Information Interchange)

**Definición:** Un estándar de codificación de caracteres basado en el alfabeto inglés. Asigna un número (del 0 al 127) a cada letra, número y símbolo de control. Fue el precursor de Unicode y hoy en día es un subconjunto de UTF-8.

### Binario (Binary)

**Definición:** El sistema numérico de base 2, que utiliza solo dos dígitos: 0 y 1. Es el lenguaje fundamental que entienden las computadoras, donde el 0 puede representar "apagado" o "falso" y el 1 "encendido" o "verdadero".

### BIOS (Basic Input/Output System)

**Definición:** Es el primer software que se ejecuta cuando enciendes tu computadora. Es un firmware almacenado en un chip en la placa base que se encarga de inicializar el hardware (como el que tiene tu LENOVO IdeaPad) y cargar el sistema operativo (Debian o Windows) desde el disco duro.

### Bit

**Definición:** La unidad de información más pequeña en una computadora. Solo puede tener uno de dos valores: 0 o 1.

### Boot / Bootear

**Definición:** El proceso de iniciar una computadora, que implica cargar el BIOS y luego el sistema operativo. Cuando tienes un "dual boot" como en tu laptop, el gestor de arranque te permite elegir qué sistema operativo (Debian 12 o Windows 11) iniciar.

### Buffer

**Definición:** Un área de memoria temporal utilizada para almacenar datos mientras se transfieren de un lugar a otro. Ayuda a compensar las diferencias de velocidad entre dispositivos, como cuando ves un video en streaming y se "carga" una parte por adelantado.

### Byte

**Definición:** Un conjunto de 8 bits. Es la unidad de medida estándar para el tamaño de los archivos y la capacidad de almacenamiento (como tus 16 GBytes de RAM o tu disco de 1000 GB). Un solo carácter, como la letra 'A', suele ocupar un byte.

### Computador / Ordenador (Computer)

**Definición:** Una máquina electrónica programable que puede recibir, almacenar, procesar y devolver datos.

### Gigabyte (GB)

**Definición:** Una unidad de medida de almacenamiento de datos. Técnicamente, son 2^30 bytes (aproximadamente 1.07 mil millones de bytes), aunque a menudo se redondea a mil millones de bytes.

### GHz (Gigahertz)

**Definición:** Una unidad de medida de frecuencia que equivale a mil millones de ciclos por segundo. Se usa comúnmente para medir la velocidad de los procesadores de las computadoras (como tu Intel Core i7-13620H). Una mayor frecuencia generalmente significa un procesador más rápido.

### Hardware

**Definición:** Todas las partes físicas y tangibles de una computadora y sus periféricos. En tu caso, esto incluye tu procesador Intel i7, tus 16 GB de RAM LPDDR5, tu disco NVMe ADATA, el monitor, el teclado, etc.

### Hertzio (Hertz)

**Definición:** La unidad de medida de la frecuencia, igual a un ciclo por segundo.

### Memoria (Memory)

**Definición:** Se refiere comúnmente a la RAM (Random Access Memory). Es el espacio de trabajo temporal y ultrarrápido de la computadora, donde se cargan el sistema operativo, las aplicaciones que estás usando y los datos con los que trabajan. Es volátil, lo que significa que su contenido se borra cuando apagas el PC. Tus 16 GB de RAM te permiten tener varios programas abiertos a la vez sin que el sistema se ponga lento.

### Monitor / Pantalla (Screen)

**Definición:** El dispositivo de salida (periférico) que muestra la información visual generada por la computadora.

### Nanosegundo (Nanosecond)

**Definición:** La milmillonésima parte de un segundo (1/1,000,000,000 s). Se usa para medir tiempos de acceso extremadamente rápidos en componentes de hardware, como la memoria RAM.

### Plataforma (Platform)

**Definición:** La combinación de un sistema operativo y una arquitectura de hardware subyacente. Por ejemplo, "Windows sobre x86" o "Linux sobre ARM". Tu laptop soporta múltiples plataformas como Debian (Linux) y Windows sobre la arquitectura x86-64 de tu CPU Intel.

### RAM (Random Access Memory)

**Definición:** Ver Memoria. Es el almacenamiento primario, rápido y volátil, donde se ejecutan los programas.

### Resolución (Resolution)

**Definición:** El número de píxeles (puntos individuales de color) que se pueden mostrar en una pantalla, expresado como ancho por alto (por ejemplo, 1920x1080). Una mayor resolución significa una imagen más nítida y detallada.

### Software

**Definición:** El conjunto de programas, instrucciones y datos que le dicen al hardware qué hacer. Es la parte intangible de la computadora. Incluye el sistema operativo (Debian), los compiladores, los navegadores web y las aplicaciones que escribes.

### Sistema Operativo (Operating System)

**Definición:** El software fundamental que gestiona todos los recursos de hardware y software de la computadora. Proporciona una interfaz entre el usuario y el hardware. En tu caso, tienes dos: Debian 12 y Windows 11.

### Terabyte (TB)

**Definición:** Una unidad de medida de almacenamiento de datos. Equivale a 1024 Gigabytes (GB). Tu disco de 1000 GB es aproximadamente 1 TB.

### Usuario (User)

**Definición:** La persona que interactúa con y utiliza una computadora o un programa.

---

## 🧮 Tipos de Datos y Operadores

### Booleano (Boolean)

**Definición:** Un tipo de dato que solo puede tener dos valores: true (verdadero) o false (falso). Es fundamental para la lógica y la toma de decisiones en programación.

**Ejemplo en Código (JavaScript):**

```javascript
let esMayorDeEdad = true;
if (esMayorDeEdad) {
    console.log("Puede entrar al sitio.");
}
```

### Dato alfanumérico (Alphanumeric/String)

**Definición:** Un tipo de dato que representa una secuencia de caracteres (letras, números, símbolos). Se conoce comúnmente como "string" o "cadena de texto".

**Ejemplo en Código (Python):**

```python
nombre_curso = "Programación Web 101"
```

### Dato numérico (Numeric)

**Definición:** Un tipo de dato que representa números. Se pueden dividir en dos subtipos principales: enteros (números sin decimales) y reales (números con decimales).

### Entero (Integer)

**Definición:** Un número entero, sin parte fraccionaria. Puede ser positivo, negativo o cero.

**Ejemplo:** -10, 0, 42.

### Expresión (Expression)

**Definición:** Cualquier fragmento de código que se evalúa y produce un valor.

**Ejemplo:** 2 + 3 es una expresión que se evalúa al valor 5. nombreUsuario.length > 0 es una expresión que se evalúa a un valor booleano (true o false).

### Expresión booleana (Boolean expression)

**Definición:** Una expresión que se evalúa para producir un resultado booleano (true o false). Se construyen comúnmente usando operadores relacionales y lógicos.

### Operador (Operator)

**Definición:** Un símbolo que representa una operación a realizar sobre uno o más valores (operandos).

**Ejemplo:** El + en 5 + 2 es un operador de suma.

### Operadores aritméticos (Arithmetic operators)

**Definición:** Símbolos utilizados para realizar operaciones matemáticas.

**Ejemplo:** + (suma), - (resta), * (multiplicación), / (división), % (módulo, que da el resto de una división), ** (potencia, en Python/JS).

### Operadores lógicos o booleanos (Logical operators)

**Definición:** Operadores que se usan para combinar o modificar expresiones booleanas.

**Ejemplo en JavaScript/Python:**

- && (en JS) o and (en Python): Devuelve true si AMBAS condiciones son verdaderas.
- || (en JS) o or (en Python): Devuelve true si AL MENOS UNA condición es verdadera.
- ! (en JS) o not (en Python): Niega una condición (convierte true en false y viceversa).

### Operadores relacionales o condicionales (Relational operators)

**Definición:** Se utilizan para comparar dos valores. El resultado de la comparación es siempre un valor booleano.

**Ejemplo en JavaScript/Python:** > (mayor que), < (menor que), == (igual a), != (diferente de), >= (mayor o igual que), <= (menor o igual que).

### Real (Real/Float)

**Definición:** Un número que puede tener una parte decimal. En programación, se les suele llamar "flotantes" (float) o "dobles" (double).

**Ejemplo:** 3.1416, -0.5, 99.99.

### Tipo de datos (Data type)

**Definición:** Una clasificación que le dice al programa qué tipo de valor tiene una variable y qué operaciones se pueden realizar con ella. Los tipos de datos básicos (como número, string, booleano) se llaman "tipos primitivos".

---

## ✍️ Estructura y Sintaxis de Código

### Argumento (Argument)

**Definición:** El valor real que se "pasa" a una función cuando se la llama.

**Ejemplo en Código (Python):**

```python
def saludar(nombre): # "nombre" es el parámetro
    print(f"Hola, {nombre}")

saludar("Mundo") # "Mundo" es el argumento
```

### Asignación (Assignment)

**Definición:** La acción de guardar un valor en una variable. Se realiza mediante el operador de asignación (=).

**Ejemplo:** edad = 20;

### Bloque (Block)

**Definición:** Un grupo de una o más sentencias de código que se tratan como una sola unidad. En muchos lenguajes (como JavaScript), los bloques se delimitan con llaves {}. En Python, se delimitan por la indentación (el espaciado al inicio de la línea).

### Código Fuente (Source Code)

**Definición:** El conjunto de instrucciones escritas por un programador en un lenguaje de programación legible por humanos. Son los archivos .js o .py que tú creas.

### Código máquina (Machine Code)

**Definición:** La forma de instrucciones más básica, representada en binario (ceros y unos), que el procesador (CPU) de una computadora puede ejecutar directamente. Todo el código fuente debe ser traducido (compilado o interpretado) a código máquina para poder ejecutarse.

### Comando (Command)

**Definición:** Una instrucción directa dada a un programa, a menudo a través de una interfaz de línea de comandos (como la terminal en Debian).

**Ejemplo:** ls para listar archivos, o git commit para guardar cambios en un repositorio.

### Comentario (Comment)

**Definición:** Texto dentro del código fuente que es ignorado por el compilador o intérprete. Su propósito es explicar el código a otros programadores (o a tu yo del futuro).

**Ejemplo en Código:**

```javascript
// Este es un comentario de una sola línea en JavaScript

/* Este es un
   comentario de
   múltiples líneas */
```

```python
# Este es un comentario en Python
```

### Concatenación (Concatenation)

**Definición:** La acción de unir dos o más cadenas de texto (strings) para formar una sola.

**Ejemplo en Código (JavaScript):**

```javascript
let saludo = "Hola" + " " + "Mundo"; // saludo es "Hola Mundo"
```

### Declaración (Declaration)

**Definición:** Una sentencia que introduce un nuevo identificador (como el nombre de una variable o una función) en el programa.

### Identificador (Identifier)

**Definición:** El nombre que se le da a una entidad en el programa, como una variable, función o clase. Deben seguir ciertas reglas (por ejemplo, no pueden empezar con un número).

### Instrucción / Sentencia (Statement)

**Definición:** Una unidad completa de ejecución; una acción que el programa debe realizar. Un programa es una secuencia de sentencias.

**Ejemplo:** let x = 5; es una sentencia. if (x > 0) { ... } es otra.

### Llamada por referencia (Call-by-reference)

**Definición:** Una forma de pasar argumentos a una función donde, en lugar de pasar una copia del valor, se pasa una referencia a la ubicación en memoria del dato original. Esto significa que si la función modifica el dato, el cambio se refleja fuera de la función.

**Relación con JS/Python:** En Python y JavaScript, el comportamiento es más sutil. Los tipos primitivos (números, strings) se pasan por valor. Los objetos (incluyendo arrays y diccionarios) se pasan por "referencia de objeto" o "valor de la referencia". Esto significa que se pasa una copia de la referencia; si modificas las propiedades internas del objeto, el cambio se ve afuera, pero si reasignas el objeto a uno nuevo dentro de la función, el objeto original no cambia.

### Llamada por valor (Call-by-value)

**Definición:** Una forma de pasar argumentos a una función donde se crea una copia del valor del argumento y se le entrega a la función. Cualquier cambio que la función haga a ese valor no afecta a la variable original fuera de la función. Este es el comportamiento para tipos primitivos en JS y Python.

### Modificador (Modifier)

**Definición:** Una palabra clave (como public, private, static, final) que se usa en la declaración de clases, métodos o atributos para especificar sus propiedades o nivel de acceso. Son muy comunes en Java, pero menos explícitos en lenguajes como Python o JavaScript.

### Palabra clave / reservada (Keyword / Reserved Word)

**Definición:** Una palabra que tiene un significado especial en la sintaxis de un lenguaje de programación y no puede ser usada como un nombre de variable u otro identificador.

**Ejemplo:** if, else, for, while, class, function son palabras clave.

### Parámetro (Parameter)

**Definición:** Es la variable que se declara en la definición de una función. Actúa como un marcador de posición para el valor (argumento) que la función espera recibir cuando es llamada.

### Sintaxis (Syntax)

**Definición:** El conjunto de reglas gramaticales que definen cómo se deben escribir y estructurar las sentencias en un lenguaje de programación para que sean consideradas válidas. Si rompes las reglas, obtienes un "error de sintaxis".

---

## 🐛 Seguridad y Errores

### Bug

**Definición:** Un error, fallo o defecto en un programa que causa que produzca un resultado incorrecto o inesperado, o que se comporte de forma imprevista.

### Cracker

**Definición:** Una persona que intenta obtener acceso no autorizado a sistemas informáticos, a menudo con intenciones maliciosas (robar datos, dañar el sistema, etc.). A diferencia de un "hacker", cuyo término originalmente se refería a un experto entusiasta, "cracker" siempre tiene una connotación negativa.

### Excepción (Exception)

**Definición:** Un evento anómalo o un error que ocurre durante la ejecución de un programa y que interrumpe su flujo normal. Los lenguajes modernos permiten "manejar" excepciones usando bloques try...catch (en JS) o try...except (en Python) para evitar que el programa se caiga por completo.

**Ejemplo en Código (Python):**

```python
try:
    resultado = 10 / 0 # Esto genera una excepción ZeroDivisionError
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
```

### Gusano (Worm)

**Definición:** Un tipo de malware que se replica a sí mismo para propagarse a otras computadoras, a menudo a través de una red. A diferencia de un virus, no necesita adherirse a un programa existente. Su principal objetivo es consumir ancho de banda y sobrecargar los sistemas.

### Hacker

**Definición:** Originalmente, un término para una persona experta y apasionada por la programación y los sistemas informáticos. Aunque popularmente se usa como sinónimo de "cracker", en las comunidades técnicas, un hacker es alguien que disfruta explorando y entendiendo los sistemas a un nivel profundo, a menudo para mejorarlos.

### Pirata Informático (Software Pirate)

**Definición:** Una persona que copia, distribuye o utiliza software comercial sin autorización y sin pagar por él, violando los derechos de autor.

### Spyware

**Definición:** Un tipo de software malicioso que se instala en una computadora sin el conocimiento del usuario para recopilar información sobre él (hábitos de navegación, contraseñas, etc.) y enviarla a terceros.

### Troyano (Trojan Horse)

**Definición:** Un tipo de malware que se disfraza de un programa legítimo e inofensivo. Cuando el usuario lo ejecuta, el troyano instala secretamente otro software malicioso (como un spyware o una "puerta trasera") que permite a un atacante tomar control del sistema. No se replica a sí mismo.

### Virus

**Definición:** Un programa malicioso que, cuando se ejecuta, se replica a sí mismo infectando otros programas o archivos. Requiere de la intervención humana (como abrir un archivo infectado) para propagarse. Puede tener efectos variados, desde mostrar mensajes molestos hasta borrar todos los datos del disco duro.# glosario-desarrollo
