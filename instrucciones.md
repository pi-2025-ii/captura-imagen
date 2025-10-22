# Instrucciones de Tarea: Procesamiento de Imágenes en Tiempo Real

## Descripción General

Esta tarea consiste en desarrollar dos scripts de procesamiento de imágenes en tiempo real utilizando OpenCV. El objetivo es implementar diferentes transformaciones de imagen y aplicar técnicas de detección de monedas usando operaciones morfológicas.

## Parte 1: Transformaciones de Imagen en Tiempo Real

### Objetivo
Crear un script (`.py` o cuaderno `.ipynb`) que aplique al menos **ocho transformaciones diferentes** a imágenes capturadas en tiempo real desde la cámara.

### Transformaciones Requeridas
El script debe incluir las siguientes transformaciones:

1. **Conversión a escala de grises**
2. **Rotación** (ángulo libre o fijo)
3. **Ajuste de brillo o contraste**
4. **Detección de bordes** (usando Canny)
5. **Difuminado (blur)**
6. **Conversión de color** (a HSV o LAB)
7. **Umbralización**
8. **Transformaciones geométricas** (escalado o traslación)

### Funcionalidades Requeridas

- **Selección de transformación**: El código debe permitir escoger una transformación a la vez
- **Visualización en tiempo real**: Mostrar la imagen original y la imagen transformada lado a lado
- **Guardado de imagen**: Presionar una tecla para guardar la imagen actual
- **Salida del programa**: Presionar la tecla 'q' para salir

### Estructura del Código Sugerida

```python
# Estructura básica recomendada
import cv2
import numpy as np

# Inicializar cámara
# Menú de selección de transformaciones
# Loop principal:
#   - Capturar frame
#   - Aplicar transformación seleccionada
#   - Mostrar imagen original y transformada
#   - Manejar teclas (guardar/salir)
```

## Parte 2: Detección y Conteo de Monedas

### Objetivo
Crear un script (`.py` o cuaderno `.ipynb`) que capture una imagen de monedas en tiempo real y aplique técnicas de conteo usando operaciones morfológicas y el algoritmo Watershed.

### Funcionalidades Requeridas

1. **Captura en tiempo real**: Iniciar la captura desde la cámara
2. **Guardado de imagen**: Capturar y guardar una imagen de monedas
3. **Procesamiento de monedas**: Aplicar el algoritmo de conteo
4. **Visualización de resultados**: Mostrar las monedas detectadas
5. **Guardado de resultados**: Guardar imagen con monedas marcadas

### Técnicas a Implementar

- **Operaciones morfológicas**: Para limpiar y preparar la imagen
- **Algoritmo Watershed**: Para separar monedas que se tocan
- **Detección de contornos**: Para identificar objetos circulares
- **Filtrado por tamaño**: Para eliminar ruido y objetos no deseados

### Recursos de Referencia

- [Tutorial Watershed de OpenCV](https://docs.opencv.org/4.x/d3/db4/tutorial_py_watershed.html)
- [Documentación Watershed](https://people.cmm.minesparis.psl.eu/users/beucher/wtshed.html)

### Estructura del Código Sugerida

```python
# Estructura básica recomendada
import cv2
import numpy as np
from scipy import ndimage
from skimage.feature import peak_local_maxima
from skimage.segmentation import watershed

# Inicializar cámara
# Capturar imagen de monedas
# Preprocesamiento (escala de grises, blur, etc.)
# Umbralización
# Operaciones morfológicas
# Aplicar Watershed
# Contar y marcar monedas
# Mostrar y guardar resultados
```

## Criterios de Evaluación

### Parte 1
- ✅ Implementación de al menos 8 transformaciones diferentes
- ✅ Interfaz para seleccionar transformaciones
- ✅ Visualización en tiempo real (original + transformada)
- ✅ Funcionalidad de guardado con tecla
- ✅ Salida con tecla 'q'
- ✅ Código bien documentado y comentado

### Parte 2
- ✅ Captura en tiempo real funcional
- ✅ Implementación correcta de operaciones morfológicas
- ✅ Uso del algoritmo Watershed
- ✅ Conteo preciso de monedas
- ✅ Visualización de resultados
- ✅ Guardado de imagen con monedas marcadas
- ✅ No usar modelos pre-entrenados

## Entregables

1. **Script Parte 1**: Archivo `.py` o cuaderno `.ipynb` con transformaciones
2. **Script Parte 2**: Archivo `.py` o cuaderno `.ipynb` con detección de monedas
3. **Imágenes de ejemplo**: Capturas de las transformaciones aplicadas
4. **Imagen de monedas**: Imagen original capturada
5. **Resultado final**: Imagen con monedas detectadas y marcadas
6. **Documentación**: Comentarios en el código explicando cada paso
7. **README.md**: Documentación completa del proyecto

## Notas Importantes

- **No usar modelos pre-entrenados** para la detección de monedas
- El código debe ser **robusto** y manejar errores apropiadamente
- Las transformaciones deben ser **aplicables en tiempo real**
- La detección de monedas debe ser **precisa** y **confiable**
- Incluir **comentarios detallados** explicando cada operación

## Documentación del Proyecto (README.md)

### Contenido Requerido del README

El archivo `README.md` debe incluir las siguientes secciones:

#### 1. **Descripción del Proyecto**
- Explicación clara del propósito de la tarea
- Descripción de las dos partes del proyecto
- Objetivos de aprendizaje

#### 2. **Instalación y Configuración**
- Dependencias requeridas
- Instrucciones de instalación
- Configuración del entorno

#### 3. **Uso de los Scripts**
- Instrucciones paso a paso para ejecutar cada script
- Explicación de las funcionalidades
- Controles de teclado disponibles
- Ejemplos de uso

#### 4. **Resultados y Ejemplos**
- Capturas de pantalla de las transformaciones
- Imágenes de ejemplo de detección de monedas
- Explicación de los resultados obtenidos

#### 5. **Estructura del Proyecto**
- Descripción de archivos y carpetas
- Explicación del código principal
- Diagramas de flujo (opcional)

#### 6. **Declaración de Uso de IA**
**SECCIÓN OBLIGATORIA**: Debe incluir una declaración clara sobre el uso de herramientas de IA:

- **¿Se utilizaron herramientas de IA?** (Sí/No)
- **Si se utilizaron, especificar cuáles:**
  - ChatGPT, Claude, Copilot, etc.
  - Para qué propósito (generación de código, debugging, optimización, etc.)
  - Qué porcentaje del código fue generado con IA
- **Declaración de autoría:**
  - Qué partes del código fueron desarrolladas manualmente
  - Qué partes fueron asistidas por IA
  - Cómo se integró la asistencia de IA en el proceso de desarrollo

#### 7. **Troubleshooting**
- Problemas comunes y soluciones
- Limitaciones conocidas
- Sugerencias de mejora

#### 8. **Conclusión**
- Reflexión sobre el aprendizaje
- Dificultades encontradas
- Logros alcanzados