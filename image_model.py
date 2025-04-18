from PIL import Image
import numpy as np
from scipy.ndimage import convolve

# Edge-detection kernel
EDGE_KERNEL = np.array([
    [-1, -1, -1],
    [-1,  8, -1],
    [-1, -1, -1]
])

def analyze_image(pil_img: Image.Image):
    # Resize and preprocess
    img_resized = pil_img.resize((200, 200))
    gray_img = img_resized.convert('L')
    gray_array = np.array(gray_img, dtype=np.float32)
    rgb_array = np.array(img_resized, dtype=np.float32)

    # 1. Edge Variance
    edge_map = convolve(gray_array, EDGE_KERNEL)
    edge_var = np.var(edge_map)

    # 2. Brightness
    brightness = np.mean(gray_array)

    # 3. Colorfulness
    color_std = np.std(rgb_array)

    # 💡 Main logic
    if edge_var > 10000:
        return 1, f"Edge variance too high: {edge_var:.2f} — may indicate FAKE packaging"
    
    # Secondary conditions (only trigger if 2+ issues)
    issues = []
    if brightness < 50 or brightness > 200:
        issues.append(f"Unusual brightness: {brightness:.2f}")
    if color_std < 25:
        issues.append(f"Very low colorfulness: {color_std:.2f}")

    if len(issues) >= 2:
        return 1, "❌ FAKE MEDICINE\n\n" + "\n".join(issues)
    else:
        return 0, f"✅ REAL MEDICINE\n\nEdge: {edge_var:.2f}, Brightness: {brightness:.2f}, Colorfulness: {color_std:.2f}"
