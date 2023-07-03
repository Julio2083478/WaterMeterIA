# *************************************************************************************
# *                                                                                   *
# *                            LIBRERÍAS                                              *
# *                                                                                   *
# *************************************************************************************

# Importación de la librería "sys".
import sys  # Proporciona acceso a variables y funciones relacionadas con el intérprete del sistema.

# Importación de la librería "numpy" con el alias "np".
import numpy as np  # Proporciona soporte para arrays y operaciones numéricas eficientes.

### IMPORTAMOS EL ARCHIVO.PY DE LA INTERFAZ ###
from ui_INTERFAZMOCKUPFINAL import *  # Importa el archivo .py "ui_INTERFAZMOCKUPFINAL" para la interfaz.

############################################### 

### LIBRERIAS PARA GRAFICAR / LECTURA DE ARCHIVOS .CSV (EXCEL) ######################

# Importación de la clase "FigureCanvasQTAgg" del módulo "matplotlib.backends.backend_qt5agg".
# Esta clase proporciona una interfaz entre Matplotlib y Qt para mostrar gráficos en una aplicación Qt.
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

# Importación de la clase "Figure" del módulo "matplotlib.figure".
# Esta clase representa una figura vacía, en la cual se pueden agregar subplots, ejes y gráficos.
from matplotlib.figure import Figure

# Importación de la librería "matplotlib.pyplot" con el alias "plt".
# Proporciona funciones para crear gráficos y visualizar datos de forma interactiva.
import matplotlib.pyplot as plt

# Importación de la librería "pandas" con el alias "pd".
# Proporciona estructuras de datos y herramientas para el análisis de datos.
import pandas as pd

#-----------------------------------------------------------------------------------#

### LIBRERÍAS PARA INTERFAZ ########################################################

# Importación de la librería "cv2".
# Proporciona funciones para el procesamiento de imágenes y visión por computadora.
import cv2

# Importación del módulo "time".
# Proporciona funciones relacionadas con el tiempo y la medición del tiempo de ejecución.
import time

#-------------------------------------------------------------------------------------------#

#IMPORTAMOS OPENPYXL
import openpyxl

#IMPORTAMOS CSV
import csv

#IMPORTAMOS LIBRERIAS DE QT PARA CAMBIOS ESTÉTICOS
from PyQt5.QtGui import QScreen
from PyQt5.QtGui import QTextCharFormat
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt, QDate
#IMPORTAMOS EL DATETIME PARA CONSUMO SEMANAL
from datetime import datetime, timedelta
from datetime import timedelta, date

#La librería "dateutil.parser" proporciona funcionalidades para analizar y convertir cadenas de
#texto en objetos de fecha y hora en Python. El módulo "parse" dentro de esta librería es 
#especialmente útil para analizar cadenas de texto que representan fechas y horas en 
#diferentes formatos y convertirlas en objetos de fecha y hora que se puedan manipular
#fácilmente en Python.
from dateutil.parser import parse

#IMPORTAMOS CALENDARIO PARA MOSTRAR EN EL CONSUMO DEL MES EL NOMBRE DEL MES Y NO EL NÚMERO CORRESPONDIENTE AL MES
import calendar
#Para poner los calendarios en español
from PyQt5.QtCore import QLocale
#para validar el line edit del codigo suscriptor
from PyQt5.QtGui import QIntValidator
#para visualizacion
import os

# Utilizando la librería PyQt5.QtGui importamos las clases QImage y QPixmap 
#para trabajar con imágenes en nuestra interfaz gráfica. Estas clases nos permiten 
#cargar, manipular y mostrar imágenes de manera sencilla y eficiente. 
#Con QImage podemos realizar operaciones más avanzadas en la imagen, mientras que QPixmap nos brinda una 
#interfaz optimizada para la visualización en widgets. Juntas, estas clases nos brindan todas las herramientas 
#necesarias para trabajar con imágenes en nuestras aplicaciones PyQt5.
from PyQt5.QtGui import QImage, QPixmap

#Para corregir la fuente de la tabla
from PyQt5.QtGui import QFont 

#para las carpetas
import shutil
import threading
import signal
import random
#Importamos la funcion que hará el proceso de inferencia del algoritmo de aprendizaje profundo
from Funcion_inferencia import inferencia
############################### FIN LIBRERÍAS #################################################

class MiApp(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow() 
        self.ui.setupUi(self)

        #Bandera para detener el proceso de "gestionar_carpetas"
        self.detener_proceso = False

        app = QApplication([])
        # Obtener la pantalla principal
        screen = app.primaryScreen()
        
        # Obtener la resolución de la pantalla
        resolution = screen.size()


        #Variable usada para alternar estados de operación de 1 a 0 y de 0 a 1 así sucesivamente-#
        self.estado = 1
        #----------------------------------------------------------------------------------------#
        #print(resolution.width(), resolution.height())#Para ver la resolución de la ventana
        self.resize(resolution.width()-1200, resolution.height()-1200)#Para volver la ventana un poco cuadrada restamos 800 a ancho y alto

        
        ## ACCESO A LAS PÁGINAS #############################################################################
        self.ui.btn_p1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_inicio))
        self.ui.btn_p2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_uno))
        self.ui.btn_p3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_dos))
        self.ui.btn_p4.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_cuatro))
        self.ui.btn_p5.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_tres))
        self.ui.btn_p6.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_cinco))
        self.ui.btn_p7.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_seis))
        ####################################################################################################

        ## MENU IZQUIERDO #########################################
        #--Las funciones aquí citadas se encuentran más abajo
        self.ui.bt_menu.clicked.connect(self.mover_menu_izq) #botón de menu
        self.ui.bt_menu.clicked.connect(self.intercambiodeiconos1) 
        self.ui.bt_atras.clicked.connect(self.mover_menu_izq) #botón "atrás" que aparece luego de pulsar menú
        self.ui.bt_atras.clicked.connect(self.intercambiodeiconos2)
        self.ui.bt_atras.hide() #Se esconde en primera instancia 
        ###########################################################

        ## MENU DERECHO ###########################################
        self.ui.bt_newref.clicked.connect(self.mover_menu_der) #botón para añadir la nueva referencia (en color amarillo)
        self.ui.bt_x.clicked.connect(self.mover_menu_der)
        ###########################################################
       

        ## LOGO QUE SOLO SE VE CUANDO ESTAMOS EN UNA PÁGINA DIFERENTE A INICIO (miniatura) ##########
        self.ui.bt_logosup.hide()#LO OCULTAMOS DE INICIO, YA QUE INICIAMOS EN LA PÁGINA "INICIO"
        #--Funciones usadas se encuentran más abajo
        self.ui.btn_p1.clicked.connect(self.esconderlogosup)#Pulsando la página inicio desaparece
        self.ui.btn_p2.clicked.connect(self.mostrarlogosup)#Pulsando la página 2 aparece
        self.ui.btn_p3.clicked.connect(self.mostrarlogosup)#Pulsando la página 3 aparece
        self.ui.btn_p4.clicked.connect(self.mostrarlogosup)#Pulsando la página 4 aparece
        self.ui.btn_p5.clicked.connect(self.mostrarlogosup)#Pulsando la página 5 aparece
        self.ui.btn_p6.clicked.connect(self.mostrarlogosup)#Pulsando la página 6 aparece
        self.ui.btn_p7.clicked.connect(self.mostrarlogosup)#Pulsando la página 7 aparece
        ############################################################################################

        ## Para los iconos + y x de la página de ref contador ####### 
        self.ui.bt_x.hide()#Se oculta de inicio el icono "X"
        self.ui.bt_newref.clicked.connect(self.alternarestado)#Si se pulsa bt_newref "Nueva referencia", se acciona alternarestado
        self.ui.bt_x.clicked.connect(self.alternarestado)#Si se pulsa bt_x "Nueva referencia", se acciona alternarestado
        #############################################################
        
        ############################## PARA GRAFICAR #############################################################
        
        #Importamos el dataframe #############################################################
        self.dataframe = pd.read_csv('water_consumption_f.csv')
        # Convierte la columna 'Fecha' en un objeto de fecha y hora en el DataFrame
        self.dataframe['Fecha'] = pd.to_datetime(self.dataframe['Fecha'], format='%d/%m/%Y') 

        

        # Centrar el texto en el QLabel consumo_m_numero
        self.ui.consumo_m_numero.setAlignment(QtCore.Qt.AlignCenter)
        # Centrar el texto en el QLabel estado_consumo_label
        self.ui.alerta_consumo.setAlignment(QtCore.Qt.AlignCenter)  
        # Centrar el título de WATER METER
        self.ui.label_2.setAlignment(QtCore.Qt.AlignCenter)

        #CONSUMO TOTAL EN LA PARTE SUPERIOR DE LA APP (COLOR AMARILLO)
        #self.actualizarConsumoTotal(mes=2)#Desplegar Febrero
        #self.actualizarConsumoTotal(mes=3)#Desplegar Marzo
        self.actualizarConsumoTotal(mes=4)#Desplegar Abril
        

        ## GRÁFICA DIARIA ######################################################################## 
        
        #Layout horizontal para la gráfica diaria
        self.horizontalLayout_44 = QtWidgets.QHBoxLayout(self.ui.frame_canvas1) #Añadimos el horizontalLayout dentro del frame_canvas1 puesto en QTDesigner
        self.horizontalLayout_44.setObjectName("horizontalLayout_4")  #Se define el nombre del objeto en el cual pondremos el canvas
        
        
        ## Inicialización de los objetos
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        
        ##Añadimos el objeto canvas al "horizontalLayout_44"
        self.horizontalLayout_44.addWidget(self.canvas) #Se añade el canvas al horizontalLayout
        
        ## FIN - GRÁFICA DIARIA ################################################################## PROBLEMA
        
        ## GRÁFICA SEMANAL ######################################################################## 
        
        #Layout horizontal para la gráfica SEMANAL
        self.horizontalLayout_222 = QtWidgets.QHBoxLayout(self.ui.frame_canvas2) #Añadimos el horizontalLayout dentro del frame_canvas2 puesto en QTDesigner
        self.horizontalLayout_222.setObjectName("horizontalLayout_222") #Se define el nombre del objeto en el cual pondremos el canvas 
        
        
        ## Inicialización de los objetos
        self.figure2 = plt.figure()
        self.canvas2 = FigureCanvas(self.figure2)
        
        ##Añadimos el objeto canvas2 al "horizontalLayout_222"
        self.horizontalLayout_222.addWidget(self.canvas2) #Se añade el canvas al horizontalLayout
        ## FIN - GRÁFICA SEMANAL ##################################################################

        ## GRÁFICA MENSUAL ######################################################################## 
        
        #Layout horizontal para la gráfica MENSUAL
        self.horizontalLayout_333 = QtWidgets.QHBoxLayout(self.ui.frame_canvas3) #Añadimos el horizontalLayout dentro del frame_canvas3 puesto en QTDesigner
        self.horizontalLayout_333.setObjectName("horizontalLayout_333") #Se define el nombre del objeto en el cual pondremos el canvas
        
        
        ## Inicialización de los objetos
        self.figure3 = plt.figure()
        self.canvas3 = FigureCanvas(self.figure3)
        
        ##Añadimos el objeto canvas2 al "horizontalLayout_333"
        self.horizontalLayout_333.addWidget(self.canvas3) #Se añade el canvas al horizontalLayout
        

        ## FIN - GRÁFICA MENSUAL ##################################################################


        ## GRÁFICA ANUAL ######################################################################## 
        
        #Layout horizontal para la gráfica MENSUAL
        self.horizontalLayout_444 = QtWidgets.QHBoxLayout(self.ui.frame_canvas4) #Añadimos el horizontalLayout dentro del frame_canvas4 puesto en QTDesigner
        self.horizontalLayout_444.setObjectName("horizontalLayout_444") 
        
        
        ## Inicialización de los objetos
        self.figure4 = plt.figure()
        self.canvas4 = FigureCanvas(self.figure4)
        
        ##Añadimos el objeto canvas2 al "horizontalLayout_444"
        self.horizontalLayout_444.addWidget(self.canvas4) #Se añade el canvas al horizontalLayout
        ## FIN - GRÁFICA ANUAL ##################################################################
        

        ## INSTANCIAS DE LAS GRAFICAS DIARIAS/SEMANAL/MENSUAL/ANUAL
        self.ui.btn_p3.clicked.connect(self.Funciongraficadiaria) #Pulsando el btn_p3 se inicia "Funciongraficadiaria"
        self.ui.btn_p4.clicked.connect(self.Funciongraficasemanal) #Pulsando el btn_p4 se inicia "Funciongraficasemanal"
        self.ui.btn_p5.clicked.connect(self.Funciongraficamensual) #Pulsando el btn_p5 se inicia "Funciongraficamensual"
        self.ui.btn_p6.clicked.connect(self.Funciongraficaanual) #Pulsando el btn_p6 se inicia "Funciongraficaanual"
        
        ##### CALENDARIOS ###################################################################################
        ##CALENDARIO
        self.calendario = self.ui.calendarWidget

        ##CALENDARIO 2
        self.calendario2 = self.ui.calendariosemanal

        ##CALENDARIO 3
        self.calendario3 = self.ui.calendariomensual

        ##CALENDARIO 4
        self.calendario4 = self.ui.calendarioanual
        ##### FIN - CALENDARIOS ###################################################################################


        ### PARA CAMBIAR EL IDIOMA DE LOS CALENDARIOS A ESPAÑOL
        locale = QLocale(QLocale.Spanish, QLocale.Spain) # Establece la configuración regional para el idioma español de España
        # Asignación de la configuración a cada calendario
        self.calendario.setLocale(locale) 
        self.calendario2.setLocale(locale)
        self.calendario3.setLocale(locale)
        self.calendario4.setLocale(locale)


        ## FUNCIONES DE LOS CALENDARIOS ##

        #Se insta la función "Funciongraficadiaria" cada vez que se seleccione un día
        self.calendario.selectionChanged.connect(self.Funciongraficadiaria) 
       
        #Se insta la función "obtener_rango_semana" (que es la que nos da las semanas que se plotearán) cada vez que se seleccione un día 
        self.calendario2.selectionChanged.connect(lambda: self.obtener_rango_semana(self.calendario2, self.calendario2.selectedDate().toString("M/d/yyyy")))
        
        #Se insta la función "Funciongraficasemanal" cada vez que se selecciona un día
        self.calendario2.selectionChanged.connect(self.Funciongraficasemanal)

        #Se insta la función "Funciongraficamensual" cada vez que se cambia el día ó el mes ó el año
        self.calendario3.currentPageChanged.connect(self.Funciongraficamensual)
        
        #Se insta la función "Funciongraficaanual" cada vez que se cambia el día ó el mes ó el año
        self.calendario4.currentPageChanged.connect(self.Funciongraficaanual)


        ## PARA LAS REFERENCIAS ##

        #Al dar click en el botón "anadir", se insta la función guardad
        self.ui.anadir.clicked.connect(self.guardad) 

        #Al dar click en el botón "btn_p2" (que es el que direcciona a las "REFERENCIAS"), se muestran los datos actuales del .csv
        self.ui.btn_p2.clicked.connect(self.mostrar_datos_actuales) 
        
        ## Menú - Eliminar referencias ########

        #Al dar click en el botón "btn_menu_elim_ref", se activa la función "mover_menu_elim_ref" que está encargada de la animación del menú (aparición)
        self.ui.btn_menu_elim_ref.clicked.connect(self.mover_menu_elim_ref) 
        #Al dar click en el botón "btn_menu_elim_ref", se activa la función "actualizar_datos_elim_codigo_sus" que está encargada de actualizar los datos del .csv
        self.ui.btn_menu_elim_ref.clicked.connect(self.actualizar_datos_elim_codigo_sus)
        #Al dar click en el botón "btn_eliminar", se activa la función "eliminar_codigos_sus" que está encargada de eliminar el código de suscriptor seleccionado en el combobox
        self.ui.btn_eliminar.clicked.connect(self.eliminar_codigos_sus)
        #Al dar click en el botón "anadir", se activa la función "actualizar_datos_elim_codigo_sus" que está encargada de actualziar los datos del .csv
        self.ui.anadir.clicked.connect(self.actualizar_datos_elim_codigo_sus)


        #VISUALIZACION
        self.ui.btn_p7.clicked.connect(self.procesar_imagen)

        #GESTIONAR CARPETAS
        self.gestionar_carpetas()

    # *************************************************************************************
    # *                                                                                   *
    # *                            FUNCIONES                                              *
    # *                                                                                   *
    # *************************************************************************************

    #La función "gestionar_carpetas" está encargada de realizar la inferencia, así como el manejo de las carpetas
    #encargada de la eliminación de las imagenes de inferencias y de enviar la última inferencia a la carpeta visualizacion
    def gestionar_carpetas(self):
        # Ruta de las carpetas
        carpeta_inferencias = "inferencias"
        carpeta_visualizacion = "visualizacion"
        archivo_csv = "water_consumption_f.csv"

        # Enlistar los archivos en la carpeta "inferencias"
        archivos_inferencias = sorted(os.listdir(carpeta_inferencias), key=lambda x: datetime.strptime(x[:-4], "%d_%m_%Y_%H"))



        if archivos_inferencias:
            if not hasattr(self, "primera_ejecucion"):
                # Borrar el contenido de la carpeta "visualizacion"
                if os.path.exists(carpeta_visualizacion):
                    shutil.rmtree(carpeta_visualizacion)
                os.makedirs(carpeta_visualizacion)

                # Procesar la primera imagen del arreglo
                imagen_en_proceso = archivos_inferencias[0]
                imagen_para_visualizacion = archivos_inferencias[-1]#Esta es la iamgen que usaremos para visualizacion (la última del arreglo)

                # Simular la medición obteniendo un número aleatorio
                #print("Esta es la imagen en proceso ",imagen_en_proceso)#Si se quiere ver la imagen en proceso
                medicion = inferencia(os.path.join('inferencias', imagen_en_proceso))#Se hace la inferencia
                medicion2 = inferencia(os.path.join('inferencias', imagen_para_visualizacion))#Se hace la inferencia de la imagen que irá a visualizacion
                
                
                ###############################
                #self.ui.QLinferencia.setText(str(medicion2))#Actualizamos el QLabel que mostrará la última inferencia
                #self.ui.QLinferencia.setAlignment(QtCore.Qt.AlignCenter)#Se centra el label

                # Extraer información de la imagen (fecha y hora)
                nombre_archivo_split = os.path.splitext(imagen_en_proceso)[0].split("_")
                dia = nombre_archivo_split[0].zfill(2)
                mes = nombre_archivo_split[1].zfill(2)
                anio = nombre_archivo_split[2]
                hora = nombre_archivo_split[3]

                # Crear un objeto datetime con la fecha y hora extraídas del nombre del archivo
                fecha_hora = datetime(int(anio), int(mes), int(dia), int(hora))

                # Formatear la fecha y hora en el formato deseado
                fecha_formateada = fecha_hora.strftime("%d/%m/%Y")
                hora_formateada = fecha_hora.strftime("%H:%M")

                # Leer el archivo CSV existente
                datos_csv = []
                if os.path.exists(archivo_csv):
                    with open(archivo_csv, mode='r', newline='') as file:
                        reader = csv.reader(file)
                        datos_csv = list(reader)

                # Verificar si hay información con la misma fecha en el archivo CSV
                fecha_existente = False
                for i, fila in enumerate(datos_csv):
                    if len(fila) > 0 and fila[0] == fecha_formateada and fila[2] == hora_formateada:#Si encuentra datos con la misma fecha y hora, se sobreescriben
                        datos_csv[i] = [fecha_formateada, medicion, hora_formateada]
                        fecha_existente = True
                        break

                # Si no hay información con la misma fecha, agregar una nueva fila al archivo CSV
                if not fecha_existente:
                    datos_csv.append([fecha_formateada, medicion, hora_formateada])

                # Guardar los datos actualizados en el archivo CSV
                with open(archivo_csv, mode='w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(datos_csv)

                # Mover el archivo procesado a la carpeta "visualizacion"
                ruta_origen = os.path.join(carpeta_inferencias, imagen_para_visualizacion)
                ruta_destino = os.path.join(carpeta_visualizacion, imagen_para_visualizacion)
                ruta_nueva = "visualizacion/" + medicion2
                shutil.copy(ruta_origen, ruta_destino)#shutil.copy para no eliminar la última imagen o no se verá en el excel, ya que no se guardará su info
                shutil.copy(ruta_origen, ruta_nueva)#genero una imagen nueva para conservar la inferencia
                # Registrar que ya se realizó la primera ejecución
                self.primera_ejecucion = True
            else:
                # Procesar cada archivo del arreglo
                for imagen_en_proceso in archivos_inferencias:
                    # Simular la medición obteniendo un número aleatorio
                    #print("Esta es la imagen en proceso ",imagen_en_proceso)#Si se quiere ver la imagen en proceso
                    medicion = inferencia(os.path.join('inferencias', imagen_en_proceso))#Se hace la inferencia

                    # Extraer información de la imagen (fecha y hora)
                    nombre_archivo_split = os.path.splitext(imagen_en_proceso)[0].split("_")
                    dia = nombre_archivo_split[0].zfill(2)
                    mes = nombre_archivo_split[1].zfill(2)
                    anio = nombre_archivo_split[2]
                    hora = nombre_archivo_split[3]

                    # Crear un objeto datetime con la fecha y hora extraídas del nombre del archivo
                    fecha_hora = datetime(int(anio), int(mes), int(dia), int(hora))

                    # Formatear la fecha y hora en el formato deseado
                    fecha_formateada = fecha_hora.strftime("%d/%m/%Y")
                    hora_formateada = fecha_hora.strftime("%H:%M")

                    # Leer el archivo CSV existente
                    datos_csv = []
                    if os.path.exists(archivo_csv):
                        with open(archivo_csv, mode='r', newline='') as file:
                            reader = csv.reader(file)
                            datos_csv = list(reader)

                    # Verificar si hay información con la misma fecha en el archivo CSV
                    fecha_existente = False
                    for i, fila in enumerate(datos_csv):
                        if len(fila) > 0 and fila[0] == fecha_formateada and fila[2] == hora_formateada:
                            datos_csv[i] = [fecha_formateada, medicion, hora_formateada]
                            fecha_existente = True
                            break

                    # Si no hay información con la misma fecha, agregar una nueva fila al archivo CSV
                    if not fecha_existente:
                        datos_csv.append([fecha_formateada, medicion, hora_formateada])

                    # Guardar los datos actualizados en el archivo CSV
                    with open(archivo_csv, mode='w', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerows(datos_csv)

                    # Eliminar el archivo procesado de la carpeta "inferencias"
                    ruta_archivo = os.path.join(carpeta_inferencias, imagen_en_proceso)
                    os.remove(ruta_archivo)

            # Repetir el procedimiento hasta que no haya más imágenes
            if len(os.listdir(carpeta_inferencias)) > 0 and not self.detener_proceso:
                self.gestionar_carpetas()
        else:
            #print("No hay más imágenes en la carpeta 'inferencias'.")#Ayuda para visualizacion de que no hay imágenes en la carpeta "inferencias"
            self.detener_proceso = True


    #La funcion "detener_programa" está encargada de detener el proceso de eliminación de imágenes de la carpeta "inferencias"
    def detener_programa(signal, frame):
        self.detener_proceso = True #BANDERA PARA DETENER PROCESO SE PONE EN "TRUE"
        sys.exit(0)


    #La función "procesar_imagen", está encargada de mostrar la única imágen que contendrá la carpeta "visualización"
    #a su vez está también encargada de mostrarla en la pestaña "Visualización" de la interfaz de "WATER_METER"
    def procesar_imagen(self):
        carpeta_visualizacion = "visualizacion"  # Ruta de la carpeta "visualizacion"

        # Obtener la lista de archivos en la carpeta "visualizacion"
        archivos = os.listdir(carpeta_visualizacion)

        if archivos:
            # Obtener el primer archivo de la lista
            nombre_archivo = archivos[-1]
            inferencia_archivo = archivos[0]
            # Crear la ruta completa del archivo
            ruta_archivo = os.path.join(carpeta_visualizacion, nombre_archivo)

            # Cargar la imagen utilizando cv2
            imagen = cv2.imread(ruta_archivo)
            # Redimensionar la imagen a 800x600
            imagen_redimensionada = cv2.resize(imagen, (500, 500))
            # Mostrar la imagen en un QLabel (suponiendo que tienes un QLabel llamado "FeedLabel")
            imagen_rgb = cv2.cvtColor(imagen_redimensionada, cv2.COLOR_BGR2RGB)
            height, width, channel = imagen_rgb.shape
            bytes_per_line = channel * width
            q_image = QImage(imagen_rgb.data, width, height, bytes_per_line, QImage.Format_RGB888)
            self.ui.FeedLabel.setPixmap(QPixmap.fromImage(q_image))#La imagen que va al FeedLabel

            # Transformar el nombre del archivo a un formato deseado
            nombre_archivo_split = os.path.splitext(nombre_archivo)[0].split("_")
            dia = nombre_archivo_split[0].zfill(2)
            mes = nombre_archivo_split[1].zfill(2)
            anio = nombre_archivo_split[2]
            hora = nombre_archivo_split[3]

            # Crear un objeto datetime con la fecha y hora extraídas del nombre del archivo
            fecha_hora = datetime(int(anio), int(mes), int(dia), int(hora))

            # Formatear la fecha y hora en el formato deseado
            fecha_hora_formateada = fecha_hora.strftime("%d/%m/%Y - %H:%M")
            # Centramos el label
            self.ui.label_10.setAlignment(QtCore.Qt.AlignCenter)
            # Mostrar la fecha y hora formateada en un QLabel (suponiendo que tienes un QLabel llamado "label_10")
            self.ui.label_10.setText(fecha_hora_formateada)
            # Mostrar los datos de la última inferencia en un QLabel
            self.ui.QLinferencia.setText(str(inferencia_archivo))#Actualizamos el QLabel que mostrará la última inferencia
            self.ui.QLinferencia.setAlignment(QtCore.Qt.AlignCenter)#Se centra el label
        else:
            # No hay archivos en la carpeta "Visualización"
            self.ui.FeedLabel.clear()
            self.ui.label_10.setText("No hay imágenes disponibles")



    #La función "guardad()"" se encarga de guardar un nuevo registro en el archivo CSV
    #'registros.csv' con la información ingresada en la interfaz de usuario.  
    #También actualiza la tabla tablaregistros con los datos actualizados del archivo CSV.

    def guardad(self):
        # Lee el archivo CSV existente
        df = pd.read_csv('registros.csv')

        # LIMITAR CODIGO SUSCRIPTOR
        # Establece la longitud máxima a 6 caracteres
        self.ui.codigo_suscriptor.setMaxLength(6)
        # Establece un validador para aceptar solo números enteros en el campo código suscriptor
        self.ui.codigo_suscriptor.setValidator(QIntValidator())

        # Obtiene los valores ingresados en la interfaz de usuario
        c_s = self.ui.codigo_suscriptor.text()
        use = self.ui.cb_uso.currentText()
        cgory = self.ui.cb_categoria.currentText()
        municip = self.ui.cb_municipio.currentText()

        # Crea un nuevo registro con los valores ingresados
        registro = [(c_s, use, cgory, municip)]
        df1 = pd.DataFrame(registro, columns=['CODIGO SUSCRIPTOR', 'USO', 'CATEGORIA', 'MUNICIPIO'])

        # Agrega el nuevo registro al DataFrame existente
        df = df.append(df1, ignore_index=True)

        # Elimina las columnas no deseadas que tienen 'Unnamed' en el nombre
        eliminar_colum = [col for col in df.columns if 'Unnamed' in col]
        df.drop(eliminar_colum, axis='columns', inplace=True)

        # Guarda los datos actualizados en el archivo CSV
        df.to_csv('registros.csv')

        # Configura la tabla tablaregistros con los nuevos datos
        self.ui.tablaregistros.setColumnCount(len(df.columns))
        self.ui.tablaregistros.setRowCount(len(df))
        self.ui.tablaregistros.setHorizontalHeaderLabels(df.columns)

        # Establecer el tamaño de todas las columnas
        column_width = 150  # Ancho deseado para todas las columnas (ajusta el valor según tus necesidades)
        for column in range(self.ui.tablaregistros.columnCount()):
            self.ui.tablaregistros.setColumnWidth(column, column_width)

        # Agrega los datos a la tabla
        font = QtGui.QFont()
        font.setBold(True)  # Establece la fuente en negrita
        
        #Estética de la tabla #############################################
        for i in range(len(df)):
            for j in range(len(df.columns)):
                item = QtWidgets.QTableWidgetItem(str(df.iat[i, j]))
                item.setFont(font)  # Aplica la fuente en negrita
                item.setTextAlignment(QtCore.Qt.AlignCenter)  # Centra el contenido de la celda
                self.ui.tablaregistros.setItem(i, j, item)

        
        # Eliminar el borde del QTableWidget
        self.ui.tablaregistros.setStyleSheet("QTableView { border: none; }")
        # Colorea las filas con contenido
        for i in range(len(df)):
            for j in range(len(df.columns)):
                if df.iat[i, j] != "":
                    self.ui.tablaregistros.item(i, j).setBackground(QtGui.QColor(224, 224, 224))  # Color de fondo amarillo para las celdas con contenido

        # Colorea las columnas con contenido
        for j in range(len(df.columns)):
            column_has_content = False
            for i in range(len(df)):
                if df.iat[i, j] != "":
                    column_has_content = True
                    break
            if column_has_content:
                for i in range(len(df)):
                    self.ui.tablaregistros.item(i, j).setBackground(QtGui.QColor(224, 224, 224))  # Color de fondo verde para las celdas con contenido
        #FIN - Estética de la tabla #############################################


    #La función "mostrar_datos_actuales()" está encargada de actualizar los datos en pantalla 
    #con respecto a los actuales en el .csv sin que se añada o elimine información
    def mostrar_datos_actuales(self):
        # Cargar el archivo CSV y crear el DataFrame
        df = pd.read_csv('registros.csv')

        # LIMITAR CODIGO SUSCRIPTOR
        # Establece la longitud máxima a 6 caracteres
        self.ui.codigo_suscriptor.setMaxLength(6)
        # Establece un validador para aceptar solo números enteros en el campo código suscriptor
        self.ui.codigo_suscriptor.setValidator(QtGui.QIntValidator())

        # Eliminar la columna "Unnamed: 0" si existe
        df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

        # Configurar la tabla tablaregistros con las columnas y filas necesarias
        self.ui.tablaregistros.setColumnCount(len(df.columns))
        self.ui.tablaregistros.setRowCount(len(df))
        self.ui.tablaregistros.setHorizontalHeaderLabels(df.columns)

        

        # Agregar los datos al QTableWidget
        font = QtGui.QFont()
        font.setBold(True)  # Establece la fuente en negrita
        for i in range(len(df)):
            for j in range(len(df.columns)):
                item = QtWidgets.QTableWidgetItem(str(df.iat[i, j]))
                item.setFont(font)  # Aplica la fuente en negrita
                item.setTextAlignment(QtCore.Qt.AlignCenter)  # Centra el contenido de la celda
                self.ui.tablaregistros.setItem(i, j, item)

                # Colorea las celdas con contenido
                if df.iat[i, j] != "":
                    item.setBackground(QtGui.QColor(224, 224, 224))  # Color de fondo amarillo para las celdas con contenido

        # Establecer el tamaño de todas las columnas
        column_width = 150  # Ancho deseado para todas las columnas (ajusta el valor según tus necesidades)
        for column in range(self.ui.tablaregistros.columnCount()):
            self.ui.tablaregistros.setColumnWidth(column, column_width)
        # Eliminar el borde del QTableWidget
        self.ui.tablaregistros.setStyleSheet("QTableView { border: none; }")
    
    #En resumen, la función "actualizar_datos_elim_codigo_sus()" carga los datos del archivo CSV 'registros.csv' en un DataFrame. 
    #Luego, obtiene los códigos únicos de la columna "CODIGO SUSCRIPTOR" y los agrega al combobox cb_el_code_sus de la interfaz de usuario. 
    #Antes de agregar los códigos al combobox, se asegura de convertirlos en cadenas de texto utilizando una comprensión de lista. 
    #Además, se limpia el combobox antes de agregar los nuevos elementos. 
    #Esto garantiza que el combobox se actualice con los códigos más recientes cada vez que se llama a esta función.

    def actualizar_datos_elim_codigo_sus(self):
        # Cargar el archivo CSV y crear el DataFrame
        df = pd.read_csv('registros.csv')
    
        # Obtener los códigos únicos de la columna "CODIGO SUSCRIPTOR"
        codigos = df['CODIGO SUSCRIPTOR'].unique()

        # Limpiar el combobox cb_el_code_sus
        self.ui.cb_el_code_sus.clear()

        # Agregar los códigos al combobox cb_el_code_sus como elementos de texto
        self.ui.cb_el_code_sus.addItems([str(codigo) for codigo in codigos])




    # En resumen, la función "eliminar_codigos_sus()" elimina un código de suscriptor seleccionado del archivo CSV 'registros.csv'.
    # Primero, carga los datos del archivo CSV en un DataFrame.
    # Luego, obtiene el código seleccionado del combobox cb_el_code_sus de la interfaz de usuario.
    # Si se ha seleccionado un código, elimina las filas del DataFrame que coinciden con ese código.
    # Después, guarda el DataFrame actualizado en el archivo CSV 'registros.csv'.
    # A continuación, actualiza el combobox cb_el_code_sus con los códigos actualizados del DataFrame.
    # Finalmente, llama a la función mostrar_datos_actuales para actualizar la visualización de los datos en la interfaz de usuario.

    def eliminar_codigos_sus(self):
        # Cargar el archivo CSV y crear el DataFrame
        df = pd.read_csv('registros.csv')

        # Obtener el código seleccionado del combobox cb_el_code_sus
        codigo_seleccionado = self.ui.cb_el_code_sus.currentText()

        # Verificar si se ha seleccionado un código
        if codigo_seleccionado:
            # Eliminar las filas correspondientes al código seleccionado del DataFrame
            df = df[df['CODIGO SUSCRIPTOR'] != int(codigo_seleccionado)]

            # Guardar el DataFrame actualizado en el archivo CSV
            df.to_csv('registros.csv', index=False)

            # Obtener los códigos actualizados del DataFrame
            codigos_actualizados = df['CODIGO SUSCRIPTOR'].unique()

            # Limpiar el combobox cb_el_code_sus
            self.ui.cb_el_code_sus.clear()

            # Agregar los códigos actualizados al combobox cb_el_code_sus como elementos de texto
            self.ui.cb_el_code_sus.addItems([str(codigo) for codigo in codigos_actualizados])

            # Actualizar la visualización de los datos en la interfaz de usuario llamando a la función mostrar_datos_actuales
            self.mostrar_datos_actuales()


    ## FUNCIÓN PARA MOVER EL MENÚ DER - MEDIANTE ESTA SE DEFINE EL TAMAÑO Y TIEMPO DE ANIMACIÓN
    def mover_menu_elim_ref(self):
        if True:
            #Capturamos la dimensión del frame (En QTDesigner se define como 0)
            width = self.ui.frame_elim_ref.width()
            #----------------------------------------------------------------#
            normal = 0
            if width==0:
                #Dimensión final del frame o menú
                extender = 230
                #-------------------------------#
            else:
                extender = normal
            
            self.animacion = QPropertyAnimation(self.ui.frame_elim_ref, b'minimumWidth')
            #Tiempo de la animación-------#
            self.animacion.setDuration(300)
            #-----------------------------#
            self.animacion.setStartValue(width)
            self.animacion.setEndValue(extender)
            self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            #Se ejecuta la animación
            self.animacion.start()

        


    #La función "actualizarConsumoTotal()" está encargada de general el consumo del mes que se le indique, que en este caso se pondrá
    #en la parte superior de la aplicación 
    def actualizarConsumoTotal(self, mes):
        # Filtrar los datos del DataFrame para el mes seleccionado
        datos_mes_seleccionado = self.dataframe[
            self.dataframe['Fecha'].dt.month == mes
        ]

        
        # Verificar si hay datos para el mes seleccionado
        if not datos_mes_seleccionado.empty:
            # Obtener el último valor del mes seleccionado
            consumo_total_mes = datos_mes_seleccionado['Medición'].iloc[-1]
            consumo_total_mes = (consumo_total_mes/1000) #Se pasa a metros cúbicos para realizar el cálculo del precio
            # Actualizar el QLabel con el consumo total del mes #109800
            self.ui.consumo_m_numero.setText("{:.2f} m³".format(consumo_total_mes))
            #PROCESO DE CALCULO DEL ACUEDUCTO
            if mes == 3: #marzo
                referencia_consumo = 2858
                referencia_cargo_fijo = 9586
            if mes == 4: #abril
                referencia_consumo = 2957
                referencia_cargo_fijo = 9919
            else:
                referencia_consumo = 2957
                referencia_cargo_fijo = 9919

            #PROCESO DE CÁLCULO DEL COSTO DEL CONSUMO DE AGUA EN M^3
            consumo_metros_cubicos = (int(consumo_total_mes)*referencia_consumo)
            consumo_basico = referencia_consumo*16 #16 representan los 16 primeros metros cúbicos
            descuento = 0.1
            subsidio_cargo_fijo = referencia_cargo_fijo*descuento
            subsidio_cargo_basico = consumo_basico*descuento
            total_acueducto = (referencia_cargo_fijo + consumo_metros_cubicos - subsidio_cargo_fijo - subsidio_cargo_basico)

            
        else:
            # No hay datos para el mes seleccionado
            self.ui.consumo_m_numero.setText("No hay datos para el mes seleccionado")
            self.ui.precio_consumo_total.setText("No hay un precio para el mes seleccionado")

        # Actualizar el estado del consumo
        self.actualizarEstadoConsumo(consumo_total_mes, mes, total_acueducto)
        
    
    #La función "actualizarEstadoConsumo()" está encargada de generar la alerta del consumo del mes, los posibles estados son ANORMAL y Normal

    def actualizarEstadoConsumo(self, consumo_total_mes, mes, total_acueducto):
        
        #Mediante condicional if se realiza la definición de los rangos ANORMAL y Normal
        if 22 < consumo_total_mes < 38: #RANGO PARA ESTABLECER UN CONSUMO "NORMAL"
            estado_consumo = "Normal"
            self.ui.alerta_consumo.setStyleSheet(
            "background-color: #90CAF9;"
            "border: 5px solid black;"
            "border-color: black;"
            "color: #000000;"
            "font: 2200 15pt 'Ubuntu Mono';"
            )
            # Establecer el texto en la etiqueta
            self.ui.alerta_consumo.setText(estado_consumo)
        elif consumo_total_mes: #RANGO PARA ESTABLECER UN CONSUMO "ANORMAL"
            estado_consumo = "ANORMAL"
            self.ui.alerta_consumo.setStyleSheet(
            "background-color: #90CAF9;"
            "border: 5px solid black;"
            "border-color: black;"
            "color: #000000;"
            "font: 2200 15pt 'Ubuntu Mono';"
            )
            self.ui.alerta_consumo.setText(estado_consumo)
        else:
            estado_consumo = "Error en el dato"
        
        #Se definen en español los nombres del mes, que luego servirán para indicar el mes que se está mostrando.Todo esto según el número del mes
        if mes == 1:
            nombre_mes = "Enero"
        elif mes == 2:
            nombre_mes = "Febrero"
        elif mes == 3:
            nombre_mes = "Marzo"
        elif mes == 4:
            nombre_mes = "Abril"
        elif mes == 5:
            nombre_mes = "Mayo"
        elif mes == 6:
            nombre_mes = "Junio"
        elif mes == 7:
            nombre_mes = "Julio"
        elif mes == 8:
            nombre_mes = "Agosto"
        elif mes == 9:
            nombre_mes = "Septiembre"
        elif mes == 10:
            nombre_mes = "Octubre"
        elif mes == 11:
            nombre_mes = "Noviembre"
        elif mes == 12:
            nombre_mes = "Diciembre"
        else:
            nombre_mes = "Mes Inválido"

        # Actualizar el QLabel con el estado del consumo
        self.ui.consumo_total_m.setAlignment(QtCore.Qt.AlignCenter)
        self.ui.consumo_total_m.setText(f"Consumo del mes {nombre_mes}")
        #Estética del label precio_consumo_total
        self.ui.precio_consumo_total.setStyleSheet(
            "background-color: #90CAF9;"
            "border: 5px solid black;"
            "border-color: black;"
            "color: #000000;"
            "font: 2200 15pt 'Ubuntu Mono';"
            )
        self.ui.precio_consumo_total.setAlignment(Qt.AlignCenter)
        self.ui.precio_consumo_total.setText("${:.2f}".format(total_acueducto))#Se actualiza el texto del label con el precio   

    
    #La función "obtener_rango_semana" permite obtener las semanas del mes
    def obtener_rango_semana(self, calendario, fecha):
        # Convertir la fecha en un objeto datetime
        fecha_objeto = parse(fecha)
        
        # Calcular el día de la semana (0 es lunes, 6 es domingo)
        dia_semana = fecha_objeto.weekday()

        # Obtener la fecha del lunes de la semana
        inicio_semana = fecha_objeto - timedelta(days=dia_semana)

        # Obtener la fecha del domingo de la semana
        fin_semana = inicio_semana + timedelta(days=6)

        # Crear una lista con el rango de fechas de la semana
        rango_semana = []
        dia_actual = inicio_semana
        while dia_actual <= fin_semana:
            rango_semana.append(dia_actual)
            dia_actual += timedelta(days=1)

        # Devolver el rango de fechas en el formato deseado
        print([fecha.strftime("%d/%m/%Y") for fecha in rango_semana])
        return [fecha.strftime("%d/%m/%Y") for fecha in rango_semana]

    #La función "colorear_fechas" permite resaltar las semanas que se estarán graficando al dar click en alguno de los días de la semana
    def colorear_fechas(self, rango_fechas):
        # Limpiar formato de fechas anteriores
        self.calendario2.setDateTextFormat(QDate(), QTextCharFormat())

        # Aplicar formato a las nuevas fechas
        formato_fondo = QTextCharFormat()
        formato_fondo.setBackground(QColor(0, 0, 255))  # Azul

        # Iterar sobre el rango de fechas
        for fecha in rango_fechas:
            # Convertir la fecha a formato adecuado
            fecha_convertida = pd.to_datetime(fecha, format='%d/%m/%Y').date()
        
            # Crear un objeto QDate con la fecha convertida
            qdate = QDate(fecha_convertida.year, fecha_convertida.month, fecha_convertida.day)
        
            # Aplicar el formato de fondo al objeto QDate en el calendario
            self.calendario2.setDateTextFormat(qdate, formato_fondo)

   
    #La función "Funciongraficadiaria()" está encargada de graficar los datos diarios
    def Funciongraficadiaria(self):
        fecha_seleccionada_dia = self.calendario.selectedDate().toString("M/d/yyyy")
        #print("Entró en funcion grafica DIARIA")#Indicativo para identificar cuando entra en la función gráfica diaria

        # Leer el archivo CSV nuevamente para obtener los datos más recientes
        self.dataframe = pd.read_csv('water_consumption_f.csv')
        self.dataframe['Fecha'] = pd.to_datetime(self.dataframe['Fecha'], format='%d/%m/%Y')

        # Filtrar los datos del día seleccionado en el calendario
        datos_filtrados = self.dataframe[self.dataframe['Fecha'] == fecha_seleccionada_dia]

        # Imprimir los datos filtrados en la consola
        #print(datos_filtrados)#Descomentar para observar los datos filtrados en consola

        # Limpiar el canvas de la gráfica diaria
        self.figure.clear()
        ax = self.figure.add_subplot(111)  # Crear un nuevo subplot en la figura

        # Obtener los datos de las columnas 'Hora' y 'Medición'
        horas = datos_filtrados['Hora'].astype(str)  # Convertir a cadena
        lts = datos_filtrados['Medición'].astype(float)  # Convertir a flotante

        # Graficar puntos en la gráfica diaria
        ax.plot(horas, lts, color='red')
        ax.set_xlabel("Horas", fontsize=12)
        ax.set_ylabel("Consumo (L)", fontsize=14)

        # Añadir esta línea para ajustar automáticamente el tamaño de la gráfica al canvas
        self.figure.tight_layout()
        # Refrescar el lienzo de la gráfica diaria
        self.canvas.draw()

        #De modo que no se tengan datos vacíos y nos dé error con ellos
        primer_valor = datos_filtrados['Medición'].iloc[0] if not datos_filtrados.empty else None
        ultimo_valor = datos_filtrados['Medición'].iloc[-1] if not datos_filtrados.empty else None

        
        #Cálculo del valor "consumo diario" en la interfaz
        if ultimo_valor is not None:
            #Se pasan los valores a metros cúbicos
            primer_valor = primer_valor / 1000
            ultimo_valor_metros_cubicos = ultimo_valor / 1000
            #Se actualiza el label, donde será la resta de los valores
            self.ui.label_12.setText("{:.2f} m³".format(ultimo_valor_metros_cubicos - primer_valor))
        else:
            self.ui.label_12.setText("N/A")  # Valor predeterminado si no hay datos disponibles


    #La función "Funciongraficasemanal()" está encargada de graficar los datos semanales
    def Funciongraficasemanal(self):
        fecha_seleccionada_semana = self.calendario2.selectedDate().toString("M/d/yyyy")
        
        #print("Entró en funcion grafica SEMANAL")#Indicativo para saber si se entró en la función gráfica semanal

        # Leer el archivo CSV nuevamente para obtener los datos más recientes
        self.dataframe = pd.read_csv('water_consumption_f.csv')
        self.dataframe['Fecha'] = pd.to_datetime(self.dataframe['Fecha'], format='%d/%m/%Y')


        # Limpiamos el canvas de la gráfica semanal
        self.figure2.clear()

        # Obtener el rango de fechas de la semana
        rango_fechas = self.obtener_rango_semana(self.calendario2, self.calendario2.selectedDate().toString("M/d/yyyy"))
        self.colorear_fechas(rango_fechas)
        #print("Rango de fechas:", rango_fechas)  #Descomentar para imprimir el rango de fechas

        # Ejes
        horas = []
        lts = []

        for fecha in rango_fechas:
            fecha_buscar = pd.to_datetime(fecha, format='%d/%m/%Y').date()
            datos_filtrados = self.dataframe[self.dataframe['Fecha'].dt.date == fecha_buscar]
            if not datos_filtrados.empty:
                
                ultima_medicion = datos_filtrados['Medición'].iloc[-1]  # Obtener la última medición
                
                horas.append(fecha)
                lts.append(ultima_medicion)
            else:
                #print("No hay datos para la fecha:", fecha)  # Descomentar para :Verificación de fechas sin datos
                horas.append(fecha)
                lts.append(None)  # Agregar un valor nulo para fechas sin datos

        # Graficar puntos en la gráfica semanal
        ax2 = self.figure2.add_subplot(111)  # Crear un nuevo subplot en la figura de la gráfica semanal
        ax2.plot(horas, lts, color='red')  # Graficar los puntos en el subplot
        ax2.set_xlabel("Días", fontsize=12)
        ax2.set_ylabel("Consumo (L)", fontsize=14)

        # Añadir esta línea para ajustar automáticamente el tamaño de la gráfica al canvas
        self.figure2.tight_layout()
    
        # Obtener el último dato o última medición de la semana
        ultimo_dato_semana = lts[-1] if lts else None
        # Obtener el primer dato o primera medición de la semana
        primer_dato_semana = lts[0] if lts else None
        # Verificar si hay un último valor disponible
        if ultimo_dato_semana is not None:
            if primer_dato_semana is not None:
                # Realizar la conversión de litros a metros cúbicos dividiendo por 1000
                ultimo_valor_metros_cubicos = (ultimo_dato_semana / 1000)
                primer_valor_metros_cubicos = (primer_dato_semana / 1000)
                # Establecer el texto en la etiqueta "label_24" con el valor convertido y formateado
                
                if (ultimo_valor_metros_cubicos - primer_valor_metros_cubicos) < 0:
                    #Si la semana incluye datos de otro mes:
                    self.ui.label_24.setText("{:.2f} m³".format(ultimo_valor_metros_cubicos))
                else: 
                    #Si no contiene datos de otro mes, entonces hace la resta del último valor y el primero
                    self.ui.label_24.setText("{:.2f} m³".format(ultimo_valor_metros_cubicos - primer_valor_metros_cubicos))

        else:
            # Si no hay datos disponibles, establecer el texto en la etiqueta "label_24" como "N/A"
            self.ui.label_24.setText("N/A")  # Valor predeterminado si no hay datos disponibles

        self.canvas2.draw()

    #La función "Funciongraficamensual()" está encargada de graficar los datos mensuales
    def Funciongraficamensual(self):
        mes_seleccionado = self.calendario3.monthShown()
        año_seleccionado = self.calendario3.yearShown()

        fecha_seleccionada = f"{mes_seleccionado}/14/{año_seleccionado}"
        
        #self.canvas3.setFixedSize(1100, 335)  # Ajusta el tamaño según tus necesidades
        #print("SELECCIONO:", fecha_seleccionada)#Descomentar para observar en consola la fecha seleccionada
        #print("Entró en función de gráfica mensual")#Indicativo para observar si se entró en la función gráfica mensual

        # Leer el archivo CSV nuevamente para obtener los datos más recientes
        self.dataframe = pd.read_csv('water_consumption_f.csv')
        self.dataframe['Fecha'] = pd.to_datetime(self.dataframe['Fecha'], format='%d/%m/%Y')
        
        
        # Limpiar el lienzo de la gráfica mensual
        self.figure3.clear()
        
        mes = mes_seleccionado #Esto si funciona al cambiar los meses y año nada más sin seleccionar el día
        año = año_seleccionado

        # Filtrar los datos del DataFrame para el mes y año seleccionados
        datos_filtrados = self.dataframe[
            (self.dataframe['Fecha'].dt.month == mes) &
            (self.dataframe['Fecha'].dt.year == año)
        ]

        # Agrupar los datos por semana
        datos_semanales = datos_filtrados.groupby(datos_filtrados['Fecha'].dt.week)['Medición'].last()

        # Calcular el número de semanas completas e incompletas
        num_semanas_completas = datos_semanales.count()
        num_semanas_incompletas = len(pd.unique(datos_filtrados['Fecha'].dt.week)) - num_semanas_completas

        #print("Número de semanas completas:", num_semanas_completas)#Descomentar para ver el cálculo
        #print("Número de semanas incompletas:", num_semanas_incompletas)#Descomentar para ver el cálculo

        # Crear una lista de etiquetas para el eje x (semanas) sin los rangos de fechas
        etiquetas_semanas = [f"Semana {i}" for i in range(1, num_semanas_completas + 1)]

        if num_semanas_incompletas > 0:
            etiquetas_semanas.append(f"Semanas incompletas ({num_semanas_incompletas})")

        # Crear una lista de valores para el consumo mensual
        consumo_mensual = datos_semanales.tolist()
        if num_semanas_incompletas > 0:
            ultimo_valor = datos_filtrados['Medición'].tail(num_semanas_incompletas).values[-1]
            consumo_mensual.append(ultimo_valor)

        # Graficar el consumo mensual
        ax3 = self.figure3.add_subplot(111)
        ax3.bar(etiquetas_semanas, consumo_mensual)
        ax3.set_xlabel("Semanas", fontsize=12)
        ax3.set_ylabel("Consumo (L)", fontsize=14)
        
        ax3.tick_params(axis='x', rotation=0)

        #Para observar correctamente las barras
        if consumo_mensual:
            limite_superior_izq = max(consumo_mensual) + 5000  # Define el valor máximo en el lado izquierdo que deseas establecer
        else:
            limite_superior_izq = 5000  # Define un valor predeterminado si no hay datos disponibles

        # Ajustar los lí    mites del eje y
        ax3.set_ylim(0, limite_superior_izq)


        # Añadir esta línea para ajustar automáticamente el tamaño de la gráfica al canvas
        self.figure3.tight_layout()
        # Mostrar los valores específicos de las semanas en la gráfica
        for i, valor in enumerate(consumo_mensual):
            ax3.text(i, valor, str(int(valor)), ha='center', va='bottom')

        # Obtener el último valor o medición del mes seleccionado
        ultimo_valor_mes = consumo_mensual[-1] if consumo_mensual else None

        # Verificar si hay un último valor disponible
        if ultimo_valor_mes is not None:
            # Realizar la conversión de litros a metros cúbicos dividiendo por 1000
            ultimo_valor_metros_cubicos = ultimo_valor_mes / 1000
            # Establecer el texto en la etiqueta "label_32" con el valor convertido y formateado
            self.ui.label_32.setText("{:.2f} m³".format(ultimo_valor_metros_cubicos))
        else:
            # Si no hay datos disponibles, establecer el texto en la etiqueta "label_32" como "N/A"
            self.ui.label_32.setText("N/A")  # Valor predeterminado si no hay datos disponibles

        self.canvas3.draw()

    #La función "Funciongraficaanual()" está encargada de graficar los datos anuales #MODIFIQUE
    def Funciongraficaanual(self):
        mes_seleccionado = self.calendario4.monthShown()
        año_seleccionado = self.calendario4.yearShown()

        fecha_seleccionada = f"{mes_seleccionado}/14/{año_seleccionado}"

        #print("SELECCIONO:", fecha_seleccionada)#Descomentar para observar la fecha seleccionada

        self.dataframe = pd.read_csv('water_consumption_f.csv')
        self.dataframe['Fecha'] = pd.to_datetime(self.dataframe['Fecha'], format='%d/%m/%Y')

        mes = mes_seleccionado
        año = año_seleccionado

        fecha_seleccionada = self.calendario4.selectedDate().toString("M/d/yyyy")
        #print("Entró en función de gráfica anual")#Indicativo para observar si se entró en la función grafica anual

        self.figure4.clear()

        datos_filtrados = self.dataframe[self.dataframe['Fecha'].dt.year == año]

        datos_mensuales = datos_filtrados.groupby(datos_filtrados['Fecha'].dt.month)['Medición'].last()

        etiquetas_meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
        

        suma = 0 #Variable para realizar la suma de los meses

        consumo_anual = [0] * 12 #Se inicializan los valores en 0

        # Inicializar la variable suma
        
        for mes, consumo in datos_mensuales.items():
            consumo_anual[mes - 1] = consumo

        ax4 = self.figure4.add_subplot(111)
        ax4.bar(etiquetas_meses, consumo_anual)
        ax4.set_xlabel("Meses", fontsize=12)
        ax4.set_ylabel("Consumo (L)", fontsize=14)
        ax4.tick_params(axis='x', rotation=0)
        
        #Para observar correctamente las barras
        if consumo_anual:
            limite_superior_izq = max(consumo_anual) + 5000  # Define el valor máximo en el lado izquierdo que deseas establecer
        else:
            limite_superior_izq = 5000  # Define un valor predeterminado si no hay datos disponibles

        # Ajustar los lí    mites del eje y
        ax4.set_ylim(0, limite_superior_izq)

        # Añadir esta línea para ajustar automáticamente el tamaño de la gráfica al canvas
        self.figure4.tight_layout()

        for i, valor in enumerate(consumo_anual):
            if valor > 0:
                #Texto superior que muestra el consumo en lts
                ax4.text(i, valor + 10, str(int(valor)) + "", ha='center', va='bottom')
                #Precios para los meses conocidos, si no se tiene el precio se pone el más alto registrado en los recibos del AMB
                if mes == 3:  # marzo
                    referencia_consumo = 2858
                    referencia_cargo_fijo = 9586
                elif mes == 4:  # abril
                    referencia_consumo = 2957
                    referencia_cargo_fijo = 9919
                else:
                    referencia_consumo = 2957
                    referencia_cargo_fijo = 9919

                #Cálculo del precio del consumo
                consumo_metros_cubicos = int(valor / 1000) * referencia_consumo #Se pasa a metros cúbicos
                consumo_basico = referencia_consumo * 16  # 16 representan los 16 primeros metros cúbicos
                descuento = 0.1
                subsidio_cargo_fijo = referencia_cargo_fijo * descuento
                subsidio_cargo_basico = consumo_basico * descuento
                total_acueducto = (referencia_cargo_fijo + consumo_metros_cubicos - subsidio_cargo_fijo - subsidio_cargo_basico)
                
                #Texto vertical
                ax4.text(i, valor / 2, "${:.2f}".format(total_acueducto), ha='center', va='center', rotation=90)

        
        #Para sacar el consumo anual
        if suma is not None:
            for elemento in consumo_anual:
                suma = suma + elemento 
                #print(suma)#Descomentar para mostrar la suma progresiva  
            ultimo_valor_metros_cubicos = suma / 1000 
            self.ui.label_41.setText("{:.2f} m³".format(ultimo_valor_metros_cubicos))
        else:
            self.ui.label_41.setText("N/A")

        self.canvas4.draw()


    ## FUNCIÓN PARA MOSTRAR + Y x al pulsar "nueva referencia"
    #--Esta función alterna entre 0 y 1 al accionarla
    def alternarestado(self): 
        
        if self.estado==0:
            #Se esconde icono x y se muestra +
            self.ui.bt_x.hide()
            self.ui.bt_newref.show()
            #Cambiamos el estado
            self.estado = 1 
            
            
        else:
            #Se esconde icono + y se muestra x
            self.ui.bt_newref.hide()
            self.ui.bt_x.show()
            #Cambiamos el estado
            self.estado = 0
           
        
    
    
    ## FUNCIONES PARA INTERCAMBIAR LOS ICONOS MENU Y ATRÁS
    def intercambiodeiconos1(self):
        #Se esconde icono menú y se muestras atrás
        self.ui.bt_menu.hide()
        self.ui.bt_atras.show()
    def intercambiodeiconos2(self):
        #Se esconde icono atrás y se muestras menú
        self.ui.bt_atras.hide()
        self.ui.bt_menu.show()
       
    ## FUNCIONES PARA MOSTRAR/ESCONDER EL LOGO SUPERIOR 
    def mostrarlogosup(self):
        #Se muestra logo superior
        self.ui.bt_logosup.show()
    def esconderlogosup(self):
        #Se esconde logo superior
        self.ui.bt_logosup.hide()

    ## FUNCIÓN PARA MOVER EL MENÚ IZQ - MEDIANTE ESTA SE DEFINE EL TAMAÑO Y TIEMPO DE ANIMACIÓN
    def mover_menu_izq(self):
        if True:
            #Capturamos la dimensión del frame (En QTDesigner se define como 0)
            width = self.ui.frame_lateral.width()
            #----------------------------------------------------------------#
            normal = 0 
            if width==0:
                #Dimensión final del frame o menú
                extender = 230
                #self.ui.frame_lateral.setMinimumWidth(300)
                #-------------------------------#
            else:
                extender = normal
                #self.ui.frame_lateral.setMinimumWidth(0)
            
            self.animacion = QPropertyAnimation(self.ui.frame_lateral, b'minimumWidth')
            #Tiempo de la animación-------#
            self.animacion.setDuration(300)
            #-----------------------------#
            self.animacion.setStartValue(width)
            self.animacion.setEndValue(extender)
            self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            #Se ejecuta la animación
            self.animacion.start() 
    
    ## FUNCIÓN PARA MOVER EL MENÚ DER - MEDIANTE ESTA SE DEFINE EL TAMAÑO Y TIEMPO DE ANIMACIÓN
    def mover_menu_der(self):
        if True:
            #Capturamos la dimensión del frame (En QTDesigner se define como 0)
            width = self.ui.frame_newref.width()
            #----------------------------------------------------------------#
            normal = 0
            if width==0:
                #Dimensión final del frame o menú
                extender = 230
                #-------------------------------#
            else:
                extender = normal
            
            self.animacion = QPropertyAnimation(self.ui.frame_newref, b'minimumWidth')
            #Tiempo de la animación-------#
            self.animacion.setDuration(300)
            #-----------------------------#
            self.animacion.setStartValue(width)
            self.animacion.setEndValue(extender)
            self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            #Se ejecuta la animación
            self.animacion.start()

#Para ejecutar la aplicación si se insta main.py desde la consola o CMD
if __name__ == "__main__":
     app = QApplication(sys.argv)
     mi_app = MiApp()
     mi_app.show()
     sys.exit(app.exec_())  

