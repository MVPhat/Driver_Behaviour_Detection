import cv2
import torch
import numpy as np
from ultralytics import YOLO
from tqdm import tqdm

model = YOLO('yolo11n.pt', verbose=False)

model.train(data='/path/to/data.yaml',
            epochs=50,
            patience=5,
            save=True,
            device=torch.device('cuda' if torch.cuda.is_available() else 'cpu'),
            project='MOT')