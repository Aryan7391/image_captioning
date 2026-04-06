# model/encoder.py — CNN Encoder (ResNet-50)

import torch
import torch.nn as nn
import torchvision.models as models

class EncoderCNN(nn.Module):
    def __init__(self, embed_size):
        super(EncoderCNN, self).__init__()

        # Load pretrained ResNet-50
        resnet = models.resnet50(weights=models.ResNet50_Weights.IMAGENET1K_V1)

        # Remove final classification layer
        # We need features, not class labels
        modules = list(resnet.children())[:-1]
        self.resnet = nn.Sequential(*modules)

        # Resize 2048 → embed_size
        self.linear = nn.Linear(resnet.fc.in_features, embed_size)
        self.bn = nn.BatchNorm1d(embed_size, momentum=0.01)

        # Freeze ResNet — no training needed
        for param in self.resnet.parameters():
            param.requires_grad = False

    def forward(self, images):
        # Extract visual features
        with torch.no_grad():
            features = self.resnet(images)              # (batch, 2048, 1, 1)

        features = features.reshape(features.size(0), -1)   # (batch, 2048)
        features = self.bn(self.linear(features))            # (batch, embed_size)
        return features