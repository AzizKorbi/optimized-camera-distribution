import os
from flask import render_template, request, redirect, url_for
from . import app
from .image_processing import load_image, apply_canny_edge_detection, find_contours, draw_contours, annotate_key_areas, overlay_camera_fov
import cv2

@app.route('/upload', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        image_file = request.files['image']

        if image_file:
            image_path = os.path.join('static', 'uploads', image_file.filename)
            image_file.save(image_path)

            # Process the image
            image, gray_image = load_image(image_path)
            edges = apply_canny_edge_detection(gray_image)
            contours = find_contours(edges)
            contour_image = draw_contours(image, contours)
            annotated_image = annotate_key_areas(contour_image, contours)

            # Example Camera Parameters (you can change these)
            center = (300, 300)  # Example center of the camera's FOV
            radius = 150  # Example radius of the camera's coverage
            angle = 90  # Example field of view angle

            # Overlay the camera FOV on the annotated image
            fov_image = overlay_camera_fov(annotated_image, center, radius, angle)

            # Save the processed images
            contour_image_path = os.path.join('static', 'uploads', 'contour_' + image_file.filename)
            annotated_image_path = os.path.join('static', 'uploads', 'annotated_' + image_file.filename)
            fov_image_path = os.path.join('static', 'uploads', 'fov_' + image_file.filename)


            cv2.imwrite(contour_image_path, contour_image)
            cv2.imwrite(annotated_image_path, annotated_image)
            cv2.imwrite(fov_image_path, fov_image)

            return render_template('results.html', original=image_file.filename, 
                                   contour_image='contour_' + image_file.filename,
                                   annotated_image='annotated_' + image_file.filename,
                                   fov_image='fov_' + image_file.filename)

    return render_template('upload.html')
