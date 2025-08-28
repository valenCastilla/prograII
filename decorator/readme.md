Trabajo Práctico: Patrón de Diseño Decorator - Starbuzz Coffee ☕
Introducción
Este repositorio contiene el código de ejemplo para la Clase 2: Patrón de Diseño Decorator. La implementación se basa en el caso de estudio de la cafetería "Starbuzz Coffee", extraído del libro "Head First Design Patterns".

El objetivo de este ejercicio es aplicar de manera práctica los conceptos teóricos vistos en clase para resolver un problema de diseño común: cómo añadir funcionalidades (responsabilidades) a objetos de forma dinámica y flexible, evitando la "explosión de clases" que generaría un mal uso de la herencia.

Objetivo del Trabajo Práctico
El alumno deberá analizar, ejecutar y extender el código proporcionado para:

Comprender la estructura y los participantes del Patrón Decorator (Componente, Componente Concreto, Decorador y Decorador Concreto).

Ver en acción cómo la composición se utiliza para extender el comportamiento de los objetos en tiempo de ejecución.

Relacionar la solución implementada con el Principio de Diseño Abierto/Cerrado.

Practicar la modificación y extensión de un sistema diseñado con este patrón.

Estructura del Repositorio
El proyecto está organizado en tres archivos principales, cada uno representando una parte lógica del patrón:

beverages.py:

Rol: Define los Componentes.

Contenido: Incluye la clase abstracta Beverage (el Componente) y las clases concretas como HouseBlend, DarkRoast, etc. (los Componentes Concretos). Estos son los objetos base que serán "decorados".

condiments.py:

Rol: Define los Decoradores.

Contenido: Incluye la clase abstracta CondimentDecorator (el Decorador) y las clases concretas como Mocha, Whip, Soy, etc. (los Decoradores Concretos). Cada una de estas clases "envuelve" a un Beverage para añadirle costo y descripción.

main.py:

Rol: Es el Cliente que utiliza el patrón.

Contenido: Script principal que simula la creación de varios pedidos de café. Aquí es donde se instancia una bebida base y se la envuelve dinámicamente con múltiples decoradores.

¿Cómo ejecutar el código?
Para ver el sistema en funcionamiento, simplemente ejecuta el script main.py desde tu terminal. Asegúrate de tener los tres archivos (main.py, beverages.py, condiments.py) en la misma carpeta.

python main.py

Salida Esperada
Al ejecutar el script, deberías ver la siguiente salida en tu consola, mostrando la descripción y el costo final de cada pedido:

Bienvenido a Starbuzz Coffee!
--- Preparando pedidos ---
Pedido 1: Espresso $1.99
Pedido 2: Café Dark Roast, Mocha, Mocha, Crema $1.49
Pedido 3: Café de la Casa, Soja, Mocha, Crema $1.34

🚀 ¡Ejercicio Práctico y Desafío!
Ahora es tu turno de aplicar el Principio Abierto/Cerrado. El sistema debe estar abierto a la extensión (añadir nuevas funcionalidades) pero cerrado a la modificación (sin alterar el código que ya funciona).

Tu tarea: Starbuzz Coffee ha decidido añadir un nuevo condimento: Caramelo, que tiene un costo de $0.25.

Extender el sistema:

Crea una nueva clase Caramel en el archivo condiments.py.

Esta clase debe heredar de CondimentDecorator.

Implementa los métodos get_description() y cost() para que añadan la descripción "Caramelo" y sumen el costo correspondiente.

Probar la extensión:

Modifica el archivo main.py para crear un nuevo pedido (Pedido 4) que sea un Decaf con Caramel y Whip.

Ejecuta el programa y verifica que la descripción y el costo del nuevo pedido sean correctos.

Pregunta para reflexionar: ¿Tuviste que modificar los archivos beverages.py o las clases de los otros condimentos para añadir esta nueva funcionalidad? ¿Por qué?

Conceptos Clave a Observar en el Código
Herencia de tipo: Fíjate que CondimentDecorator hereda de Beverage. Esto no es para heredar comportamiento, sino para asegurar que los decoradores tengan el mismo tipo que los objetos que envuelven.

Composición para comportamiento: Cada decorador tiene una (has-a) referencia a un Beverage (la variable _beverage). El nuevo comportamiento se logra delegando la llamada al objeto envuelto y luego sumando la propia funcionalidad.

Delegación en cadena: Analiza cómo una llamada a cost() en el decorador más externo desencadena una serie de llamadas que recorren toda la cadena de decoradores hasta llegar a la bebida base.
