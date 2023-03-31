import cv2
import mediapipe as mp

webcam = cv2.VideoCapture(0)
reconhecimento_rosto = mp.solutions.face_detection
reconhecedor_rosto = reconhecimento_rosto.FaceDetection()
desenho = mp.solutions.drawing_utils

while True:
    #Ler as informações da webcam
    verificador, frame = webcam.read()
    if not verificador: #Verifica sem tem imagem na webcam
        break

    #Reconhecer os rostos que tem ali dentro
    lista_rostos = reconhecedor_rosto.process(frame) #cria uma lista com os rostos apresentados na tela

    if lista_rostos.detections: #Verifica se tem algum rosto na tela
        for rosto in lista_rostos.detections:
            desenho.draw_detection(frame, rosto) #onde desenha e o que desenha

    cv2.imshow("Detector Facial", frame) #Abre a janela da webcam

    #Quando apertar esc ele para o loop
    if cv2.waitKey(1) == 27: #outra solução ord("letra")
        break

webcam.release() #Desliga a webcam
cv2.destroyAllWindows()
