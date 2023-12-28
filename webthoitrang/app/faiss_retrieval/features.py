import numpy as np
from PIL import Image
import torch
import torchvision.transforms as transforms
from fashion_clip.fashion_clip import FashionCLIP

def extract_CLIP_features(image_path):
    """Extracts image features using a provided feature extractor."""
    image = Image.open(image_path)
    feature_extractor = FashionCLIP('fashion-clip')
    features = feature_extractor.predict(np.array(image))
    return features