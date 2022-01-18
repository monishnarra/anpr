import cv2
import random
import os
import numpy as np
import matplotlib.pyplot as plt
import datetime
import os.path, time

import pytesseract


images_dir = r"C:\Users\Monish Narra\Desktop\project\anpr\data"
image_files = os.listdir(images_dir)
image_path = "{}/{}".format(images_dir, "plate.png")
now = datetime.datetime.now()


text = pytesseract.image_to_string(image_path, lang="eng")


print("The License Plate number is :- ")
print(text)
print("vehicle entered : %s" % time.ctime(os.path.getctime(image_path)))

