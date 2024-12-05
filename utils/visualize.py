import os
import random
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import cv2
import numpy as np

# Paths
img_path = '/path/to/train/images'
label_path = '/path/to/train/labels'

# Class names
classname = ['Distracted', 'Drowsy', 'Eating', 'No seatbelt', 'Seatbelt', 'Smoking']

# Number of images to display
num_data = 15

# Get all available images and labels
all_imgs = sorted(os.listdir(img_path))
all_labels = sorted(os.listdir(label_path))

# Randomly select indices
selected_indices = random.sample(range(len(all_imgs)), num_data)
imgs = [all_imgs[i] for i in selected_indices]
labels = [all_labels[i] for i in selected_indices]

# Create a 3x5 grid for the images
fig, axes = plt.subplots(3, 5, figsize=(21, 15))

# Plot each image in the grid
for idx, ax in enumerate(axes.flat):
    if idx < len(imgs):
        # Open the image
        img_path_full = os.path.join(img_path, imgs[idx])
        img = np.array(Image.open(img_path_full))  # Convert to numpy array for cv2 compatibility
        img_h, img_w, _ = img.shape

        # Open the label file and read annotations
        label_path_full = os.path.join(label_path, labels[idx])
        with open(label_path_full, 'r') as file:
            # Read the entire line, remove any newlines, and split by spaces
            ann = file.read().strip().replace('\n', '').split(' ')
            label = int(ann[0])
            x, y, w, h = map(float, ann[1:])
            x_center, y_center = x * img_w, y * img_h
            box_w, box_h = w * img_w, h * img_h

            x1 = x_center - box_w // 2
            y1 = y_center - box_h // 2
            x2 = x_center + box_w // 2
            y2 = y_center + box_h // 2

            bbox = patches.Rectangle((x1, y1), box_w, box_h, linewidth=2, edgecolor='red', facecolor='none')
            ax.add_patch(bbox)
            ax.set_title(f'{classname[label]}', fontsize=20)
            # ax.text(x1, y1 - 10, classname[label], color='red', fontsize=10, verticalalignment='top')
        ax.imshow(img)
        ax.axis('off')
plt.tight_layout()
plt.show()