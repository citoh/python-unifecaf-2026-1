# INSTALANDO A APLICAÇÃO:
# python3 -m venv venv
# source venv/bin/activate
# pip install opencv-python

# cv2 se refere a opencv-python - utilizado para processar imagens
import cv2 

# sys.argv - ler argumentos
# sys.exit - fechar a aplicação
import sys 
    
def face_detection():
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
    
    #PROCESSANDO IMAGEM - os passos abaixo são técnicas para processar imagem e detectar rostos
    
    # 1) Pré-processamento
    # Convertendo para tons de cinza para otimizar o processamento
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Exibindo pré-processamento
    cv2.imshow("Pre_processamento", gray)
    print("Pressione qualquer tecla para coninuar")
    cv2.waitKey(0)
    
    # 2) Classificadores Haar
    # Carregando classificador Haar - necessário para detecção de rostos
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    if face_cascade.empty():
        print("Falha ao carregar classificador Haar.")
        sys.exit(1)

    # 3) Detecção de rostos (parâmetros mais conservadores)
    # Detectando rostos
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Circulando rostos encontrados
    stroke = (0, 255, 0) # rgb: 0000FF
    for (x, y, w, h) in faces:
        cx, cy = x + w // 2, y + h // 2
        r = int(0.6 * max(w, h))
        cv2.circle(img, (cx, cy), r // 2, stroke, thickness=1, lineType=cv2.LINE_AA)

    #---------------------------------------------------

    # Exibindo resultado final
    cv2.imshow("Rostos detectados", img)
    print("Pressione qualquer tecla para fechar...")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

face_detection()