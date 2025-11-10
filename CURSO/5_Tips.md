### Reportes y buenas prácticas

## Generación de reportes en HTML con Behave
En este framework, utilizamos un generador de reportes personalizado que crea informes en formato HTML después de la ejecución de las pruebas. Estos reportes proporcionan una visión clara de los resultados de las pruebas, incluyendo detalles sobre los escenarios ejecutados, su estado (éxito o fallo) y cualquier error encontrado.

Después de ejecutar las pruebas con el comando:

```bash
python ./main.py
```
Los reportes se generan automáticamente en la carpeta `reports/` del proyecto. Puedes abrir estos archivos HTML en cualquier navegador web para revisar los resultados de las pruebas.

## Organización de escenarios y steps reutilizables
Para mantener un código limpio y fácil de mantener, es importante organizar los escenarios y steps de manera eficiente. Aquí hay algunas buenas prácticas:

- **Reutilización de Steps**: Siempre que sea posible, reutiliza los steps existentes en lugar de crear nuevos. Esto reduce la duplicación de código y facilita el mantenimiento.
- **Modularidad**: Divide los steps en módulos lógicos basados en funcionalidades o áreas de la aplicación. Esto facilita la navegación y comprensión del código.
- **Nombres descriptivos**: Utiliza nombres claros y descriptivos para los escenarios y steps. Esto ayuda a entender rápidamente qué hace cada parte del código.
- **Uso de Tags**: Utiliza tags en los archivos feature para categorizar y filtrar las pruebas durante la ejecución. Esto es especialmente útil en proyectos grandes con muchas pruebas.
- **Evita detalles técnicos en el Gherkin**: Mantén los archivos feature enfocados en el comportamiento del usuario y evita incluir detalles técnicos que puedan cambiar con el tiempo. Recuerda que los archivos feature deben ser legibles para todas las partes interesadas, incluyendo aquellas sin conocimientos técnicos.
- **Crea steps cortos y específicos**: Cada step debe realizar una única acción o verificación. Esto facilita la reutilización y el mantenimiento del código.
- **Valida siempre dentro del step *Then***: No pongas asserts en Given o When, salvo excepciones. Los steps Then son los puntos de verificación.
- **Logging y depuración**: Utiliza los mecanismos de logging para registrar información útil durante la ejecución de las pruebas. Esto facilita la depuración en caso de fallos y aporta contexto adicional sobre el comportamiento de la aplicación durante las pruebas, sobre todo en steps complejos o casos de error.
- **Cobertura de pruebas**: Incrementar la cobertura de pruebas es un objetivo continuo. A medida que se desarrollan nuevas funcionalidades, asegúrate de agregar escenarios y steps correspondientes para cubrir esos casos de uso. Mediante el Scenario Outline, puedes cubrir múltiples combinaciones de datos con un solo escenario, lo que ayuda a aumentar la cobertura sin duplicar código.

Por ejemplo, podemos crear un archivo `common_steps.py` para almacenar steps que se utilizan en múltiples features:

```python
from behave import given, when, then
@given('I click the "{button_name}" button')
def step_click_button(context, button_name):
    context.driver.find_element(By.ID, button_name).click()
```
Para dividir los steps en módulos, podemos tener una estructura como esta:

```tests/
├── steps/
│   ├── api_steps.py
│   ├── web_steps.py
│   ├── common_steps.py
```
Otro ejemplo es usar loggin en un step tanto para indicar el inicio de una acción como para capturar errores:

```python
from settings.logging import log
@when('I submit the login form')
def step_submit_login_form(context):
    try:
        log.info("Submitting login form")
        context.driver.find_element(By.ID, 'login-button').click()
    except Exception as e:
        log.error(f"Error submitting login form: {e}")
        raise
```

También podemos organizar los archivos feature en carpetas según su funcionalidad, como `features/apis/` y `features/web/`, para mantener una estructura clara.

## Mantenimiento de las pruebas

El mantenimiento de las pruebas es crucial para asegurar que el framework siga siendo efectivo a medida que la aplicación evoluciona. Aquí hay algunas recomendaciones:

- **Revisión periódica**: Revisa y actualiza regularmente los escenarios y steps para asegurarte de que reflejan los cambios en la aplicación.
- **Crea nuevas rutas de prueba**: A medida que se agregan nuevas funcionalidades a la aplicación, asegúrate de crear escenarios y steps correspondientes para cubrir esos casos de uso, por ejemplo, si hay varios mercados (españa, italia, portugal) y cada equipo desarrolla para un mercado diferente, crea rutas de prueba específicas para cada uno.
- **Eliminación de pruebas obsoletas**: Si una funcionalidad ya no es relevante, elimina las pruebas asociadas para evitar confusión.
- **Documentación**: Mantén una buena documentación del framework, incluyendo cómo ejecutar las pruebas y cómo interpretar los reportes.
- **Define un Test Framework Handbook**: Crea un manual o guía para el equipo de pruebas que detalle las convenciones, estructuras y mejores prácticas a seguir al trabajar con el framework. Esto asegura la coherencia y facilita la incorporación de nuevos miembros al equipo.
- **Versionado de las pruebas**: Utiliza una convención de versionado de las pruebas a medida que el desarrollo avanza. Esto ayuda a rastrear cambios y facilita la identificación de cuándo se introdujeron modificaciones específicas en los escenarios o steps. Por regla general, es recomendable alinear el versionado de las pruebas con el ciclo de desarrollo del software.


Si es necesario añadir algún ajuste, se puede introducir en los archivos de configuración dentro de la carpeta `settings/` como subida automática de reportes, configuración de logs, etc. El framework está diseñado para ser flexible y adaptable a las necesidades cambiantes del proyecto.
