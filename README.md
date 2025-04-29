# Computer-Vision-Project
This repository contains solutions to the internship assessment tasks using Python and OpenCV.  
It covers basic image processing, real-time color detection via webcam, and documentation of the process.

## 📁 Project Structure

├── Image_Manipulation │ 
  ├── Input_Images/ │
    └── input1.jpg
    └── input2.jpg
    └── input3.jpg
  └── Output_Images/ │
    └── CannyEdge_input1.jpg
    └── CannyEdge_input2.jpg
    └── CannyEdge_input3.jpg
    └── GaussianBlur_input1.jpg
    └── GaussianBlur_input2.jpg
    └── GaussianBlur_input3.jpg
    └── Grayscale_input1.jpg
    └──Grayscale_input2.jpg
    └──Grayscale_input3.jpg
  └── ImageManipulation.py │
├── Color_Detection │
  ├── Color_Detector.py │ 
  └── color_palette.csv │ 
  └── recording.html │ 

🧪 Task 1 – Basic Image Manipulation

✔️ Features:
- Converts images to **Grayscale**
- Applies **Gaussian Blur**
- Performs **Canny Edge Detection**
- Processes **all images in a folder** at once

### ▶️ Run:
bash

cd Image_Manipulation

py image_manipulation.py

🎨 Task 2 – Real-time Color Detector (Webcam)

✔️ Features:
- Opens webcam
- On mouse click displays RGB values
- Displays nearest color name from color palette

### ▶️ Run:
bash

cd Color_Detection

py Color_Detector.py

💡 Controls:

-Left-click on the webcam window to detect color

-Press ESC to exit the application

✅ Requirements

-Python 3.8 – 3.10

-OpenCV

-Pandas

-Webcam (for Task 2)

Install Dependencies

pip install opencv-python pandas

Output- CannyEdges

![CannyEdge_input1](https://github.com/user-attachments/assets/40e0759f-b122-41e2-bac6-cc9f45043d33)
![CannyEdge_input2](https://github.com/user-attachments/assets/beae7974-7d31-4e05-ae1e-b295af50e308)
![CannyEdge_input3](https://github.com/user-attachments/assets/240e4b2b-a950-4d5f-b5f1-abfee2a51f9f)


Output- GaussianBlur

![GaussianBlur_input1](https://github.com/user-attachments/assets/e8800609-a20d-4d6c-990b-a649226d054c)
![GaussianBlur_input2](https://github.com/user-attachments/assets/63330195-88d9-49c2-9b55-8c66c15ff32c)
![GaussianBlur_input3](https://github.com/user-attachments/assets/b38ee753-0ef6-414f-af94-7701f696cd4b)


Output- Grayscale

![Grayscale_input1](https://github.com/user-attachments/assets/7ffe2d66-2683-456a-97f2-2037d97d817c)
![Grayscale_input2](https://github.com/user-attachments/assets/aaeaa5c8-50be-4f8e-b805-b6baca734c2e)
![Grayscale_input3](https://github.com/user-attachments/assets/fe2f0858-ffb7-4ca7-a3c5-ce2e42934d44)












