import cv2
import torch
import numpy as np
from ultralytics import YOLO
from tqdm import tqdm

model = YOLO('/path/to/train/weights/last.pt', verbose=True)

results = model.val(data='/path/to/data.yaml')