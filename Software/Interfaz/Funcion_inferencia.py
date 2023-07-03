from ultralytics import YOLO
import os
import cv2
import numpy as np
from PIL import Image
import math
from deskew import determine_skew
from typing import Tuple, Union

def prod_resize_input(img_link):
    '''
    Esta función toma una imagen y la redimensiona.
    '''
    img = cv2.imread(img_link)
    img = cv2.resize(img, (224, 224))
    return img.astype('uint8')

# Crear función para recortar imágenes.
def crop_for_seg(img, bg, mask):
    '''
    Esta función extrae una imagen donde se superpone con su máscara binaria.
    img - Imagen a recortar.
    bg - El fondo sobre el cual proyectar la imagen.
    mask - La máscara binaria generada por el modelo de segmentación.
    '''
    # mask = mask.astype('uint8')
    fg = cv2.bitwise_or(img, img, mask=mask)

    fg_back_inv = cv2.bitwise_or(bg, bg, mask=cv2.bitwise_not(mask))
    New_image = cv2.bitwise_or(fg, fg_back_inv)

    return New_image

def extract_meter(image_to_be_cropped):
    '''
    Esta función extrae aún más la imagen de manera que la lectura del medidor ocupe la mayoría de la imagen.
    La función encuentra los bordes de la ROI (Region of Interest) y extrae la parte de la imagen que contiene toda la ROI.
    '''
    where = np.array(np.where(image_to_be_cropped))
    x1, y1, z1 = np.amin(where, axis=1)
    x2, y2, z2 = np.amax(where, axis=1)
    sub_image = image_to_be_cropped.astype('uint8')[x1:x2, y1:y2]
    return sub_image

def rotate(image: np.ndarray, angle: float, background: Union[int, Tuple[int, int, int]]) -> np.ndarray:
    '''
    Esta función intenta rotar las imágenes de lectura del medidor para que queden horizontales.
    Sus argumentos son los siguientes:

    image - La imagen que se va a desesquilar (en formato de matriz numpy).
    angle - El ángulo actual de la imagen, encontrado con la función determine_skew de la biblioteca deskew.
    background - Los valores de píxeles del borde, ya sea int (por defecto 0) o una tupla.

    La función devuelve una matriz numpy.
    '''
    old_width, old_height = image.shape[:2]

    angle_radian = math.radians(angle)
    width = abs(np.sin(angle_radian) * old_height) + abs(np.cos(angle_radian) * old_width)
    height = abs(np.sin(angle_radian) * old_width) + abs(np.cos(angle_radian) * old_height)

    image_center = tuple(np.array(image.shape[1::-1]) / 2)
    rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
    rot_mat[1, 2] += (width - old_width) / 2
    rot_mat[0, 2] += (height - old_height) / 2
    return cv2.warpAffine(image, rot_mat, (int(round(height)), int(round(width))), borderValue=background)

def resize_aspect_fit(img, final_size: int):
    '''
    Esta función redimensiona la imagen al tamaño especificado.

    img - La imagen a redimensionar.
    final_size - El tamaño al que quieres que se redimensionen las imágenes finales. Debe ser un entero (se usará para w y h).
    '''
    im_pil = Image.fromarray(img)
    size = im_pil.size
    ratio = float(final_size) / max(size)
    new_image_size = tuple([int(x*ratio) for x in size])
    im_pil = im_pil.resize(new_image_size, Image.LANCZOS)
    new_im = Image.new("RGB", (final_size, final_size))
    new_im.paste(im_pil, ((final_size-new_image_size[0])//2, (final_size-new_image_size[1])//2))
    new_im = np.asarray(new_im)
    return np.array(new_im)

def segment_input_img(img):
    # Redimensionar imagen.
    img_small = prod_resize_input(img)

    # Abrir imagen y obtener dimensiones.
    input_img = cv2.imread(img, cv2.IMREAD_UNCHANGED)
    input_w = int(input_img.shape[1])
    input_h = int(input_img.shape[0])
    dim = (input_h, input_w)

    # Cargar modelo, preprocesar la entrada y obtener la predicción.
    modelo = YOLO("best2.pt")
    ro = rotate(img_small, 90, (0, 0, 0))

    # Inferencia del modelo segmentador
    results = modelo.predict(source=ro, conf=0.8)
    mask = (results[0].masks.masks[0].numpy() * 255).astype("uint8")

    # Redimensionar máscara al tamaño de la imagen de entrada.
    mask = cv2.resize(mask, dsize=dim, interpolation=cv2.INTER_AREA)


    # Crear una matriz de fondo
    rot = rotate(input_img, 90, (0, 0, 0))
    bg = np.zeros_like(rot, 'uint8')

    # Obtener nueva imagen recortada y convertirla a RGB.
    New_image = crop_for_seg(rot, bg, mask)
    New_image = cv2.cvtColor(New_image, cv2.COLOR_BGR2RGB)

    # Luego de cortar y girar la imagen se extrae solo la región de interez
    extracted = extract_meter(New_image)

    # por ultimo se gira el recorte y se redimensiona
    rotated = rotate(extracted, -90, (0, 0, 0))
    img = resize_aspect_fit(rotated, 640)

    return img





def inferencia(path):
    h = segment_input_img(path)

    model = YOLO("bestdetect.pt")
    cajas = model.predict(source=h, conf=0.4)

    for caja in cajas:
        caja = caja.boxes

        coordenadas_x = caja.xyxy[:, 0]

        # Ordenar las cajas según las coordenadas x
        indices_ordenados = np.argsort(coordenadas_x)

        # Obtener las clases correspondientes a las cajas ordenadas
        clases_ordenadas = caja.cls[indices_ordenados]

        # Crear una cadena de texto con las clases ordenadas
        clases_string = "".join([str(int(clase.numpy())) for clase in clases_ordenadas])

        mapping = {
            '0': '0',
            '2': '4',
            '6': '6',
            '8': '3',
            '9': '1',
            '1': '5',
            '3': '2',
            '4': '9',
            '5': '8',
            '7': '7',

        }

        # Cambio de la lectura preliminar deaciuerdo al formato de etiquetas con las que se entrenó el modelo
        def replace_digits(string, mapping):
            result = ''
            for char in string:
                if char in mapping:
                    result += mapping[char]
                else:
                    result += char
            return result

        transformed_string = replace_digits(clases_string, mapping)

        #Se asigna un valor decimal, en este caso en particular el ultimo número corresponde al decimal

        if len(clases_string) == 7:
            string = transformed_string + '.0'
        if len(clases_string) == 8:
            string = transformed_string[:7] + '.' + transformed_string[7:]
        if len(clases_string) > 8:
            string = transformed_string[:7] + '.' + transformed_string[8]


    #se retorna la lectura
    return string



