import cv2
from ultralytics import YOLO
from PIL import Image
import os


# Carregando o modelo 
def load_model(path):
    model = YOLO(path)
    return model

# Carregando um array com todos os itens da pasta asset 
def load_assets(path):
    assets_folder = os.listdir(path)
    paths = []

    for asset in assets_folder:
        file_path = os.path.join('..', 'assets', asset)
        paths.append(file_path)

    return paths

# Criando as imagens resposta do modelo
def detect(predictions_output):
    for i, r in enumerate(predictions_output):
        # Plot results image
        im_bgr = r.plot()  # BGR-order numpy array
        im_rgb = Image.fromarray(im_bgr[..., ::-1])  # RGB-order PIL image

        # Save results to disk
        r.save(filename=f"../predictions/results{i}.jpg")



def main():
    # Carregando o modelo
    model = load_model('../models/yolo_v8_n.pt')

    # Carregando as imagens
    load_imgs = load_assets('../assets')

    # Realizando as predições
    results = model(load_imgs)
    
    # Salvando as classificações
    imgs_result = detect(results)

if __name__ == "__main__":
    main()