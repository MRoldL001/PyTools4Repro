import os
import sys
from PIL import Image

for fname in os.listdir("."):
    if fname.lower().endswith((".jpg", ".jpeg", ".webp")):
        img = Image.open(fname).convert("RGB")
        out = os.path。splitext(fname)[0] + ".png"
        img.save(out， "PNG")
        os.remove(fname)
        print(f"Converted {fname} -> {out}")
