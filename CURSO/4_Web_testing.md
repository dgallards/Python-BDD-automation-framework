### Introducción a pruebas web con Selenium

Selenium es una herramienta de automatización de navegadores web que permite controlar y automatizar las interacciones con páginas web. Es ampliamente utilizado para pruebas automatizadas de aplicaciones web.

## 1. Uso de **Selenium** y drivers de navegador  

Al instalar Selenium tenemos cargados los drivers de navegador en la carpeta `venv`.

## 2. Inicialización de Selenium en Python
Para utilizar Selenium en nuestros *steps* de Behave, primero debemos importar la librería y configurar el driver del navegador que vamos a utilizar (por ejemplo, Chrome, Firefox, etc.).

### Ejemplo de inicialización de Selenium en Python

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
# Inicializar el driver de Chrome
driver = webdriver.Chrome()
# Navegar a una página web
driver.get('https://www.ejemplo.com')
```

## 3. Localización de elementos y acciones básicas
Selenium ofrece varias formas de localizar elementos en una página web, como por ID, nombre, selectores CSS, XPath, entre otros. Una vez localizado un elemento, podemos realizar diversas acciones como hacer clic, ingresar texto, etc.

### Ejemplo de localización de elementos y acciones básicas

```python
# Localizar un elemento por ID y hacer clic
button = driver.find_element(By.ID, 'submit-button')
button.click()
# Localizar un campo de texto por nombre e ingresar texto
input_field = driver.find_element(By.NAME, 'username')
input_field.send_keys('mi_usuario')
```

Tambien podemos utilizar selectores CSS y XPath para localizar elementos:

```python
# Localizar un elemento por selector CSS
element = driver.find_element(By.CSS_SELECTOR, '.mi-clase')
# Localizar un elemento por XPath
element = driver.find_element(By.XPATH, '//*[@id="mi-id"]')
```

## 4. Interacciones avanzadas
Selenium también permite realizar interacciones más avanzadas, como clicar, rellenar formularios, etc. Aquí hay algunos ejemplos:

```python
from selenium.webdriver.common.action_chains import ActionChains
# Hacer doble clic en un elemento
element = driver.find_element(By.ID, 'mi-elemento')
actions = ActionChains(driver)
actions.double_click(element).perform()

# Rellenar un formulario
form = driver.find_element(By.ID, 'mi-formulario')
form.find_element(By.NAME, 'campo1').send_keys('valor1')
form.find_element(By.NAME, 'campo2').send_keys('valor2')
form.submit()
```

## 5. Integración de Selenium con Behave (features + steps)
Para integrar Selenium con Behave, podemos definir nuestras pruebas en archivos *feature* y luego implementar los *steps* en Python utilizando Selenium para interactuar con la aplicación web.

### Ejemplo de archivo feature para pruebas web

```gherkin
@web_tests
Feature: Pruebas de login web

  @happy_path
  Scenario: Login exitoso
    Given que estoy en la página de login
    When ingreso el usuario "mi_usuario" y la contraseña "mi_contraseña"
    And hago clic en el botón de login
    Then debería ser redirigido a la página de inicio
```
### Ejemplo de steps en Python para pruebas web

```python
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
@given('que estoy en la página de login')
def step_given_en_login(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://www.ejemplo.com/login')

@when('ingreso el usuario "{username}" y la contraseña "{password}"')
def step_when_ingreso_credenciales(context, username, password):
    context.driver.find_element(By.NAME, 'username').send_keys(username)
    context.driver.find_element(By.NAME, 'password').send_keys(password)

@when('hago clic en el botón de login')
def step_when_hago_clic_login(context):
    context.driver.find_element(By.ID, 'login-button').click()

@then('debería ser redirigido a la página de inicio')
def step_then_redirigido_inicio(context):
    assert "inicio" in context.driver.current_url
    context.driver.quit()
```
#### Page Objects con Behave y Selenium
Con este framework también se pueden usar Page Objects para mejorar la mantenibilidad del código de pruebas, pero eso lo veremos en otro curso más avanzado, sin embbargo aqui os dejo un ejemplo sencillo de cómo integrar Page Objects con Behave y Selenium:

```python
# page_objects/login_page.py
from selenium.webdriver.common.by import By
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.NAME, 'username')
        self.password_field = (By.NAME, 'password')
        self.login_button = (By.ID, 'login-button')

    def enter_username(self, username):
        self.driver.find_element(*self.username_field).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()
```

```python 
# steps/login_steps.py
from behave import given, when, then
from selenium import webdriver
from page_objects.login_page import LoginPage

@given('que estoy en la página de login')
def step_given_en_login(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://www.ejemplo.com/login')
    context.login_page = LoginPage(context.driver)

@when('ingreso el usuario "{username}" y la contraseña "{password}"')
def step_when_ingreso_credenciales(context, username, password):
    context.login_page.enter_username(username)
    context.login_page.enter_password(password)

@when('hago clic en el botón de login')
def step_when_hago_clic_login(context):
    context.login_page.click_login()
```

```gherkin
# features/login.feature
Feature: Login de usuario
    Scenario: Login exitoso
        Given que estoy en la página de login
        When ingreso el usuario "mi_usuario" y la contraseña "mi_contraseña"
        And hago clic en el botón de login
        Then debería ser redirigido a la página de inicio
``` 

De no usar Page objects la definición de los elementos y las acciones se harían directamente en los steps, lo que puede hacer que el código sea menos mantenible a medida que crece el número de pruebas.
