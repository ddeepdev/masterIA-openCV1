import cv2
import sys
import numpy as np


def aclarar_imagen(imagen, factor=50):
    """
    Aclara una imagen sumando un valor constante a todos los píxeles.

    Args:
        imagen: Imagen de entrada (puede ser color o escala de grises)
        factor: Valor a sumar a cada píxel (por defecto 50)

    Returns:
        Imagen aclarada
    """
    # Convertir a int16 para evitar overflow al sumar
    img_aclarada = imagen.astype(np.int16)
    img_aclarada = img_aclarada + factor

    # Limitar valores entre 0 y 255
    img_aclarada = np.clip(img_aclarada, 0, 255)

    # Convertir de vuelta a uint8
    img_aclarada = img_aclarada.astype(np.uint8)

    return img_aclarada


def reducir_ruido(imagen, metodo='gaussian', kernel_size=5):
    """
    Reduce el ruido de una imagen usando diferentes métodos de filtrado.

    Args:
        imagen: Imagen de entrada (puede ser color o escala de grises)
        metodo: Tipo de filtro ('gaussian', 'median', 'bilateral')
        kernel_size: Tamaño del kernel (debe ser impar)

    Returns:
        Imagen con ruido reducido
    """
    # Asegurar que kernel_size sea impar
    if kernel_size % 2 == 0:
        kernel_size += 1

    if metodo == 'gaussian':
        # Filtro Gaussiano - suaviza la imagen
        img_sin_ruido = cv2.GaussianBlur(imagen, (kernel_size, kernel_size), 0)

    elif metodo == 'median':
        # Filtro de Mediana - muy efectivo contra ruido "salt and pepper"
        img_sin_ruido = cv2.medianBlur(imagen, kernel_size)

    elif metodo == 'bilateral':
        # Filtro Bilateral - reduce ruido preservando bordes
        img_sin_ruido = cv2.bilateralFilter(imagen, kernel_size, 75, 75)

    else:
        print(f"Método '{metodo}' no reconocido. Usando 'gaussian' por defecto.")
        img_sin_ruido = cv2.GaussianBlur(imagen, (kernel_size, kernel_size), 0)

    return img_sin_ruido


def ajustar_brillo_contraste(imagen, alpha=1.0, beta=0):
    """
    Ajusta el brillo y contraste de una imagen.

    Args:
        imagen: Imagen de entrada
        alpha: Factor de contraste (1.0 = sin cambio, >1 aumenta, <1 disminuye)
        beta: Factor de brillo (0 = sin cambio, positivo aclara, negativo oscurece)

    Returns:
        Imagen ajustada
    """
    # Aplicar la transformación: nueva_imagen = alpha * imagen + beta
    img_ajustada = cv2.convertScaleAbs(imagen, alpha=alpha, beta=beta)

    return img_ajustada


imagen_prueba = 'img/pruebaImg2.png'
try:
    # Cargar la imagen a color (por defecto cv2.IMREAD_COLOR)
    img_color = cv2.imread(imagen_prueba, cv2.IMREAD_COLOR)

    # Verificar si la imagen se cargó correctamente
    if img_color is None:
        raise FileNotFoundError("No se pudo cargar la imagen. Verifica que el archivo existe en la ruta especificada.")

    print(f"Imagen a color cargada correctamente")
    print(f"Dimensiones: {img_color.shape}")
    print(f"Tipo de dato: {img_color.dtype}")

    # Cargar la imagen en escala de grises
    img_gris = cv2.imread(imagen_prueba, cv2.IMREAD_GRAYSCALE)

    if img_gris is None:
        raise FileNotFoundError("No se pudo cargar la imagen en escala de grises.")

    print(f"\nImagen en escala de grises cargada correctamente")
    print(f"Dimensiones: {img_gris.shape}")
    print(f"Tipo de dato: {img_gris.dtype}")

    # Mostrar la matriz de la imagen en escala de grises
    print("\n" + "="*80)
    print("MATRIZ DE LA IMAGEN EN ESCALA DE GRISES")
    print("="*80)

    altura, ancho = img_gris.shape

    # Si la imagen es pequeña (menos de 20x20), mostrar toda la matriz
    if altura <= 20 and ancho <= 20:
        print("\nMatriz completa:")
        print(img_gris)
    else:
        # Mostrar solo una región de 10x10 de la esquina superior izquierda
        print(f"\nMuestra de la matriz (10x10 píxeles de la esquina superior izquierda):")
        print(img_gris[:10, :10])

        print(f"\nNota: La imagen completa es de {altura}x{ancho} píxeles.")
        print("Mostrando solo una muestra. Para ver la matriz completa, usa: print(img_gris)")

    # Mostrar estadísticas de la matriz
    print("\n" + "-"*80)
    print("ESTADÍSTICAS DE LA IMAGEN EN ESCALA DE GRISES:")
    print("-"*80)
    print(f"Valor mínimo: {np.min(img_gris)}")
    print(f"Valor máximo: {np.max(img_gris)}")
    print(f"Valor promedio: {np.mean(img_gris):.2f}")
    print(f"Desviación estándar: {np.std(img_gris):.2f}")

    # Mostrar información sobre la matriz de color
    print("\n" + "="*80)
    print("MATRIZ DE LA IMAGEN A COLOR (BGR)")
    print("="*80)

    altura_c, ancho_c, canales = img_color.shape

    # Mostrar una muestra pequeña de cada canal
    print(f"\nLa imagen a color tiene {canales} canales (Blue, Green, Red)")
    print(f"Muestra de 5x5 píxeles de la esquina superior izquierda por canal:\n")

    print("Canal AZUL (B):")
    print(img_color[:5, :5, 0])

    print("\nCanal VERDE (G):")
    print(img_color[:5, :5, 1])

    print("\nCanal ROJO (R):")
    print(img_color[:5, :5, 2])

    print("\n" + "-"*80)
    print("ESTADÍSTICAS DE LA IMAGEN A COLOR:")
    print("-"*80)
    for i, canal in enumerate(['Azul', 'Verde', 'Rojo']):
        print(f"\nCanal {canal}:")
        print(f"  Valor mínimo: {np.min(img_color[:,:,i])}")
        print(f"  Valor máximo: {np.max(img_color[:,:,i])}")
        print(f"  Valor promedio: {np.mean(img_color[:,:,i]):.2f}")

    print("\n" + "="*80 + "\n")

    # ========== APLICAR FUNCIONES DE PROCESAMIENTO ==========

    print("APLICANDO PROCESAMIENTO A LAS IMÁGENES...")
    print("="*80)

    # 1. Aclarar imagen en escala de grises
    img_gris_aclarada = aclarar_imagen(img_gris, factor=50)
    print("\n1. Imagen en escala de grises aclarada (+50)")

    # 2. Reducir ruido en escala de grises con diferentes métodos
    img_gris_gaussian = reducir_ruido(img_gris, metodo='gaussian', kernel_size=5)
    print("2. Ruido reducido con filtro Gaussiano")

    img_gris_median = reducir_ruido(img_gris, metodo='median', kernel_size=5)
    print("3. Ruido reducido con filtro de Mediana")

    img_gris_bilateral = reducir_ruido(img_gris, metodo='bilateral', kernel_size=9)
    print("4. Ruido reducido con filtro Bilateral")

    # 3. Aclarar imagen a color
    img_color_aclarada = aclarar_imagen(img_color, factor=50)
    print("5. Imagen a color aclarada (+50)")

    # 4. Ajustar brillo y contraste
    img_color_contraste = ajustar_brillo_contraste(img_color, alpha=1.3, beta=20)
    print("6. Imagen con contraste aumentado (alpha=1.3, beta=20)")

    # 5. Reducir ruido en imagen a color
    img_color_sin_ruido = reducir_ruido(img_color, metodo='bilateral', kernel_size=9)
    print("7. Imagen a color con ruido reducido (bilateral)")

    # 6. Combinación: reducir ruido y aclarar
    img_gris_combinada = reducir_ruido(img_gris, metodo='gaussian', kernel_size=5)
    img_gris_combinada = aclarar_imagen(img_gris_combinada, factor=40)
    print("8. Imagen combinada: ruido reducido + aclarada")

    print("\n" + "="*80 + "\n")

    # Crear ventanas con nombre
    cv2.namedWindow('1. Original - Color', cv2.WINDOW_NORMAL)
    cv2.namedWindow('2. Original - Grises', cv2.WINDOW_NORMAL)
    cv2.namedWindow('3. Grises Aclarada', cv2.WINDOW_NORMAL)
    cv2.namedWindow('4. Grises - Filtro Gaussiano', cv2.WINDOW_NORMAL)
    cv2.namedWindow('5. Grises - Filtro Mediana', cv2.WINDOW_NORMAL)
    cv2.namedWindow('6. Grises - Filtro Bilateral', cv2.WINDOW_NORMAL)
    cv2.namedWindow('7. Color Aclarada', cv2.WINDOW_NORMAL)
    cv2.namedWindow('8. Color - Mayor Contraste', cv2.WINDOW_NORMAL)
    cv2.namedWindow('9. Color - Sin Ruido', cv2.WINDOW_NORMAL)
    cv2.namedWindow('10. Grises Combinada', cv2.WINDOW_NORMAL)

    # Mostrar todas las imágenes
    cv2.imshow('1. Original - Color', img_color)
    cv2.imshow('2. Original - Grises', img_gris)
    cv2.imshow('3. Grises Aclarada', img_gris_aclarada)
    cv2.imshow('4. Grises - Filtro Gaussiano', img_gris_gaussian)
    cv2.imshow('5. Grises - Filtro Mediana', img_gris_median)
    cv2.imshow('6. Grises - Filtro Bilateral', img_gris_bilateral)
    cv2.imshow('7. Color Aclarada', img_color_aclarada)
    cv2.imshow('8. Color - Mayor Contraste', img_color_contraste)
    cv2.imshow('9. Color - Sin Ruido', img_color_sin_ruido)
    cv2.imshow('10. Grises Combinada', img_gris_combinada)

    # Esperar a que el usuario presione una tecla
    print("\nVentanas abiertas. Presiona ESC o 'q' en cualquier ventana para cerrar...")

    # Bucle para manejar el cierre de ventanas
    while True:
        key = cv2.waitKey(1) & 0xFF

        # Cerrar con ESC (27) o 'q' (113)
        if key == 27 or key == ord('q'):
            print("Cerrando ventanas...")
            break

        # Verificar si alguna ventana fue cerrada manualmente
        try:
            if cv2.getWindowProperty('1. Original - Color', cv2.WND_PROP_VISIBLE) < 1:
                print("Ventana cerrada manualmente...")
                break
        except:
            break

    # Cerrar todas las ventanas
    cv2.destroyAllWindows()
    print("Ventanas cerradas correctamente")

except FileNotFoundError as e:
    print(f"Error de archivo: {e}")
    sys.exit(1)

except cv2.error as e:
    print(f"Error de OpenCV: {e}")
    sys.exit(1)

except KeyboardInterrupt:
    print("\nInterrumpido por el usuario (Ctrl+C)")
    cv2.destroyAllWindows()
    sys.exit(0)

except Exception as e:
    print(f"Error inesperado: {type(e).__name__} - {e}")
    cv2.destroyAllWindows()
    sys.exit(1)
