import cv2
import os

input_img_folder = 'Input_Images'
output_img_folder = 'Output_Images'

valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp')

#Go through all files in input folder
for filename in os.listdir(input_img_folder):
    if not filename.lower().endswith(valid_extensions):
        continue 

    img_path = os.path.join(input_img_folder, filename)
    image = cv2.imread(img_path)

    if image is None:
        print("No image found. Input again.")
        exit()

    #Converting to grayscale
    grayscale = cv2.cvtColor( image, cv2.COLOR_BGR2GRAY)
    gray_out_path = os.path.join(output_img_folder, f"Grayscale_{filename}")
    cv2.imwrite(gray_out_path, grayscale)

    #Applying gaussian blur
    GaussianB = cv2.GaussianBlur(image, (9,9), 0)
    blur_out_path = os.path.join(output_img_folder, f"GaussianBlur_{filename}")
    cv2.imwrite(blur_out_path, GaussianB)

    #Canny Edge Detection
    cannyedge = cv2.Canny(image, 50, 150)
    edge_out_path = os.path.join(output_img_folder, f"CannyEdge_{filename}")
    cv2.imwrite(edge_out_path, cannyedge)


    print("Completed changes to images and sent to " + output_img_folder)