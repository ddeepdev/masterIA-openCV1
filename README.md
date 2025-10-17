# Práctica Básica de OpenCV - Procesamiento de Imágenes

Proyecto de práctica para aprender los fundamentos de procesamiento de imágenes usando OpenCV en Python.

## Descripción

Este proyecto implementa funciones básicas de procesamiento de imágenes incluyendo:
- Lectura de imágenes a color y escala de grises
- Aclarado de imágenes
- Reducción de ruido con diferentes filtros
- Ajuste de brillo y contraste
- Visualización de matrices de píxeles
- Estadísticas de imágenes

## Requisitos

- Python 3.7+
- opencv-contrib-python
- numpy

## Instalación

1. Clona este repositorio:
```bash
git clone git@github.com:ddeepdev/masterIA-openCV1.git
cd masterIA-openCV1
```

2. Crea un entorno virtual:
```bash
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate
```

3. Instala las dependencias:
```bash
pip install opencv-contrib-python numpy
```

## Uso

Ejecuta el script principal:

```bash
python openCV.py
```

El script mostrará 10 ventanas diferentes con las siguientes transformaciones:
1. Imagen original a color
2. Imagen original en escala de grises
3. Imagen en grises aclarada
4. Imagen con filtro Gaussiano
5. Imagen con filtro de Mediana
6. Imagen con filtro Bilateral
7. Imagen a color aclarada
8. Imagen con mayor contraste
9. Imagen a color sin ruido
10. Imagen combinada (ruido reducido + aclarada)

### Cerrar las ventanas

Puedes cerrar las ventanas de cualquiera de estas formas:
- Presiona **ESC** en cualquier ventana
- Presiona **'q'** en cualquier ventana
- Presiona **Ctrl+C** en la terminal
- Haz clic en el botón X de cualquier ventana

## Funciones Implementadas

### `aclarar_imagen(imagen, factor=50)`

Aclara una imagen sumando un valor constante a todos los píxeles.

**Parámetros:**
- `imagen`: Imagen de entrada (puede ser color o escala de grises)
- `factor`: Valor a sumar a cada píxel (por defecto 50)

**Retorna:**
- Imagen aclarada

**Ejemplo:**
```python
img_aclarada = aclarar_imagen(img_gris, factor=50)
```

### `reducir_ruido(imagen, metodo='gaussian', kernel_size=5)`

Reduce el ruido de una imagen usando diferentes métodos de filtrado.

**Parámetros:**
- `imagen`: Imagen de entrada (puede ser color o escala de grises)
- `metodo`: Tipo de filtro ('gaussian', 'median', 'bilateral')
- `kernel_size`: Tamaño del kernel (debe ser impar)

**Métodos disponibles:**
- **gaussian**: Filtro Gaussiano - suaviza la imagen
- **median**: Filtro de Mediana - muy efectivo contra ruido "salt and pepper"
- **bilateral**: Filtro Bilateral - reduce ruido preservando bordes

**Retorna:**
- Imagen con ruido reducido

**Ejemplo:**
```python
img_sin_ruido = reducir_ruido(img_gris, metodo='bilateral', kernel_size=9)
```

### `ajustar_brillo_contraste(imagen, alpha=1.0, beta=0)`

Ajusta el brillo y contraste de una imagen.

**Parámetros:**
- `imagen`: Imagen de entrada
- `alpha`: Factor de contraste (1.0 = sin cambio, >1 aumenta, <1 disminuye)
- `beta`: Factor de brillo (0 = sin cambio, positivo aclara, negativo oscurece)

**Retorna:**
- Imagen ajustada

**Ejemplo:**
```python
img_ajustada = ajustar_brillo_contraste(img_color, alpha=1.3, beta=20)
```

## Estructura del Proyecto

```
masterIA-openCV1/
├── .gitignore
├── README.md
├── openCV.py          # Script principal
└── img/              # Directorio de imágenes
    ├── pruebaQR.png
    └── pruebaImg2.png
```

## Características Técnicas

### Manejo de Excepciones

El código incluye manejo robusto de excepciones:
- `FileNotFoundError`: Para errores de archivo no encontrado
- `cv2.error`: Para errores específicos de OpenCV
- `KeyboardInterrupt`: Para interrupciones del usuario (Ctrl+C)
- `Exception`: Para cualquier otro error inesperado

### Visualización de Matrices

El script muestra información detallada sobre las matrices de píxeles:
- Muestra de la matriz (10x10 para escala de grises, 5x5 por canal para color)
- Valores mínimo, máximo, promedio y desviación estándar
- Información de cada canal RGB por separado

### Procesamiento de Imágenes

Las imágenes se procesan usando:
- **NumPy**: Para operaciones matriciales eficientes
- **OpenCV**: Para filtros y transformaciones de imagen
- **Conversión segura de tipos**: Evita overflow al procesar píxeles

## Notas

- Las imágenes se cargan desde el directorio `img/`
- Puedes cambiar la imagen a procesar modificando la variable `imagen_prueba` en el código
- Los valores de los píxeles están en el rango 0-255 (uint8)
- OpenCV usa el formato de color BGR (Blue, Green, Red) en lugar de RGB

## Autor

Jagoraxr --> Proyecto creado como práctica de aprendizaje de OpenCV.

## Licencia

Este proyecto es de uso educativo.
