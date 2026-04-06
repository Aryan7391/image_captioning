# caption.py — Caption Generation using GIT-base-COCO (pretrained)

from transformers import AutoProcessor, AutoModelForCausalLM
from PIL import Image
import torch

# Device
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"Using device: {device}")

# Load pretrained model + processor
print("Loading GIT-base-COCO model...")
processor = AutoProcessor.from_pretrained('microsoft/git-base-coco')
model     = AutoModelForCausalLM.from_pretrained('microsoft/git-base-coco').to(device)
model.eval()
print("✅ Model ready")

def generate_caption(image_path, encoder=None, decoder=None, vocab=None):
    # Load image
    image = Image.open(image_path).convert('RGB')

    # Preprocess image
    inputs = processor(images=image, return_tensors='pt').to(device)

    # Generate caption
    with torch.no_grad():
        output = model.generate(
            **inputs,
            max_length=50
        )

    # Decode token ids → string
    caption = processor.decode(output[0], skip_special_tokens=True)
    return caption