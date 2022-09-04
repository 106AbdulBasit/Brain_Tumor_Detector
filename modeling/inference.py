import keras

import numpy as np

class ModelInference:
    """Inference module to predict an image class"""
    
    def __init__(self, weights_path='./Weights/model.h5', threshold=0.8):   
        self.weights_path = weights_path
        self.threshold = threshold
        
        self.model = self.load_model()
        
    def load_model(self):
        return keras.models.load_model(self.weights_path)
    
    def predict(self, image_array: np.array) -> bool:
        model_output = self.model.predict(image_array)
        prediction = self.parse_model_output(model_output)
        return prediction
        
    def parse_model_output(self, model_output: list) -> bool:
        confidence_score = model_output[0][0]
        
        result = False
        if confidence_score >= self.threshold:
            result = True
            
        return result