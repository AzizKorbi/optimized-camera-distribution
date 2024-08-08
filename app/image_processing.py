import cv2
import numpy as np
import matplotlib.pyplot as plt

def load_image(image_path):
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return image, gray_image

def apply_canny_edge_detection(gray_image, threshold1=50, threshold2=150):
    edges = cv2.Canny(gray_image, threshold1, threshold2)
    return edges

def find_contours(edges, min_area=500):
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    filtered_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_area]
    return filtered_contours

def draw_contours(image, contours):
    contour_image = image.copy()
    cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 2)
    return contour_image

def annotate_key_areas(image, contours):
    annotated_image = image.copy()
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(annotated_image, (x, y), (x+w, y+h), (255, 0, 0), 2)
    return annotated_image


# app/image_processing.py
import cv2
import numpy as np

# Existing imports and functions...

def overlay_camera_fov(image, center, radius, angle):
    """
    Overlay a camera's field of view on the image.
    
    :param image: The original image on which to overlay the FOV.
    :param center: A tuple (x, y) representing the camera's position.
    :param radius: The radius (range) of the camera's coverage.
    :param angle: The field of view angle (in degrees).
    :return: Image with the camera FOV overlay.
    """
    fov_image = image.copy()

    # Create a mask for the FOV
    mask = np.zeros_like(fov_image)
    cv2.ellipse(mask, center, (radius, radius), 0, 0, angle, (255, 255, 255), -1)

    # Overlay the FOV mask onto the original image
    fov_image = cv2.addWeighted(fov_image, 0.7, mask, 0.3, 0)

    return fov_image
