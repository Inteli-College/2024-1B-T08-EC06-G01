# Utilizando o modelo do como torchscript

import cv2
import torch
from PIL import Image
import torchvision.transforms as transforms
import os


# Carregando o modelo 
def load_model():
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    pathzin = '../models/model_v8.torchscript'
    model = torch.jit.load(pathzin)

    # model = torch.hub.load(model='../models/yolo_v8_n.pt', source='local') 
    return model



def main():
    # Modelinho
    pathzin_img = '../assets/city.jpg'

    # Carregando o modelo
    model = load_model()

    transform = transforms.Compose([
    transforms.Resize((640, 640)),
    transforms.ToTensor(),
    ])


    # Load and preprocess input image
    input_image = Image.open(pathzin_img)
    input_tensor = transform(input_image)
    input_batch = input_tensor.unsqueeze(0)  # Add batch dimension

    # Run inference
    with torch.no_grad():
        output = model(input_batch)
        print("output 1", output)
    # Reshape output tensor to match the expected shape
    output = output.view(1, 84, 8400)

    print("output 2",output)


if __name__ == "__main__":
    main()