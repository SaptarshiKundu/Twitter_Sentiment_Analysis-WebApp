# This helper script loads the model trained BERT model

import torch
import os

def load_model(model_name):
    model_path = os.path.join('model', model_name)
    model = torch.load(model_path, map_location=torch.device('cpu'))
    return model