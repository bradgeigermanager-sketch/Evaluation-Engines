"""
FILE: Evaluation-Engines/transforms/transformers/stellar_classifier/model.py
PURPOSE: Transformer-based inference module for stellar classification.
USAGE: Acts as a standardized inference bridge for spectral input data.
"""

import torch
import torch.nn as nn

class StellarTransformerClassifier(nn.Module):
    def __init__(self, input_dim, d_model, nhead, num_layers, num_classes):
        super(StellarTransformerClassifier, self).__init__()
        # Encoder layer for processing stellar light curve/spectral time-series
        encoder_layer = nn.TransformerEncoderLayer(d_model=d_model, nhead=nhead)
        self.transformer = nn.TransformerEncoder(encoder_layer, num_layers=num_layers)
        self.fc = nn.Linear(d_model, num_classes)
        
    def forward(self, x):
        # x shape expected: (sequence_length, batch_size, input_dim)
        output = self.transformer(x)
        return self.fc(output.mean(dim=0))  # Aggregating across the sequence

def get_classifier_template():
    """Returns a generic configuration for the Evaluation-Engines registry."""
    return {
        "model_type": "Encoder-only Transformer",
        "input_features": ["light_curve_flux", "wavelength_bins"],
        "output_task": "Spectral_Classification_MK"
    }
  
