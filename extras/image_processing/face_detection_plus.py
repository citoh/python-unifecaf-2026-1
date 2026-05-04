# INSTALANDO A APLICAÇÃO:
# python3 -m venv venv
# source venv/bin/activate
# pip install opencv-python

# cv2 se refere a opencv-python - utilizado para processar imagens
import cv2 

# sys.argv - ler argumentos
# sys.exit - fechar a aplicação
import sys 
    

def face_detection_plus():
    # Verificando se o nome da imagem foi passada por parâmetro
    if len(sys.argv) < 2:
        print("Passe por argumento o nome da imagem")
        sys.exit(1)

    in_name = sys.argv[1]

    # Verificando formato da imagem
    valid_exts = (".jpg", ".jpeg", ".png")
    if not in_name.lower().endswith(valid_exts):
        print(f"Formato de imagem não suportado. Formatos aceitos: {', '.join(valid_exts)}")
        sys.exit(1)

    # Carregando a imagem
    img = cv2.imread(in_name)
    if img is None:
        print(f"Não foi possível abrir a imagem: {in_name}")
        sys.exit(1)

    # Exibindo imagem de entrada    
    cv2.imshow("Imagem original", img)
    print("Pressione qualquer tecla para coninuar")
    cv2.waitKey(0)
    
    #---------------------------------------------------
    # PROCESSANDO IMAGEM — passos para detectar rostos com menos falsos positivos

    # 1) Pré-processamento
    # conversão para tons de cinza
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # melhora contraste em variações de iluminação
    gray = cv2.equalizeHist(gray)        
    # suaviza ruído preservando bordas         
    gray = cv2.bilateralFilter(gray, 7, 50, 50)   

    # Exibindo pré-processamento
    cv2.imshow("Pre_processamento", gray)
    print("Pressione qualquer tecla para coninuar")
    cv2.waitKey(0)

    # 2) Classificadores Haar
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    eye_cascade  = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye_tree_eyeglasses.xml")
    if face_cascade.empty() or eye_cascade.empty():
        print("Falha ao carregar os classificadores Haar.")
        sys.exit(1)
    # Tamanho mínimo de face relativo ao frame (evita “micro-rostos” falsos)
    h_img, w_img = gray.shape[:2]
    min_w = max(28, w_img // 30)
    min_h = max(28, h_img // 30)

    # 3) Detecção de rostos
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.08,          
        minNeighbors=8,            
        minSize=(min_w, min_h),    
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # 4) Verificação por olhos no ROI do rosto (filtra falsos)
    faces_filtradas = []
    for (x, y, w, h) in faces:
        # (opcional) checagem simples de proporção para filtrar caixas bizarras
        ar = w / float(h)
        if not (0.75 <= ar <= 1.6):
            continue

        roi = gray[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(
            roi,
            scaleFactor=1.08,
            minNeighbors=6,
            minSize=(max(10, w // 8), max(10, h // 8))
        )
        if len(eyes) >= 1:  # exige ao menos 1 olho visível
            faces_filtradas.append((x, y, w, h))

    # 5) Desenho dos círculos — RGB #0000FF → BGR (255, 0, 0)
    stroke = (255, 0, 0)
    for (x, y, w, h) in faces_filtradas:
        cx, cy = x + w // 2, y + h // 2
        r = int(0.5 * max(w, h))  # raio proporcional à caixa do rosto
        cv2.circle(img, (cx, cy), r, stroke, thickness=2, lineType=cv2.LINE_AA)
    #---------------------------------------------------

    # Exibindo resultado final
    cv2.imshow("Rostos detectados", img)
    print("Pressione qualquer tecla para fechar...")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

face_detection_plus()