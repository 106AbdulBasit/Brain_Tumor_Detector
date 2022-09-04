from utils.reader import ImageReader
from modeling.inference import ModelInference

import argparse

import os

def main(image_path):
    
    # initialize objects
    ir_obj = ImageReader()
    mi_obj = ModelInference()
    
    # load/transform image
    img = ir_obj.read_image(image_path=image_path)
    
    # inference
    class_flag = mi_obj.predict(image_array=img)
    
    if class_flag:
        print('\n--> Tumor Detected\n')
    else:
        print('\n--> No Tumor Detected\n')

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='Allow to input image path from cli'
    )

    parser.add_argument(
        '--path',
        type=str,
        help='the path to list'
    )

    args = parser.parse_args()

    main(image_path=args.path)


