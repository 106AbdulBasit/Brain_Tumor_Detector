# Brain_Tumor_Detector

![Brain Tumor](https://raw.githubusercontent.com/106AbdulBasit/Kaggle-Projects/main/Brain%20Tumor%20Classification%2C%20Transfer%20Learning/robina-weermeijer-3KGF9R_0oHs-unsplash.jpg)

# Introduction
The project aims to classify the brain tumor whether the MRI image of the brain contains the brain tumor or not. This repository contains the weights file of the trained model. The user can download the repository and then use it to classify the images. The production code  repository is in the given. [Link](https://github.com/106AbdulBasit/Kaggle-Projects). The model is trained on the resnet 50 with the accuracy of more than 90 percent.

# Installation
```
 python3 -m venv /path/to/new/virtual/environment
 
 #activate the virtual environment
 
 $ git clone https://github.com/ 106AbdulBasit/Brain_Tumor_Detector 
#Go into the repository
$ cd Brain_Tumor_Detector

#Install dependencies
$ pip3 install -r requirements.txt

 #Execute the file. You can set your own path to the image as well
$ python3 main.py --path Samples/y1.jpg

```


# Control Flow

This repository contains three modules.
1. Image Reader
2. Model Inference
3. Main.py

        
**Image Reader**:
The Image module takes care of the valid input. Handles the edge cases for the input like the size of the image and color mode of the image, do the preprocessing of the input.

**Model Inference**:
The model inference module loads the weights file set the threshold and gives the output. it takes the input from the image reader module.If the value is greater than the threshold the model classifies the images as the brain tumor.

**Main.py**
The main file makes the object of the two modules and then executes the file from the given path.

**Every module is written in a generic form so it can be expanded or be utilised for other future project**.



# Important Note

At the moment in the main.py file, the argument parser allows input of the path of the image. The structure of the module is written in a way that more argument parsers can be added to the main.py file which would allow the following functionality:

1. Set the size of the image.
2. Set the color mode.



