# Git Hut: Simulador de Bus

## Asignatura

**Programación 1**

## Integrantes

**Marcelo Nacimba, Erick Estrada**

## Nombre del proyecto

**Bus Simulator 2024**

## Descripción del repositorio

- Visual Studio Code versión 17.0.14
- MySQL
- Funciones, Métodos, Clases, Concatenación, Tablas, Interfaz Gráfica, Componentes, Gráficos, Editores (Krita), Base de Datos, Importaciones, Colores, Videos, Posiciones, Bucles, Condiciones

## Descripción

Bus Simulator 2024 es un proyecto de programación en Python que simula el funcionamiento de un bus que realiza paradas en un total de 10 estaciones. En cada estación, el sistema cuenta cuántas personas entraron y cuáles asientos eligieron mediante reconocimiento de rostros. El cobro por cada persona que sube es de 0.35 centavos. Al finalizar todas las estaciones, el programa muestra el total de personas que se subieron y la recaudación total. La simulación incluye un efecto visual con la carretera para dar la impresión de que el bus está en movimiento.

![Imagen de la Simulación](ruta/a/la/imagen_simulacion.png)

## Motivación

La motivación de este proyecto fue poner en práctica lo que hemos aprendido, ya que vemos la base de este programa en Apache NetBeans con código Java.

## ¿Por qué se construyó este proyecto?

Este proyecto fue construido con el fin de implementar una interfaz interactiva con las nuevas características, funciones y métodos dados en la teoría.

## ¿Qué se aprendió?

Aprendimos nuevas metodologías, funciones, casos, variables enteras y variables con caracteres.

## Requisitos para abrir Bus Simulator 2024

- Sistema Operativo: Windows 10, Windows 11 o MacOS versión 12.7.5 o posterior.
- Python 3.12
- Librería para operaciones aleatorias (`random`)
- Librerías de reconocimiento facial (`cv2`)
- Librería para desarrollo de juegos (`pygame`)
- Tener Python y las librerías mencionadas correctamente configuradas en su ordenador.

## Instrucciones para abrir Bus Simulator 2024

1. Ve al repositorio y abre la carpeta `Bus-simulator-2024`.
2. Descarga el archivo `BusSimulator2024.exe`.
3. Cuando se instale, verás una advertencia. Haz clic derecho sobre ella y selecciona "Mantener".
4. Saldrá una nueva advertencia. Ve a "Más información" y selecciona "De todas formas, mantener".
5. Abre `BusSimulator2024.exe`.

![Imagen de la Instalación](ruta/a/la/imagen_instalacion.png)

## ¿Qué destaca en su proyecto?

Mi proyecto se destaca en su interfaz gráfica, su facilidad de uso y también la comunicación con los colaboradores.

## Descripción de la base de datos

La base de datos utilizada en el proyecto es MySQL y se encarga de almacenar la información relacionada con las personas que suben al bus, los asientos que eligen y la recaudación total. La estructura de la base de datos incluye tablas para usuarios, transacciones y estaciones.

### Ejemplo de tabla de usuarios

![Tabla de Usuarios](ruta/a/la/imagen_tabla_usuarios.png)

Bus-simulator-2024/
│
├── .vs/
│
├── assets/
│   ├── assetsBus/
│   ├── assetsComplements/
│   ├── assetsGrass/
│   ├── assetsInterface/
│   ├── assetsPerson/
│   ├── assetsShutdown/
│
├── game/
│   ├── __init__.py
│   ├── game_logic.py
│   ├── movement_bus.py
│
├── model/
│   ├── deploy.prototxt
│   ├── res10_300x300_ssd_iter_140000.caffemodel
│
├── ui/
│   ├── buttons.py
│   ├── main_menu.py
│   ├── screens.py
│   ├── ui_elements.py
│
├── utils/
│   ├── connector_database.py
│   ├── constants.py
│   ├── face_detector.py
│
├── video/
│
├── __pycache__/
│
└── README.md
