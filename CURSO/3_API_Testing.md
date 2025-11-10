# Introducción a pruebas de APIs

Con el auge de las aplicaciones web y móviles, las APIs (Application Programming Interfaces) se han convertido en un componente esencial para la comunicación entre diferentes sistemas. Asegurar la calidad y funcionalidad de estas APIs es crucial para el éxito de cualquier aplicación. En este apartado, aprenderemos los conceptos básicos del testing de APIs utilizando la librería Requests junto con Behave para automatizar nuestras pruebas.

## 1. Conceptos básicos de testing de APIs
El testing de APIs implica la verificación de que una API funciona según lo esperado. Esto incluye validar las respuestas HTTP, los códigos de estado, los encabezados y el contenido del cuerpo de la respuesta. Algunas de las pruebas comunes incluyen:

- Verificar que la API responde con el código de estado correcto (por ejemplo, 200 para éxito, 404 para no encontrado).
- Validar que los datos devueltos en el cuerpo de la respuesta son correctos y están en el formato esperado (JSON, XML, etc.).
- Comprobar que los encabezados HTTP contienen la información necesaria (autenticación, tipo de contenido, etc.).

y tests negativos, como manejar errores y respuestas inesperadas:

- Probar cómo la API maneja solicitudes inválidas o mal formateadas.
- Verificar que la API responde adecuadamente a condiciones de error, como límites de tasa o problemas de autenticación.


## 2. Uso de la librería Requests
La librería Requests es una herramienta poderosa y fácil de usar para realizar solicitudes HTTP en Python. Nos permite enviar solicitudes GET, POST, PUT, DELETE, entre otras, y manejar las respuestas de manera sencilla.


### Implementación básica de Requests GET, POST, etc.

```python
import requests
response = requests.get('https://api.ejemplo.com/endpoint')
print(response.status_code)  # Código de estado HTTP
print(response.json())       # Cuerpo de la respuesta en formato JSON
```

```python
import requests
data = {'key': 'value'}
response = requests.post('https://api.ejemplo.com/endpoint', json=data)
print(response.status_code)  # Código de estado HTTP
print(response.json())       # Cuerpo de la respuesta en formato JSON
```

```python
import requests
data = {'key': 'updated_value'}
response = requests.put('https://api.ejemplo.com/endpoint/1', json=data
print(response.status_code)  # Código de estado HTTP
print(response.json())       # Cuerpo de la respuesta en formato JSON
```

```python
import requests
response = requests.delete('https://api.ejemplo.com/endpoint/1')
print(response.status_code)  # Código de estado HTTP
```
## 3. Creación de features y steps para pruebas de API

Al igual que con las pruebas de comportamiento (BDD) para aplicaciones, podemos utilizar Behave para definir nuestras pruebas de API en archivos *feature* y luego implementar los *steps* en Python.

### Ejemplo de archivo feature para pruebas de API

```gherkin
@api_tests
Feature: Pruebas de API de usuarios

  @happy_path
  Scenario: Obtener lista de usuarios
    Given que la API de usuarios está disponible
    When hago una solicitud GET a /users
    Then la respuesta debería tener un código de estado 200
    And la respuesta debería contener una lista de usuarios
```

### Ejemplo de steps en Python para pruebas de API

```python
from behave import given, when, then
import requests
@given('que la API de usuarios está disponible')
def step_given_api_disponible(context):
    context.base_url = 'https://api.ejemplo.com'
    # Se podría agregar una verificación de disponibilidad aquí

@when('hago una solicitud GET a /users')
def step_when_solicitud_get(context):
    context.response = requests.get(f'{context.base_url}/users')

@then('la respuesta debería tener un código de estado {status_code:d}')
def step_then_codigo_estado(context, status_code):
    assert context.response.status_code == status_code

@then('la respuesta debería contener una lista de usuarios')
def step_then_lista_usuarios(context):
    data = context.response.json()
    assert isinstance(data, list)

```

### Qué es context?

En Behave, `context` es un objeto que se utiliza para compartir datos entre los diferentes steps de un escenario. Permite almacenar información que puede ser accedida y modificada a lo largo de la ejecución de los steps, facilitando la comunicación entre ellos. Por ejemplo, en el step `step_when_solicitud_get`, almacenamos la respuesta de la solicitud HTTP en `context.response`, lo que nos permite acceder a esa respuesta en los steps posteriores para realizar validaciones.

### Cómo pasar parámetros en steps?
En Cucumber, puedes pasar parámetros en los steps utilizando expresiones regulares o tipos de datos específicos. Por ejemplo, en el step `step_then_codigo_estado`, utilizamos `{status_code:d}` para indicar que esperamos un número entero como parámetro. Behave automáticamente convierte el valor pasado en el step al tipo de dato especificado (en este caso, un entero) y lo pasa como argumento a la función del step.

para los diferentes tipos de datos que puedes usar en los steps:

|Sintaxis	        |   Tipo Python          |   Ejemplo en feature             |   Resultado en Python |
|-------------------|------------------------|----------------------------------|-----------------------|
{palabra} o {w}     |	str (una palabra)    |	"Diego"                         |	"Diego"             |
"{texto}"           |	str (texto completo) |	"Hola mundo"	                |   "Hola mundo"        |
{n:d}               |	int	                 |  {status_code:d} con valor 404	|   404                 |
{f:f}	            |   float	             |  {peso:f} con valor 3.14         |	3.14                |
{valor:g}           |	float o int          |	2, 2.5                          |	2 o 2.5             |
{bool:boolean}      |	bool                 |	"True", "false"	                |   True / False        |

```python
@then('la respuesta debería devolver el usuario {user:w}')
```

```python
@then('el error debería contener el mensaje "{mensaje}"')
```

```python
@then('la respuesta debería tener un código de estado {status_code:d}')
```

```python
@then('el precio debería ser {precio:f}')
```

```python
@then('la cantidad debería ser {cantidad:g}')
```

```python
@then('el usuario debería estar activo: {activo:boolean}')
```
### Schemas

Para validar que las respuestas de la API cumplen con un formato específico, tambien podemos utilizar esquemas (schemas). Una librería popular para esto es `jsonschema`, que nos permite definir un esquema JSON y validar las respuestas contra ese esquema.

```python
from jsonschema import validate, ValidationError
_example_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "email": {"type": "string", "format": "email"}
    },
    "required": ["id", "name", "email"]
}

@then('la respuesta debería cumplir con el esquema definido')
def step_then_validar_esquema(context):
    data = context.response.json()
    try:
        validate(instance=data, schema=_example_schema)
    except ValidationError as e:
        assert False, f"Esquema inválido: {e.message}"
```

Los schemas también pueden ser definidos en archivos externos (por ejemplo, en formato JSON) y cargados en los steps para mantener el código más limpio y organizado.
