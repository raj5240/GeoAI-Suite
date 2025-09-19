
import torch
import torch.nn as nn

class DummySegModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = nn.Conv2d(3, 1, kernel_size=3, padding=1)

    def forward(self, x):
        return torch.sigmoid(self.conv(x))

def load_model(path=None, device="cpu"):
    model = DummySegModel()
    if path:
        model.load_state_dict(torch.load(path, map_location=device))
    model.to(device).eval()
    return model
