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

## Link de la base de datos para segmentar.

* https://app.roboflow.com/ds/DAJvCus5p3?key=saQ0dXVDxN

## Link de la base de datos para detección. 

* Para la YoloV8: https://app.roboflow.com/ds/EEVCR4GifU?key=4THAoHTpj3
* Para Detectron: https://app.roboflow.com/ds/PTGveqEZnr?key=orbd7gfs7z

## Manual de usuario. 

### Paso a paso del Hardware.
1. Cuidadosamente ajuste el contador R200 al dispositivo, desatornillando sus extremos y apretandolo al mismo, teniendo en cuenta que el contador debe estar de forma paralela a la superficie que se encuentre la camara.

| ![Alt Text](https://i.imgur.com/3TAgVZ6.jpg) | ![Alt Text](https://i.imgur.com/BaZHDOm.jpg)  | ![Alt Text](https://i.imgur.com/JFChdmN.jpg)  |
|----------------------------------------------|---------------------------------------------|---------------------------------------------|

### NOTA: 
Verique que el dispositivo se encuentre con carga, de lo contrario ponga a cargar las baterias. 

### Paso a paso del servidor.
<p align="justify">
1.Dirijase desde su navegador a la pagina de filezilla(https://filezilla-project.org/) luego descargue FileZilla Server.

2.Luego de descargar FileZilla Proceda a abrirlo, en la sección de Host debes ingresar "localhost", el puerto puedes dejar el que aparezca por defecto y pudes definir la contraseña que desees.

3.Realiza la cofiguración de los usuarios y grupos, en caso de solo haber usuarios individuales asegurese de dar acceso a cada uno de ellos a la carpeta donde se guardarán las imagenes(permisos de escritura y lectura).

4.Verifica que el cortafuegos de tu computadora le permita a filezilla realizar solicitudes por el puerto asignado, por defecto es el puerto 21 , para más información revise la documentación de FilezZilla en su pagina oficial.
</p>

### Paso a paso de la Interfaz de usuario.
1. Busque la aplicación "water meter IA" y dele doble click.
   
2. Se debe abrir una pestaña de incio como esta.
   
<p align="center">
  <img src="https://i.imgur.com/9qoZ4Hj.png" alt="Alt Text">
</p>

3. En la pestaña Ref Contadores encontraras la información general de los usuarios.

<p align="center">
  <img src="https://i.imgur.com/FFEQMcV.png" alt="Alt Text">
</p>

4. En la pestaña medición diaria observaras graficas del consumo diario.

<p align="center">
  <img src="https://i.imgur.com/7Dku74f.png" alt="Alt Text">
</p>

5. En la pestaña medición semanal observaras graficas del consumo semanal.

<p align="center">
  <img src="https://i.imgur.com/hcb77sv.png" alt="Alt Text">
</p>

6. En la pestaña medición mensual observaras graficas del consumo mensual.

<p align="center">
  <img src="https://i.imgur.com/p7HhSBp.png" alt="Alt Text">
</p>

7. En la pestaña medición anual observaras graficas del consumo anual.

<p align="center">
  <img src="https://i.imgur.com/gjcs74i.png" alt="Alt Text">
</p>

8. En la pestaña visualización observaras la ultima inferencia que se realizó.
 
<p align="center">
  <img src="https://i.imgur.com/577xzOy.png" alt="Alt Text">
</p>

## Contribución.

Este proyecto se encuentra en constante evolución, por lo que cualquier contribución será bienvenida. Si deseas contribuir, por favor envía un pull request o contacta al equipo de desarrollo.

## Contacto.

* KATHERINE PAOLA PARRA TARAZONA. katherineparratarazona@gmail.com 
* JULIO ANDRÉS SÁNCHEZ ABELLO. jasanchezabe@gmail.com 
