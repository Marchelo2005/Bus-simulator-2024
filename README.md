#  Simulador de Bus

## Asignatura

**Programación 1**

## Integrantes

**Marcelo Nacimba, Erick Estrada**

## Nombre del proyecto

**Bus Simulator 2024**

## Descripción del repositorio

- Visual Studio 2022 versión 17.0.14
- Python Version 3.12.4
- MySQL 8.4.1
- Funciones, Métodos, Clases, Concatenación, Tablas, Interfaz Gráfica, Componentes, Gráficos, Editores (Krita), Base de Datos, Importaciones, Colores, Videos, Posiciones, Bucles, Condiciones, Objetos

## Requerimientos Funcionales

### Detección y Conteo de Pasajeros
Implementar un sistema que utilice la librería `cv2` de OpenCV para detectar y contar el número de personas que suben al bus en cada estación

### Asignación de Asientos
Asignar aleatoriamente asientos a cada pasajero detectado por el sistema

### Recaudación de Tarifas
Calcular y registrar una tarifa de 0.35 centavos por cada pasajero que sube al bus

### Gestión de Estaciones
Simular paradas en un total de 10 estaciones

### Base de Datos
Almacenar la información de los pasajeros, los asientos ocupados y la recaudación total en una base de datos MySQL
La tabla de base de datos debe incluir al menos los campos: `ID` (identificador único), `date` (fecha y hora del evento), `totalPersons` (número total de personas) y `totalMoney` (dinero total recaudado)

### Simulación Visual del Movimiento del Bus
Crear un efecto visual que simule el movimiento del bus por la carretera

### Interfaz Gráfica de Usuario (GUI)
Desarrollar una interfaz gráfica para que los usuarios puedan interactuar con el simulador de manera intuitiva

### Actualización en Tiempo Real
Actualizar los datos en la base de datos cada vez que se detectan nuevos pasajeros y se asignan asientos

## Requerimientos No Funcionales

### Compatibilidad
El sistema debe funcionar en sistemas operativos Windows 10, Windows 11 y MacOS versión 12.7.5 o posterior

### Rendimiento
La detección de rostros y procesamiento deben ocurrir en tiempo real, sin retrasos perceptibles para el usuario

### Escalabilidad
El sistema debe ser capaz de manejar un creciente número de registros de pasajeros y transacciones sin afectar negativamente el rendimiento

### Facilidad de Uso
La interfaz gráfica de usuario (GUI) debe ser intuitiva y fácil de navegar para los usuarios, incluso aquellos con poca experiencia técnica

### Disponibilidad
La base de datos debe estar alojada en la nube para permitir el acceso desde cualquier ubicación con conexión a Internet

### Documentación y Tutoriales
Debe haber documentación adecuada y tutoriales (incluyendo videos) que guíen a los usuarios en la instalación, configuración y uso del sistema


## Descripción

Bus Simulator 2024 es un proyecto de programación en Python que simula el funcionamiento de un bus que realiza paradas en un total de 10 estaciones. En cada estación, el sistema cuenta cuántas personas entraron y cuáles asientos eligieron mediante reconocimiento de rostros. El cobro por cada persona que sube es de 0.35 centavos. Al finalizar todas las estaciones, el programa muestra el total de personas que se subieron y la recaudación total. La simulación incluye un efecto visual con la carretera para dar la impresión de que el bus está en movimiento.

<img width="596" alt="Captura de pantalla 2024-07-22 204956" src="https://github.com/user-attachments/assets/d9e2544f-31b3-46a3-8428-1a0d1ec5ec9c">

## Detector de Caras

El detector de caras en Bus Simulator 2024 utiliza la librería `cv2` de OpenCV para detectar y contar el número de personas que suben al bus en cada estación. Este componente es fundamental para simular la interacción de los pasajeros con el bus, permitiendo un conteo preciso y la asignación aleatoria de asientos. A continuación se describen los elementos clave del detector de caras:

## Elementos Clave del Detector de Caras:

- **Librería Utilizada**: El detector de caras está implementado utilizando OpenCV (`cv2`), una biblioteca de visión por computadora muy popular.
- **Modelo Preentrenado**: Utiliza un modelo de red neuronal convolucional preentrenado, conocido como `res10_300x300_ssd_iter_140000.caffemodel`, que es eficaz para la detección de rostros en tiempo real.
- **Integración con el Sistema**: Cada vez que una persona sube al bus, el detector de caras registra su presencia y asigna un asiento de manera aleatoria. Además, actualiza la base de datos con esta información para mantener un registro detallado.

### Ejemplo de Detección de Caras




https://github.com/user-attachments/assets/1a5b2d4a-eff1-4669-bb20-ba95a297af99






A continuación se muestra un ejemplo visual de cómo el detector de caras identifica y cuenta a las personas en una imagen:



En la imagen, se pueden ver los cuadros delimitadores alrededor de los rostros detectados, lo que indica que el sistema ha reconocido correctamente a cada individuo.

## Motivación

La motivación detrás del desarrollo de Bus Simulator 2024 surge de la necesidad de aplicar y consolidar los conocimientos adquiridos en el curso de Programación 1. A lo largo del curso, hemos estudiado diversos conceptos y técnicas de programación, incluyendo funciones, métodos, clases, manejo de bases de datos, y el desarrollo de interfaces gráficas. Este proyecto nos proporciona una oportunidad única para integrar todos estos elementos en una aplicación práctica y funcional.


Nuestro objetivo principal fue desarrollar un proyecto que reflejara el nivel de conocimiento y competencia que hemos alcanzado, al mismo tiempo que nos enfrentamos a desafíos reales de programación y diseño. Esperamos que Bus Simulator 2024 no solo sea una demostración de nuestras capacidades, sino también una inspiración para futuros proyectos y desarrollos en el campo de la programación.


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

![510c84bb-6e8f-4b30-8f24-9be937853781](https://github.com/user-attachments/assets/116ff195-a542-4fdf-9382-e94ff40fe8d8)

Video Tutorial
##https://www.youtube.com/watch?v=qORN56tScEU


## ¿Qué destaca en su proyecto?

Mi proyecto se destaca en su interfaz gráfica, su facilidad de uso y también la comunicación con los colaboradores.

## Descripción de la base de datos (esestrada_simula)

La base de datos utilizada en el proyecto es MySQL y se encarga de almacenar la información relacionada con las personas que suben al bus, los asientos que eligen y la recaudación total. La estructura de la base de datos incluye tablas para usuarios, transacciones y estaciones.

Durante el desarrollo del proyecto, probamos diferentes opciones de bases de datos y concluimos que Alwaysdata fue la mejor opción debido a su oferta de 100 MB de espacio gratuito y por estar en la nube. Esta capacidad nos permite almacenar toda la información necesaria sin costos adicionales y facilita el acceso a los datos desde cualquier ubicación, proporcionando flexibilidad y escalabilidad.

## Base de Datos alwaysdata
![image](https://github.com/user-attachments/assets/a055667b-b10a-4382-ab6c-2d4f16c3fbf9)

## Databases - MySQL
![image](https://github.com/user-attachments/assets/df9e698b-bf4b-45fc-b55e-ea1f88e13f34)

## phpMyAdmin
![image](https://github.com/user-attachments/assets/9f61a0dd-7933-489f-9ad0-65a4de8e224b)

### Ejemplo de tabla de usuarios (ACCOUNTINGTWO)

<img width="263" alt="Captura de pantalla 2024-07-22 233418" src="https://github.com/user-attachments/assets/8e9659ae-643c-4337-b388-0746dcae05c2">



## Estructura del Proyecto

```plaintext
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



















video 
https://youtube.com/shorts/GQObzGnVibA?si=UBIfqSVLVzO1tzFF
