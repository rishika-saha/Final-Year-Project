import torch
from torch_snippets import *
import torch.nn as nn
from torchvision import transforms
import urllib.request
from .modifier import changer
import cv2

device = 'cuda' if torch.cuda.is_available() else 'cpu'

def convBlock(ni, no):
    return nn.Sequential(
        nn.Dropout(0.2),
        nn.Conv2d(ni, no, kernel_size=3, padding=1, padding_mode='reflect'),
        nn.ReLU(inplace=True),
        nn.BatchNorm2d(no),
    )

class SiameseNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.features = nn.Sequential(
            convBlock(1,4),
            convBlock(4,8),
            convBlock(8,8),
            nn.Flatten(),
            nn.Linear(8*100*100, 500), 
            nn.ReLU(inplace=True),
            nn.Linear(500, 500), 
            nn.ReLU(inplace=True),
            nn.Linear(500, 5)
        )

    def forward(self, input1, input2):
        output1 = self.features(input1)
        output2 = self.features(input2)
        return output1, output2
    
model = SiameseNetwork().to(device)
state_dict = torch.load(r'D:\Final_Year_Project_Dataset\Student\ml_models\Few_Shot_Learning_Siamese-Networks.pth')
model.load_state_dict(state_dict)
model.to(device)

val_tfms = transforms.Compose([
    transforms.ToPILImage(),
    transforms.Resize((100,100)),
    transforms.ToTensor(),
    transforms.Normalize((0.5), (0.5))
])

def give_results(img_1, img_2):
    try:
        urllib.request.urlretrieve(img_1,"Images_Folder/Img_1.jpg")
        urllib.request.urlretrieve(img_2,"Images_Folder/Img_2.jpg")

        changer('D:\Final_Year_Project_Dataset\Student\Images_Folder\Img_1.jpg')

        img_1 = read(r'Images_Folder\Img_1.jpg')
        img_2 = read(r'Images_Folder\Img_2.jpg')

        img_1 = val_tfms(img_1)
        img_1 = img_1.view(-1, 1, 100, 100)
        img_2 = val_tfms(img_2)
        img_2 = img_2.view(-1, 1, 100, 100)
        model.eval()
        output_1, output_2 = model(img_1, img_2)
        euclidean_distance = F.pairwise_distance(output_1, output_2)
        os.remove("Images_Folder\Img_1.jpg")
        os.remove("Images_Folder\Img_2.jpg")
        return float(euclidean_distance.item())
    except:
        return 3