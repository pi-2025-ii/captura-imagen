import cv2
import numpy as np

# abrir la camara
cap = cv2.VideoCapture(0)
# verificar si la camara se abrio correctamente
if not cap.isOpened():
    print("Error: No se pudo abrir la camara")
    exit()
# leer la imagen de la camara
ret, frame = cap.read()
# verificar si se leyo la imagen correctamente
if not ret:
    print("Error: No se pudo leer la imagen")
    exit()
# mostrar la imagen en tiempo real
# capturar y guardar la imagen si se presiona la tecla 's'  y salir si se presiona la tecla 'q'
while True:
    ret, frame = cap.read()
    # binarizar la imagen in escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)
    binary_3ch = np.stack([np.zeros_like(binary), binary, binary], axis=2)

    # mostrar en tiempo real la imagen original y la imagen en escala de grises en una misma ventana
    cv2.imshow("Imagen", np.hstack([frame, binary_3ch]))
    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):
        cv2.imwrite("imagen.jpg", gray)
        print("Imagen guardada como imagen.jpg")
    elif key == ord('q'):
        break

# cerrar la camara
cap.release()
# cerrar todas las ventanas
cv2.destroyAllWindows()
