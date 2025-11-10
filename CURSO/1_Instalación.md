# Instalación y configuración del entorno

En este apartado configuraremos el framework de desarrollo, instalaremos las dependencias y librerías necesarias y por último ojearemos la estructura del framework y cómo está orientado.

## 1. Instalación de Python

Crear un entorno de desarrollo sencillo
Desde la consola de Windows Powel Shell ejecutaremos:

` python3 `

En Windows el sistema nos abrirá la Microsoft Store si no se ha instalado antes. Lo instalaremos ya que no necesita privilegios adicionales.

Una vez instalado, volveremos a ejecutar el código anterior y nos debería aparecer un prompt como el siguiente:

```
 $ python3 

Python 3.10.9 (tags/v3.10.9:1dd9be6, Dec  6 2022, 20:01:21) [MSC v.1934 64 bit (AMD64)] on win32

Type "help", "copyright", "credits" or "license" for more information.

>>>
```
## 2. Instalación del IDE

Ahora instalaremos **VS Code.** VS Code es un editor de código Open Source multiplataforma muy potente que nos permite instalar multitud de extensiones creadas por la comunidad. Lo podemos instalar desde la Microsoft Store.

Desde el gestor de extensiones instalaremos el **plug-in Microsoft** para Python, que instalará otras dependencias que vamos a usar en este curso.

## 3. Preparar el entorno virtual

Para instalar las dependencias del proyecto, es recomendable crear un entorno virtual. Un entorno virtual es un espacio aislado donde podemos instalar paquetes específicos para nuestro proyecto sin afectar al resto del sistema.

Para crear un entorno virtual, abrimos una terminal en VS Code y ejecutamos el siguiente comando:

` python -m venv venv `

Esto creará una carpeta llamada `venv` en nuestro proyecto que contendrá el entorno virtual.

Para activar el entorno virtual, ejecutamos el siguiente comando en la terminal:

  ` .\venv\Scripts\activate `

Veremos que el prompt de la terminal cambia para indicar que estamos dentro del entorno virtual.

## 4. Instalación de dependencias con pip

Pip es el instalador de paquetes para Python. Es una herramienta de consola que permite instalar y gestionar paquetes o módulos de Python, que están disponibles en el Python Package Index (PyPI).

Con Pip, puedes instalar paquetes desde la línea de comandos escribiendo :

`pip install <nombre_paquete>`

Nosotros instalaremos nuestras dependencias directamente desde el archivo *requirements.txt*

`pip install -r requirements.txt`

Si aparece un error, podríamos ejecutar lo siguiente:

`$ pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt`

o bien:

`$ pip install --user --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt`

## 5. Estructura del framework

La estructura del framework es la siguiente:

```
Python-BDD-automation-framework/
│
├── settings/
│   ├── environments/
│   │   ├── cer/
│   │   ├── dev/
|   ├── report_templates/
│   │   ├── feature_template.html
│   │   ├── global_template.html
│   ├── logging.py
│   ├── report_generator.py
│   ├── settings.py
├── tests/
│   ├── features/
│   │   ├── apis/
│   │   │   ├── api_tests.feature
│   │   ├── web/
│   │   │   ├── web_tests.feature
│   ├── steps/
│   │   ├── api_steps.py
│   │   ├── web_steps.py
|   ├── helpers/
│   │   ├── schemas/
│   │   │   ├── user_schema.py
│   ├── environment.py              # hooks de Behave
├── reports/
│   ├── <report_files>.html
├── venv/
├── requirements.txt
├── main.py
├── README.md
```

