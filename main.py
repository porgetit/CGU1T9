from ImageProcessor import Imagen as img
from SimpleImageViewer import SimpleImageViewer as siv

if __name__ == '__main__':
    # Cargar la imagen fuente
    image = img.desde_archivo('img.jpg')
    
    # ================== EJERCICIO 1: Ajuste de brillo ==================
    image_brightness = image.copy().ajuste_brillo(0.4)
    
    # ================== EJERCICIO 2: Ajuste de brillo en un canal ==================
    # Se aumenta el brillo del canal rojo (índice 0)
    image_channel_brightness = image.copy().adjust_channel_brightness(0, 0.4)
    
    # ================== EJERCICIO 3: Ajuste de contraste ==================
    image_contrast = image.copy().ajustar_contraste(-0.5)
    
    # ================== EJERCICIO 4: Zoom ==================
    # Se realiza zoom en la región central de la imagen
    h, w, _ = image.datos.shape
    left = w // 4
    top = h // 4
    right = left + w // 2
    bottom = top + h // 2
    image_zoom = image.copy().zoom(left, top, right, bottom)
    
    # ================== EJERCICIO 5: Binarización ==================
    image_binary = image.copy().binarize(0.5)
    
    # ================== EJERCICIO 6: Rotación ==================
    image_rotated = image.copy().rotate(45)
    
    # Preparar una imagen para mostrar histogramas (EJERCICIO 7)
    image_histogram = image.copy()
    
    # Crear el visor con las imágenes transformadas
    viewer = siv({
        'Original': image,
        'Ejercicio 1 - Brightness Adjusted': image_brightness,
        'Ejercicio 2 - Channel Brightness (R)': image_channel_brightness,
        'Ejercicio 3 - Contrast Adjusted': image_contrast,
        'Ejercicio 4 - Zoom': image_zoom,
        'Ejercicio 5 - Binarized': image_binary,
        'Ejercicio 6 - Rotated': image_rotated,
    })
    viewer.show()
    
    # ================== EJERCICIO 7: Mostrar Histogramas ==================
    image_histogram.show_histogram()
