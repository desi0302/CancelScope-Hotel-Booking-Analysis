from PIL import Image
from pathlib import Path

src = Path(__file__).resolve().parents[1] / 'images' / 'dataset-cover.png'
dst = src.with_name('dataset-cover-small.png')

print(f"Loading {src}")
img = Image.open(src)
# target width
target_w = 600
w, h = img.size
if w <= target_w:
    print("Image already smaller than or equal to target width; copying file as-is.")
    img.save(dst, optimize=True)
else:
    ratio = target_w / float(w)
    target_h = int(h * ratio)
    img = img.resize((target_w, target_h), Image.LANCZOS)
    img.save(dst, optimize=True, quality=85)
    print(f"Saved resized image to {dst}")