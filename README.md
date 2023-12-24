# Agro-Samadhan
 A web-based tool for detecting and finding solutions to the  three (3) different classes of Plant Leaf Diseases Using a custom Convolutional Neural Network(CNN) model.

# Problem Statement
 To develop a deep learning model which can detect plant diseases from leaf images using the custom CNN architecture. The model could be used by farmers and beginners to deal with the crop health management. It will be helpful to prevent the plant diseases and crop loss.

# Aims and objectives
•	AGRO-SAMADHAN, a Plant Leaf Disease Detection system aims to efficiently identify and classify plant diseases to facilitate disease monitoring and surveillance, minimize crop losses, optimize resource utilization, enable sustainable farming practices, support decision making, enhance farmer knowledge and capacity, and perform early disease detection.
•	The model strategically employs a minimal number of layers and neurons in fully connected layers. This design accelerates training time and ensures minimum utilization of computer resources.
•	By fulfilling these goals, this system could improve agricultural productivity and reduces crop losses. It improves farmer livelihoods and ensures preventive disease control.
# Dataset Description

**Three Main types of Plant leaf are collected that are namely *Broad beans* , *Ridge Gourd* and *Tomato* based on their disease *Cercospora leaf spot* , *Alternaria Leaf Spot* and *Leaf Miner* respectively each assigned a class with 100 images in each class type totalling to 300 images in the whole dataset.**

# Plant leaf Images description in table

![Screenshot 2023-12-22 224816](https://github.com/gigakad8811/Agro_Samadhan/assets/120395102/3015af35-91cf-415f-bb38-a174ee8f61fc)

# Plant Leaf Classes with sample images and class names

**Broadbeans With Cercospora leaf spot**

![Screenshot 2023-12-22 224823](https://github.com/gigakad8811/Agro_Samadhan/assets/120395102/811b5f8e-103e-471e-b02d-765221e43149)

**Ridge Gourd with Alternaria Leaf Spot**

![Screenshot 2023-12-22 224826](https://github.com/gigakad8811/Agro_Samadhan/assets/120395102/e47c58cf-b859-4f74-b1b7-e1d049e0dddb)

**Tomato with Leaf miner disease**

![Screenshot 2023-12-22 224831](https://github.com/gigakad8811/Agro_Samadhan/assets/120395102/39dee0dd-674d-4c47-964d-846378ec6b43)


**The dataset is allocated to training, testing and validation.**

**1.Training Data:**

•	Total Images: 300

•	Test Size: 0.2

•	Training Data = (300 × (1 - 0.2) = 240 images

**2. Validation Data:**

•	Test Size: 0.2 (of the remaining data after training split)

•	Validation Data = (240 ×0.2 = 48) images

**3. Testing Data:**

•	Test Size: 0.2 (of the total data)

•	Testing Data = (300 × 0.2 = 60) images

**So, the data allocation is as follows:**

•	Training Data: 240 images (80%)

•	Validation Data: 48 images (20% of Training data)

•	Testing Data: 60 images (20% of the whole dataset)

# Model Network Architecture

**This is the diagram of the customised neural network that was used to train the model on the given dataset -**

![Custom CNN model architecture png](https://github.com/gigakad8811/Agro_Samadhan/assets/120395102/428caa80-f39c-408d-a78a-852722c302f6)



**Fully detailed information of Layers and activation function ussed in this network architecture -**

![Screenshot 2023-11-30 213714](https://github.com/gigakad8811/Agro_Samadhan/assets/120395102/3e2fda02-32c1-4005-9d4d-039e71cd0a39)


**Activity diagram of the system workflow -**

![WhatsApp Image 2023-12-01 at 01 01 21_9bebd4b3](https://github.com/gigakad8811/Agro_Samadhan/assets/120395102/6ec9980b-3a7a-48d6-93d9-f13e05c57c19)

**List of accuracy and loss of the trained model -**

![Screenshot 2023-11-30 213754](https://github.com/gigakad8811/Agro_Samadhan/assets/120395102/655491f4-92c4-4a3a-bce4-f4b9fbe29a39)


# User Interface Demo

![FireShot Capture 001 - main_app · Streamlit - localhost](https://github.com/gigakad8811/Agro_Samadhan/assets/120395102/09eb6fcb-223b-47c9-9db7-f1f062283c8f)


# Installation and setup

1. First Install and setup Anaconda latest version

2. Open conda command line and change the directory to the folder where you have downloaded the repository files

3. Then create a virtual environment such as "project" in the conda commandline prompt using the command

 **"conda create --name project"**

 **"conda activate project"**

4. Then install necessary python libraries to run the model successfully

 **" pip install tensorflow"**

 **" pip install streamlit"**

 **" pip install Keras"**

 **" pip install numpy"**

 **" pip install opencv_python"**

5. Finally Run the main .py app.

 **"streamlit run main_app.py   "**
