import cv2
import os
from deepface import DeepFace

# Yüz algılayıcıyı yükle
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Kamerayı başlat
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Kamera görüntüsü alınamadı")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Yüz algılandığında kare içine al
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        
        # Yüzü kes ve DeepFace ile duygu analizi yap
        face_crop = frame[y:y+h, x:x+w]
        try:
            
            # Dönen sonuç listeyse, ilk elemanı al
            if isinstance(emotion_result, list):
                emotion_result = emotion_result[0]

            # dominant_emotion'u al ve ekrana yaz
            dominant_emotion = emotion_result['dominant_emotion']

        except Exception as e:
            print(f"Hata: {str(e)}")

    cv2.imshow('Yüz ve Duygu Analizi', frame)

    # 'q' tuşuna basıldığında döngüyü sonlandır
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
