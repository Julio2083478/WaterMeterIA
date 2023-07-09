# DISEÑO DE UN SISTEMA DIGITAL PARA LA LECTURA DE CONTADORES DE AGUA POR MEDIO DE CÁMARAS E IA. 

<p align="center">
  <img src="https://i.imgur.com/2JUb7EV.png" alt="Alt Text">
</p>


## Descripción del sistema.
<p align="justify">
La toma de datos de los medidores es realizada manualmente por las empresas prestadoras de servicios, que van casa por casa registrando el consumo mensual de las mismas, lo que implica que el usuario no pueda llevar un seguimiento detallado de su consumo, supone errores humanos, baja eficiencia, baja efectividad, susceptibilidad a factores ambientales y costos adicionales por la mano de obra requerida. Esto lleva a la necesidad de crear sistemas y/o elementos que automaticen o digitalicen el proceso de recolección de datos en los medidores y faciliten al usuario el seguimiento de su consumo a lo largo del mes.
</p>
<p align="justify">
La inclusión de instrumentos inteligentes debe ser clave, ya que brindan al usuario la posibilidad de llevar un registro detallado del uso del servicio para así poder identificar malos hábitos de consumo, fugas en las tuberías, posible deterioro de estas, desgaste de los sellos o malos empalmes que generan consumos fantasmas, para así tomar las acciones necesarias en pro de evitar sobrecostos generados. Este proyecto pretende implementar un módulo o estructura de fácil acople para medidores de agua convencionales, por medio del cual se capturarán imágenes que serán enviadas inalámbricamente para su posterior análisis y digitalización por medio de IA. 
</p>

## Enlace de la base de datos para segmentar.

* https://app.roboflow.com/ds/DAJvCus5p3?key=saQ0dXVDxN

## Enlace de la base de datos para detección. 

* Para la YoloV8: https://app.roboflow.com/ds/EEVCR4GifU?key=4THAoHTpj3
* Para Detectron: https://app.roboflow.com/ds/PTGveqEZnr?key=orbd7gfs7z

## Instrucciones de uso. 

### Instructivo del Hardware.

<p align="justify">
1. Para ajustar el contador de agua modelo R200 a la estructura, inicie aflojando levemente las tuercas de los extremos, luego coloque el cuerpo principal asegurándose que los orificios en forma de "U" encajen correctamente a cada extremo del tubo del contador, una vez en su lugar finalice apretando nuevamente las tuercas para asegurar la estructura al contador. Es importante tener en cuenta  que el lente de la cámara debe quedar paralelo al contador para garantizar una captura óptima de las imágenes.
</p>

| ![Alt Text](https://i.imgur.com/3TAgVZ6.jpg) | ![Alt Text](https://i.imgur.com/BaZHDOm.jpg)  | ![Alt Text](https://i.imgur.com/JFChdmN.jpg)  |
|----------------------------------------------|---------------------------------------------|---------------------------------------------|

### NOTA: 
Verifique el nivel de carga del dispositivo. Esto se puede hacer  a través de los  LED’s indicadores incorporados , si todos los LED’s están encendidos la power bank tiene suficiente carga. En caso contrario asegúrese de recargar las baterías para garantizar que el dispositivo esté listo para su uso. 

### Paso a paso del servidor.
<p align="justify">
1.Dirijase desde su navegador a la pagina de filezilla(https://filezilla-project.org/) luego descargue FileZilla Server.
</p>

<p align="justify">
2.Luego de descargar FileZilla Proceda a abrirlo, en la sección de Host debe ingresar "localhost", el puerto puede dejar el que aparezca por defecto y pude definir la contraseña que desee.
</p>

<p align="justify">
3.Realice la cofiguración de los usuarios y grupos, en caso de solo haber usuarios individuales asegurese de dar acceso a cada uno de ellos a la carpeta donde se guardarán las imagenes (permisos de escritura y lectura).
</p>

<p align="justify">
4.Verifique que el cortafuegos de su computadora le permita a filezilla realizar solicitudes por el puerto asignado, por defecto es el puerto 21 , para más información revise la documentación de FilezZilla en su pagina oficial.
</p>

### Paso a paso de la Interfaz de usuario.
<p align="justify">
1. Busque la aplicación "water meter IA" y dele doble click.
</p>

<p align="center">
  <img src="https://i.imgur.com/5sWeFKc.png" alt="Alt Text">
</p>


<p align="justify">
2. Se debe abrir una pestaña de incio como esta.
</p>
   
<p align="center">
  <img src="https://i.imgur.com/u1us7qT.png" alt="Alt Text">
</p>

<p align="justify">
3. En la pestaña Ref Contadores encontrara la información general de los usuarios.
</p>

<p align="center">
  <img src="https://i.imgur.com/CLFNdMS.png" alt="Alt Text">
</p>

<p align="justify">
4. En la pestaña medición diaria observara la gráfica del consumo diario.
</p>

<p align="center">
  <img src="https://i.imgur.com/o6EXqwF.png" alt="Alt Text">
</p>

<p align="justify">
5. En la pestaña medición semanal observara la gráfica del consumo semanal.
</p>

<p align="center">
  <img src="https://i.imgur.com/TkU3QoH.png" alt="Alt Text">
</p>

<p align="justify">
6. En la pestaña medición mensual observara la gráfica del consumo mensual.
</p>

<p align="center">
  <img src="https://i.imgur.com/7gBMfnQ.png" alt="Alt Text">
</p>

<p align="justify">
7. En la pestaña medición anual observara la gráfica del consumo anual.
</p>

<p align="center">
  <img src="https://i.imgur.com/ZTOhhG0.png" alt="Alt Text">
</p>

<p align="justify">
8. En la pestaña visualización observara la ultima inferencia que se realizó.
</p>

<p align="center">
  <img src="https://i.imgur.com/sAflurm.png" alt="Alt Text">
</p>

## Contribución.
<p align="justify">
Este proyecto se encuentra en constante evolución, por lo que cualquier contribución será bienvenida. Si desea contribuir, por favor envíe un pull request o contacta al equipo de desarrollo.
</p>

## Contacto.

* KATHERINE PAOLA PARRA TARAZONA. katherineparratarazona@gmail.com
  
* JULIO ANDRÉS SÁNCHEZ ABELLO. jasanchezabe@gmail.com 

