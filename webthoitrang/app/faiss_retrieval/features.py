import numpy as np
import torch
import torchvision.transforms as transforms
from fashion_clip.fashion_clip import FashionCLIP


CLIP_FEATURE_EXTRACTOR = FashionCLIP('fashion-clip')


def extract_CLIP_features(image_path):
    """Extracts image features using a provided feature extractor."""
    try:
        features = CLIP_FEATURE_EXTRACTOR.encode_images([image_path], batch_size=32)
        return features
    except IOError:
        # Handle the error, e.g., print a message
        print("Error opening image:", image_path)
        raise Exception('Cannot open the image')