# Componentes de software
En este apartado se encuentran todos los codigos para el desarrollo del proyecto, los cuales incluyen:

1) Codigo para toma de datos con la ESP32-Cam.
2) Codigos de entrenamiento del modelo de segmentacaón y el modelo de detección.
3) Codigo de la interfaz.

## Codigo de la ESP32-Cam.
En dicho apartado se encuentra el codigo de la ESP32-Cam, donde se realiza el proceso de la conexión al servidor FTP o en caso de no estar disponible se guardan las capturas en la tarjeta sd hasta que se encuentre disponible para ser enviadas y eliminadas de la memoria.

## Codigos de entrenamiento
En esta carpeta se encuentran los codigos de YOLOv8m para segmentar, YOLOv8m para detección y Detectron2 tambien para detección, con el fin de realizar una comparativa de rendimiento entre estos dos ultimos, cada modelo se encuentra con su respectivo colab donde fueron ejecutados y se  observan las metricas de rendimiento.

## Codigo de la interfaz
En esta carpeta se encuentran los archivos necesarios para el funcionamiento de la interfaz desarrollada en Qt Designer.
******
