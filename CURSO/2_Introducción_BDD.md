# Introducción al BDD con Gherkin y Behave

En este apartado aprenderemos los conceptos básicos del BDD (Behavior Driven Development) y cómo utilizar la librería Behave para implementar pruebas automatizadas siguiendo esta metodología. Veremos la sintaxis de los archivos *feature* escritos en Gherkin, cómo crear escenarios y steps en Python, y cómo ejecutar las pruebas con Behave.

## 1. ¿Qué es BDD?
BDD (Behavior Driven Development) es una metodología de desarrollo de software que se centra en la colaboración entre desarrolladores, testers y stakeholders para definir el comportamiento esperado del sistema a través de ejemplos concretos. Utiliza un lenguaje natural estructurado llamado Gherkin para describir las funcionalidades del sistema en archivos *feature*.

## 2. Sintaxis de Gherkin
Gherkin es un lenguaje específico de dominio (DSL) que permite describir el comportamiento del software de manera legible para humanos. Los archivos *feature* escritos en Gherkin tienen la extensión `.feature` y utilizan las siguientes palabras clave principales:
- `Feature`: Describe la funcionalidad que se va a probar.
- `Scenario`: Define un caso de prueba específico dentro de la funcionalidad.
- `Given`: Establece el contexto inicial o las precondiciones.
- `When`: Describe la acción o evento que se va a realizar.
- `Then`: Define el resultado esperado después de la acción.
- `And`, `But`: Permiten encadenar múltiples condiciones o acciones.

### Background 
`Background`: Permite definir pasos comunes que se ejecutan antes de cada escenario en un archivo *feature*. Es útil para evitar la duplicación de código cuando varios escenarios comparten el mismo contexto inicial.

### Ejemplo práctico:

```gherkin  
@api_tests
Feature: Pruebas de API de usuarios

  Background:
    Given que la API de usuarios está disponible

    @happy_path
    Scenario: Obtener lista de usuarios
        When hago una solicitud GET a /users
        Then la respuesta debería tener un código de estado 200
        And la respuesta debería contener una lista de usuarios

    @error_path
    Scenario: Obtener usuario inexistente
        When hago una solicitud GET a /users/9999
        Then la respuesta debería tener un código de estado 404
```

## 3. Creación de Scenarios y Scenario Outlines
Un *Scenario* es una descripción concreta de una situación que se va a probar. Un *Scenario Outline* permite definir un escenario genérico que puede ser ejecutado con diferentes conjuntos de datos.

### Ejemplo de Scenario
```gherkin
Feature: Calculadora de suma

  Scenario: Sumar dos números positivos
    Given que tengo una calculadora
    When sumo 2 y 3
    Then el resultado debería ser 5
```
### Ejemplo de Scenario Outline
```gherkin
Feature: Calculadora de suma

  Scenario Outline: Sumar dos números
    Given que tengo una calculadora
    When sumo <num1> y <num2>
    Then el resultado debería ser <resultado>

    Examples:
      | num1 | num2 | resultado |
      | 2    | 3    | 5         |
      | 10   | 15   | 25        |
      | -1   | 1    | 0         |
```
## 4. Creación de Steps en Python
Los *steps* son las implementaciones en Python de las acciones descritas en los archivos *.feature*. Cada step se asocia a una expresión regular que coincide con la descripción en Gherkin.

### Ejemplo de Steps en Python
```python
from behave import given, when, then
@given('que tengo una calculadora')
def step_given_calculadora(context):
    context.calculadora = Calculadora()

@when('sumo {num1:d} y {num2:d}')
def step_when_sumo(context, num1, num2):
    context.resultado = context.calculadora.sumar(num1, num2)

@then('el resultado debería ser {resultado:d}')
def step_then_resultado(context, resultado):
    assert context.resultado == resultado
```

### Tags

En Gherkin, los *tags* son etiquetas que se pueden añadir a los *features* o *scenarios* para organizarlos y filtrarlos durante la ejecución de las pruebas. Los tags comienzan con el símbolo `@` y pueden ser utilizados para agrupar pruebas relacionadas (por versión o funcionalidad) o para ejecutar solo un subconjunto específico de pruebas.

Tambien se pueden usar tags para marcar escenarios como `@smoke`, `@regression`, `@api_tests`, `@web_tests`, etc., lo que facilita la gestión y ejecución de pruebas en función de diferentes criterios o para diferentes entornos.

Por último puedes combinar múltiples tags para ejecutar escenarios que cumplan con varias condiciones.

## 6. Ejecución de pruebas con Behave

Para ejecutar las pruebas definidas en nuestros archivos *.feature*, primero debemos asegurarnos de que estamos en el directorio raíz del proyecto y que el entorno virtual está activado. Luego, escribiremos las etiquetas de las pruebas que queremos ejecutar en el archivo `main.py`.

Finalmente, ejecutamos el siguiente comando en la terminal:

```bash
python ./main.py
```

Esto iniciará la ejecución de las pruebas definidas en los archivos *.feature* y creará los reportes correspondientes.

## 7. Otros conceptos importantes

- **Hooks**: Son funciones especiales que se ejecutan en momentos específicos del ciclo de vida de las pruebas, como antes o después de cada escenario. Se utilizan para configurar el entorno de prueba o limpiar recursos. En nuestro framework, los hooks se encuentran en el archivo `environment.py`.
- **Context**: Es un objeto que se utiliza para compartir datos entre los diferentes steps de un escenario. Permite almacenar información que puede ser accedida y modificada a lo largo de la ejecución de los steps.

La combinación de Gherkin y Behave nos permite crear pruebas automatizadas de manera estructurada y colaborativa, facilitando la comunicación entre los diferentes miembros del equipo de desarrollo y asegurando que el software cumple con los requisitos definidos.

Los archivos *.feature* sirven como contrato entre los desarrolladores, testers y stakeholders, ya que describen el comportamiento esperado del sistema de una manera clara y comprensible para todos. Crea un puente entre el lenguaje técnico y el lenguaje del negocio, facilitando la colaboración y la comprensión mutua.

BDD solo funciona si todos los involucrados en el proyecto (desarrolladores, testers, product owners, etc.) participan activamente en la definición de los escenarios y en la revisión de los archivos *.feature*. Esto asegura que las pruebas reflejen fielmente los requisitos del negocio y que todos estén alineados en cuanto a las expectativas del sistema, por lo que es esencial sesiones de trabajo conjuntas para definir y revisar los escenarios (Three Amigos).

Si negocio o desarrollo no participan, entonces no es BDD, es solo automatización de pruebas usando Gherkin y Behave.

Pregunta: 

- Qué debería pasar si...
- Cómo debería comportarse...
- Cuál es el resultado esperado cuando...
- Qué sucede si ingreso datos inválidos...

## 8. Errores comunes al escribir archivos feature

| Error común                                                | Por qué es malo                   | Alternativa                                |
| ---------------------------------------------------------- | --------------------------------- | ------------------------------------------ |
| Mezclar varios comportamientos en un escenario             | Dificulta lectura y mantenimiento | Divide en varios escenarios                |
| Steps con detalles técnicos (“click”, “selector”, “XPath”) | Hace el feature frágil            | Describe intención (“selecciona producto”) |
| Depender del orden de ejecución                            | Genera resultados inconsistentes  | Asegura independencia entre escenarios     |
| Datos codificados directamente en los steps                | Dificulta mantenimiento           | Usa tablas o fixtures                      |
| Scenarios muy genéricos (“el sistema funciona”)            | Poco valor                        | Define comportamientos verificables        |



## 6. Documentación adicional
- [Documentación oficial de Behave](https://behave.readthedocs.io/en/latest/)
- [Gherkin Reference](https://cucumber.io/docs/gherkin/reference/)