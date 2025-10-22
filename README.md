# Tarea: Procesamiento de Imágenes en Tiempo Real

**Estudiante 1**: [Tu nombre]
**Estudiante 2**: [Tu nombre]
**Estudiante 3**: [Tu nombre]  
**Curso**: [Nombre del curso]

> 📋 **Nota**: Esta es una plantilla para la elaboración del README.md. Elabora el contenido de acuerdo a lo indicado en el archivo [instrucciones.md](instrucciones.md)

## Descripción de la Tarea

Esta tarea consiste en desarrollar dos scripts de procesamiento de imágenes en tiempo real utilizando OpenCV:

1. **Parte 1 - Transformaciones de Imagen**: Implementar al menos 8 transformaciones diferentes aplicadas a imágenes capturadas en tiempo real
2. **Parte 2 - Detección de Monedas**: Desarrollar un sistema de conteo de monedas usando operaciones morfológicas y el algoritmo Watershed

## Instalación y Configuración
[Realiza la descripción de acuerdo a tu implementación]

### Dependencias Requeridas

```bash
pip install opencv-python
pip install numpy
pip install scipy
pip install scikit-image
pip install matplotlib
```

### Configuración del Entorno
[Realiza la descripción de acuerdo a tu implementación]

1. Asegúrate de tener una cámara web conectada
2. Instala las dependencias listadas arriba
3. Ejecuta los scripts desde el directorio del proyecto

## Uso de los Scripts

### Parte 1: Transformaciones de Imagen
[Realiza la descripción de acuerdo a tu implementación]

**Archivo**: `transformaciones_imagen.py` o `transformaciones_imagen.ipynb`

#### Funcionalidades:
- 8 transformaciones diferentes disponibles
- Visualización en tiempo real (original + transformada)
- Guardado de imágenes con tecla
- Salida con tecla 'q'

#### Controles:
- **Teclas numéricas (1-8)**: Seleccionar transformación
- **Tecla 's'**: Guardar imagen actual
- **Tecla 'q'**: Salir del programa

#### Transformaciones Disponibles:
[Realiza la descripción de acuerdo a tu implementación]

1. Escala de grises
2. Rotación
3. Ajuste de brillo/contraste
4. Detección de bordes (Canny)
5. Difuminado (Blur)
6. Conversión de color (HSV/LAB)
7. Umbralización
8. Transformaciones geométricas

### Parte 2: Detección de Monedas
[Realiza la descripción de acuerdo a tu implementación]

**Archivo**: `deteccion_monedas.py` o `deteccion_monedas.ipynb`

#### Funcionalidades:
- Captura en tiempo real
- Detección automática de monedas
- Conteo preciso usando Watershed
- Visualización de resultados

#### Controles:
- **Tecla 'c'**: Capturar imagen de monedas
- **Tecla 'q'**: Salir del programa

## Resultados y Ejemplos

### Transformaciones de Imagen
- [Enlace a carpeta de imágenes de ejemplo](./imagenes/transformaciones/)
- [Cuaderno con demostraciones](./transformaciones_demo.ipynb)
- Capturas de pantalla de cada transformación aplicada

### Detección de Monedas
[Incluir imágenes de ejemplo mostrando:]
- Imagen original de monedas
- Imagen procesada con monedas detectadas
- Resultado final con conteo

## Estructura de la Tarea
[Realiza la descripción de acuerdo a tu implementación]

```
tarea-procesamiento-imagenes/
├── README.md
├── instrucciones.md
├── transformaciones_imagen.py
├── deteccion_monedas.py
├── imagenes/
│   ├── transformaciones/
│   └── monedas/
└── resultados/
    ├── imagenes_guardadas/
    └── monedas_detectadas/
```

### Archivos de la Tarea:
[Realiza la descripción de acuerdo a tu implementación]

- `README.md`: Documentación de la tarea (este archivo)
- `instrucciones.md`: Especificaciones detalladas de la tarea
- `transformaciones_imagen.py`: Script para Parte 1
- `deteccion_monedas.py`: Script para Parte 2
- `imagenes/`: Carpeta para almacenar imágenes de ejemplo
- `resultados/`: Carpeta para guardar resultados

## Declaración de Uso de IA
[Realiza la descripción de acuerdo a tu implementación]

### ¿Se utilizaron herramientas de IA?
[ ] Sí  [ ] No

### Si se utilizaron, especificar:

**Herramientas utilizadas:**
- [ ] ChatGPT
- [ ] Claude
- [ ] GitHub Copilot
- [ ] Otras: _______________

**Propósito del uso:**
- [ ] Generación de código inicial
- [ ] Debugging y corrección de errores
- [ ] Optimización de algoritmos
- [ ] Documentación
- [ ] Otros: _______________

**Porcentaje de código generado con IA:**
- [ ] 0-25%
- [ ] 26-50%
- [ ] 51-75%
- [ ] 76-100%

## Troubleshooting

### Problemas Comunes:
[Realiza la descripción de acuerdo a tu implementación]

1. **Error de cámara no encontrada**
   - Verificar que la cámara esté conectada
   - Cerrar otras aplicaciones que usen la cámara

2. **Dependencias faltantes**
   - Ejecutar: `pip install -r requirements.txt`

3. **Bajo rendimiento en tiempo real**
   - Reducir resolución de la cámara
   - Optimizar parámetros de las transformaciones

### Limitaciones Conocidas:
- La detección de monedas funciona mejor con monedas de diferentes tamaños
- Las transformaciones pueden afectar el rendimiento en tiempo real
- La iluminación afecta la calidad de la detección

## Reflexión sobre la Tarea

### Aprendizajes Adquiridos:
[Describe qué aprendiste durante el desarrollo de la tarea - mínimo 3 párrafos]

### Dificultades Encontradas:
[Describe los principales desafíos y cómo los resolviste - incluir ejemplos específicos]

### Logros Alcanzados:
[Destaca los logros más importantes de la tarea - ser específico sobre métricas o resultados]

### Sugerencias de Mejora:
[Propón mejoras futuras para la tarea - mínimo 3 sugerencias concretas]

---

