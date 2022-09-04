from tensorflow.keras.preprocessing.image import load_img

import numpy as np
import os

class ImageReader:
    """Utility module to read and transform images"""
    
    def __init__(self, image_size=224, color_mode='rgb'):    
        self.image_size = image_size
        self.color_mode = color_mode
        
        self.extensions = ['.png', '.jpg', '.jpeg']
        self.color_codes = ['grayscale', 'rgb', 'rgba']
        
        # test two parameters for invalid values
        self.test_parameters()
        
    def test_parameters(self):
        """Tests color mode and image size for validity"""
        
        if not self.color_mode in self.color_codes:
            raise Exception(
                f'Color code mismatch, Acceptable color codes: {self.color_codes}'
            )
        if self.image_size <= 0:
            raise Exception(
                f'Image size must be > 0'
            )    
        
    def test_path(self, image_path: str):
        """Tests image path for validity"""
        
        extension = os.path.splitext(image_path)[-1]
        
        if extension in self.extensions:
            if not os.path.isfile(image_path):
                raise Exception(f"Image not found in path: '{image_path}'")
        else:
            raise Exception(
                f"Extension mismatch, Acceptable extensions: {self.extensions}"
            )
        
    def read_image(self, image_path: str) -> np.array:
        """Read image from a path and return array
        
        Args: 
            image_path: string path to the image
        
        Returns:
            img: image as np.array as required by the model input
        
        """
        
        # test the image path provided
        self.test_path(image_path)
        
        # load image with required height, width, channel
        img = load_img(
            path=image_path,
            color_mode='rgb',
            target_size=(self.image_size,self.image_size)
        )
        
        # image processing
        img = self.preprocess_image(img)
        
        return img
    
    def preprocess_image(self, img: np.array) -> np.array:
        """Transformation function to pre-process the image"""
        img = np.array(img)
        img = np.expand_dims(img, axis=0)
        return img