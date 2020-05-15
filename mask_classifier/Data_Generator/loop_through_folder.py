import cv2
import os
from mask import create_mask
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--path", help="path to images folder")
args = parser.parse_args()

folder_path = args.path
print("Target folder: ", folder_path)

colors = [ "default", "black", "blue", "red" ]

images = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
for i in range(len(images)):
    # print("the path of the image is", images[i])
    create_mask(images[i], colors[i%len(colors)] )
