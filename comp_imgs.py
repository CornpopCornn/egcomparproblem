import tkinter as tk
import tkinter.filedialog
import cv2
import numpy as np
import os

def compare_images(img1_path, img2_path):
    # Load images
    img1 = cv2.imread(img1_path, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(img2_path, cv2.IMREAD_GRAYSCALE)

    # Resize images to the same size
    img2 = cv2.resize(img2, img1.shape[::-1])

    # Find differences between the two images
    difference1 = cv2.subtract(img2, img1)
    difference2 = cv2.subtract(img1, img2)

    # Find pixels that are only in image 2 and mark them in green
    green_mask = difference1 > 0
    difference1_color = cv2.cvtColor(img2, cv2.COLOR_GRAY2BGR)
    difference1_color[green_mask] = [0, 255, 0]

    # Find pixels that are only in image 1 and mark them in red
    red_mask = difference2 > 0
    difference2_color = cv2.cvtColor(img2, cv2.COLOR_GRAY2BGR)
    difference2_color[red_mask] = [0, 0, 255]

    # Show and save the resulting difference images
    cv2.imwrite("difference1.jpg", difference1_color)
    cv2.imwrite("difference2.jpg", difference2_color)

def choose_images():
    root = tk.Tk()
    root.withdraw()

    img1_path = tk.filedialog.askopenfilename(title="Choose first image")
    img2_path = tk.filedialog.askopenfilename(title="Choose second image")

    compare_images(img1_path, img2_path)

if __name__ == "__main__":
    choose_images()