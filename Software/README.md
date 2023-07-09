# Componentes de software
En esta carpeta se encuentran todos los códigos desarrollados para el funcionamiento de este proyecto, los cuales incluyen:

1) Código para toma y transferencia de datos con la ESP32-Cam.
2) Códigos de entrenamiento del modelo de segmentación y de los modelos de detección.
3) Código de la interfaz de usuario.

## Código de la ESP32-Cam.
En este apartado se encuentra el código de la ESP32-Cam, donde se captura una imagen del contador de agua cada tres horas. Además, realiza el proceso de conexión al servidor local FTP para enviar las imágenes capturadas,  en caso de no estar disponible se guardan en la tarjeta SD hasta indicar disponibilidad para ser enviadas y eliminadas de la memoria.

## Códigos de entrenamiento
En esta carpeta se encuentran los códigos realizados para el entrenamiento y validación con YOLOv8m en segmentación, YOLOv8m y Detectron2 para detección, con el fin de realizar una comparativa de rendimiento entre estos dos últimos, cada modelo se encuentra con su respectivo código en google colab donde fueron ejecutados y se  observan las métricas de rendimiento obtenidas en cada caso.

## Código de la interfaz
En esta carpeta se encuentran todos los archivos y los recursos utilizados para el funcionamiento de la interfaz desarrollada en Qt Designer. Se incluyen todos los elementos visuales como iconos e imágenes que se muestran en la interfaz, así como los códigos generados para su correcto funcionamiento y despliegue.
******

