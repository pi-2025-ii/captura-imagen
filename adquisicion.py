import cv2

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
    cv2.imshow("Imagen", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):
        cv2.imwrite("imagen.jpg", frame)
        print("Imagen guardada como imagen.jpg")
    elif key == ord('q'):
        break
# cerrar la camara
cap.release()
# cerrar todas las ventanas
cv2.destroyAllWindows()

